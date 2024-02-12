number = int (input ("Enter number"))
factorial = 1
for i in range(number + 1):
    if  i == 0:
        print(f"{i}! =", factorial)
        continue
    factorial = factorial * i
    print(f"{i}! =", factorial)
print(f"So  {number}! = {factorial}")

 
