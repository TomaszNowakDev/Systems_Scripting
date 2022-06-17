def assign_to_dictionary(sentence):
    dictionary = {}

    # sentence = sentence.lower()
    sentence = sentence.split()
    for word in sentence:
        dictionary.setdefault(word, 0)
        dictionary[word] = dictionary[word] + 1

    return dictionary


def main():
    while True:
        words = str(input("Please input a long sentence containing repetition of words "
                          "or \"finish now\" to terminate the program.\n>>>"))

        if words == "finish now":
            print("Thank you goodbye")
            exit()
        result = assign_to_dictionary(words)
        print(result)


if __name__ == '__main__':
    main()
