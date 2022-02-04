from db import db
from flask_restful import Resource, reqparse, abort, fields, marshal_with

class EntityModel(db.Model):
    entityId = db.Column(db.String(30), primary_key= True)
    entityType = db.Column(db.String(20), nullable=False)
    entityGroup = db.Column(db.String(1), nullable=False)
    userName = db.Column(db.String(30))
    userPassword = db.Column(db.String)
    phoneNo = db.Column(db.String(14), nullable=False)
    financialInstitutionId = db.Column(db.String(4), nullable=False)
    PAN = db.Column(db.String(19), nullable=False)
    IPIN = db.Column(db.String(4), nullable=False)
    mbr = db.Column(db.String(3))
    expDate = db.Column(db.String(4))
    panCategory = db.Column(db.String(10))
    registrationType = db.Column(db.String(2), nullable=False)
    fullName = db.Column(db.String(255), nullable= False)
    dateOfBirth = db.Column(db.String(10))
    customerIdNumber = db.Column(db.String(40))
    customerIdType = db.Column(db.String(36))
    bankAccountNumber = db.Column(db.String(36))
    bankAccountType = db.Column(db.String(12))
    bankBranchId = db.Column(db.String(3))
    job = db.Column(db.String(50))
    email = db.Column(db.String(50))
    extraInfo = db.Column(db.String(255))
    

    def __repr__(self):
        # TODO: Rewrite __repr__ function.
        return f"Account()"



class Account(Resource):
    # TODO: Rewrite class.
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