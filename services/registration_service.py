from flask_restful import Resource, reqparse, abort, fields, marshal_with
from datetime import datetime as dt
from model.entity import EntityModel
from services.helper_fields import help_fields
from db import db

class Registration(Resource):
    entity_fields = {
        "entityId" : fields.String,
        "entityType" : fields.String,
        "entityGroup" : fields.String,
        "userName" : fields.String,
        "userPassword" : fields.String,
        "phoneNo" : fields.String,
        "financialInstitutionId" : fields.String,
        "PAN" : fields.String,
        "IPIN" : fields.String,
        "mbr" : fields.String,
        "expDate" : fields.String,
        "panCategory" : fields.String,
        "registrationType" : fields.String,
        "fullName" : fields.String,
        "dateOfBirth" : fields.String,
        "customerIdNumber" : fields.String, 
        "customerIdType" : fields.String,
        "bankAccountNumber" : fields.String,
        "bankAccountType" : fields.String,
        "bankBranchId" : fields.String,
        "job" : fields.String,
        "email" : fields.String,
        "extraInfo" : fields.String,
        }
    
    registration_post_args = reqparse.RequestParser()
    registration_post_args.add_argument("applicationId", type=str, help=help_fields['applicationId'], required=True)
    registration_post_args.add_argument("tranDateTime", type=str, help=help_fields['tranDateTime'], required=True)
    registration_post_args.add_argument("UUID", type=str, help=help_fields['UUID'], required=True)
    registration_post_args.add_argument("entityId", type=str, help=help_fields['entityID'], required=True)
    registration_post_args.add_argument("entityType", type=str, help=help_fields['entityType'], required=True)
    registration_post_args.add_argument("entityGroup", type=str, help=help_fields['entityGroup'], required=True)
    registration_post_args.add_argument("userName", type=str, help=help_fields['userName'], required=False, default=None)
    registration_post_args.add_argument("userPassword", type=str, help=help_fields['userPassword'], required=False, default=None)
    registration_post_args.add_argument("phoneNo", type=str, help=help_fields['phoneNo'], required=False, default=None)
    registration_post_args.add_argument("financialInstitutionId", type=str, help=help_fields['financialInstitutionId'], required=False, default=None)
    registration_post_args.add_argument("PAN", type=str, help=help_fields['PAN'], required=False, default=None)
    registration_post_args.add_argument("IPIN", type=str, help=help_fields['IPIN'], required=False, default=None)
    registration_post_args.add_argument("mbr", type=str, help=help_fields['mbr'], required=False, default=None)
    registration_post_args.add_argument("expDate", type=str, help=help_fields['expDate'], required=False, default=None)
    registration_post_args.add_argument("panCategory", type=str, help=help_fields['panCategory'], required=False, default=None)
    registration_post_args.add_argument("registrationType", type=str, help=help_fields['registrationType'], required=True)
    registration_post_args.add_argument("fullName", type=str, help=help_fields['fullName'], required=False, default=None)
    registration_post_args.add_argument("dateOfBirth", type=str, help=help_fields['dateOfBirth'], required=False, default=None)
    registration_post_args.add_argument("customerIdNumber", type=str, help=help_fields['customerIdNumber'], required=False, default=None)
    registration_post_args.add_argument("customerIdType", type=str, help=help_fields['customerIdType'], required=False, default=None)
    registration_post_args.add_argument("bankAccountNumber", type=str, help=help_fields['bankAccountNumber'], required=False, default=None)
    registration_post_args.add_argument("bankAccountType", type=str, help=help_fields['bankAccountType'], required=False, default=None)
    registration_post_args.add_argument("bankBranchId", type=str, help=help_fields['bankBranchId'], required=False, default=None)
    registration_post_args.add_argument("job", type=str, help=help_fields['job'], required=False, default=None)
    registration_post_args.add_argument("email", type=str, help=help_fields['email'], required=False, default=None)
    registration_post_args.add_argument("extraInfo", type=str, help=help_fields['extraInfo'], required=False, default=None)
        
    
    
    @marshal_with(entity_fields)
    def post(self):
        args = self.registration_post_args.parse_args()
        result = EntityModel.query.filter_by(entityId=args['entityId']).first()
        if result:
            abort(409, message="Entity Already exists....")
        entity = EntityModel(entityId = args['entityId'],
                    entityType = args['entityType'],
                    entityGroup = args['entityGroup'],
                    userName = args['userName'],
                    userPassword = args['userPassword'],
                    phoneNo = args['phoneNo'],
                    financialInstitutionId = args['financialInstitutionId'],
                    PAN = args['PAN'],
                    IPIN = args['IPIN'],
                    mbr = args['mbr'],
                    expDate = args['expDate'],
                    panCategory = args['panCategory'],
                    registrationType = args['registrationType'],
                    fullName = args['fullName'],
                    dateOfBirth = args['dateOfBirth'],
                    customerIdNumber = args['customerIdNumber'],
                    customerIdType = args['customerIdType'],
                    bankAccountNumber = args['bankAccountNumber'],
                    bankAccountType = args['bankAccountType'],
                    bankBranchId = args['bankBranchId'],
                    job = args["job"],
                    email = args['email'],
                    extraInfo = args['extraInfo'])
        db.session.add(entity)
        db.session.commit()
        return {
            "PAN": entity['PAN'],
            "responseCode": 0,
            "registrationType": entity['registrationtype'],
            "UUID": args['UUID'],
            "applicationId": args['applicationID'],
            "entityId": entity['entityId'],
            "expDate": entity['expDate'],
            "entityGroup": entity['entityGroup'],
            "entityType": entity['entityType'],
            "tranDateTime": dt.now().strftime("%d%m%y%H%M%S"),
            "phoneNo": entity['phoneNo'],
            "responseMessage": "Approved",
            "email": entity['email'],
            "responseStatus": "Successful",
            "userName": entity['userName'],
            "extraInfo": entity['extraInfo'],
            "mbr": entity['mbr']
            }, 201