a = 10
if a > 5:
    print(a)
    print("This is if block.")

print("This is regular statement after if")

b = 0
if a and b:
    print("a = ", a)
    print("b = ", b)

if a > b:
    print("a is greater than b")

data = None

if data is None:
    print("data is None")

if data:
    print("data is None")

####################################

# grading system

marks = 99
if marks > 33:
    print("Pass")
    if marks > 60:
        print("With First Class")
        if marks > 90:
            print("And Distinction")
            if marks > 95:
                print("Congratulations!")

# print grades based marks

marks = 90
if (marks >= 91 and marks <= 100):
    print("A Grade")

if (marks >= 60 and marks <= 90):
    print("B Grade")

if (marks >= 45 and marks <= 61):
    print("C Grade")

if (marks >= 30 and marks <= 46):
    print("D Grade")
else:
    print("This Person has FAILED with F grade.")

# grading system with elif ladder, to solve the above bug

marks = 22
print("Printing Grade for marks : ", marks)

if marks >= 90 and marks <= 100:
    print("A Grade")
elif marks >= 60 and marks <= 90:
    print("B Grade")
elif marks >= 45 and marks <= 60:
    print("C Grade")
elif marks >= 30 and marks <= 45:
    print("D Grade")
else:
    print("This Person has FAILED with F grade.")

# Simplified if conditions:
marks = 22
print("Printing Grade for marks : ", marks)

if 90 <= marks <= 100:
    print("A Grade")
elif 60 <= marks <= 90:
    print("B Grade")
elif 45 <= marks <= 60:
    print("C Grade")
elif 30 <= marks <= 45:
    print("D Grade")
else:
    print("This Person has FAILED with F grade.")

