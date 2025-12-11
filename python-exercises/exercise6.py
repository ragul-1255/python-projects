import random
import string
import time

chars=list(string.ascii_letters+' '+string.digits)
key=chars.copy()
random.shuffle(key)
encrypt=[]
decrypt=[]
def encryption(message):
    print("encrypting")
    for i in message:
        index=key.index(i)
        encrypt.append(chars[index])
        print("..",end='')
        time.sleep(0.5)
    print("done!")
def decryption():
    dec=input("\nenter your encrypted message to be decrypted:")
    print("decrypting")
    for j in dec:
        index=chars.index(j)
        decrypt.append(key[index])
        print("..",end="")
        time.sleep(0.5)
    print("done!") 
message=input("enter a message to encrypt: ")
encryption(message)
print("\nencrypted message : ")
for i in encrypt:
    print(i,end="")
decryption()
print("decrypted message : ")
for j in decrypt:
    print(j,end='')



