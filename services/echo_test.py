from flask_restful import Resource, reqparse
from datetime import datetime as dt

class EchoTest(Resource):
    
    is_alive_parser = reqparse.RequestParser()
    is_alive_parser.add_argument("applicationId", type=str, required=True)
    is_alive_parser.add_argument("UUID", type=str, required=True)
    is_alive_parser.add_argument("tranDateTime", type=str, required=True)
    
    def post(self):
        args = self.is_alive_parser.parse_args()
        response = {
            "applicationId": args['applicationId'],   
            "responseMessage": "Approved",
            "responseCode": 0,
            "responseStatus": "Successful",
            "UUID": args['UUID'],
            "tranDateTime": dt.now().strftime("%d%m%y%H%M%S")
        }
        
        return response
