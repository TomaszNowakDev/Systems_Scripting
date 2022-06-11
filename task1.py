# A function that collects words from the user and returns that word table to the main function
def get_words():
    # declare the table of words
    words = []
    while True:
        word = str(input("Enter a word, or enter nothing to stop: "))
        # When the user does not enter anything, the function returns the saved words
        if word == "":
            break
            # append word to the table
        words.append(word)
        # return word table
    return words


# Main function definition
def main():
    # Calling function get_words() and storing result in list_of_words
    list_of_words = get_words()
    print(list_of_words)


if __name__ == '__main__':
    main()
