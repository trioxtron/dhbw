import random
import string
import pyperclip


def pwGenerator(n, l, store):
    passwords = []

    for i in range(n):
        password = "".join(random.choices(string.ascii_letters + string.digits, k=l))
        passwords.append(password)

    match store:
        case 1:
            path = input("Enter the path where you want the passwords to be stored: ")
            with open("passwords.txt", "w") as f:
                for password in passwords:
                    f.write(password + "\n")
            print("Passwords have been stored in ", path)
        case 2:
            for password in passwords:
                print(password)
        case 3:
            pyperclip.copy("\n".join(passwords))
            print("Passwords have been copied to your clipboard")
        case _:
            print("Invalid input")
    return passwords


def main():
    n = int(input("How many passwords do you need? "))
    l = int(input("How long do you want your passwords to be? "))
    store = int(input("Where do you want your passwords to be stored?\n1: In a file\n2: In the CLI\n3. In my clipboard\nInput: "))

    pwGenerator(n, l, store)


if __name__ == '__main__':
    main()
