

from flask import jsonify
from api.app.models import  products, product_categories
from api.app.models.database import Database

class ProductCategories(Database):

    def __init__(self, category_name):
        self.category_name = category_name

    def add_product_category(self):

        try:
            get_added_products_query = "SELECT * FROM product_categories"
            self.cursor.execute(get_added_products_query)
            product_categories = self.cursor.fetchall()

            if self.category_name in product_categories:
                return False
            else:
                add_product_category_query = """
                        INSERT INTO product_categories
                        (category_name, added_by)
                        VALUES(self.category_name, 1)
                    """
                self.cursor.execute(add_product_category_query)
                return True
            
        except:
            return False
        


    def update_product_category(self, category):
        if len(category) == 0:
            return False
        else:
            if category[0]["category_name"] != self.category_name:
                category[0]["category_name"] = self.category_name

            return True

class Products(Database):

    def __init__(self, product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed):
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_minimum_stock_allowed = product_minimum_stock_allowed

    def add_product(self):
        product = {
            "product_id" : len(products) + 1,
            "product_name" : self.product_name,
            "product_category" : self.product_category,
            "product_price" : self.product_price,
            "product_quantity" : self.product_quantity,
            "product_minimum_stock_allowed" : self.product_minimum_stock_allowed
        }

        if product in products or [
                                    product for product in products
                                    if product["product_name"] ==  self.product_name
                                    and product["product_category"] ==  self.product_category
                                    and product["product_price"] == self.product_price
                                    and product["product_quantity"] ==  self.product_quantity
                                    and product["product_minimum_stock_allowed"] ==  self.product_minimum_stock_allowed
                                ]:
            return False

        else:
            products.append(product)
            return True
    
    def update_product(self, product):
        if len(product) == 0:
            return False
        else:
            product[0]["product_name"] = self.product_name
            product[0]["product_category"] = self.product_category
            product[0]["product_price"] = self.product_price
            product[0]["product_quantity"] = self.product_quantity
            product[0]["product_minimum_stock_allowed"] =  self.product_minimum_stock_allowed
            return True

