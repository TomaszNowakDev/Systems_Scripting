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


# A function definition which uses a loop to go through all the words in the words table
def question_marks_check(words_ch):
    print("\nQuestion marks check: ")
    # loop through all the words
    for word in words_ch:
        # if char '?' in word print message
        if '?' in word:
            print(f"{word} contains question mark")


# Main function definition
def main():
    # Calling function get_words() and storing result in list_of_words
    list_of_words = get_words()
    # Calling function question_marks_check() with 1 parameter
    question_marks_check(list_of_words)
    # Getting input from user, casting to string and storing in variable letter
    letter = str(input("Enter a letter: "))


if __name__ == '__main__':
    main()
