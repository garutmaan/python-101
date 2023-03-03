# bitwise

number1 = 5
number2 = 6

# bit wise AND
print(number1 & number2)

# bit wise OR
print(number1 | number2)

# bit wise XOR
print(number1 ^ number2)

# bit wise NOT
print(~number1)
print(~number2)

number1 = 16
n_bits = 3

# 2 ^ n, n = number of bits

#  shift operators <<
print(number1 << n_bits)

#  shift operators <<
print(number1 >> n_bits)

print(True << 1)  # 1 * 2 = 2
print(False << 1)  # 0 * 2 = 0

print(True << 2)  # 1 * 4 = 4
print(False << 2)  # 0 * 4 = 0

print(True >> 1)  # 1 / 2 = 0
print(False >> 1)

print(True >> 2)  # 1/ 4 = 0
print(False >> 2)

# Assignment Operators:

# assign
# it will take Right Value and put in left value (holder/bag/variable)

data_1 = "Hello World"  # string data "hello world" will sit inside data_1 variable

# add and assign
# shorthand notation
x = 10
x += 10  # x will be assigned a value after doing addition with right-value first and then result will be added back
# to x

x = x + 10  # similar to above

# subtract and assign
x = 10
x -= 10  # x will be 0 now

# % and assign
x = 10
x %= 10  # x will be 0 now

# increment and decrement using assignment operator
# if you want to do, x++ or x-- (increment or decrement by 1)
# ex : add to cart : items count + 1
# delete from cart : items count - 1

x = 10
x -= -1  # x => 11

print(x)
