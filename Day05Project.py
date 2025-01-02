import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator \n")
userInputLetters=int(input("Enter the no. of letters in the password: \n"))
userInputChar=int(input("Enter the no. of characters in the password: \n"))
userInputNum=int(input("Enter the no. of numbers in the password: \n"))


passwordList=[]
for i in range(0,userInputLetters):
    passwordList += random.choice(letters)

for i in range(0,userInputChar):
    passwordList += random.choice(symbols)

for i in range(0,userInputNum):
    passwordList += random.choice(numbers)

random.shuffle(passwordList)

password=""
for i in passwordList:
    password += i

print(f"Your password is: \n{password}")
