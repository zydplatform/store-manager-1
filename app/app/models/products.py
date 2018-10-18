
from app.models import  products

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

