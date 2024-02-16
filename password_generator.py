import string
import random

def generate_password(length, letters= True, numbers= True, symbols= True):
    char= ''
    if letters:
        char += string.ascii_letters
    if numbers:
        char += string.digits
    if symbols:
        char += string.punctuation
    if not char:
        print("Select atleast one character")
        return None

    password = ''.join(random.choice(char) for _ in range(length))
    return password

def main():
    print("PASSWORD GENERATOR")
    try:
        length = int(input("Enter the lengh of the password:"))
        if (length <0):
                     print("Error, please enter positive integer")
    except:
        print("Invalid input,please Enter the valid length")
        return
    letters = input("Include letters? (y/n): ").lower() == 'y'
    number = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length,letters,number,symbols)

    if password:
        print("Your generated password is:",password)

if __name__ == "__main__":
    main()
