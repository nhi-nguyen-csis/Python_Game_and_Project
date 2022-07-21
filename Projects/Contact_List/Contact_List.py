import json
from typing import List

'''
This function return the number of times the name appears in the contact list - in case we have duplicate names
it also returns an array of all the information of the people with the similar name we found
'''
def findSomeone(arr: List, name: str):
    count = 0
    phone = []
    for person in arr:
        if name in person['name']:
            currPerson = {'name': person["name"],
                          'phone': person["phone"],
                          'age' : person["age"],
                          'is family?': person["is family?"],
                          'note': person['note']}
            phone.append(currPerson)
            count += 1
    return count, phone

def printInfo(contact: List):
    for idx, person in enumerate (contact):
        print(f"{idx + 1}:\t{person['name']}")
        print(f"\t{person['phone']}")
        print(f"\tIs your family member? {person['is family?']}")
        if person['note'] != 'None':
            print(f"\tNote: {person['note']}")

def searching(data: dict):
    # searching contact list
    contactList = data["contact list"]
    # print(contactList)
    # ask user the name of the person they want to search for the phone number
    while True:
        name = input("\nEnter a person name you want to search for\nOr enter 'Done' to exit: ").capitalize()

        if name in {'Done', 'Exit'}:
            break

        # call the findSomeone() method to find if the person's name is in the contact list
        count, contact = findSomeone(contactList, name)

        # show the result
        if count == 0:
            print(f"\nCannot find anyone named '{name}' in your contact list")
        elif count == 1:
            printInfo(contact)
        else:
            print(f"\nWe have found {count} '{name}' in your contact list")
            printInfo(contact)

def save_contact(contact: dict, fileName: str, data: dict):
    data['contact list'].append(contact)
    with open(fileName, "w") as f:
        json.dump(data, f, indent=4)
    print("\nNew contact has been added to your contact list")

def add(data):
    while True:
        name = input("Person name: ").capitalize()
        age = input("Person age: ")
        phone = input("Person phone number: ")
        isFamily = input("Is the person your family member? ").lower()
        wantToNote = input("Do you want to make a note about this person contact? ").lower()
        if wantToNote in {"yes", "y"}:
            note = input("Input the note here: ")
        else:
            note = "None"
        id = data['contact list'][len(data['contact list']) - 1]['id'] + 1
        newContact = {
            'id': id,
            'name': name,
            'age': age,
            'phone': phone,
            "is family?": isFamily,
            "note": note
        }

        save_contact(newContact, "contactList.json", data)

        addMore = input("\nDo you want to add another contact? ").lower()
        if addMore in {"no", "n"}:
            break

def main():
    while True:
        userChoice = input("\nEnter 'Show' if you want to see all information of your contact list"
                           "\nEnter 'Search' if you want to search for a person info"
                           "\nOr enter 'Add' if you want to add a new person info to your contact list"
                           "\nOr enter 'Done' to exit"
                           "\nEnter your choice here: ").lower()
        if userChoice in {"done", 'd'}:
            break
        elif userChoice not in {'search', 'add', 'show'}:
            print("Invalid choice")
        else:
            # open the json file that stores all the contact info
            with open("contactList.json", "r") as f:
                data = json.load(f)
            if userChoice == 'show':
                printInfo(data['contact list'])
            elif userChoice == 'search':
                searching(data)
            else:
                add(data)
    print(" -------- Goodbye! --------")


if __name__ == '__main__':
    main()