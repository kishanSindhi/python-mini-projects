from time import sleep
contact = {"kishan": "123456", "akshay": "1234", "shivam": "1234567",
           "dad": "12312", "mom": "123123", "abhi": "4556345", "bonny": "534513"}


def show():
    print(contact)
    sleep(5)


def add(key, value):
    contact[key] = value


def search(key):
    print(contact[key])


def dlt(key):
    del contact[key]


while True:
    ans = int(input("1 for viewing contact list\n2 for search number\n3 for adding contacts\n4 for deleting contacts\n5 to exit\n"))

    if ans == 1:
        show()

    elif ans == 2:
        name = input("Enter the name\n")
        search(name)

    elif ans == 3:
        name = input("Enter the name\n")
        number = input("Enter the number\n")
        add(name, number)

    elif ans == 4:
        name = input("Enter the name you want to delete\n")
        dlt(name)

    else:
        exit()
