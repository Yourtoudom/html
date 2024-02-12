age = 19
height = 2.5 # 2.5 mters
print(type(age))
print(type(height))
print(type(student))

# Part 2: Operators
## 1. arithmetic operations
res_add = age + 5
res_subtract = height - 2.5
res_multiply = age * 2
res_divide = height / 2
print("Add: ", res_add)
print("Subtract: ", res_subtract)
print("Multiply: ", res_multiply)
print("Divide: ", res_divide)

## Use in-place operators to modify the variables
age += 1 # age = age + 1
height *= 2 # height = height * 2
print("new age: ", age)
print("new height: ", height)

## Compare age and height using comparison operators 
result = age >= height
print(result)

# Use logical operators to combine the boolean value 
comp_result = result == student
print(comp_result)

# Part 3: Membership Operation
## Create a list called colors with at least five color names 
color = ["red", "blue", "yellow", "white", "green"]
item_to_check = "black"
result = item_to_check in color
print("Green is", result, "in the list")
color.append("purple")
print(color)

# Part 4: String Manipulation
sentence = "Python is an amazing programming language."
sentence += "I enjoy learning it."
print(sentence)
name = "John"
age = 19
text = f"My name is {name} and my age is {age} years old"
text = "My name is {} and my age is {} years old".format(name, age)
print(text)

length = len(text)
print("Length of text is ", length)

extract = sentence[13:21]
print(extract)

uppercase = sentence.upper()
print(uppercase)

new_sentence = sentence.replace("Python", "JavaScript")
print(new_sentence)

check = "programming"
result = check in sentence
print(result)

splitted = sentence.split()
print(splitted)