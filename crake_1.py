import hashlib

pass_hash = input("enter md5 hash: ")

wordlist = input("file name: ")

try:
	pass_file = open (wordlist, "r")
except:
	print("No file found")
	quit()

for word in pass_file:

	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	print(word)
	print(digest)
	print(pass_hash)

	if digest == pass_hash:
		print("passward found")
		print("passward is " + word)
		flag = 1
		break
	if flag == 0:
		print("passward/passphrase is not in the list")
