
#intro

print("Welcome to myContact")
print("what you want today?!")

contacts = {}

while True :


    userchoice = int(input("1.show contacts 2.add contact 3.delete contact 4.exit : "))

    #main function

    if userchoice == 1 :
        if contacts == {} :
            print("There is no Contact")
        else:
            print(contacts)

    elif userchoice == 2 :
        contactname = input("Please enter Contact Name:  ")
        contactnumber = input("Please enter Contact Number:  ")
        contacts[contactname] = contactnumber
    elif userchoice == 3 :
        for i , k in enumerate(contacts) :
            print(i , k)
        contactdelete = int(input("Enter number of contact you want to delete : "))
        contactlist = list(contacts)

        if contactdelete < len(contactlist):
            contactselected = contactlist[contactdelete]
            contacts.pop(contactselected)
        else :
            print("Enter correct number")
    elif userchoice == 4 :
        exit()

    else:
        print("We dont Have this!!!")