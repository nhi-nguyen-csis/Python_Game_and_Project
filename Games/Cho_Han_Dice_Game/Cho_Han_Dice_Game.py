import random

JAPANESE_NUMBERS = {1: 'ICHI',
                    2: 'NI',
                    3: 'SAN',
                    4: 'SHI',
                    5: 'GO',
                    6: 'ROKU'}

def showRule() -> None:
    str = '''
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.'''
    print(str)

def get_user_guess():
    '''
    :return: String, either 'CHO' or 'HAN'
    '''
    while True:
        user_guess = input("CHO (even) or HAN (odd)? ").upper()
        if user_guess == "CHO" or user_guess == "HAN":
            return user_guess
        print("Please enter either [Cho] or [Han]")

def main():

    # STEP 2: Show the game rule
    showRule()
    totalAmount = 5000
    isContinue = True

    while isContinue and totalAmount > 0:

        # STEP 2: get user valid input, if user wants to quit, then exit
        # if they want to play, then get valid bet amount
        while True:
            choice = input(f"\nYou have ${totalAmount}. How much do you bet? (or QUIT): ")
            if choice.upper().startswith("Q"):
                isContinue = False
                print("Bye!")
                break
            elif choice.isdecimal():
                betAmount = int(choice)
                if betAmount <= totalAmount: # valid input bet amount
                    break
                else:
                    print(f"You cannot bet more than ${totalAmount} the total amount of money you have")

        # STEP 3: if user wants to play
        if isContinue:
            print('''
            The dealer swirls the cup and you hear the rattle of dice.
            The dealer slams the cup on the floor, still covering the
            dice and asks for your bet
            ''')

            # Step 4: get user guess: CHO or HAN (even or odd)
            user_guess = get_user_guess()

            # STEP 5: randomly generate 2 dices
            print("The dealer lifts the cup to reveal")
            dice1, dice2 = random.randint(1, 6), random.randint(1, 6)

            # step 6: show the dices
            print(f"\t{JAPANESE_NUMBERS[dice1]}\t-\t{JAPANESE_NUMBERS[dice2]}")

            # STEP 7: show if user wins
            sum_dice = dice1 + dice2
            if (sum_dice % 2 == 0 and user_guess == 'CHO') \
                    or (sum_dice % 2 != 0 and user_guess == 'HAN'):
                print(f"You won! You take ${betAmount * 2}")
                totalAmount += (betAmount * 2)
            else:
                print(f"You lost ${betAmount}")
                totalAmount -= betAmount

    if totalAmount <= 0:
        print("\nOh no! You have lost all of your money and cannot play anymore")


if __name__ == '__main__':
    main()