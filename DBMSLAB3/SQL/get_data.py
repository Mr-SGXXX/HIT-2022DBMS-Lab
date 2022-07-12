import time

from SQL.insert_data import connect_db, disconnect_db
import psycopg2
import psycopg2.extras


def Employee_login(EPhone, password):
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute("SELECT password from Employee where EPhone = %s", (EPhone,))
    end_time = time.time()
    row = cur.fetchone()
    if row[0].strip(' ') == password.strip():
        disconnect_db(conn)
        return end_time - start_time, True
    disconnect_db(conn)
    return end_time - start_time, False


def Employee_information():
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute("SELECT ename,sex,age,ephone,information from Employee where work = \'客服\'")
    end_time = time.time()
    rows = cur.fetchall()
    disconnect_db(conn)
    return end_time - start_time, rows


def Customer_login(CPhone, password):
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute("SELECT password, deleted from Customer where CPhone = %s", (CPhone,))
    end_time = time.time()
    row = cur.fetchone()
    if row[0].strip(' ') == password.strip() and not row[1]:
        disconnect_db(conn)
        return end_time - start_time, True
    disconnect_db(conn)
    return end_time - start_time, False


def get_customer_name_sex(phone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT cname, sex from Customer where CPhone = %s", (phone,))
    row = cur.fetchone()
    disconnect_db(conn)
    return row[0].strip(' '), row[1].strip(' ')


def get_customer_info(phone):
    conn = connect_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * from Customer where CPhone = %s", (phone,))
    row = cur.fetchone()
    for key, item in dict(row).items():
        row[key] = str(item).strip(' ')
    disconnect_db(conn)
    return row


def get_single_employee_info(phone):
    conn = connect_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    start_time = time.time()
    cur.execute("SELECT ename, sex, ephone, information from employee where ePhone = %s", (phone,))
    end_time = time.time()
    row = cur.fetchone()
    for key, item in dict(row).items():
        row[key] = str(item).strip(' ')
    disconnect_db(conn)
    return end_time - start_time, row


def get_account_house_info(phone):
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute(
        "SELECT location, area, is_renovated, value, sell_or_rent, price, moremsg, stime, hid from house where "
        "owner_phone = %s",
        (phone,))
    end_time = time.time()
    rows = cur.fetchall()
    rst_rows = []
    for row in rows:
        row_ = []
        for i in range(9):
            if row[i] is True:
                row_.append("是")
            elif row[i] is False:
                row_.append("否")
            elif row[i] is None:
                row_.append("")
            else:
                row_.append(str(row[i]).strip(' '))
        rst_rows.append(row_)
    disconnect_db(conn)
    return end_time - start_time, rst_rows


def get_sell_house_info():
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute("SELECT location, area, is_renovated, owner_phone, sell_or_rent, price, moremsg, stime, hid "
                "from house where owner_phone is not null and sell_or_rent is not null")
    end_time = time.time()
    rows = cur.fetchall()
    rst_rows = []
    for row in rows:
        row_ = []
        for i in range(9):
            if row[i] is True:
                row_.append("是")
            elif row[i] is False:
                row_.append("否")
            elif row[i] is None:
                row_.append("")
            else:
                row_.append(str(row[i]).strip(' '))
        rst_rows.append(row_)
    disconnect_db(conn)
    return end_time - start_time, rst_rows


def get_record(cphone):
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute(
        "select seller_phone, buyer_phone, record.sell_or_rent, location, area, is_renovated, record.price, rtime "
        "from record join house on record.hid = house.hid "
        "where seller_phone = %s or buyer_phone = %s", (cphone, cphone))
    end_time = time.time()
    rows = cur.fetchall()
    rst_rows = []
    for row in rows:
        row_ = []
        for i in range(8):
            if row[i] is True:
                row_.append("是")
            elif row[i] is False:
                row_.append("否")
            else:
                row_.append(str(row[i]).strip(' '))
        rst_rows.append(row_)
    disconnect_db(conn)
    return end_time - start_time, rst_rows


def get_buyer_info():
    conn = connect_db()
    cur = conn.cursor()
    start_time = time.time()
    cur.execute("SELECT cname, customer.cphone, buy_or_rent, area, price, more_msg, btime "
                "from customer join buyer_msg on buyer_msg.buyer_phone = customer.cphone")
    end_time = time.time()
    rows = cur.fetchall()
    disconnect_db(conn)
    return end_time - start_time, rows


def get_employee_title(ephone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("select work, ename from employee where ephone = %s", (ephone,))
    row = cur.fetchone()
    disconnect_db(conn)
    return row
