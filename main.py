import random

all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
       'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
       'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
       'T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8',
       '9','0', '!','@','#','$','&','%','DG']
for i in range(1,100):
    random.shuffle(all)




numberChar = int(input("How many characters do you want in the password?(Minimum 6 characters) :\n"))
password = []
for i in range(0, numberChar):
    x = all[i]
    password.append(x)

charpass = "1"
for i in range(numberChar):
    charpass += password[i]
print("Your Password is:\n" + "=>" +str(charpass))
