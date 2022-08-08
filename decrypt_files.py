import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file=="thekey.key" or file=="decrypt_files.py" or file=="encrypt_files.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key",'rb') as key:
    secretkey = key.read()

secret_code = "kewal1712"
user_input = input("Enter the Secret Code to decrypt : ")
if user_input==secret_code:
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
            contents_decrypt = Fernet(secretkey).decrypt(contents)
        with open(file,'wb') as thefile:
            thefile.write(contents_decrypt)
            
print("All your Files are Decrypted! LOL! Enjoy your day now!")