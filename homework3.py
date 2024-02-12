age = input("enter age: ")
age = int(age)
if age >= 18:
    experinece = int(input("enter experirece"))
    if experinece == 0:
    print("you need assistant")
elif experinece <= 10:
    print("you are allowed to dive 20m depth")
else:
    print ("you are allowed to dive 50m depth")
else:
    print ("you can't play")
