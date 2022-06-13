import random
import copy
import time


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


# Define a function to play the game
def play_the_game(players):
    # Validation infinite while loop to get valid input from user
    while True:
        try:
            # Getting input from user, casting to an integer
            elimination = int(input("How many players do you want to eliminate in this game? (min 2, max 6) "))
            # if input is in required range break the loop
            if 1 < elimination <= 6:
                break
            else:
                # print message if input is not in required range
                print("You can eliminate between 2 – 6 players only.")
        except ValueError:
            # print message if input is not an integer
            print("Numbers only please!")
    # calling function one_round() with 2 parameters and store the result of it in variable result
    result = one_round(elimination, players)
    # return result to the main()
    return result


# Define function to play
def one_round(num, players_list):
    print(f"Game Has started!\nPlayers list: {players_list}\nPlayers to eliminate: {num}.")
    for i in range(num):
        index = random.randint(1, 6)
        busted = players_list.pop(index)
        print(f"Player {busted} was eliminated!")
        # wait to 30 seconds before next elimination
        time.sleep(30)
    # return list of not eliminated players
    return players_list


def main():
    #  Calling function get_players() and storing result of it in players_list
    players_list = get_players()
    # copying list of players in order to keep it in memory
    game_list = copy.copy(players_list)
    # calling function play_the_game() with 1 parameter and store the result of it in variable after_game
    after_game = play_the_game(game_list)

    # cast list to the tuple
    players_tuple = tuple(i for i in after_game)
    # print list of players before the game and tuple of players left after the game
    print(players_list)
    print(players_tuple)


if __name__ == '__main__':
    main()
