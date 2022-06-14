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


# Function definition
def converge(num):
    # print the number passed to the function cast it to an integer for correct formatting
    print(int(num))
    # define base case for recursive function
    if num == 1:
        return 1
    # if number passed to the function is even return recursive call function with parameter number divided by 2
    elif num % 2 == 0:
        return converge(num/2)
    # if number passed to the function is odd return recursive call function with parameter multiply by 3 and add 1
    else:
        return converge((num*3)+1)


def main():
    # Calling function get_number() and storing result of it in number
    number = get_number()
    print(f"You entered a number {number}.\nLet's start the game...")
    # call the function converge() with 1 parameter and store the result of it
    result = converge(number)
    # if result present that means the game ended
    if result:
        print("Game ended!")


if __name__ == '__main__':
    main()
