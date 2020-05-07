import random
print("Program to Generate a Random Password")
name=input("Enter your Name: ")
print("Hey "+name)
length=int(input("How Long should your pass be : "))
pwd="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}<>|\/?-_"
password=" "

if length < 6:
    print("Password length should be greater than 6 letters") 
else:
    for i in range(length):
        password += random.choice(pwd)    
print(password)