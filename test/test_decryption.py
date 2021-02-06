import unittest
import os

from simple_encryption.decryption import Decryptor as decryptor

class TestDecryption(unittest.TestCase):
    def test_key_load(self):
        demo_key_val = b'C0JMjOk24fFZTz4Fqm_y6m0iaLSVR_9HOPlf0BSgthI='
        if(os.path.exists('./.secrets') == False):
            os.mkdir('./.secrets')
        
        fd = os.open('./.secrets/test_key', os.O_RDWR|os.O_CREAT)
        os.write(fd, demo_key_val)
        decrypt = decryptor()
        key = decrypt.key_load('./.secrets/test_key')
        os.remove('./.secrets/test_key')
        self.assertAlmostEqual(key, demo_key_val, 'Test key load')