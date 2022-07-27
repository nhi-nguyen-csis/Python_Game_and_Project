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
(carrot!)
'''

OPEN_BOX_IMAGE_2 = '''
                   ___VV____
                  |   VV    |
                  |   VV    |
 __________       |___||____|  
/         /|     /    ||   /|
+---------+ |   +---------+ |
|   RED   | |   |   BLUE  | | 
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/ 
                 (carrot!)
'''

def who_go_first(user1, user2):
    print("Now both users throw the dice to decide who goes first")
    while True:
        user1_dice = random.randint(1,6)
        user2_dice = random.randint(1, 6)
        if user1_dice != user2_dice:
            break
    print(f"{user1} threw a dice: {user1_dice}")
    print(f"{user2} threw a dice: {user2_dice}")
    return user1 if user1_dice > user2_dice else user2

def generate_random_carrot_box(user1, user2):
    boxes = [OPEN_BOX_IMAGE_1, OPEN_BOX_IMAGE_2]
    carrot_box = random.choice(boxes)
    if carrot_box == OPEN_BOX_IMAGE_1:
        print(OPEN_BOX_IMAGE_1)
    else:
        print(OPEN_BOX_IMAGE_2)
    print(f"\t\t{user1}\t\t{user2}")

def main():
    # get users name
    user1 = input("Human player 1, enter your name: ").capitalize()
    user2 = input("Human player 2, enter your name: ").capitalize()
    print(f"HERE ARE TWO BOXES: {CLOSE_BOX_IMAGE}")
    print(f"\t{user1}\t\t{user2}")
    # throw dice to decide who goes first
    first_person = who_go_first(user1, user2)
    second_person = user1 if first_person != user1 else user2
    print(f"\n{first_person}, you will go first. You can see what's inside the box")
    # start playing the game
    str = f'''
    {first_person}, you have a RED box in front of you.
    {second_person}, you have a BLUE box in front of you.'''
    print(str)
    print(f"{first_person}, you will get to look into your box.")
    print(f'{second_person}, close your eyes and don\'t look!!!')
    input(f'When {second_person} has closed their eyes, press Enter...')
    # open one of the box for first person
    str = f'''
    {first_person}, you will get to look into your box
    When {second_person} has closed their eyes, press Enter...
    '''
    print(str)
    input("Press Enter to continue...")
    print(f"{first_person} here is the inside of your box:")
    if first_person == user1:
        print(OPEN_BOX_IMAGE_1)
        print(f"\t\t{user1}\t\t{user2}")
    else:
        print(OPEN_BOX_IMAGE_2)
        print(f"\t\t{user1}\t\t{user2}")
    time.sleep(1)
    print('\n' * 100)
if __name__ == '__main__':
    main()