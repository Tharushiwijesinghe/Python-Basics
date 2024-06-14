#q1
length = 92
wide = 48.8

area = (length * wide)
print("Total Area: " , area)


#q2
chips = 9
cost = 1.49
amount = 20

balance = amount - (chips*cost)
print("Balance is: ",balance)


#q3
length = 5.5
area = length ** 2

print("Total cost = ", area*500)


#q4
num = 17

binaryno = " "

while num > 0:
    binaryno = str(num % 2) + binaryno
    num = num // 2

print(binaryno)

#format(num,'b') -  convert for binary number
num=17
print('Binary of number 17 is:',format(num,'b')) 
