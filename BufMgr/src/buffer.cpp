/**
 * @author See Contributors.txt for code contributors and overview of BadgerDB.
 *
 * @section LICENSE
 * Copyright (c) 2012 Database Group, Computer Sciences Department, University of Wisconsin-Madison.
 */

#include <memory>
#include <iostream>
#include "buffer.h"
#include "exceptions/buffer_exceeded_exception.h"
#include "exceptions/page_not_pinned_exception.h"
#include "exceptions/page_pinned_exception.h"
#include "exceptions/bad_buffer_exception.h"
#include "exceptions/hash_not_found_exception.h"

namespace badgerdb { 

BufMgr::BufMgr(std::uint32_t bufs)
	: numBufs(bufs) {
	bufDescTable = new BufDesc[bufs];		//页框

    for (FrameId i = 0; i < bufs; i++) 
    {
    	bufDescTable[i].frameNo = i;
    	bufDescTable[i].valid = false;
    }

    bufPool = new Page[bufs];		//缓存池

	int htsize = ((((int) (bufs * 1.2))*2)/2)+1;
    hashTable = new BufHashTbl (htsize);    // allocate the buffer hash table

    clockHand = bufs - 1;
}


BufMgr::~BufMgr() {
	for (std::uint32_t i = 0; i < numBufs; i++)
	{
		if (bufDescTable[i].dirty == true)
			bufDescTable[i].file->writePage(bufPool[i]);		//写回
	}
	delete[] bufDescTable;
	delete[] bufPool;
	delete hashTable;
}

void BufMgr::advanceClock()
{
	clockHand = (clockHand + 1) % numBufs;
	while (bufDescTable[clockHand].refbit && bufDescTable[clockHand].valid) {
		bufDescTable[clockHand].refbit = 0;
		clockHand = (clockHand + 1) % numBufs;
	}
}

void BufMgr::allocBuf(FrameId & frame) 
{
	FrameId clockHand0 = clockHand;
	while(bufDescTable[clockHand].pinCnt != 0) {
		advanceClock();
		if (clockHand == clockHand0) throw BufferExceededException();
	}
	if (bufDescTable[clockHand].valid)
	try {hashTable->remove(bufDescTable[clockHand].file, bufDescTable[clockHand].pageNo);}
	catch (HashNotFoundException &e) {}
	if (bufDescTable[clockHand].dirty){
		bufDescTable[clockHand].file->writePage(bufPool[clockHand]);	//写回
	}
	frame = clockHand;	
}

	
void BufMgr::readPage(File* file, const PageId pageNo, Page*& page)
{
	FrameId frame;
	try {
		hashTable->lookup(file, pageNo, frame);
	} catch (HashNotFoundException &e) {
		allocBuf(frame);
		bufPool[frame] = file->readPage(pageNo);
		bufDescTable[frame].Set(file, pageNo);
		hashTable->insert(file, pageNo, frame);
		page = &bufPool[frame];
		return;
	}
	bufDescTable[frame].refbit = true;
	bufDescTable[frame].pinCnt++;
	page = &bufPool[frame];
}


void BufMgr::unPinPage(File* file, const PageId pageNo, const bool dirty) 
{
	FrameId frame;
	try {
		hashTable->lookup(file, pageNo, frame);
	} catch (HashNotFoundException &e) {
		return;
	}
	if (dirty == true)
		bufDescTable[frame].dirty = dirty;
	if (bufDescTable[frame].pinCnt == 0) throw PageNotPinnedException(file->filename(), pageNo, frame);
	bufDescTable[frame].pinCnt--;
}

void BufMgr::flushFile(const File* file) 
{
	for (std::uint32_t i = 0; i < numBufs; i++)
	{
		if (bufDescTable[i].file == file) {
			if (bufDescTable[i].pinCnt != 0)
				throw PagePinnedException(file->filename(),bufDescTable[i].pageNo, i);
			if (!bufDescTable[i].valid)
				throw BadBufferException(i, bufDescTable[i].dirty, bufDescTable[i].valid, bufDescTable[i].refbit);
			if (bufDescTable[i].dirty) {
				bufDescTable[i].file->writePage(bufPool[i]);
				hashTable->remove(file, bufDescTable[i].pageNo);
				bufDescTable[i].Clear();
			}
		}
	}
}

void BufMgr::allocPage(File* file, PageId &pageNo, Page*& page) 
{
	FrameId frame;
	allocBuf(frame);
	bufPool[frame] = file->allocatePage();
	pageNo = bufPool[frame].page_number();
	bufDescTable[frame].Set(file, pageNo);
	hashTable->insert(file, pageNo, frame);
	page = &bufPool[frame];
}

void BufMgr::disposePage(File* file, const PageId PageNo)
{
	FrameId frame;
	try {
		hashTable->lookup(file, PageNo, frame);
		bufDescTable[frame].Clear();
		hashTable->remove(file, PageNo);
	} catch (...) {}
	file->deletePage(PageNo);
}

void BufMgr::setBuffer(File* file, const PageId PageNo, bool valid)
{
	FrameId frame;
	try {
		hashTable->lookup(file, PageNo, frame);
		bufDescTable[frame].valid = valid;
	} catch (...) {}
}

void BufMgr::printSelf(void) 
{
    BufDesc* tmpbuf;
	int validFrames = 0;
    
    for (std::uint32_t i = 0; i < numBufs; i++)
	{
    	tmpbuf = &(bufDescTable[i]);
		std::cout << "FrameNo:" << i << " ";
		tmpbuf->Print();

    	if (tmpbuf->valid == true)
        	validFrames++;
    }

	std::cout << "Total Number of Valid Frames:" << validFrames << "\n";
}

}
