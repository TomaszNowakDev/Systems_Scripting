def decorating_function(string, number):
    if len(string.split()) <= 5 and number == 1:
        print("Sentence is less than 5 words and number of line is 1:")
        return f"{string.title()}"
    else:
        print("Sentence contains more than 5 words:")
        return f"{string.capitalize()}"


def main():
    while True:
        inputs = str(input("Please input a sentence or \"finish the work\" to terminate the program.\n>>>"))
        line_number = int(input("Please a line number: "))
        if inputs == "finish the work":
            print("Thank you goodbye")
            exit()
        if len(inputs.split()) > 1:
            result = decorating_function(inputs.lower(), line_number)
            print(result)
        else:
            print("Not a sentence")


if __name__ == '__main__':
    main()
