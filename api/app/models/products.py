""" Products file for handling product operations """

from api.app.models.database import Database

class Product(Database):
    """ Product Class for handling stock products """

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
                                    if product[1].lower() == product_name.lower()
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

    def get_all_products(self):
        """ get all products from database """

        get_products_query = "SELECT * FROM products"
        self.cursor.execute(get_products_query)
        all_products = self.cursor.fetchall()

        if all_products == None:
            return {}
        
        products = []

        for product in all_products:
            product_details = {
                "product_id" : product[0],
                "product_name" : product[1],
                "product_category" : product[2],
                "product_price" : product[3],
                "product_quantity" :  product[4],
                "product_minimum_stock_allowed" : product[5],
                "added_by" : product[6],
                "added_on" : product[7]
            }
            products.append(product_details)

        return products

    def get_a_product_by_id(self, product_id):
        """ get a specific product from the database """

        get_a_product_query = "SELECT * FROM products WHERE product_id = %s"
        self.cursor.execute(get_a_product_query, str(product_id))
        product_details = self.cursor.fetchone()
            
        if product_details == None:
            return {}
        
        product = {
            "product_id" : product_details[0],
            "product_name" : product_details[1],
            "product_category" : product_details[2],
            "product_price" : product_details[3],
            "product_quantity" :  product_details[4],
            "product_minimum_stock_allowed" : product_details[5],
            "added_by" : product_details[6],
            "added_on" : product_details[7]
        }

        return product

    def update_product(self, product_id, product_name, 
        product_category, product_price, product_quantity, 
        product_minimum_stock_allowed, added_by):
        """ modify a specific product details """

        get_a_product_query = "SELECT * FROM products WHERE product_id = %s"
        self.cursor.execute(get_a_product_query, str(product_id))
        product_details = self.cursor.fetchone()
        product = product_details[1]

        if len(product) == 0:
            return False
        else:
            update_product_query = """
                UPDATE products SET 
                product_name = %s,
                product_category = %s, 
                product_price = %s,
                product_quantity = %s,
                product_minimum_stock_allowed = %s,
                added_by = %s
                WHERE product_id = %s
            """

            self.cursor.execute(update_product_query, (product_name, product_category, 
                product_price, product_quantity, product_minimum_stock_allowed, 
                added_by, product_id))

            self.connection.commit()

            return product     

    def remove_a_specific_product(self, product_id):
        """ delete or remove a specific product """

        get_a_product_query = "SELECT * FROM products WHERE product_id = %s"
        self.cursor.execute(get_a_product_query, str(product_id))
        product = self.cursor.fetchone()
        product_name = product[1]

        delete_a_product_query = "DELETE FROM products WHERE product_id = %s"
        self.cursor.execute(delete_a_product_query, str(product_id))
        self.connection.commit()

        return product_name  

class ProductCategory(Database):
    """ Product Category Class for handling product category """

    def __init__(self):
        """ Initalizing the product category """
        
        super().__init__()


    def add_product_category(self, category_name, added_by):
        category = {
            "category_name" : category_name
        }

        get_all_product_categoriess_query = "SELECT * FROM product_categories"

        self.cursor.execute(get_all_product_categoriess_query)

        product_categories = self.cursor.fetchall()

        if category in product_categories or [
                                    product_category for product_category in product_categories
                                    if product_category[1].lower() == category_name.lower()
                                ]:
            return False

        else:
            add_product_category_query = """
                INSERT INTO product_categories
                (category_name, added_by)
                VALUES (%s, %s);
            """
            self.cursor.execute(add_product_category_query, 
                (category_name, added_by)
            )
            self.connection.commit()
            return True   

    
    def get_all_product_categories(self):
        """ get all product categories from database """

        get_categories_query = "SELECT * FROM product_categories"
        self.cursor.execute(get_categories_query)
        all_product_categories = self.cursor.fetchall()

        if all_product_categories == None:
            return {}
        
        product_categories = []

        for product_category in all_product_categories:
            category = {
                "category_id" : product_category[0],
                "category_name" : product_category[1],
                "added_by" : product_category[2],
                "added_on" : product_category[3]
            }
            product_categories.append(category)

        return product_categories
    
    def get_a_product_category_by_id(self, category_id):
        """ get a specific product category from the database """

        get_a_product_category_query = "SELECT * FROM product_categories WHERE category_id = %s"
        self.cursor.execute(get_a_product_category_query, str(category_id))
        product_category_details = self.cursor.fetchone()
            
        if product_category_details == None:
            return {}
        
        product_category = {
            "category_id" : product_category_details[0],
            "category_name" : product_category_details[1],
            "added_by" : product_category_details[2],
            "added_on" : product_category_details[3]
        }

        return product_category

    def update_product_category(self, category_id, category_name, added_by):
        """ modify a specific product category details """

        get_a_product_category_query = "SELECT * FROM product_categories WHERE category_id = %s"
        self.cursor.execute(get_a_product_category_query, str(category_id))
        product_category_details = self.cursor.fetchone()

        if len(product_category_details) == 0:
            return False
        else:
            update_product_category_query = """
                UPDATE product_categories SET 
                category_name = %s,
                added_by = %s
                WHERE category_id = %s
            """

            self.cursor.execute(update_product_category_query, (category_name, added_by, category_id))

            self.connection.commit()

            return product_category_details[1]

    def remove_a_specific_product_category(self, category_id):
        """ delete or remove a specific product category """

        get_a_product_category_query = "SELECT * FROM product_categories WHERE category_id = %s"
        self.cursor.execute(get_a_product_category_query, str(category_id))
        product_category = self.cursor.fetchone()
        product_category_name = product_category[1]

        delete_a_product_category_query = "DELETE FROM product_categories WHERE category_id = %s"
        self.cursor.execute(delete_a_product_category_query, str(category_id))
        self.connection.commit()
        
        return product_category_name