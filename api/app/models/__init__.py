
from api.app.models.database import Database

MINIMUM_STOCK_ALLOWED = 10

db = Database()
db.create_tables()

products = [
                {
                    "product_id": 1,
                    "product_name": "Mangoes",
                    "product_category": "Fruits",
                    "product_price": 500,
                    "product_quantity": 34,
                    "product_minimum_stock_allowed": 20
                },
                {
                    "product_id": 2,
                    "product_name": "Cabbage",
                    "product_category": "Vegatables",
                    "product_price": 1500,
                    "product_quantity": 23,
                    "product_minimum_stock_allowed": 20
                }
            ]

product_categories = [
                        {
                            "category_id": 1,
                            "category_name": "Fruits"
                        },
                        {
                            "category_id": 2,
                            "category_name": "Drinks"
                        }
                    ]


attendants = [
                {
                    "attendant_id": 1,
                    "id_number": "A/2018/001",
                    "attendant_name": "Walujo Emmanuel",
                    "attendant_username" : "A/2018/001",
                    "attendant_password" : "A/2018/001"
                },
                {
                    "attendant_id": 2,
                    "id_number": "A/2018/002",
                    "attendant_name": "Edmon Walulo",
                    "attendant_username" : "A/2018/002",
                    "attendant_password" : "A/2018/002"
                }
            ]

        
sales = [
            {
                "sales_id": 1,
                "seller": "Walujo Emmanuel",
                "product": "aple",
                "price" : 1000,
                "quantity" : 2,
                "total_cost": 2000,
                "date_sold": "12/10/2018"
            },
            {
                "sales_id": 2,
                "seller": "Mukisa Amos",
                "product": "Mangoes",
                "price" : 500,
                "quantity" : 6,
                "total_cost": 3000,
                "date_sold": "10/10/2018"
            }
        ]