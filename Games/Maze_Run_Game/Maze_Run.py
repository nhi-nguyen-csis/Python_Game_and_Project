import random

def getUsername():
    print("\nCool! Let's play the Maze Run Game")
    return input("Please enter your username: ").capitalize()

def paths(maxList):
    pathNum = random.randint(0, maxList - 1)
    return pathNum

def getRandomCharacter(characterDict):
    characterList = list(characterDict)
    characterIdx = random.randint(0, len(characterList) - 1)
    return characterList[characterIdx]

def printGameRules():
    print("\n---------- HERE IS THE GAME RULE ------------")
    print("You have 50 lives at the beginning of the game.\n"
          "If you meet a Dementors monster, then you die\n"
          "If you meet other monsters, then you loose 10 lives\n"
          "If you meet a saver, then you gain 5 lives\n"
          "If you are in a dead end, then you die\n"
          "If you find an exit, then you win")
    print("---------------------------------------------\n")

def wannaPlay():
    print("Welcome to Maze Run!")
    isValidAnswer = False
    while not isValidAnswer:
        yes_or_no = input("Are you scared of seeing monsters (yes/no)? ").lower()
        if yes_or_no == 'yes' or yes_or_no == 'no':
            isValidAnswer = True
        else:
            print("Please choose [yes] or [no] only")
    return yes_or_no

def go_left_or_go_right():
    isValidAnswer = False
    while not isValidAnswer:
        left_or_right = input("\nDo you want to go left or right (left/right)? ").lower()
        if left_or_right == 'left' or left_or_right == 'right':
            isValidAnswer = True
        else:
            print("Please choose to go [left] or go [right] only")
    return left_or_right

def win_or_lose(isWin):
    if isWin:
        print(f"\n{username}, you win the game!")
    else:
        print(f"\nSorry! {username}, you lose the game")

if __name__ == '__main__':

    characterDict = {
                        'Harry Potter': 1,
                        'Ron Weasley': 1,
                        'Hermione Granger': 1,
                        'Bogeyman': 0,
                        'Vampire': 0,
                        'Zoombie':0,
                        'Banshee': 0,
                        'Basilisk': 0,
                        'Dragon': 0,
                        'Dementors': 0
                    }

    pathList = ['Dead Mud', 'River', 'Mountain', 'Desert', 'Forest', 'Exit!']
    pathChoice = ['die', 'swim', 'climb', 'run', 'walk', 'win']

    play = wannaPlay()

    if play == 'no':

        # get username
        username = getUsername()

        # print the game rules
        printGameRules()

        # set up the game
        lives = 50
        isWin = False

        # start the game
        while lives > 0 and not isWin:
            print(f"{username}, you have {lives} lives!")
            path = go_left_or_go_right()

            # who you are facing with? monster or saver
            # whoYouMeet = monster_or_saver()
            whoYouMeet = getRandomCharacter(characterDict)

            # if you met a monster
            if characterDict[whoYouMeet] == 0:
                if whoYouMeet == 'Dementors':
                    print(f"Oooh! no. You are facing with {whoYouMeet}.\n"
                          f"There's no one can fight against them, except Harry Potter")
                    lives = 0
                    continue
                else:
                    print(f"{username}, you are facing with {whoYouMeet}\n"
                          f"You lost 10 lives")
                lives -= 10
            # if you met a saver
            else:
                print(f"{username}, you are meeting with {whoYouMeet}\n"
                      f"{whoYouMeet} gave you extra 5 lives")
                lives += 5
            print(f"{username}, you have {lives} lives left!")
            # choose to go left or right to go to the next path
            path = go_left_or_go_right()
            # what is next path
            route = paths(len(pathList))

            # if they are in the dead mud, then they die
            if route == 0:
                print(f"Now you are in a {pathList[route]}")
                print("There is no way to survive!")
                lives = 0
                continue
            # if they are in the exit, then they win
            elif route == 5:
                print(f"Woohoo! {username}, you have found the exit from the maze")
                isWin = True
                continue

            print(f"You are in {pathList[route]}")

            # get the new route if player still has lives
            if lives > 0:
                print(f"Now, you have to {pathChoice[route]} ...\n")

        # let playsers know if they win or lose the game
        win_or_lose(isWin)
    else:
        print("\nSorry! This game is not for you.\nMaybe you should read Harry Potter to be more brave :)")