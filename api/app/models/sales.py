""" Sales file for handling sales operations """

from api.app.models.database import Database

db = Database()

class Sale:
    """ Sales Class for handling product sales """

    def __init__(self, products, quantity, seller):
        """ Initalizing the sales """
        
        self.products = products
        self.quantity = quantity
        self.seller = seller

    def make_sale(self):
        """ make sales """

        get_product_quantity = "SELECT * FROM products WHERE product_id = %s"
        db.cursor.execute(get_product_quantity, (self.products,))
        product_quantity = db.cursor.fetchone()        

        if product_quantity == None:
            return False
        else:
            remaining_products = product_quantity[4] - self.quantity
            
            make_sale_query = """
                INSERT INTO sales
                (product, quantity, seller)
                VALUES (%s, %s, %s);
            """
            db.cursor.execute(make_sale_query, 
                (self.products, self.quantity, self.seller)
            )
            db.connection.commit()

            update_product_query = """
                UPDATE products SET product_quantity = %s
                WHERE product_id = %s
            """
            db.cursor.execute(update_product_query, 
                (remaining_products, self.products)
            )
            db.connection.commit()

            get_made_sale = """
                SELECT * FROM sales WHERE sales_id = currval(pg_get_serial_sequence('sales','sales_id'));
            """
            db.cursor.execute(get_made_sale)
            made_sale = db.cursor.fetchone()

            made_sale_details = {
                "sales_id" : made_sale[0],
                "product" : made_sale[1],
                "quantity" : made_sale[2],
                "seller" : made_sale[3],
                "date_sold" : made_sale[4]
            }

            return made_sale_details

    def get_all_sales(self):
        """ get all sales  """
        
        get_sales_query = "SELECT * FROM sales"
        db.cursor.execute(get_sales_query)
        all_sales = db.cursor.fetchall()

        if all_sales == None:
            return {}
        
        sales_records = []

        for sales_details in all_sales:
            sale = {
                "sales_id" : sales_details[0],
                "product" : sales_details[1],
                "quantity" : sales_details[2],
                "seller" : sales_details[3],
                "date_sold" : sales_details[4]
            }
            sales_records.append(sale)

        return sales_records

    def get_aspecific_sales_record(self, sales_id):
        """ get a specific sales record"""

        get_sales_record_query = "SELECT * FROM sales WHERE sales_id = %s"
        db.cursor.execute(get_sales_record_query, (sales_id,))
        sales_record = db.cursor.fetchone()

        if sales_record == None:
            return {}
        
        sales_record_details = {
            "sales_id" : sales_record[0],
            "product" : sales_record[1],
            "quantity" : sales_record[2],
            "seller" : sales_record[3],
            "date_sold" : sales_record[4]
        }

        return sales_record_details
    
