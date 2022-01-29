from flask import Flask
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
from model.account import Account

from services import public_key_service

from crypto import Crypto



app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


api.add_resource(Account, "/account/<int:account_id>")
api.add_resource(public_key_service.GetPublicKey, "/MCSConsumer/getPublicKey")

crypto_instance = Crypto()


if __name__ == "__main__":
    from db import db
    db.init_app(app)

    app.run(debug=True)