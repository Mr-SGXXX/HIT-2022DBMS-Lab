import random

import psycopg2

from SQL.insert_data import *

f_name = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "楚", "褚", "卫", "蒋", "沈", "曲", "韩", "杨", "朱",
          "秦", "尤", "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻"]

loc = ["村", "区", "县", "镇", "市", "乡", "屯", "庄"]

sex = ["男", "女"]

aim = ["求购", "求租", "卖房", "出租"]

moreMsg_employee = ["十年专业中介", "毕业于名牌大学", "知名房地产中介", "精通房地产中介", "新人客服", "从业五年以上", "业界精英", "曾获销售冠军", "客户好评如潮", "无"]

moreMsg_buyer = ["能住就行", "要求位于学校附近", "周边有商场优先", "优先考虑郊区", "需要带有阳台", "院子得够大", "低租金优先"]

moreMsg_sell_house = ["带有阁楼", "拎包即住", "豪华装修", "周围基础设施完善", "公交站附近", "毛坯房", "低额押金", "五室一厅三独卫", "无卫生间", "低楼层"]

moreMsg_record = ["双方对交易都很满意", "经过交涉双方圆满达成交易", "买卖双方进行了友好的沟通最后达成了交易", "卖家和买家在客服的交涉下完成了交易"]

sell_rent = ["出售", "出租"]

buy_rent = ["买房", "租房"]

record_type = ["买卖", "租赁"]

global phone


def gen_word():
    try:
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x}{body:x}'
        return bytes.fromhex(val).decode('gb2312')
    except:
        return gen_word()


def gen_name():
    return random.choice(f_name) + ''.join([gen_word() for _ in range(random.randint(1, 2))])


def gen_phone():
    global phone
    phone += 1
    return '1' + str(phone).rjust(10, '0')


def get_phone(start, end):
    return '1' + str(random.randint(start, end)).rjust(10, '0')


def gen_location():
    return "".join([gen_word() for _ in range(random.randint(1, 3))]) + random.choice(loc)


def translate_timestamp(timestamp):
    return {"year": int(timestamp[0:4]), "month": int(timestamp[5:7]), "day": int(timestamp[8:10]),
            "hour": int(timestamp[11:13]), "minute": int(timestamp[14:16]), "second": int(timestamp[17:19])}


def translate_time(timestamp_dict):
    return translate_time_(timestamp_dict["year"], timestamp_dict["month"], timestamp_dict["day"],
                           timestamp_dict["hour"], timestamp_dict["minute"], timestamp_dict["second"])


def translate_time_(year, month, day, hour, minute, second):
    return "select (to_timestamp(\'" + str(year) + '-' + str(month).rjust(2, '0') + '-' + str(day).rjust(2, '0') + \
           ' ' + str(hour) + ':' + str(minute).rjust(2, '0') + ':' + str(second).rjust(2, '0') \
           + "\',\'yyyy-MM-dd hh24:mi:ss\'))"


def gen_time():
    year = 2020 + random.randint(-2, 2)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    h = random.randint(0, 23)
    m = random.randint(0, 59)
    s = random.randint(0, 59)
    return "select (to_timestamp(\'" + str(year) + '-' + str(month).rjust(2, '0') + '-' + str(day).rjust(2, '0') + \
           ' ' + str(h) + ':' + str(m).rjust(2, '0') + ':' + str(s).rjust(2, '0') + "\',\'yyyy-MM-dd hh24:mi:ss\'))"


def gen_employee(num):
    global phone
    for _ in range(num):
        insert_employee(gen_phone(), gen_name(), random.choice(sex), random.randint(18, 50), gen_location(), "客服",
                        random.randint(1000, 10000), random.randint(1000000, 9999999),
                        random.choice(moreMsg_employee))


def gen_customer(num):
    global phone
    for _ in range(num):
        insert_customer(gen_phone(), gen_name(), random.choice(sex), random.randint(18, 99), random.choice(aim),
                        random.randint(1000000, 9999999), get_phone(1, 999))


def gen_house(num):
    for _ in range(num):
        insert_house(gen_location(), random.randint(40, 500), bool(random.choice([True, False])),
                     random.randint(100, 100000) * 100, get_phone(1000, phone))


def gen_sell_house(num):
    for _ in range(num):
        insert_sell_house(random.randint(3, 100), random.choice(sell_rent), random.randint(100, 100000) * 100,
                          gen_time(), random.choice(moreMsg_sell_house))


def gen_buyer_msg(num):
    for _ in range(num):
        insert_buyer_msg(get_phone(1000, phone), gen_time(), random.choice(buy_rent), random.randint(100, 100000) * 100,
                         random.randint(4, 50) * 10, random.choice(moreMsg_buyer))


def gen_record(num):
    for _ in range(num):
        phone1 = get_phone(1000, phone)
        phone2 = phone1
        while phone1 == phone2:
            phone2 = get_phone(1000, phone)
        insert_record(phone1, phone2, random.randint(3, 100), random.choice(record_type),
                      random.randint(100, 100000) * 100,
                      gen_time())


if __name__ == "__main__":
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        cur.execute("select setval(\'house_hid_seq\', 1, false)")
        cur.execute("Delete from buyer_msg cascade")
        cur.execute("Delete from Record cascade")
        cur.execute("Delete from House cascade")
        cur.execute("Delete from customer cascade")
        cur.execute("Delete from employee cascade")
    print("数据删除成功")
    disconnect_db(conn)
    insert_employee("10000000000", "张三", "男", "35", "南岗区", "老板", 100000, "1234567", "公司创始人")
    insert_employee("10000000001", "李四", "女", "18", "王家屯", "客服", 1000, "7654321", "新人客服")
    phone = 1
    gen_employee(998)
    print("员工生成成功")
    insert_customer("10000001000", "王五", "女", "21", "求购", "0000000", "10000000001")
    insert_customer("10000001001", "赵六", "男", "75", "卖房", "6666666", "10000000001")
    phone += 2
    gen_customer(9998)
    print("顾客生成成功")
    phone = 9999
    insert_house("道外区", 100, False, 100000, "10000001001")
    insert_house("纽约市", 500, True, 8000000, "10000001000")
    gen_house(4998)
    print("房屋生成成功")
    insert_sell_house(1, "出售", 50000, gen_time(), "急卖！！！")
    gen_sell_house(1999)
    print("房屋出售记录生成成功")
    insert_buyer_msg("10000001000", gen_time(), "买房", 75000, 120, "随缘收购")
    gen_buyer_msg(1999)
    print("房屋求购记录生成成功")
    insert_record("10000001001", "10000001000", 2, "买卖", 750000, gen_time())
    gen_record(999)
    print("房屋交易记录生成成功")
