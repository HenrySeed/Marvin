from rsa import rsa
from marvin_utils import options

def new_cipher():
    cipher = RSA_Cipher()
    print(cipher)
    print()
    save = input('Would you like to save this as your new cipher? [y/n]\n> ')
    if 'y' in save:
        options = options.Options()
        options.change_cipher(cipher.public_key, cipher.private_key)
        options.save()
        print('saved')


def encrypt(message):    
    rsa.rsa_encrypt(options.public_key(), message)

def decrypt(message):
    rsa.rsa_decrypt(options.public_key(), message)
        



