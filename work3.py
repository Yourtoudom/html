count = 1
forgiven = False
while  not  forgiven:
    print(f"l'm sorry{count}time")
    response = input ().lower()
    if response == "yes":
        print("Thank you for your forgiveness")
    else:
        count+=1
