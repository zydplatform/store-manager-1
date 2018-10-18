
from app.models import  products, product_categories

class Products:

    def __init__(self, product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed):
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_minimum_stock_allowed = product_minimum_stock_allowed

    def add_product(self):
        product = {
            "product_id" : products[-1]["product_id"]+1,
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
            if product[0]["product_name"] != self.product_name:
                product[0]["product_name"] = self.product_name

            if product[0]["product_category"] != self.product_category:
                product[0]["product_category"] = self.product_category

            if product[0]["product_price"] != self.product_price:
                product[0]["product_price"] = self.product_price

            if product[0]["product_quantity"] != self.product_quantity:
                product[0]["product_quantity"] = self.product_quantity

            if product[0]["product_minimum_stock_allowed"] != self.product_minimum_stock_allowed:
                product[0]["product_minimum_stock_allowed"] =  self.product_minimum_stock_allowed

            return True


class ProductCategories:

    def __init__(self, category_name):
        self.category_name = category_name

    def add_product_category(self):
        category = {
            "category_id" : product_categories[-1]["category_id"]+1,
            "category_name" : self.category_name
        }

        if category in product_categories or [
                                    category for category in product_categories
                                    if category["category_name"] ==  self.category_name
                                ]:
            return False

        else:
            product_categories.append(category)
            return True


    def update_product_category(self, category):
        if len(category) == 0:
            return False
        else:
            if category[0]["category_name"] != self.category_name:
                category[0]["category_name"] = self.category_name

            return True