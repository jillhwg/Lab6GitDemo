'''
Debugger program
'''

def encode(password):
    encoded_password = ''
    for i in password:
        encoded_number = int(i) + 3
        encoded_password += str(encoded_number)
    return encoded_password

'''
maile's code
'''
def decode(numbers):
    encoded_password = ''
    for i in numbers:
        decoded_number = int(i) - 3
        encoded_password += str(decoded_number)
    return encoded_password


def menu():
    print("Menu")
    print("----------")
    print("1. Encode\n2. Decode\n3. Quit")
    print()

def main():

    while True:
        menu()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            encoded_password = encode(password)
            print()
        if option == 2:
            decoded_code = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_code}")
            print()
        if option == 3:
            break

if __name__ == '__main__':
    main()
