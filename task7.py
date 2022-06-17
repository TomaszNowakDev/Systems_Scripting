def main():
    # define dictionary
    athletes = {'986478A': 'negative', '666783B': 'positive', '876634C': 'negative', '674373D': 'positive',
                '674672E': 'negative'}

    while True:
        # get input from the user
        inputs = str(input("Please enter: PPS number or \"dope\" or \"clean\" or \"stop\"\n>>>"))
        if inputs == "dope":
            counter_pos = 0
            for a in athletes:
                if athletes[a] == 'positive':
                    counter_pos = counter_pos + 1
            print(f"Numbers of positive tests: {counter_pos}.")

        elif inputs == "clean":
            counter_neg = 0
            for a in athletes:
                if athletes[a] == 'negative':
                    counter_neg = counter_neg + 1
            print(f"Numbers of negative tests: {counter_neg}.")

        elif inputs == "stop":
            print("Thank you goodbye")
            exit()

        else:
            if inputs in athletes:
                print(inputs + " test result: " + athletes[inputs])
            else:
                print(f" There is no test result for {inputs}, would you like to add test result? (y/n)")
                choice = input(">>>")
                if choice.lower() == 'y':
                    result = str(input("What was the result of the test: "))
                    athletes.setdefault(inputs, result)


if __name__ == '__main__':
    main()
