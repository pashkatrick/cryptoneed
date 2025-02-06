import os
from cryptography.fernet import Fernet


class Encryptor:
    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def file_encrypt(self, key, original_file, encrypted_file):
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(encrypted_file, 'wb') as file:
            file.write(encrypted)

    def dir_encrypt(self, key, original_dir, encrypted_dir, only_files):
        if not os.path.exists(encrypted_dir):
            os.mkdir(encrypted_dir)

        item_list = os.listdir(original_dir)

        for item in item_list:
            item_path = os.path.join(original_dir, item)
            enc_item_path = os.path.join(encrypted_dir, item)

            if os.path.isdir(item_path):
                if not only_files:
                    self.dir_encrypt(key, item_path, enc_item_path, 0)
                else:
                    continue
            else:
                self.file_encrypt(key, item_path, enc_item_path)


# encrypt = Encryptor()
# key = encrypt.key_create()
# encrypt.key_write(key, 'enc_key')
# encrypt.file_encrypt(key, 'test-file.txt', 'encrypted-file.txt')
# encrypt.dir_encrypt(1234, './test-dir/', './enc-test-dir')
