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


# A function definition checking whether passed char occurs in all passed words, takes char and list of words
def common_character_check(letter_to_check, words_ch):
    print("\nCommon character check: ")
    # declare counter
    count = 0
    # a loop that goes through all the words in the list
    for word in words_ch:
        # if char occurs in word increase the count
        if letter_to_check in word:
            count += 1
    # if count equals length of words list that means that the character appears in each word in the list
    if count == len(words_ch):
        print(f"Character {letter_to_check} appears in all items ")
        # If char occurs in each word loop again through list
        for word in words_ch:
            count_letter = 0
            # if letter to check occurs in word go through the word
            if letter_to_check in word:
                for i in word:
                    # loop through each char in word and increase letter count every time char is found
                    # In order for uppercase and lowercase letters to have the same value, they must be reduced
                    # to a common form, because the function uses the values from the ASCII table to compare
                    if i.lower() == letter_to_check.lower():
                        count_letter += 1
                print(f"{word} contains {count_letter} {letter_to_check}")
    # Print a message if letter is not present in all words from list
    else:
        print(f"Character {letter_to_check} does not appear in all words.")


# Main function definition
def main():
    # Calling function get_words() and storing result in list_of_words
    list_of_words = get_words()
    # Calling function question_marks_check() with 1 parameter
    question_marks_check(list_of_words)
    # Getting input from user, casting to string and storing in variable letter
    letter = str(input("Enter a letter: "))
    # Calling common_character_check() with 2 parameters
    common_character_check(letter, list_of_words)


if __name__ == '__main__':
    main()
