# Systems_Scripting
Lab Exercises from the Modul taught at MTU.

Task 1
Write a Python script that implements two functions where each accepts a single list parameter
containing strings. The first function should check and output the list items containing a
question mark. The second function should check and output all characters that appear in each
of the list items.
Interactively create a list with the following content to test your functions:
“barack”, “obar?ma”, “?america?”, “war”, “russia?”, “mak?er”
Sample output:
Question marks check:
obar?ma contains question mark
?america? contains question mark
russia? contains question mark
mak?er contains question mark
Common character check:
Character a appears in all items
barack contains 2 a
obar?ma contains 2 a
?america? contains 2 a
war contains 1 a
russia? contains 1 a
mak?er contains 1 a
Character r appears in all items
barack contains 1 r
obar?ma contains 1 r
?america? contains 1 r
war contains 1 r
russia? contains 1 r
mak?er contains 1 r

Task 2
Write a Python script that uses a function or functions to implement an elimination game. The
game starts with a team of 12 players. During the play, randomly eliminate between 2 – 6
players. Each time a player is eliminated, output the name of the player with a send-forth
message. Wait for 30 seconds before the next round.
Note your core function should accept two parameters. The first parameter should be a list data
type for holding the players and the second parameter should be an integer value denoting the
index of a player to eliminate. Use a random generator to generate the indexes within a range
of 1 to 6. In each case, remove a player from the given list (first parameter) based on the
randomly generated index. The function should return the resulting list as a tuple.
Interactively create a list of 12 player names. Then request a user to enter the number of players
to be eliminated. Remember that at max 6 players could be eliminated. Ensure that this range
is enforced and handle exceptions. Invoke your function with the appropriate parameters. At
the end of the program, output per line, first the returned tuple of remaining players and then
the original set of players.
Sample program output when 4 players were randomly eliminated:
Result tuple: ('Jan', 'Ti', 'Me', 'Hua', 'Ka', 'Po', 'Zo', 'Ca')
Original List: ['Jan', 'Bill', 'Ti', 'Lo', 'Me', 'Da', 'Hua', 'Be', 'Ka', 'Po', 'Zo', 'Ca']


Task 3
Write a Python script that implements a recursive function named converge() that accepts an
integer parameter. If parameter value is even then converge() should divide parameter value by
2 and return this value. If parameter value is odd, then function should return 3 times parameter
value + 1.
Then request a user to enter an integer number and recursively call converge() on that number
until the function returns the value 1. Use exception handling to ensure that user enters an
integer number before proceeding. (Amazingly, this sequence works for any integer value.
Sooner or later you will arrive at value 1).


