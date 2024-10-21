#Alain Lee

#Takes a string of integers and cycles each digit up by 3 to encode it.
def encode(plain_password):
	encoded_password = "";
	for i in plain_password:
		encoded_password += str((int(i) + 3) % 10);
	return encoded_password


def decode(stored_encoded_password):
	decoded_password = ""
	for i in stored_encoded_password:
		decoded_password += str((int(i) - 3) % 10);
	return decoded_password

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
			decoded_password = decode(stored_encoded_password)
			print(f'The encoded password is {stored_encoded_password}, and the original password is {decoded_password}')
		elif user_option == 3:
			break


if __name__ == "__main__":
	main()
