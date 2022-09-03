# Systems_Scripting
Lab Exercises from the Module taught at MTU.

### Task 1
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

### Task 2
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


### Task 3
Write a Python script that implements a recursive function named converge() that accepts an
integer parameter. If parameter value is even then converge() should divide parameter value by
2 and return this value. If parameter value is odd, then function should return 3 times parameter
value + 1.
Then request a user to enter an integer number and recursively call converge() on that number
until the function returns the value 1. Use exception handling to ensure that user enters an
integer number before proceeding. (Amazingly, this sequence works for any integer value.
Sooner or later you will arrive at value 1).


### Task 4
Write a Python script that implements functions to address the following task. The first function
should accept a string parameter representing a folder name. This folder name should be
interactively provided by the user.
The first function should automate the creation of a folder structure starting with the provided
folder name. If this folder exist, delete it and recrate it. Inside this folder, create two subfolders
named “backup” and “working”. Inside the “working” folder create three other subfolders
named “pics”, “docs” and “movie”. Inside the “docs” folder create five files
(CORONAVIRUS.txt, DANGEROUS.txt, KEEPSAFE.txt, STAYHOME.txt, HYGIENE.txt)
with varying content of your choice and two subfolders (school and party).
Use another function to rename all the files in the “docs” folder to lowercase. The extension
“.txt” should be renamed to uppercase. Ensure that the folder exist before proceeding and note
that the subfolders in that directory should remain unchanged.
When the renaming is complete, use another function to implement the Python zipfile module
to archive the “docs” folder and make seven backup archives of it in the top-level “backup”
folder. Output the content of the backup folder and one of the zip archives for verification
purpose.


### Task 5
Write a Python script with a function that accepts a single string parameter. The function should
count the number of occurrence of each word in the string and return a dictionary containing
each word as key and the number of its occurrence as value.
Interactively request a user to input a long sentence containing repetition of words. Invoke your
function with the user’s input as parameter. Output the returned dictionary. If the user enters
“finish now” the script should terminate with a goodbye message.
Sample user input: “Hello how are you doing there with you and hello are we doing it there
again”
Sample Output: { 'Hello': 1, 'how': 1, 'are': 2, 'you': 2, 'doing': 2, 'there': 2, 'with': 1, 'and': 1,
'hello': 1, 'we': 1, 'it': 1, 'again': 1}.


### Task 6
Write a Python script with a function that accepts a single parameters representing a sentence.
The function should identify and report when the sentence contains a component consisting of
numbers. In that case, output the number of words contained in the sentence and furthermore,
output the component containing numbers.
Now interactively request inputs from user and call the function to operate on the inputs and
output the results. Check input to ensure that user entered a sentence (more than two words).
The program should terminate when the phrase “end me now” is entered and notify the user.
Sample input: how are you 44 me
Sample output:
Sentence contains 5 words
44


### Task 7
Write an interactive Python script to manage and to store doping test results for a sport
tournament. Use PPS number as identification for each sports person. The PPS number
should be a combination of numbers and characters. Make it up for this script. The script
should request a user to input a PPS number or stop or dope or clean.
When a user enters a given PPS number, the script should output the PPS number and the
corresponding test result. The test result should be either positive or negative. If a PPS
number does not exist, the script should offer the option of storing it with a corresponding
test result.
When a user enters the word “dope”, the script should output the total number of positive
results recorded so far for the tournament. When a user enters the word “clean”, the script
should output the total number of negative results. The word “stop”, irrespective of how it
is written, should be used to end the program.


### Task 8
Write an interactive Python script that implements a function, which accepts two parameters - a
string representing a sentence and a number indicating line of the sentence.
The function should raise to upper case the first letters of the words appearing in the sentence on
the first line as long as the sentence contains less than 5 words. When the first sentence contains
more than 5 words, only the first letter of the first word should be raised to upper case and the user
should be informed of the situation. For the other subsequent sentences only the first letter of the
first word should be raised to upper case. The function should return value.
Continuously and interactively request user to input sentences to be processed and outputted.
Check input to ensure that user entered a sentence (more than two words). In addition, the
sentence must be in lower case before passing it to the function. The program should terminate
when the phrase “finish the work” is entered and notify the user.


### Task 9
Write a bash script that searches for patterns in files located in a folder. The script should be
called with two input parameter arguments. Make sure that the arguments are provided before
proceeding. The first parameter should be a path to a folder and the second parameter should
be a string pattern.
The script should search the provided folder and print out the following details for only files
identified (that is no sub-folder should be considered):
• Name of the file.
• Date and time of file creation.
• Size of the file in bytes.
• How many times the input string pattern (second parameter) appeared in the file (case
insensitive).
Use an array structure to store the file names for those that contain the input string pattern
(second parameter) at least twice.
An until loop should be used to iterate through the above array and print out to the terminal all
the file names as well as write them into a file named report.txt. Use comments to properly
document your script.


### Task 10
Write an interactive bash script that implements a set of menus for creating and writing contents
into a file, outputting to the terminal the content of a file, change file permission and to
terminate the script. The write, output and permission change operations should be
implemented using functions.
When the user selects the write option, the script should demand for a file name, create it if it
does not exist, and continuously demand for inputs and write them to the file until the user
enters the word “stop” then the script should finish writing and return back to the menu options.
When the output option is selected, the script should demand for the name of the file to be
printed and output its content. The script should ensure that the file exist and not empty before
outputting all of its content to the screen. Then return back to the menu options.
When the permission option is selected, the script should demand for a name of the file, check
if the file exist and assign execution permission to the file if not already assigned. In case
execution permission is already assigned, simply report it. The terminate option should end the
script with a goodbye message. Properly comment your code.


### Task 11
Write a bash script that automates the creation and deletion of user accounts. The script should
accept as input argument, a file containing a list of usernames to be created on the system.
Enforce that the user provides this input file when running the script.
The script should check if the usernames already exist on the system before creating the
accounts. If a user account exit, the script should notify the user and skip that user name to the
next one. Make sure to create a home directory as well. When the input list has been exhausted
and all the user account created, output the content of “/etc/passwd” file and “/home” directory
to the terminal for verification.
In a next step, the script should ask if user wants to delete the newly created accounts? If yes,
the script should delete the accounts including their home directories and output again the
content of “/etc/passwd” file and “/home” directory for verification. If no, the script should
terminate with appropriate message.
Use functions to implement the account creation and deletion operations. The functions should
in each case accept one parameter. This script should only be tested/executed with root user
privileges. Ensure its enforcement. Properly comment your code.
