""" Handling Databases"""

import psycopg2
from werkzeug.security import generate_password_hash

class Database:
    """ Class For Handling Databases """

    def __init__(self):
        """ Connecting to the database """
        try:
            self.connection = psycopg2.connect(
                "dbname = 'storemanager' \
                user = 'andela' \
                host = 'localhost' \
                password = 'andela' \
                port = '5432'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("API can not connect to the database")

    def create_tables(self):
        """ Create all the required tables """
        querys = (
            """ CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL NOT NULL PRIMARY KEY,  
                full_name VARCHAR (30) NOT NULL, 
                email VARCHAR (30) NOT NULL UNIQUE, 
                password TEXT NOT NULL,  
                admin BOOLEAN NOT NULL DEFAULT FALSE, 
                registered_by INT NOT NULL,  
                registered_on TIMESTAMP DEFAULT NOW());
            """,
            """ CREATE TABLE IF NOT EXISTS product_categories (
                category_id SERIAL NOT NULL PRIMARY KEY,  
                category_name VARCHAR (20) NOT NULL UNIQUE, 
                added_by INT NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT, 
                added_on TIMESTAMP DEFAULT NOW());
            """,
            """ CREATE TABLE IF NOT EXISTS products (
                product_id SERIAL NOT NULL PRIMARY KEY,  
                product_name VARCHAR (30) NOT NULL UNIQUE, 
                product_category INT REFERENCES product_categories(category_id) ON DELETE RESTRICT, 
                product_price INT NOT NULL,
                product_quantity INT NOT NULL,
                product_minimum_stock_allowed INT NOT NULL,
                added_by INT NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT, 
                added_on TIMESTAMP DEFAULT NOW());
            """,
            """ CREATE TABLE IF NOT EXISTS sales (
                sales_id SERIAL NOT NULL PRIMARY KEY,  
                product INT NOT NULL,
                quantity INT NOT NULL, 
                seller INT NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT, 
                date_sold TIMESTAMP DEFAULT NOW());
            """
        )

        try:
            for query in querys:
                self.cursor.execute(query)
                
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_super_admin_account(self):
        """ Insert the first admin in the users table """

        try:

            get_registered_users_query = "SELECT * FROM users"
            self.cursor.execute(get_registered_users_query)
            registered_users = self.cursor.fetchall()

            if not registered_users:
                password = generate_password_hash("admin")
                register_admin = """
                    INSERT INTO users
                    (full_name, email, password, admin, registered_by)
                    VALUES (%s, %s, %s, %s, %s);
                """
                self.cursor.execute(register_admin, ("Administrator", "admin@api.com", password, True, 0))
                
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)