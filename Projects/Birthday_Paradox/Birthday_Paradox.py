'''
Source: Automate the Boring Stuff with Python
https://inventwithpython.com/bigbookpython/project2.html
'''
import random


def generateBirthday(number_birthdays, numMatch = 0, showBirthdays = True):
    '''
    :param number_birthdays:
    :param numMatch:
    :param showBirthdays:
    :return: boolean if showBirthdays is False, else show random birthdays
    (10 birthdays on each line) and present which dates people have same birthdays
    '''
    monthDates = {
        'January': 31,
        'February': 29, # max is 29 days in leap years
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'Septempber': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }

    # dictionary to keep track of the frequencies of a certain birthday
    # with key: brithday, value: frequency
    alreadyGenerated = dict()

    for i in range(number_birthdays):
        # generate random month
        randomMonth = random.choice(list(monthDates))
        # generate random date within the month's dates
        randomDate = random.randint(1, monthDates[randomMonth])
        # print out the random birthday
        if showBirthdays:
            if i != 0:
                print(", ", end="")
            print(f"{randomMonth} {randomDate}", end="")
        # add the random birthday to the dictionary
        dateOfBirth = randomMonth + " " + str(randomDate)
        # keep track of how many times the birthday appears in the collection
        alreadyGenerated[dateOfBirth] = alreadyGenerated.get(dateOfBirth, 0) + 1
        # check if there are at least 2 people have the same birthdays in the dictionary
        if not showBirthdays and alreadyGenerated[dateOfBirth] > 1:
            return True

    # show match if we have multiple people with the same birthday at the first time we run the program
    if showBirthdays:
        isSameBirthday(alreadyGenerated)

def isSameBirthday(mDict):
    '''
    :param mDict:
    :return: void
    show which dates that multiple people have the same birthdays
    '''
    isFirstTime = True
    foundMath = False
    for k, v in mDict.items():
        if v > 1 and isFirstTime:
            print(f"\nIn this simulation,\n\t{v} people have a birthday on {k}")
            isFirstTime = False
            foundMath = True
        elif v > 1:
            print(f"\t{v} people have a birthday on {k}")
    if not foundMath:
        print("\nThere are no matching birthdays")

def getNumberBirthdays():
    '''
    :return: valid total number of random birthdays that users want us to generate
    '''
    while True:
        numBirthdays = int(input("How many birthdays shall I generate (Min 1 - Max 100)? "))
        if 0 < numBirthdays <= 100:
            break
        print("Invalid input. Please enter a number from 1 to 100")
    return numBirthdays

def calProbabilities(numMatch, total, people):
    '''
    :param numMatch:
    :param total:
    :param people:
    :return: void
    calculate and show the probability of multiple people having same birthdays in 100,000 simulations
    '''
    print(f"\nOut of 100,000 simulations of {people} people, "
          f"there was a matching birthday in that group {numMatch} times")
    chances = (numMatch / total) * 100
    print(f"\nThis means that {people} people have a {chances:.2f} % chance of "
          f"having a matching birthday in their group."
          f"\nThat's probably more than you would think!")

def generateSimulations(totalBirthdays):
    '''
    :param totalBirthdays:
    :return: void
    generate 100,000 random birthdays and show the probability of multiple people having
    same birthdays
    '''
    print(f"Generating {totalBirthdays} random birthdays 100,000 times...")
    input('Press Enter to begin...')
    count = 0  # count how many matching birthday found in 100,000 simulations
    for i in range(100_000):
        # only report the progress every 10,000 simulations
        if i % 10_000 == 0:
            print(f"{i} simultaions run...")
        # if we found a match, then increment the count variable by 1
        if generateBirthday(totalBirthdays, count, showBirthdays=False):
            count += 1
    # after finishing 100,000 simulations, report the probabilities of having matching birthdays
    if count > 0:
        calProbabilities(count, 100000, totalBirthdays)

def main():
    # Step 1: generate random birthdays
    totalBirthdays = getNumberBirthdays()
    # Step 2: print all the random birthdays we generate for the first time
    print(f"\nHere are {totalBirthdays} birthdays:")
    generateBirthday(totalBirthdays)
    print()
    # Step 3: Now, let's generate simulation 100,000 times and check the probabilities
    generateSimulations(totalBirthdays)


if __name__ == '__main__':
    main()