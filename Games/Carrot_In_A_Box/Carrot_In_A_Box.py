import random
import time

CLOSE_BOX_IMAGE = '''
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   BLUE  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''

OPEN_BOX_IMAGE_1 = '''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   BLUE  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(carrot!)'''

OPEN_BOX_IMAGE_2 = '''
   _________
  |         |
  |        |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   BLUE  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(NO carrot!)'''

BOX1_WITH_CARROT = '''
        ___VV____      _________
       |   VV    |    |         |
       |   VV    |    |         |
       |___||____|    |_________|
      /    ||   /|   /         /|
     +---------+ |  +---------+ |
     |   RED   | |  |   BLUE  | |
     |   BOX   | /  |   BOX   | /
     +---------+/   +---------+/'''

BOX2_WITH_CARROT = '''
        _________      ___VV____
       |         |    |   VV    |
       |         |    |   VV    |
       |_________|    |___||____|
      /         /|   /    ||   /|
     +---------+ |  +---------+ |
     |   RED   | |  |   BLUE  | |
     |   BOX   | /  |   BOX   | /
     +---------+/   +---------+/'''

def who_go_first(user1, user2) -> tuple:
    '''
    :param user1:
    :param user2:
    :return: tuple
    if user2 won, then swap position of user1 and user2 so that user1 is always the one who goes first
    '''
    print("Now both users throw the dice to decide who goes first")
    while True:
        user1_dice = random.randint(1,6)
        user2_dice = random.randint(1, 6)
        if user1_dice != user2_dice:
            break
    print(f"{user1} threw a dice: {user1_dice}")
    print(f"{user2} threw a dice: {user2_dice}")
    if user1_dice < user2_dice:
        return user2, user1 # swap position of user1 and user2
    else:
        return user1, user2

def generate_random_carrot_box(user1, user2)-> bool:
    '''
    :param user1:
    :param user2:
    :return: hasCarrot: boolean
    '''
    boxes = [OPEN_BOX_IMAGE_1, OPEN_BOX_IMAGE_2]
    carrot_box = random.choice(boxes)
    hasCarrot = False
    if carrot_box == OPEN_BOX_IMAGE_1:
        print(OPEN_BOX_IMAGE_1)
        hasCarrot = True
    else:
        print(OPEN_BOX_IMAGE_2)
    print(f"\t{user1}\t\t{user2}")
    return hasCarrot

def convine(user1, user2) -> None:
    str = f"""\n{user1}, say one of the following sentences to {user2}.
      1) There is a carrot in my box.
      2) There is not a carrot in my box.
    """
    print(str)
    input('Then press Enter to continue...')

def swap_or_not_swap(user1, user2, user1_has_carrot: bool) -> bool:
    user2_want_swap = False
    while True:
        user2_choice = input(f"{user2}, do you want to swap your box with {user1} (yes/no)? ").lower()
        if user2_choice.startswith("y"):
            user2_want_swap = True
            break
        elif user2_choice.startswith("n"):
            break
        print("Invalid input. Please enter 'yes' or 'no'")
    # if user1 has a carrot and user2 wanted to swap, then
    # user1 no longer has the box with the carrot inside
    if user1_has_carrot and user2_want_swap:
        user1_has_carrot = False
    # if user1 doesn't have carrot and user2 did not want to swap
    # user1 swap and get the box with the carrot inside
    elif not user1_has_carrot and not user2_want_swap:
        user1_has_carrot = False
    else:
        user1_has_carrot = True
    return user1_has_carrot

def who_win(user1, user2, user1_has_carrot: bool) -> None:
    # show both of the boxes at the end
    if user1_has_carrot:
        print(BOX1_WITH_CARROT) # show image with the carrot inside
    else:
        print(BOX2_WITH_CARROT) # show image without the carrot inside
    print(f"\t{user1}\t\t{user2}")
    # declare who is the winner
    winner = {user1} if user1_has_carrot else {user2}
    print(f"\n{winner} is the winner!")

def main():
    # STEP 1: get users name
    user1 = input("Human player 1, enter your name: ").capitalize()
    user2 = input("Human player 2, enter your name: ").capitalize()
    print(f"HERE ARE TWO BOXES: {CLOSE_BOX_IMAGE}")

    # STEP 2: throw dice to decide who can see one of the boxes
    # user1 is the one who win and will be the one who can see the box
    user1, user2 = who_go_first(user1, user2)
    print(f"\n{user1}, you will go first. You can see what's inside the box")

    # STEP 3: start playing the game
    str = f'''
    {user1}, you have a RED box in front of you.
    {user2}, you have a BLUE box in front of you.'''
    print(str)

    # STEP 4: user2 closes the eyes and we will let user1 see what's inside the box
    print(f"\n{user1}, you will get to look into your box.")
    print(f'{user2}, close your eyes and don\'t look!!!')
    input(f'When {user2} has closed their eyes, press Enter...')
    # open user1's box
    str = f'''
    {user1}, you will get to look into your box
    When {user2} has closed their eyes, press Enter...
    '''
    print(str)
    print(f"{user1}, here is the inside of your box:")

    # STEP 5: randomly generate if carrot is or is not in the user1's box
    user1_has_carrot = generate_random_carrot_box(user1, user2)
    time.sleep(2)
    print('\n' * 100) # clear the screen

    # STEP 6: user1 now convinces user2 to swap or not to swap the box
    convine(user1, user2)

    # STEP 7: user2 decides where he/she wants swap the box with user1 or not
    user1_has_carrot = swap_or_not_swap(user1, user2, user1_has_carrot)

    # STEP 8: show the boxes at the end and declare who is the winner
    who_win(user1, user2, user1_has_carrot)

if __name__ == '__main__':
    main()