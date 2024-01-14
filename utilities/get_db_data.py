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


class EquipmentData(GetData):

    def __init__(self):
        super().__init__()

    def get_eq_description(self, id):
        table_name = 'equipment_equipment'
        column_name = "description"

        select_names_query = f"SELECT {column_name} FROM {table_name} WHERE id = {id}"

        self.cursor.execute(select_names_query)
        description = self.cursor.fetchone()[0]
        return description

    def get_eq_type(self, id):
        table_name = 'equipment_equipment'
        column_name = "type"

        select_names_query = f"SELECT {column_name} FROM {table_name} WHERE id = {id}"

        self.cursor.execute(select_names_query)
        eq_type = self.cursor.fetchone()[0]
        return eq_type

    def get_eq_acquisition_value(self, id):
        table_name = 'equipment_equipment'
        column_name = "acquisition_value"

        select_names_query = f"SELECT {column_name} FROM {table_name} WHERE id = {id}"

        self.cursor.execute(select_names_query)
        value = self.cursor.fetchone()[0]
        return value

    def get_currency(self, id):
        table_name = 'equipment_equipment'
        column_name = "currency_code"

        select_names_query = f"SELECT {column_name} FROM {table_name} WHERE id = {id}"

        self.cursor.execute(select_names_query)
        currency = self.cursor.fetchone()[0]
        return currency

    def get_manufacturer(self, id):
        table_name = 'equipment_equipment'
        column_name = "manufacturer"

        select_names_query = f"SELECT {column_name} FROM {table_name} WHERE id = {id}"

        self.cursor.execute(select_names_query)
        manufacturer = self.cursor.fetchone()[0]
        return manufacturer


class PlantsData(GetData):
    def __init__(self):
        super().__init__()

    def get_all_plants(self):
        table_name = 'plant_plant'
        column_name = "name"

        select_names_query = f"SELECT {column_name} FROM {table_name} ORDER BY id"

        self.cursor.execute(select_names_query)
        all_plants = self.cursor.fetchall()
        plants = [plant[0] for plant in all_plants]

        return list(plant for plant in plants)
