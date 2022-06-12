
# Define a function that collects input from the user and returns that list of players to the main function
def get_players():
    # declare the list of players
    p_list = []
    # collects 12 inputs from the user
    for i in range(12):
        word = str(input(f"Player {i+1}: Enter name: "))
        # append each player to the players list
        p_list.append(word)
    # return list to the main()
    return p_list


def main():
    #  Calling function get_players() and storing result of it in players_list
    players_list = get_players()


if __name__ == '__main__':
    main()
