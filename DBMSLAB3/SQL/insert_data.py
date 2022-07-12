import time

import psycopg2


def connect_db():
    conn = psycopg2.connect(database="lab3", user="postgres", password="703700a.", host="localhost", port="5432")
    return conn


def disconnect_db(conn):
    conn.commit()
    conn.close()


def insert_employee(EPhone, Ename, sex, age, home, work, salary, password, information):
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Employee values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (EPhone, Ename, sex, age, home, work, salary, password, information))
    disconnect_db(conn)


def insert_customer(CPhone, Cname, sex, age, aim, password, server):
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        start_time = time.time()
        cur.execute("select deleted from customer where cphone = %s", (CPhone,))
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT INTO Customer values(%s, %s, %s, %s, %s, %s, %s, false)",
                        (CPhone, Cname, sex, age, aim, password, server))
        elif row[0]:
            cur.execute("update customer set cname = %s, sex = %s, age = %s, aim = %s, password = %s, server = %s, "
                        "deleted = false where cphone = %s",
                        (Cname, sex, age, aim, password, server, CPhone))
        else:
            raise Exception
        end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time


def insert_house(location, area, is_renovated, value, owner_phone):
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        start_time = time.time()
        cur.execute(
            "INSERT INTO House(location, area, is_renovated, value, owner_phone)"
            + " values(%s, %s, %s, %s, %s)",
            (location, area, is_renovated, value, owner_phone))
        end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time


def insert_sell_house(Hid, sell_or_rent, price, stime, moremsg):
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        start_time = time.time()
        cur.execute(
            "update house set sell_or_rent = %s where Hid = %s",
            (sell_or_rent, Hid))
        cur.execute(
            "update house set price = %s where Hid = %s",
            (price, Hid))
        if stime is not None:
            cur.execute(f"update house set stime = ({stime}) where Hid = {Hid}")
        else:
            cur.execute(f"update house set stime = current_timestamp(0)::timestamp without time zone where Hid = {Hid}")
        cur.execute(
            "update house set moremsg = %s where Hid = %s",
            (moremsg, Hid))
        end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time


def insert_record(seller_phone, buyer_phone, Hid, sell_or_rent, price, rtime):
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        if rtime is not None:
            start_time = time.time()
            cur.execute(
                "INSERT INTO Record(seller_phone, buyer_phone, Hid, sell_or_rent, price, rtime)"
                + f" values(%s, %s, %s, %s, %s, ({rtime}))",
                (seller_phone, buyer_phone, Hid, sell_or_rent, price))
            end_time = time.time()
        else:
            start_time = time.time()
            cur.execute(
                "INSERT INTO Record(seller_phone, buyer_phone, Hid, sell_or_rent, price, rtime)"
                + f" values(%s, %s, %s, %s, %s, current_timestamp(0)::timestamp without time zone)",
                (seller_phone, buyer_phone, Hid, sell_or_rent, price))
            end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time


def insert_buyer_msg(buyer_phone, btime, buy_or_rent, price, area, more_msg):
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        if btime is not None:
            start_time = time.time()
            cur.execute(
                "INSERT INTO buyer_msg(buyer_phone, btime, buy_or_rent, price, area, more_msg)"
                + f" values(%s, ({btime}), %s, %s, %s, %s)",
                (buyer_phone, buy_or_rent, price, area, more_msg))
            end_time = time.time()
        else:
            start_time = time.time()
            cur.execute(
                "INSERT INTO buyer_msg(buyer_phone, btime, buy_or_rent, price, area, more_msg)"
                + f" values(%s, current_timestamp(0)::timestamp without time zone, %s, %s, %s, %s)",
                (buyer_phone, buy_or_rent, price, area, more_msg))
            end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time
