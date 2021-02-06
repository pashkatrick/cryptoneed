# Simple Encryption
A simple CLI to encrypt and decrypt files using Python


## Installation

Use the following commands to install

Note - You might need root privilege to run this command

```bash
$ python3 setup.py install
```

## Usage

### Encryption

To encrypt source file
```bash
$ simple_encryption encyrpt <filename or path>
```
To encrypt source file to a destination file
```bash
$ simple_encryption encrypt <filename or filepath> -d <filename or path>
```
To encrypt source directory
```bash
$ simple_encryption encrypt -r <dirname or path>
```

To encrypt source directory to destination directory
```bash
$ simple_encryption encrypt -r <dirname or path> -d <dirname or path>
```

To encrypt only files in the root of a directory name
```bash
$ simple_encryption encrypt -r -f <dirname or path>
```

In the all the above examples a key was created by default and stored in the file ".secrets/enc_key"

To encrypt with your key
```bash
$ simple_encryption encrypt <filename or path> -K <your key>
```

To encrypt with your key stored in a file
```bash
$ simple_encryption encrypt <filename or path> -k <key filename or path>
```

### Decryption

To decrypt source file
```bash
$ simple_encryption decyrpt <filename or path>
```
To decrypt source file to a destination file
```bash
$ simple_encryption decrypt <filename or filepath> -d <filename or path>
```
To decrypt source directory
```bash
$ simple_encryption decrypt -r <dirname or path>
```

To decrypt source directory to destination directory
```bash
$ simple_encryption decrypt -r <dirname or path> -d <dirname or path>
```

To decrypt only files in the root of a directory name
```bash
$ simple_encryption decrypt -r -f <dirname or path>
```

In the all the above examples a key was extracted by default from the file ".secrets/enc_key", which was created during encryption without using your own key

To decrypt with your key
```bash
$ simple_encryption decrypt <filename or path> -K <your key>
```

To decrypt with your key stored in a file
```bash
$ simple_encryption decrypt <filename or path> -k <key filename or path>
```

## Built With

* [Python](https://www.python.org/)

## Author

* [Soutrik Neogi](https://github.com/soutrikneogi)

## Reference

* [Towards Data Science Blog](https://towardsdatascience.com/how-to-build-and-publish-command-line-applications-with-python-96065049abc1
)