import os
from cryptography.fernet import Fernet

class Decryptor():
    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key
    
    
    def file_decrypt(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)
            
    
    def dir_decrypt(self, key, encrypted_dir, decrypted_dir, only_files):
        if(os.path.exists(decrypted_dir) == False):
            os.mkdir(decrypted_dir)
        
        item_list = os.listdir(encrypted_dir)
        
        for item in item_list:
            item_path = os.path.join(encrypted_dir, item)
            dec_item_path = os.path.join(decrypted_dir, item)
            
            if(os.path.isdir(item_path)):
                if(only_files == False):
                    self.dir_decrypt(key, item_path, dec_item_path, 0)
                else:
                    continue
            else:
                self.file_decrypt(key, item_path, dec_item_path)


# decryptor = Decryptor()
# key = decryptor.key_load('enc_key')
# decryptor.file_decrypt(key, 'encrypted-file.txt', 'decrypted-file.txt')