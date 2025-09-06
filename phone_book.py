Phone_Book = {}
def serch():
    name = input("Serch Name: ")
    if (name in Phone_Book):
        print(f"{name} : {Phone_Book[name]}")
    else:
        print(f"{name} not found!")
    file = open("D:\\Python\\WorkBook\\Phone_Book1.txt", "r",encoding="utf8")
    my_file = file.read()
    print(my_file)

def add():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    Phone_Book[name] = number
    print("saved:)")
    file = open("D:\\Python\\WorkBook\\Phone_Book1.txt", "w")
    file.write(f"{name} : {number}")
    file.close()
def show():
    if Phone_Book:
        print("\nPhone Book:")
        for name, number in Phone_Book.items():
            print(f"{name} : {number}")
    else:
        print("Phone book is empty!")

print("Welcome to Phone Book")
print("1. Search\n2. Add Phone\n3. Show\n4. Exit")

a = input("Enter number: ")

if a in ["1", "Search", "search"]:
    serch()
elif a in ["2", "Add Phone", "AddPhone", "add phone", "addphone"]:
    add()
elif a == "3":
    show()
elif a in ["4", "Exit", "exit"]:
    print("Exiting...")
else:
    print("The entered option is not correct!")