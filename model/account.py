from db import db
from flask_restful import Resource, reqparse, abort, fields, marshal_with

class AccountModel(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable= False)
    balance = db.Column(db.Float, nullable= False)

    def __repr__(self):
        return f"Account(name= {name}, balance= {balance})"


class Account(Resource):

    account_put_args = reqparse.RequestParser()
    account_put_args.add_argument("name", type=str, help="Name of account holder is required.", required=True)
    account_put_args.add_argument("balance", type=float, help="Account Balance is required.", required=True)

    account_update_args = reqparse.RequestParser()
    account_update_args.add_argument("name", type=str)
    account_update_args.add_argument("balance", type=float)

    account_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'balance': fields.Float
}

    @marshal_with(account_fields)
    def get(self, account_id):
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="Could not find account with that id...")
        return result

    @marshal_with(account_fields)
    def put(self, account_id):
        args = self.account_put_args.parse_args()
        result = AccountModel.query.filter_by(id=account_id).first()
        if result:
            abort(409, message="Account Already exists....")
        account = AccountModel(id=account_id, name=args['name'], balance=args['balance'])
        db.session.add(account)
        db.session.commit()
        return account, 201

    @marshal_with(account_fields)
    def patch(self, account_id):
        args = self.account_update_args.parse_args()
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="Account doesn't exist, cannot update.")
        if args['name']:
            result.name = args['name']
        if args['balance']:
            result.balance = args['balance']

        db.session.commit()
        return result, 202