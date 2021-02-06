import unittest
import os

from simple_encryption.encryption import Encryptor as encryptor

class TestEncryption(unittest.TestCase):
    def test_key_create(self):
        demo_key_val = b'C0JMjOk24fFZTz4Fqm_y6m0iaLSVR_9HOPlf0BSgthI'
        encrypt = encryptor()
        key = encrypt.key_create()
        self.assertIs(type(key), type(demo_key_val), "Test key create")
        
    def test_key_write(self):
        encrypt = encryptor()
        demo_key_val = b'C0JMjOk24fFZTz4Fqm_y6m0iaLSVR_9HOPlf0BSgthI'
        if(os.path.exists('./.secrets') == False):
            os.mkdir('./.secrets')
        encrypt.key_write(demo_key_val, './.secrets/test_key')
        
        fd = os.open('./.secrets/test_key', os.O_RDWR)
        read_bytes = os.read(fd, 45)
        
        os.remove('./.secrets/test_key')
        self.assertAlmostEqual(demo_key_val, read_bytes)