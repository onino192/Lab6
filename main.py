#Alain Lee

#Takes a string of integers and cycles each digit up by 3 to encode it.
def encode(plain_password):
	encoded_password = "";
	for i in plain_password:
		encoded_password += str((int(i) + 3) % 10);
	return encoded_password

#Main function. Loops the menu.
def main():
	while True:
		print("Menu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit")
		user_option = int(input("Please enter an option: "))
		if user_option == 1:
			password = input("Please enter your password to encode: ")
			stored_encoded_password = encode(password); #This variable stores the encoded password.
			print("Your password has been encoded and stored!")
		elif user_option == 2:
			continue #remove the continue keyword and insert your code
		elif user_option == 3:
			break


if __name__ == "__main__":
	main()
