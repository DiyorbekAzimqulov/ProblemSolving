number = int(input("enter a credit card number: "))
len_num = len(str(number))
ctr = 0
total = 0
for i in range(len_num):
    ctr += 1
    temp = number % 10
    if ctr % 2 == 0:
        temp1 = temp * 2
        if (temp1 >= 10):
            temp1 = temp1 % 10 + 1
            total += temp1
        else:
            total += temp1
    else:
        total += temp
    number -= temp
    number = int(number / 10)
print(total)