import psycopg2


class GetData:
    dbname = 'mp_dp_updated'
    user = 'postgres'
    password = 'root'
    host = '127.0.0.1'
    port = '5433'

    def __init__(self):
        self.cursor = self.connect_to_database()

    def connect_to_database(self):
        connection = psycopg2.connect(dbname=self.dbname,
                                      user=self.user,
                                      password=self.password,
                                      host=self.host,
                                      port=self.port
                                      )
        cursor = connection.cursor()
        return cursor

    def get_all_plants(self):
        table_name = 'plant_plant'
        column_name = "name"

        select_names_query = f"SELECT {column_name} FROM {table_name} ORDER BY id"

        self.cursor.execute(select_names_query)
        all_plants = self.cursor.fetchall()
        plants = [plant[0] for plant in all_plants]

        return list(plant for plant in plants)

    def get_all_users(self):
        table_name = 'accounts_profile'
        pass

    def get_all_departments(self):
        pass

    def get_all_equipment(self):
        pass
