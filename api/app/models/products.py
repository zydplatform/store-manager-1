""" Products file for handling user operations """

from api.app.models.database import Database

class Product(Database):
    """ User Class for handling stock products """

    def __init__(self):
        """ Initalizing the product """

        super().__init__()

    def add_product(self, product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed, added_by):
        product = {
            "product_name" : product_name,
            "product_category" : product_category,
            "product_price" : product_price,
            "product_quantity" : product_quantity,
            "product_minimum_stock_allowed" : product_minimum_stock_allowed
        }

        get_all_products_query = "SELECT * FROM products"

        self.cursor.execute(get_all_products_query)

        products = self.cursor.fetchall()

        if product in products or [
                                    product for product in products
                                    if product[1] == product_name
                                ]:
            return False

        else:
            add_product_query = """
                INSERT INTO products
                (product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed, added_by)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            self.cursor.execute(add_product_query, 
                (product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed, added_by)
            )
            self.connection.commit()
            return True   