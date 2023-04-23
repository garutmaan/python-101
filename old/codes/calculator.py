# Print basic calculator functionality

# + addition
# - subtraction
# / division
# * multiplication

# expected output:
'''
WELCOME TO CLASS 1
SIMPLE CALCULATOR
SUM OF X AND Y IS Z
DIFF OF X AND Y IS Z
PRODUCT OF X AND Y IS Z
DIVISION OF X BY Y IS Z
'''

# declare variables
value_1 = 10
value_2 = 20

print("WELCOME TO CLASS 1")
print("SIMPLE CALCULATOR")

value_3 = value_1 + value_2  # add v1 and v2 and store in v3
print("SUM OF", value_1, "AND", value_2, "IS", value_3)

value_3 = value_1 - value_2  # add v1 and v2 and store in v3
print("DIFF OF", value_1, "AND", value_2, "IS", value_3)

value_3 = value_1 * value_2  # add v1 and v2 and store in v3
print("PRODUCT OF", value_1, "AND", value_2, "IS", value_3)

value_3 = value_1 / value_2  # add v1 and v2 and store in v3
print("DIVISION OF", value_1, "BY", value_2, "IS", value_3)

value_4 = complex(10, 9)
value_5 = [10, 20, 30]

print("DATA TYPE OF VALUE_1 IS ", type(value_1))
print("DATA TYPE OF VALUE_2 IS ", type(value_2))
print("DATA TYPE OF VALUE_3 IS ", type(value_3))
print("DATA TYPE OF VALUE_4 IS ", type(value_4))
print("DATA TYPE OF VALUE_4", value_4, "IS ", type(value_4))
print("DATA TYPE OF VALUE_4", value_5, "IS ", type(value_5))
