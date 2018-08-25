from sys import argv, exit
from helpers import user_input_is_valid, encrypt

def main():

    if user_input_is_valid(argv) == False:
        print("usage: python3 caesar.py n")
        exit(1)

    message = input("Type a message:\n")

    key = int(argv[1])

    scrambled = encrypt(message, key)

    print("ciphertext: " + scrambled)

if __name__ == '__main__':
    main()