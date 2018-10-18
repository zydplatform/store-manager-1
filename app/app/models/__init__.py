
from flask import jsonify, abort
from datetime import datetime

time = str(datetime.now())

products = [{
            "product_id": 1,
            "product_name": "Mangoes",
            "product_category": "Fruits",
            "product_price": 500,
            "product_quantity": 34,
            "product_minimum_stock_allowed": 20
        }]