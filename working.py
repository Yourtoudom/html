score = input ("enter your score: ")
score = float(score)
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif score <60:
    print("F")
else :
    print("invalid score")

