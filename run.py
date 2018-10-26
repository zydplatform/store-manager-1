
from api.app import app
from api.app.views import main, users, products, sales


if __name__ == '__main__':
    app.run()