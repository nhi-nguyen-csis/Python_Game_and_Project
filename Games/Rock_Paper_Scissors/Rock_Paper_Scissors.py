import random

def welcome():
    print("Hey! Let's play 'Rock - Paper - Scissors Game'")

def getUserChoice():
    print("----------------------------------------------")
    isContinue = True
    while isContinue:
        userChoice = input("Enter 'R' for rock"
                           "\nor 'P' for paper"
                           "\nor 'S' for scissors"
                           "\nor 'Q' to quit"
                           "\nPlease enter your choice here: ").upper()
        if userChoice in {'R', 'P', 'S', 'Q'}:
            isContinue = False
        else:
            print("Invalid choice. Please choose only [R], [P] or [S]")
    return userChoice

def getComputerChoice():
    return random.choice(['R', 'P', 'S'])

def whoWin(userChoice, computerChoice):
    userWin = -1 # -1 means computer wins
    mList = ["RS", "PR", "SP"]
    for choice in mList:
        if userChoice == choice[0]:
            if computerChoice == choice[0]:
                userWin = 0 # 0 means it's a tie
            elif computerChoice == choice[1]:
                userWin = 1 # 1 means user wins
    return userWin

def getPoint(userChoice, computerChoice, userPt, computerPt):
    # check who win
    userWin = whoWin(userChoice, computerChoice)
    if userWin == 0:
        print("It's a tie!")
    elif userWin == 1:
        print("User wins!")
        userPt += 1
    else:
        print("Computer wins!")
        computerPt += 1
    # show point after each game
    print(f"User point: {userPt}\t|\tComputer point: {computerPt}\n")
    return userPt, computerPt

def main():
    welcome()
    userPt, computerPt = 0, 0
    isContinue = True
    rockPaperScissor = {'R': "Rock", 'P': "Paper", "S": "Scissors"}
    while isContinue:
        userChoice = getUserChoice()
        # users don't want to play anymore
        if userChoice == 'Q':
            break
        # if users wants to play
        computerChoice = getComputerChoice()
        # show what they picked
        print(f"\nUser: {rockPaperScissor[userChoice]}\t|\tComputer: {rockPaperScissor[computerChoice]}")
        # save userPt and computerPt
        userPt, computerPt = getPoint(userChoice, computerChoice, userPt, computerPt)
    # users stopped the game
    print("\nGood bye!")

if __name__ == '__main__':
    main()

