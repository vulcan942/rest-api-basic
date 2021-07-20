from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import os
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///data.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.debug = True
app.config["SECRET_KEY"] = "nishant"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    app.run()
