def operation(string):
    words = string.split()
    numbers = []  # in case there is more than one number in the string
    for word in words:
        if word.isnumeric():
            numbers.append(word)
    print(f"Sentence contains {len(words)} words.")
    print(numbers)


def main():
    while True:
        inputs = str(input("Please input a sentence or \"end me now\" to terminate the program.\n>>>"))
        if inputs == "end me now":
            print("Thank you goodbye")
            exit()
        if len(inputs.split()) > 1:
            operation(inputs)
        else:
            print("Too short for a sentence")


if __name__ == '__main__':
    main()
