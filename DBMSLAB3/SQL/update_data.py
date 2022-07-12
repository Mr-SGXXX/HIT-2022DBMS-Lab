import time

from SQL.insert_data import connect_db, disconnect_db
from SQL.gen_data import translate_time
import psycopg2


def delete_customer(Cphone):
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute("update customer set deleted = true where cphone = %s", (Cphone,))
    cur.execute("update house set owner_phone = null, price = null, sell_or_rent = null, stime = null, moremsg = null"
                " where owner_phone = %s", (Cphone,))
    end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time


def change_password(cphone, password):
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute("update customer set password = %s where cphone = %s", (password, cphone))
    end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time


def update_buy_house(hid, new_phone):
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute(
        "update house set owner_phone = %s, sell_or_rent = null, moremsg = null, price = null, stime = null"
        " where hid = %s",
        (new_phone, hid))
    end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time


def delete_buyer_msg(bphone, btime_dict):
    btime = translate_time(btime_dict)
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute(
        "delete from buyer_msg"
        f" where buyer_phone = %s and btime = ({btime})",
        (bphone,))
    end_time = time.time()
    disconnect_db(conn)
    return end_time - start_time
