import psycopg2


def db_connection():
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='postgres', host='localhost')
    cursor = conn.cursor()
    return cursor


def get_list_of_users():
    cursor = db_connection()
    cursor.execute("SELECT username FROM auth_user ;")
    users_l = []
    for i in cursor.fetchall():
        users_l.append(i[0])
    cursor.close()
    return users_l
