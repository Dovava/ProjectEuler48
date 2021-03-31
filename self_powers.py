num = 0
for number in range(1,1001):
    num += number**number
print(str(num)[-10:])
