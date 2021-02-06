import sys
import os
import click
from simple_encryption.encryption import Encryptor as encryptor
from simple_encryption.decryption import Decryptor as decryptor


@click.group()
@click.version_option("1.0.0")
def main():
    """CLI for encrypting and decrypting files"""
    pass


@main.command()
def create_key():
    """Create a key"""
    
    encrypt = encryptor()
    key = encrypt.key_create()
    
    print(str(key, 'utf-8'))
    pass
 

@main.command()
@click.option('-r', '--recursive/--no-recursive', required=False, default=False)
@click.option('-f', '--files/--not-files', required=False, default=False)
@click.argument('src', required=True)
@click.option('-d', '--dest')
@click.option('-k', '--keyname', default='enc_key')
@click.option('-K', '--key', required=False)
def decrypt(recursive, files, src, dest, keyname, key):
    """Decrypt file(s)"""
    
    decrypt = decryptor()
    if(key):
        KEY=key
    else:
        KEY = decrypt.key_load('./.secrets/' + keyname)
    
    if(dest):
        if(recursive):
            if(files):
                decrypt.dir_decrypt(KEY, src, dest, 1)
            else:
                decrypt.dir_decrypt(KEY, src, dest, 0)
        else:
            decrypt.file_decrypt(KEY, src, dest)
    else:
        if(recursive):
            if(files):
                decrypt.dir_decrypt(KEY, src, src, 1)
            else:
                decrypt.dir_decrypt(KEY, src, src, 0)
        else:
            decrypt.file_decrypt(KEY, src, src)
    pass


@main.command()
@click.option('-r', '--recursive/--no-recursive', required=False, default=False)
@click.option('-f', '--files/--not-files', required=False, default=False)
@click.argument('src', required=True)
@click.option('-d', '--dest')
@click.option('-k', '--keyname', default='enc_key')
@click.option('-K', '--key', required=False)
def encrypt(recursive, files, src, dest, keyname, key):
    """Encrypt file(s)"""
    
    encrypt =  encryptor()
    if(key):
        KEY = key
    else:
        KEY = encrypt.key_create()
        if(os.path.exists('./.secrets') == False):
            os.mkdir('./.secrets')
        encrypt.key_write(KEY, './.secrets/' + keyname)
    
    if(dest):
        if(recursive):
            if(files):
                encrypt.dir_encrypt(KEY, src, dest, 1)
            else:
                encrypt.dir_encrypt(KEY, src, dest, 0)
        else:
            encrypt.file_encrypt(KEY, src, dest)
    else:
        if(recursive):
            if(files):
                encrypt.dir_encrypt(KEY, src, src, 1)
            else:
                encrypt.dir_encrypt(KEY, src, src, 0)
        else:
            encrypt.file_encrypt(KEY, src, src)
    pass


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Simple Encryption CLI")
    main()