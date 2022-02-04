import requests
from datetime import datetime as dt
import uuid

BASE = "http://127.0.0.1:5000/"

request = {
   "applicationId": "1234APP",
   "UUID": uuid.uuid4(),
   "tranDateTime": dt.now().strftime("%d%m%y%H%M%S"),
   "PAN": "8888446754770886",
   "registrationType": "10",
   "entityId": "0912312123",
   "expDate": "1804",
   "entityGroup": "1",
   "fullName": "Ahmed Osman",
   "financialInstitutionId":"123",
   "IPIN": "Hj3unPtqZsWeUQtT0GYJbZU79MghhLir8YMzCgXm5Xr9e/WUk38AWWOhOl1xHxkAIVMbGhNetRnel0cOGpJUsA==",
   "userPassword": "P2qtkSKCNTS72X3pVal6sYJuU1/WloVcD92FNYGK8xTF0cnPzwcygcySTVujcNXyDVYZd3onMNkNFkdYN5Zgvg==",
   "entityType": "Phone No",
   "phoneNo": "0912399665",
   "email": "abc@xyz.com",
   "userName": "Mohammed",
   "mbr": "0",
   "extraInfo": "No extra info HAHAHAHA",
   "job" : "Engineer"
}

response = requests.post(BASE + "MCSConsumer/register", request)
print(response.json())