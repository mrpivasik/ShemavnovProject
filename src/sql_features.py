def get_list_of_users(db_connection):
    db_connection.execute("SELECT username FROM auth_user ;")
    users_l = []
    for i in db_connection.fetchall():
        users_l.append(i[0])
    return users_l


def check_user_in_db(db_connection, username):
    assert username in get_list_of_users(db_connection), "User was not found in db"
