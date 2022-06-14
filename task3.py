# Function the gets input from the user
def get_number():
    # validation in infinite while loop to get valid input from user
    while True:
        try:
            # Getting input from user, casting to an integer
            number = int(input('Enter a whole number: '))
            # if number entered meets requirements break the loop
            if number > 0:
                break
            else:
                # print message if input is not whole positive number
                print("Whole positive numbers only, please.")
        except ValueError:
            # print message if except ValueError caught
            print(f"Is this a whole positive number?Whole positive numbers only, please.")
    # return the number entered
    return number


def main():
    # Calling function get_number() and storing result of it in number
    number = get_number()


if __name__ == '__main__':
    main()
