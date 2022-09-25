import hashlib
hash = input("password : ")
encryp= hashlib.md5(hash.encode())
print("here is your md5 encryption",encryp.digest())






