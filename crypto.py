from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
import schedule
import time


class Crypto():

    def __init__(self):
        self.key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=512
        )
        self._set_keystore()
        # schedule.every().day.at("00:00").do(self._set_keystore)
    
    def _set_keystore(self):
        
        self._private_key = self.key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption()
        )
        
        self._public_key = self.key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        )
        
        pem_public_key = self.key.public_key().public_bytes(
            encoding=crypto_serialization.Encoding.PEM,
            format=crypto_serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        private_key_file = open("private_key.pem", "w")
        private_key_file.write(self._private_key.decode())
        private_key_file.close()

        public_key_file = open("public_key.pub", "w")
        public_key_file.write(pem_public_key.decode())
        public_key_file.close()
        
    @property
    def private_key(self):
        return self._private_key
    
    @property
    def public_key(self):
        return self._public_key