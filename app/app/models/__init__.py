
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
                            "category_name": "Fruits"
                        },
                        {
                            "category_name": "Drinks"
                        }
                    ]