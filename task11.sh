
#!/bin/bash

#First I check if the user is root and if he gave 1 argument. Then we pass the file name to the function. Which are created by the users.

# making sure the user has the root privilege and provided an argument
readiness_check(){
#if $EUID equals 0 we have root privilege
if [ $EUID -ne 0 ]
then
	echo "Log in as root user!"
	exit 1
elif [[ $EUID -ne 0 && $# -ne 1 ]]
then
    echo "Please provide a file as an argument"
    exit 1
fi
}

# Creating accounts from file
create_accounts(){
IFS=$'\r\n'
file=(`cat $1`)
#loop for every entry in the file
for user in "${file[@]}"
do
    if [ `sed -n "/^$user/p" /etc/passwd` ]
    then
	    echo "User $user already exists"
	    continue
    else
	    useradd -m $user
    fi
done
}

#deleting accounts
delete_accounts(){
echo  "Do you want to delete newly created accounts? type 'yes' to delete ";read choice
if [ "${choice,,}" == "yes" ]
then
	IFS=$'\r\n'
	file=(cat $1)
	for user in "${file[@]}"
	do
		userdel -rf $user
	done
else
	echo "Newly created accounts have not been deleted"
fi
}

show_content(){
num_lines=${#file[@]}
echo -e "\n/etc/passwd content: \n"
echo /etc/passwd
echo -e "\nhome directory: \n"
ls -all /home
}

#declering main function
main(){
readiness_check $1
create_accounts $1
show_content
delete_accounts $1
show_content

}

#calling main function
main $1


