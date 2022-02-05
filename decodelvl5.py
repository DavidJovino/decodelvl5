import hashlib
import sys


pos_pw_list = []
with open("dictionary.txt","r") as my_file:
    first_list = my_file.readlines() 
    for i in first_list: 
        pos_pw_list.append(i.strip())


correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

for user_pw in pos_pw_list:
	user_pw_hash = hash_pw(user_pw)
	if( user_pw_hash == correct_pw_hash ):
		print(user_pw)

