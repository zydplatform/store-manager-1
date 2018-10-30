

class Sales:

    def __init__(self, seller, product, price, quantity, total_cost, date_sold):
        self.seller = seller
        self.product = product
        self.price = price
        self.quantity = quantity
        self.total_cost = total_cost
        self.date_sold = date_sold

    def make_sale(self):
        sale = {
            "sales_id" : len(sales) + 1,
            "seller" : self.seller,
            "product" : self.product,
            "price" : self.price,
            "quantity" : self.quantity,
            "total_cost" : self.total_cost,
            "date_sold" : self.date_sold
        }

        sales.append(sale)
        return True
    
    def modify_sale(self, sale):
        if len(sale) == 0:
            return False
        else:

            if sale[0]["seller"] != self.seller:
                sale[0]["seller"] = self.seller

            if sale[0]["product"] != self.product:
                sale[0]["product"] = self.product

            if sale[0]["price"] != self.price:
                sale[0]["price"] = self.price

            if sale[0]["quantity"] != self.quantity:
                sale[0]["quantity"] = self.quantity

            if sale[0]["total_cost"] != self.total_cost:
                sale[0]["total_cost"] =  self.total_cost

            if sale[0]["date_sold"] != self.date_sold:
                sale[0]["date_sold"] =  self.date_sold

            return True
