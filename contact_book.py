#Contact Book //simple contact book application that allows the user to store and retrieve contact information.

contact = {}
count = 0

def valid_email(email):
    import re
    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while not re.match(reg, email):
        email = input("Mail is Invalid. Please  enter the new  mail: ")
    return (email)


def valid_number(num):
    print("If there are non-numeric simbols in the number, they will be deleted and please enter the number with a length between 7 and 15")
    new_number = ''.join(c for c in num if c.isdigit())
    while len(new_number) < 7 or len(new_number) > 15:
        new_number = input("\nPhone number is Invalid . Please  enter the new  number: ")
        new_number = ''.join(c for c in new_number if c.isdigit())
    return (new_number)


def add_contact():
    name = input("\nPlease enter the  (e.g., example@email.com): ")
    email = input("\nPlease enter the e-mail: ")
    email = valid_email(email)
    phone_number = input("\nPlease enter the phone number: ")
    phone_number = valid_number(phone_number)

    global count
    contact[count] = {"name": name,
                      "phone": phone_number,
                      "Email": email}
    count += 1
    print("\nContact added successfully!")


def view_all():
    print("\n List of Contacts: ")
    if not len(contact) == 0:
        for i in contact:
            print(contact[i])
    else:
        print("List is empty")


def search_by_name():
    name = input("\n Please input the name for search: ")
    tmp = True
    try:
        if len(contact)==0:
            print("\nContact Book is empty, please create a contact first")
        else:
            for i in contact:
                if name == contact[i]["name"]:
                    print("\nHere is all information about '" + name + "' contact")
                    print(contact[i])
                    tmp = False
                elif i == list(contact)[-1] and tmp:
                    print("\nContact '" + name + "' details were not found")
    except KeyError:
        print("\nContact white  named '" + name + "'  was deleted")


def delet_by_name():
    name = input("\nplease input the name for deleted: ")
    if len(contact) == 0:
        print("\nContact Book is empty, please create a contact first")
    else:
        for i in contact:
            tmp = True
            if name == contact[i]["name"]:
                del (contact[i])
                print("\nThe contact '" + name + "'wad deleted ")
                global count
                count -= 1
                tmp = False
                break
        if tmp:
            print("\nContact not found")


def menu():
    pult = int(input("\nPlease choose the option\n1. Start\n2. Stop\n"))
    while pult==1:
        choose = int(input(
            "\nPlease choose an action:\n1. Add new contact\n2. View all contacts\n3. Search contact by name\n4. Delet contact by name\n"))
        if choose == 1:
            add_contact()
        elif choose == 2:
            view_all()
        elif choose == 3:
            search_by_name()
        elif choose == 4:
            delet_by_name()
        pult = int(input("\nPlease choose the option\n1. Start\n2. Stop\n"))
    if pult==2:
        print("Thank you for your testing )) ")
        return


menu()
