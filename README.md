# Cryptoneed
A simple CLI to encrypt and decrypt files using Python


## Installation

Use the following commands to install

Note - You might need root privilege to run this command

```bash
git clone https://github.com/pashkatrick/cryptoneed.git
cd cryptoneed
python3 setup.py install
```

## Usage

### Encryption

To encrypt source file
```bash
cryptoneed encyrpt <filename or path>
```
To encrypt source file to a destination file
```bash
cryptoneed encrypt <filename or filepath> -d <filename or path>
```
To encrypt source directory
```bash
cryptoneed encrypt -r <dirname or path>
```

To encrypt source directory to destination directory
```bash
cryptoneed encrypt -r <dirname or path> -d <dirname or path>
```

To encrypt only files in the root of a directory name
```bash
cryptoneed encrypt -r -f <dirname or path>
```

In the all the above examples a key was created by default and stored in the file ".secrets/enc_key"

To encrypt with your key
```bash
cryptoneed encrypt <filename or path> -K <your key>
```

To encrypt with your key stored in a file
```bash
cryptoneed encrypt <filename or path> -k <key filename or path>
```

### Decryption

To decrypt source file
```bash
cryptoneed decyrpt <filename or path>
```
To decrypt source file to a destination file
```bash
cryptoneed decrypt <filename or filepath> -d <filename or path>
```
To decrypt source directory
```bash
cryptoneed decrypt -r <dirname or path>
```

To decrypt source directory to destination directory
```bash
cryptoneed decrypt -r <dirname or path> -d <dirname or path>
```

To decrypt only files in the root of a directory name
```bash
cryptoneed decrypt -r -f <dirname or path>
```

In the all the above examples a key was extracted by default from the file ".secrets/enc_key", which was created during encryption without using your own key

To decrypt with your key
```bash
cryptoneed decrypt <filename or path> -K <your key>
```

To decrypt with your key stored in a file
```bash
cryptoneed decrypt <filename or path> -k <key filename or path>
```

## Note

Warning! This is a simple encryption tool and it is advised to use it with caution. Do backup your data before encrypting
