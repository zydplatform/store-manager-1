
from api.app.models.database import Database

MINIMUM_STOCK_ALLOWED = 10

db = Database()
db.create_tables()
db.create_super_admin_account()