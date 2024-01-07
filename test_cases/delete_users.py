import psycopg2
from psycopg2 import sql

dbname = 'mp_dp_updated'
user = 'postgres'
password = 'root'
host = '127.0.0.1'
port = '5433'
table_name = 'accounts_appuser'


def delete_users():
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = connection.cursor()

    delete_profile = sql.SQL(
        "DELETE FROM accounts_profile WHERE id NOT IN (SELECT id FROM accounts_profile ORDER BY id LIMIT 4)")
    cursor.execute(delete_profile)

    delete_users = sql.SQL(
        "DELETE FROM accounts_appuser WHERE id NOT IN (SELECT id FROM accounts_appuser ORDER BY id LIMIT 4)")
    cursor.execute(delete_users)

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    delete_users()
