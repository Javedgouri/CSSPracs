#function of encryption
encrypt = lambda plaintext,shift :''.join(chr(((ord(text)-65+shift) % 26) + 65) if text.isupper() else chr(((ord(text)-97 + shift) % 26)+ 97) if text.islower() else text for text in plaintext)

#function for decryption
decrypt = lambda plaintext,shift :''.join(chr(((ord(text)-65-shift) % 26) + 65) if text.isupper() else chr(((ord(text)-97 - shift) % 26) + 97) if text.islower() else text for text in plaintext)

#to iterate
while True:
	print "1.Encrypt"
	print "2.Decrypt"
	print "3.Exit"
	choice = int(raw_input('Enter your Choice:'))
	if choice == 1:
		#input from user
		plaintext = raw_input("Enter the text you want to encrypt:")
		key = int(raw_input("Enter the key:"))
		ciphertext=encrypt(plaintext,key)
		print "Your CipherText = {} \n\n" .format(ciphertext)
	if choice == 2:
		#input from user
		ciphertext = raw_input("Enter the Cipher text you want to decrypt:")
		key = int(raw_input("Enter the key:"))
		plaintext=decrypt(ciphertext,key)
		print "Your PlainText = {} \n\n" .format(plaintext)
	if choice == 3:
		print "Thank you..................."
		break
