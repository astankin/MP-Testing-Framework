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


class UserData(GetData):
    TABLE_NAME = "accounts_appuser"
    COLUM_ID = "id"
    COLUM_USERNAME = 'username'
    COLUM_FIRST_NAME = "first_name"
    COLUM_LAST_NAME = "last_name"
    COLUM_EMAIL = "email"
    COLUM_ROLE = "role"

    def __init__(self):
        super().__init__()

    def get_last_user_id(self):
        select_users = f"SELECT {self.COLUM_ID} FROM {self.TABLE_NAME} ORDER BY id DESC"
        self.cursor.execute(select_users)
        last_created_user_id = self.cursor.fetchone()[0]
        return last_created_user_id

    def get_user_username(self, user_id):
        select_user = f"SELECT {self.COLUM_USERNAME} FROM {self.TABLE_NAME} WHERE id = {user_id}"
        self.cursor.execute(select_user)
        username = self.cursor.fetchone()[0]
        return username

    def get_first_name(self, user_id):
        select_user = f"SELECT {self.COLUM_FIRST_NAME} FROM {self.TABLE_NAME} WHERE id = {user_id}"
        self.cursor.execute(select_user)
        first_name = self.cursor.fetchone()[0]
        return first_name

    def get_last_name(self, user_id):
        select_user = f"SELECT {self.COLUM_LAST_NAME} FROM {self.TABLE_NAME} WHERE id = {user_id}"
        self.cursor.execute(select_user)
        last_name = self.cursor.fetchone()[0]
        return last_name

    def get_email(self, user_id):
        select_user = f"SELECT {self.COLUM_EMAIL} FROM {self.TABLE_NAME} WHERE id = {user_id}"
        self.cursor.execute(select_user)
        email = self.cursor.fetchone()[0]
        return email

    def get_role(self, user_id):
        select_user = f"SELECT {self.COLUM_ROLE} FROM {self.TABLE_NAME} WHERE id = {user_id}"
        self.cursor.execute(select_user)
        role = self.cursor.fetchone()[0]
        return role


if __name__ == "__main__":
    data = UserData()
    user_id = data.get_last_user_id()
    print(data.get_user_username(user_id))
    print(data.get_first_name(user_id))
