
from api.app import app
from api.app.models.database import Database
from api.app.views import main, users


if __name__ == '__main__':
    app.run()