


phonebook = {} # global variable

# {
#     "Anna": "333-333-3333"
# }

def searchName():
    print(f'''
Search Contacts
====================
''')
    name = input('Search for a name>> ') #Melissa

    if name in phonebook:
        print(f'{name} {phonebook[name]}')
    else:
        print('Contact not found')
    

def addContact():
    name = input('Enter a name>>')  #Anna
    phoneNumber = input('Enter a phone number >> ') #333-333-3333
    
    phonebook[name] = phoneNumber


def deleteContact():
    print(f'''
Delete Contacts
=====================
''')
    name = input('insert a name to delete >>') #Melissa

    if name in phonebook:
        del phonebook[name]
    else:
        print('no contact to delete')
        

def listAllEntries():
    print(f'''
Phone Book Contacts
======================
''')
    
    for name, phonenumber in phonebook.items(): #[("Anna", "333-333-3333"), ()]
        print(f'{name}\t\t{phonenumber}')
        


def menu(): 
    selection = int(input("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Exit
                      

"""))
    return selection


endProgram = False

while not endProgram:

    selection = menu()
    
    if selection == 1:
        searchName()
    elif selection == 2:
        addContact()
    elif selection == 3:
        deleteContact()
    elif selection == 4:
        listAllEntries()
    elif selection == 5:
        endProgram = True
        
