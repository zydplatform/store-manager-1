""" Handling Databases"""

import psycopg2

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
                id_number VARCHAR (15) NOT NULL, 
                full_name VARCHAR (50) NOT NULL, 
                username VARCHAR (30) NOT NULL, 
                password VARCHAR (50) NOT NULL,  
                admin BOOLEAN NOT NULL DEFAULT FALSE, 
                registered_by INT NOT NULL,  
                registered_on TIMESTAMP DEFAULT NOW());
            """,
            """ CREATE TABLE IF NOT EXISTS product_categories (
                category_id SERIAL NOT NULL PRIMARY KEY,  
                category_name VARCHAR (20) NOT NULL, 
                added_by INT NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT, 
                added_on TIMESTAMP DEFAULT NOW());
            """,
            """ CREATE TABLE IF NOT EXISTS products (
                product_id SERIAL NOT NULL PRIMARY KEY,  
                product_name VARCHAR (30) NOT NULL, 
                product_category INT NOT NULL REFERENCES product_categories(category_id) ON DELETE RESTRICT, 
                product_price INT NOT NULL,
                product_quantity INT NOT NULL,
                product_minimum_stock_allowed INT NOT NULL,
                added_by INT NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT, 
                added_on TIMESTAMP DEFAULT NOW());
            """,
            """ CREATE TABLE IF NOT EXISTS sales (
                sales_id SERIAL NOT NULL PRIMARY KEY,  
                products JSONB NOT NULL,
                total_cost INT NOT NULL, 
                seller INT NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT, 
                date_sold TIMESTAMP DEFAULT NOW());
            """
        )

        try:
            for query in querys:
                self.cursor.execute(query)
                
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)