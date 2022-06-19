
# write to file function called when option 1 from main menu is use
write_to_file(){
	echo -en "Enter the name of the file: \n>>> "; read name

	# checking if the file exists
	if [ -e $name ]
	then

		loop_controller=1
		while [ $loop_controller -eq 1 ];
		do
			echo -en "File already exists. What do You want to do? o=overwrite, a=append, c=cancel. \n>>> "; read write_choice
			# case statement to select option
			case $write_choice in
				o | O) overwrite
				break;;
				a | A) append
				break;;
				c | C) echo -e "Operation canceled!"
				loop_controller=0;;
				*) echo -en "What do You want to do? o=overwrite, a=append, c=cancel \n>>> ";;
			esac
		done
	else
		overwrite
	fi
}

overwrite(){

	input=""
	while [ "$input" != "stop" ]
	do
		echo -en "Enter the text, type 'stop' to finish: \n>>> "; read input
		if [ "$input" == "stop" ]
		then
		     break
		else
		    echo $input > $name
		fi
	done
}

append(){

	input=""
	while [ "$input" != "stop" ]
	do
		echo -en "Enter the text, type 'stop' to finish: \n>>> "; read input
		if [ "$input" == "stop" ]
		then
		     break
		else
		    echo $input >> $name
		fi
	done
}

# output the file function when option 2 from main menu is used
output(){
	echo -en "Enter the name of the file: \n>>> "; read filename
	if [[ -e $filename && -s $filename ]]
	then
		cat $filename
	elif [[ ! -s $filename && -e $filename ]]
	then
		echo -e "\nSelected file is empty!"
	else

		echo -e "\nFile does not exist!"

	fi
}

# change permission function when option 3 is used
change_permission(){

echo -en "Enter the name of the file: \n>>> "; read filename
if [[ -e $filename && ! -x $filename ]]
then
	chmod u+x $filename
	echo -e "\nExecution permission granted!"

elif [ -x $filename ]
then
	echo -e "\nFile already has execution permission!"

else
	echo -e "\nFile does not exists!"
fi
}

#main function definition
main(){
	while [ 1 ];
	do
	echo -en "\nTask 2 application\n1. Create File and Write content to a File \n2. Output content of a file to the Terminal \n3. Change File permission \n4. Exit \n>>> ";read choice
		case $choice in
			1)write_to_file;;
			2)output;;
			3)change_permission;;
			4) echo "Thank you, goodbye!"
			exit 1;;
			*) echo "Choose one of the following options";;

		esac
	done
	}

#main function called
main
