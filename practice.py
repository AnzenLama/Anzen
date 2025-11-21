import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol=['!','@','#','$','^','&','(',')']
numer=[1,2,3,4,5,6,7,8,9,0]
lists=[]
number_of_letter=int(input("enter the number of letter you want"))
number_of_symbol=int(input("enter the number of the symbol you want"))
number_of_number=int(input("enter the number of number you want in your passowrd"))
password=''
for l in range(number_of_letter):
    lists.append(random.choice(letter))
for b in range(number_of_symbol):
    lists.append(random.choice(symbol))
for a in range(number_of_number):
    lists.append(random.choice(numer))
print(lists)
random.shuffle(lists)
print(lists)
for passw in lists:
    password +=str(passw)
print("your password is=",password)
