'''
In Bagels, a deductive logic game, you must guess a secret
three-digit number based on clues. The game offers one of
the following hints in response to your guess: “Pico” when
your guess has a correct digit in the wrong place, “Fermi”
when your guess has a correct digit in the correct place,
and “Bagels” if your guess has no correct digits.
You have 10 tries to guess the secret number.
'''
import random


def showGameRule():
    print("I am thinking of a 3-distinct-digit number. Try to guess what it is"
          "\nHere are some clues:"
          "\nWhen I say:\tThat means:"
          "\n\tPico\tOne digit is correct but in the wrong position"
          "\n\tFermi\tOne digit is correct and in the right position"
          "\n\tBagels\tNo digit is correct"
          "\nFor example:"
          "\n128 --> Fermi Fermi"
          "\n875 --> Bagels"
          "\n096 --> Pico Pico"
          "\nNOTE: 3 digits in the number are distinct"
          "and Pico and Fermi are not in the order of the correct digit"
          "......"
          "\nI have thought up a number"
          "\nYou have 10 guesses to get it")
    print()

def getSecretNumber():
    """ Return a string as a random 3 distinct digit"""
    arr = list('0123456789')
    random.shuffle(arr)
    return ''.join(arr[:3])

def isAllDistinctDigits(userGuess):
    """ return True if the user input a 3-distinct-digit number """
    if userGuess[0] in userGuess[1:] or userGuess[-1] in userGuess[:-1]:
        return False
    return True

def getUserGuess(alreadyGuesses):
    """ Return a string as a valid user input """
    isContinue = True
    while isContinue:
        userGuess = input(f"\tEnter your guess here: ")
        if userGuess.isdigit() and len(userGuess) == 3 \
                and isAllDistinctDigits(userGuess) and userGuess not in alreadyGuesses:
            isContinue = False
        else:
            print("\t----- Invalid guess -----")
            if not userGuess.isdigit():
                print(f"\tYour guess cannot only anything rather than numbers")
            if len(userGuess) != 3:
                print(f"\tThe input must have 3 digits")
            if not isAllDistinctDigits(userGuess):
                print(f"\tAll digits must be distinct")
            if userGuess in alreadyGuesses:
                print("\tYou already guessed this number before")
    alreadyGuesses.add(userGuess)
    return userGuess

def showHints(userGuess, secretNum):
    message = []
    for i in range(len(userGuess)):
        if userGuess[i] == secretNum[i]:
            message.append("Fermi")
        elif userGuess[i] in secretNum:
            message.append("Pico")
        if i == len(userGuess) - 1 and not message:
            message.append("Bagels")
        if i == len(userGuess) - 1:
            random.shuffle(message)
            return " ".join(message)

def startGame(secretNum):
    count = 0
    alreadyGuesses = set()
    while count < 10:
        # 5. get user valid guess
        print(f"Guess #{count + 1}")
        userGuess = getUserGuess(alreadyGuesses)
        # 6. if user's guess is correct
        if userGuess == secretNum:
            print("\nCongrats! You have guessed the computer secret number")
            break
        # if user's guess is wrong, then pop up the message
        hints = showHints(userGuess, secretNum)
        print(hints)
        count += 1
    print(f"\nYou have failed to guess the number"
          f"The secret number is {secretNum}")

def main():
    # 1. show game rule
    showGameRule()

    # 2. random generate the secret 3-digit number
    secretNum = getSecretNumber()
    # print(f"secret = {secretNum}") # uncomment this if we want to test

    # 3. play the game
    isContinue = True
    while isContinue:
        startGame(secretNum)
        playAgain = input("Do you want to play again? (yes or no)? ").lower()
        if not playAgain.startswith('y'):
            isContinue = False

    print("\nGoodbye!")

if __name__ == '__main__':
    main()