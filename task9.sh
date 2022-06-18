#Checking if 2 parameters have been given
if [ $# -eq 2 ]
then

	# declaring an array to store name of the files
	Array=()

	echo ""
	#loop that goes for every file in a folder
	for file in *
	do
		#checking content of files only
		if [ -f $file ]
		then
			#Checking how many times pattern occurs in a file
			count="`grep -oi $2 $file | wc -l`"
			if [ $count -ge 1 ]
			# printing message
			then
				ls -l | grep $file | awk '{print "Name:", $9, "\nCreated at: " $6, $7, $8, "\nSize:", $5,"bytes."}'
				echo "$2 pattern appeared: $count times."; echo ""
			fi
			#appending to array if pattern occurs at least twice
			if [ $count -ge 2 ]
			then
				Array+=("$file")
			fi
		fi
	done

	# assigning length of Array to array_len variable and declaring num to control until loop
	array_len=${#Array[@]}
	num=0

	#creating file report if not exist and removing content if does
	touch report.txt
	rm -rf report.txt

	#loop that echo content of the Array entry by entry and appending to report.txt
	until [ $num -ge $array_len ]
	do
		echo "${Array[$num]}"
		echo "${Array[$num]}">>report.txt
		num=$(($num + 1))
	done

# when two parameters are not given
else
	echo "You should provide 2 attributes!"
	exit 1
fi