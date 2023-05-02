# Relational Operator

num1 = 10
num2 = 100

result = num2 > num1  # returns True because num2 is > num1
print(result)
result = num1 > num2  # false
print(result)
result = num1 >= num2  # false
print(result)
result = num2 < num1  # false
print(result)
result = num1 < num2  # true
print(result)
result = num1 <= num2  # true
print(result)
result = num2 == num1  # false
print(result)
result = num1 != num2  # true
print(result)

# Equality Operators case

num1 = 100
num2 = 10

print("num1 is stored at : ", id(num1))
print("num2 is stored at : ", id(num2))

result = (num1 == num2)
print(result)

result = (num1 != num2)
print(result)

num1 = 100
num2 = num2 * num2

print("num1 is stored at : ", id(num1))
print("num2 is stored at : ", id(num2))

result = (num1 == num2)
print(result)

result = (num1 != num2)
print(result)

data_list = [10, 20]

result = data_list == None  # not a good idea, we should use is or is not operations here
print(result)

num1 = 10
num2 = 10
num3 = 1
num4 = 10

result = num1 == num2 == num3 == num4
print(result)

# Logical Operators:

'''
True and True => True
True and False => False

True or False => True
False or False => False

not True => False
not False => True
'''

num1 = 10
num2 = 100
num3 = 1000

print("Logical Operators")
result = (num1 > num2) and (num2 < num3)  # False
print(result)
result = (num1 > num2) or (num2 < num3)  # True
print(result)
result = (num1 > num2) and (not (num2 < num3))  # False
print(result)
