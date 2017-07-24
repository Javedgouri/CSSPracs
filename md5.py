import hashlib

text = str(input("Enter the String:"))

ciphertext = hashlib.md5(text.encode('utf-8')).hexdigest()

print("Hash:{}".format(ciphertext))
