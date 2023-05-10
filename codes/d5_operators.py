velocity_value = 10  # assignment
print(velocity_value)

velocity_value += 100  # add and assign
print(velocity_value)

velocity_value -= 100  # minus and assign
print(velocity_value)

velocity_value *= 10  # multiply and assign
print(velocity_value)

velocity_value /= 10  # divide and assign
print(velocity_value)

number1 = 10
number2 = 100

max_number = number1 if (number1 > number2) else number2

print("The max number is = ", max_number)

number1 = 100
number2 = 1000
number3 = 10

max_number = number1 if ((number1 > number2) and (number1 > number3)) else number2 if (number2 > number3) else number3

print("number1 = ", number1)
print("number2 = ", number2)
print("number3 = ", number3)
print("The max of 3 number is = ", max_number)

# special operators

# is operator
print("is operator example : ")
a = 10
b = 10

result = a is b
print(result)

a = None
result = a is None
print(result)

result = a is not None
print(result)

a = 1000
result = a is not None
print(result)

# membership operators

# in example
print("in operator example : ")

voter_list = ["Chethan", "Hanish", "John"]
result = "Raghav" in voter_list
print(result)
result = "Raghav" not in voter_list
print(result)

result = "Chethan" in voter_list
print(result)

# Operator Precedence

print("Operator percedence while execution: ")

a = 30
b = 20
c = 10
d = 5

result = (a + b) * (c + d)
print(result)

result = (a + b) * c / d
print(result)

d = 9
result = (a + b) * c / d
print(result)

d = 5
result = a + (b * c) / d
print(result)
