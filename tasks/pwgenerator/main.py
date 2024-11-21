import random
import string
import pyperclip


def genPw(n, l, charSet=string.ascii_letters + string.digits):
    """ Generates random passwords
    Parameters:
        n : int : Number of passwords to be generated
        l : int : Length of the passwords
        charSet : str : Characters to be used for generating
    Returns:
        passwords : list : List of randomly generated passwords
    """
    passwords = [] 

    for n in range(n):
        password = "".join(random.choices(charSet, k=l))
        passwords.append(password)

    return passwords


def pwGenerator():
    """
    Generates random passwords and stores them in a file, prints them in the CLI or copies them to the clipboard
    """

    # Take input from the user
    n = int(input("How many passwords do you need? "))
    l = int(input("How long do you want your passwords to be? "))
    chooseCharSet = int(input("Do you want to choose which characters are allowed for the password??\n1: Yes\n2: No\nInput: "))
    if chooseCharSet == 1:
        charSet = str(input("Enter all characters: "))
    else:
        charSet = string.ascii_letters + string.digits + string.punctuation

    store = int(input("Where do you want your passwords to be stored?\n1: In a file\n2: In the CLI\n3. In my clipboard\nInput: "))

    # Generate the passwords
    passwords = genPw(n, l, charSet)

    # Switch case statement to store, print or copy the passwords the way the user wants to
    match store:
        # Store the passwords in a file
        case 1:
            path = input("Enter the path where you want the passwords to be stored: ")
            with open(path, "w") as f:
                for password in passwords:
                    f.write(password + "\n")
            print("Passwords have been stored in ", path)
        # Print the passwords in the CLI
        case 2:
            for password in passwords:
                print(password)
        # Copy the passwords to the clipboard
        case 3:
            pyperclip.copy("\n".join(passwords))
            print("Passwords have been copied to your clipboard")
        # Default case for invalid input 
        case _:
            print("Invalid input")


def main():
    pwGenerator()


if __name__ == '__main__':
    main()
