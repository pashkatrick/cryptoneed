import unittest
import os
import cryptoneed
from cryptoneed import __main__ as main
from click.testing import CliRunner

class Test_a_EncryptionMain(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('./test-dir'):
            os.mkdir('./test-dir')
        fd = os.open('./test-dir/test-file', os.O_RDWR|os.O_CREAT)
        os.write(fd, str.encode('This is a test-file'))
        
    def test_encrypt(self):
        runner = CliRunner()
        result = runner.invoke(main.encrypt, ['-r', './test-dir', '-K', 'BS3PoSwWZkfe1j9--nnrm2z-83Nt1k0fgXrzujYuhjc='])
        
        self.assertAlmostEqual(0, result.exit_code)


class Test_b_DecryptionMain(unittest.TestCase):
    def test_decrypt(self):
        runner = CliRunner()
        result = runner.invoke(main.decrypt, ['-r', './test-dir', '-K', 'BS3PoSwWZkfe1j9--nnrm2z-83Nt1k0fgXrzujYuhjc='])
        
        self.assertAlmostEqual(0, result.exit_code)
        
        fd = os.open('./test-dir/test-file', os.O_RDONLY)
        bytesRead = os.read(fd, 500)
        
        self.assertEqual(bytesRead.decode('utf-8'), 'This is a test-file')
    
    def tearDown(self):
        if(os.path.exists('./test-dir')):
            os.remove('./test-dir/test-file')
            os.rmdir('./test-dir')