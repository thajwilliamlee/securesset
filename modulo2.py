#!/usr/bin/python3

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newletter = ""
newword = ""
newletters = ""
newwords = ""

if __name__ == "__main__":
    one = input("Use DECRYPT or ENCRYPT?")

if one == "ENCRYPT":
    word = input("What word to encrypt?")
    for letter in word:
        newletter = alphabet[(alphabet.index(letter) + 3) % 26].upper()
        newword += newletter
        print(word,newword)
elif (one == "DECRYPT"):
    dword = input("What word to decrypt?")
    for letter in dword:
        newletters = alphabet[(alphabet.index(letter) - 3) % 26].upper()
        newwords += newletters
        print(dword,newwords)
else:
    print ("cap sensitive?")





