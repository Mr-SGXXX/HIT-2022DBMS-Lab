create table if not exists Employee(
    EPhone char(11) primary key,
    Ename char(10) not null,
    sex char(2) not null check (sex in ('男', '女')),
    age int not null check (age >= 18 and age <= 100),
    home char(100) not null,
    work char(20) not null,
    salary int not null,
    password char(32) not null,
    information char(200)
);

create index if not exists eIdx1 on Employee(EPhone, password);
create index if not exists eIdx2 on employee(ephone, ename, age, sex, information);

create table if not exists Customer(
    CPhone char(11) primary key,
    cname char(10) not null,
    sex char(2) check (sex in ('男', '女')),
    age int check (age >= 18 and age <= 100),
    aim char(4) check (aim in ('求租','求购','卖房', '出租')),
    password char(32) not null,
    server char(11) not null references Employee(EPhone),
    deleted bool not null default false
);

create index if not exists cIdx on Customer(CPhone, Cname, sex);
create index if not exists cIdxDel on customer(CPhone, password, deleted);

create table if not exists House(
    Hid serial PRIMARY KEY,
    location char(100) not null,
    area int not null,
    is_renovated bool not null,
    value int,
    owner_phone char(11) references Customer(CPhone),
    sell_or_rent char(4) check(sell_or_rent in ('出租', '出售')),
    price int check(price > 0),
    stime timestamp,
    moremsg char(100)
);

create index if not exists hIdx on House(Hid, location, area, is_renovated);

create table if not exists Record(
    Seller_phone char(11) references Customer(CPhone),
    Buyer_phone char(11) references Customer(CPhone),
    Hid int references House(Hid),
    sell_or_rent char(4) check (sell_or_rent in ('买卖','租赁')),
    price int check(price > 0),
    rtime timestamp default current_timestamp,
    primary key (Seller_phone, Buyer_phone, Hid)
);

create table if not exists Buyer_msg(
    Buyer_phone char(11) references Customer(CPhone),
    Btime timestamp not null default current_timestamp,
    buy_or_rent char(4) check(buy_or_rent in ('买房', '租房')),
    price int check(price > 0),
    area int,
    more_msg char(100),
    primary key (Buyer_phone, Btime)
);
