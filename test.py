import requests

BASE = "http://127.0.0.1:5000/"

data = {"balance": 300.0}
response = requests.patch(BASE + "account/2", data)
print(response.json())

input()

request = {
   "applicationId": "1234APP",
   "UUID": "9abb80ac-2c07-4dfa-a572-00cd35a11761",
   "tranDateTime": "040318135553"
   
}

response = requests.post(BASE + "MCSConsumer/getPublicKey", request)
print(len(response.json()['pubKeyValue']))
print(len("MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJ4HwthfqXiK09AgShnnLqAqMyT5VUV0hvSdG+ySMx+a54Ui5EStkmO8iOdVG9DlWv55eLBoodjSfd0XRxN7an0CAwEAAQ=="))
