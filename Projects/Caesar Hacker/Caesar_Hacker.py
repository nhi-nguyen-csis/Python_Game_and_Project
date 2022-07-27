
def generateEncrypt(key, message):
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
    return "".join(hashMessage)

def brute_force(message):
    for i in range(27):
        print(f"Key #{i}: {generateEncrypt(i, message)}")

def main():
    message = input("Enter the decrypted Caesar cipher message to hack:\n").upper()
    brute_force(message)
if __name__ == '__main__':
    main()