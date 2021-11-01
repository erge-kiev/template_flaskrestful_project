import config

from flask import Flask
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.resources.smoke import Smoke

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# Add routes here
# api.add_resource(Foo, '/Foo', '/Foo/<string:id>')
api.add_resource(Smoke, '/smoke', strict_slashes=False)
