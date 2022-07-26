### This project is from 'Automate the Boring Stuff with Python'

Here are some notes:
- Caesar cipher only works on uppercase letters
- Caesar cipher encrypts/decrypts alphabetical letters
- I use modulus to handle the wrap-around for encrypt and decrypt

Example inputs and outputs:
```
Do you want to (e)ncrypt or (d)ecrypt? e

Please enter the key (0 to 25) to use: 10

Enter the message to encrypt: Python
ZIDRYX
```
```
Do you want to (e)ncrypt or (d)ecrypt? d

Please enter the key (0 to 26) to use: 10

Enter the message to dencrypt: ZIDRYX
PYTHON
```
