This Python script generates a specified number of passwords with user-defined lengths. Each password contains a mix of lowercase letters, numbers, and uppercase letters to enhance security. The script ensures that each password has at least one number and one uppercase letter.
Modules and Libraries
•	random: Used to generate random indices and values for creating the passwords.
Functions
1. create_passwords(lengths)
Description: Generates passwords based on the provided list of lengths.
Parameters:
•	lengths: A list of integers specifying the desired lengths for each password.
Returns:
•	generated_passwords: A list of generated passwords.
Behavior:
•	Iterates through the list of lengths.
•	For each length, generates a password of that length containing random lowercase letters.
•	Inserts at least one number and one uppercase letter into each password.
•	Appends each generated password to the list of passwords.
2. insert_number(pword)
Description: Inserts one or two random numbers into the first half of the password.
Parameters:
•	pword: A string representing the password.
Returns:
•	pword: The modified password with at least one number inserted.
Behavior:
•	Randomly chooses one or two positions within the first half of the password.
•	Replaces characters at those positions with random digits.
3. insert_uppercase(pword)
Description: Converts one or two characters in the second half of the password to uppercase.
Parameters:
•	pword: A string representing the password.
Returns:
•	pword: The modified password with at least one uppercase letter.
Behavior:
•	Randomly chooses one or two positions within the second half of the password.
•	Converts characters at those positions to uppercase.
Main Function
main()
Description: Handles user input and coordinates the generation of passwords.
Behavior:
•	Prompts the user to enter the number of passwords to generate.
•	Prompts the user to specify the length for each password, ensuring a minimum length of 3 characters.
•	Calls create_passwords to generate the passwords.
•	Prints each generated password.
How to Use
1.	Run the script: Execute the Python script to start the program.
2.	Enter the number of passwords: Input the number of passwords you want to generate when prompted.
3.	Specify password lengths: For each password, input the desired length. If a length less than 3 is specified, it will be adjusted to 3.
4.	View generated passwords: The script will output the generated passwords, each containing a mix of lowercase letters, numbers, and uppercase letters.

