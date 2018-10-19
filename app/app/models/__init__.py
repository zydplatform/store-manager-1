
from flask import jsonify, abort
from datetime import datetime

time = str(datetime.now())

MINIMUM_STOCK_ALLOWED = 10

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