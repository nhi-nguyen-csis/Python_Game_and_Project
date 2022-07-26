
def encrypt_or_decrypt():
    '''
    :return: void
    keep asking users until they input either encrypt or decrypt
    '''
    while True:
        choice = input('Do you want to (e)ncrypt or (d)ecrypt? ').upper()
        if not choice.startswith('E') and not choice.startswith('D'):
            print("Invalid choice!")
            continue
        if choice == 'E':
            getKey('encrypt', 25)
        elif choice == 'D':
            getKey('decrypt', 26)
        break

def getKey(e_or_d, maxKey):
    '''
    :param e_or_d:
    :param maxKey:
    :return: void
    get the valid key from user:
    - for encrypt: valid key is from 0 to 25
    - for decrypt: valid key is from 0 to 26
    '''
    while True:
        key = int(input(f'\nPlease enter the key (0 to {maxKey}) to use: '))
        if 0 <= key <= maxKey:
            if e_or_d == 'encrypt':
                generateEncrypt(key)
            else:
                generateDecrypt(key)
            break
        print("Invalid key!")

def generateEncrypt(key):
    # Caesar cipher only works on uppercase letters
    message = input('\nEnter the message to encrypt: ').upper()
    hashMessage = [''] * len(message)
    for i in range(len(message)):
        # if current letter is alphabetic, then encrypt it
        if message[i].isalpha():
            iLetter = ord(message[i]) + key
            if iLetter > ord('Z'):
                # the below code handle the wrap-around
                iLetter = (iLetter % ord('Z')) - 1 + ord('A')
            hashMessage[i] = chr(iLetter)
        else: # If not, then do nothing
            hashMessage[i] = message[i]
    print("".join(hashMessage))

def generateDecrypt(key):
    # Caesar cipher only works on uppercase letters
    message = input('\nEnter the message to dencrypt: ').upper()
    hashMessage = [''] * len(message)
    for i in range(len(message)):
        # if current letter is alphabetic, then dencrypt it
        if message[i].isalpha():
            iLetter = ord(message[i]) - key
            if iLetter < ord('A'):
                # the below code handle the wrap-around
                iLetter = ord('Z') - (( ord('A') % iLetter) - 1)
            hashMessage[i] = chr(iLetter)
        else: # If not, then do nothing
            hashMessage[i] = message[i]
    print("".join(hashMessage))

def main():
    encrypt_or_decrypt()

if __name__ == '__main__':
    main()