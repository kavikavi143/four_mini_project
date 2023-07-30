import random

print("Welcome to random password generator!")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&"
nbrofpwds = int(input("Please enter the number of passwords to be generated: "))
pwdlen = int(input("Please enter the length of the password needed: "))

message = "Here are your random passwords: "
for x in range(nbrofpwds):
    pwd = ""
    for chars in range(pwdlen):
        pwd = pwd + random.choice(randomchars)
    print(message + pwd)


