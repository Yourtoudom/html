# Number Classifier
number = int(input("Enter a number: "))
# Check the criteria and classify the number
if number > 0 and number % 2 == 0:
    print("Positive Even")
elif number > 0 and number % 2 != 0:
    print("Positive Odd ")
elif number < 0:
    print("Negative")
else:
    print("Zero")