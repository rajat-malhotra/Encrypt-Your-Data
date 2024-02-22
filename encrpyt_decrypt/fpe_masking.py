import pandas as pd
import os
from botocore.exceptions import ClientError
from botocore.session import Session
from java.math import BigInteger
from javax.crypto import Cipher as JavaCipher
from org.bouncycastle.crypto.engines import FPEngine
from org.bouncycastle.crypto.params import FF1Parameters, KeyParameter

class FPEMasking:
    def __init__(self, kms_key_id):
        self.kms_key_id = kms_key_id
        self.kms = Session().create_client('kms')

    def _generate_data_key(self, key_id, key_spec='AES_256'):
        try:
            response = self.kms.generate_data_key(
                KeyId=key_id,
                KeySpec=key_spec
            )
            plaintext_key = response['Plaintext']
            encrypted_key = response['CiphertextBlob']
            return plaintext_key, encrypted_key
        except ClientError as e:
            print(f"Error generating data key: {e}")
            raise e

    def _encrypt_field(self, field_value, data_key):
        # Generate FF1 parameters with provided data key
        # For demonstration purposes, we're using some hardcoded parameters
        parameters = FF1Parameters.Builder(BigInteger(data_key), 10, "Tweak".encode('utf-8')).withDomain("domain".encode('utf-8')).withRange("range".encode('utf-8')).build()
        
        # Create FF1 engine with parameters
        engine = FPEngine(FPEngine.ALGORITHM_FF1)
        engine.init(True, parameters)
        
        # Convert field value to bytes and encrypt using FF1 engine
        plaintext_bytes = field_value.encode('utf-8')
        ciphertext_bytes = engine.processBlock(plaintext_bytes, 0, len(plaintext_bytes))

        # Return encrypted value as string
        return ''.join(map(chr, ciphertext_bytes))

   