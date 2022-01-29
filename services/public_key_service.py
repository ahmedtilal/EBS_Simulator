from flask_restful import Resource, reqparse
from datetime import datetime as dt

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class GetPublicKey(Resource):
    
    public_key_parser = reqparse.RequestParser()
    public_key_parser.add_argument("applicationId", type=str, required=True)
    public_key_parser.add_argument("UUID", type=str, required=True)
    public_key_parser.add_argument("tranDateTime", type=str, required=True)

    def load_keys(self):
        with open("public_key.pub", "r") as f:
            public = f.read()
            public = public.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "").replace("\n", "")
        with open("private_key.pem", "r") as f:
            private = f.read()
            private = private.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "").replace("\n", "")
            
        self.public = public
        self.private = private
    
    def post(self):
        self.load_keys()
        args = self.public_key_parser.parse_args()
        response = {
            "responseMessage": "Approved",
            "responseCode": 0,
            "responseStatus": "Successful",
            "applicationId": "<APPLICATION_ID>",
            "UUID": "9abb80ac-2c07-4dfa-a572-00cd35a11761",
            "pubKeyValue": "",
            "tranDateTime": "040318135553"
            }
        response["applicationId"] = args["applicationId"]
        response["pubKeyValue"] = self.public

        return response