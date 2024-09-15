import argparse
from rot13 import rot13Encrypt, rot13Decrypt
from caesar import caesarEncrypt, caesarDecrypt

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Process user text to encrypt or decrypt it using various algorithms.")

# Define command-line flags
parser.add_argument('-a', '--algorithm', type=str, required=True, help='Choose an algorithm (e.g. ROT13)')
parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt a text')
parser.add_argument('-t', '--text', type=str, required=True, help='Text you want to encrypt/decrypt')
parser.add_argument('-s', '--shift', type=int, help='Number of shifts a char should do (e.g. 7 a->h)')

args = parser.parse_args()

if args.algorithm == "rot13":
    if args.decrypt == True:
        dec_string = rot13Decrypt(args.text)
        print(f"encrypted: {args.text} -> decrypted: {dec_string}")
    else:
        enc_string = rot13Encrypt(args.text)
        print(f"cleartext: {args.text} -> encrypted: {enc_string}")

if args.algorithm == "caesar" and args.shift != None:
    if args.decrypt == True:
        dec_string = caesarDecrypt(args.text, args.shift)
        print(f"encrypted: {args.text} -> decrypted: {dec_string}")
    else:
        enc_string = caesarEncrypt(args.text, args.shift)
        print(f"cleartext: {args.text} -> encrypted: {enc_string}")
