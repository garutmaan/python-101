speed_value = 10.67

# int : integers
# float : fractions, real numbers
# complex : complex numbers
# Bool : True or False values
# Str : anything in '' or "" or """ """ , character or group of characters
# bytes : numbers in format of bytes(8 bits)
# bytearray : group of bytes
# range : range() => produce or yield numbers based on start and end value, sequence
# list : collection of various data types
# tuple : list but immutable
# set : collection of data, without duplicates
# frozenset : set, which is immutable
# dict : map type, key-value pair
# None : means, memory has not been allocated yet or NULL, nothing.

print(type(speed_value))

# int
# Type Casting : converting one data to another data type
# 1. int() : converts data to int type
# converting float to int
print(int(10.544555))
# converting string to int
print(int("90123456789"))
print(type(int("90123456789")))
print(int(True))
print(int(False))

# float()

print(float(10))
print(float("10.987766"))
print(float(True))

# bool()

print(bool(1))
print(bool(1000))
print(bool(0.5))
print(bool(0.0))
print(bool(-2))
print(bool(-2))
print(bool("Hello"))
print(bool("h"))
print((bool("")))
print(type(bool("")))

# str()

print((str(1)))
print(type(str(1)))
print(str(1.0))
print(str(445566778899))
print(str(True))
print(str(False))
print(str(0))

# id()

momentum_value = 20
print(id(momentum_value))
print(hex(id(momentum_value)))

# id speciality

value_1 = 10
value_2 = 20
print(id(value_1))
print(id(value_2))

value_2 = 10
print(id(value_1))
print(id(value_2))

value_2 = value_1 + 10

print(id(value_1))
print(id(value_2))

value_2 = "hello"
value_3 = "hello123"

print(id(value_2))
print(id(value_3))

value_2 = "1"
value_3 = 1

print(id(value_2))
print(id(value_3))

value_2 = int("1")
value_3 = 1

print(id(value_2))
print(id(value_3))

# list
# bag of data
# insertion order is preserved
# heterogeneous data types are allowed
# duplicates are allowed
# Growable (takes up RAM memory)
# values are enclosed inside square bracket [ ]
# Syntax : [10, 20, 30, 40, "True", True, "hello", 9.555, 'A']
# derived data type : it is constructed using existing data types
# list() -> converts data collection to list type / creates a new empty list
fruits = list()
print(fruits)
fruits = []
print(fruits)
fruits = ["mango", "apple", "guava", "watermelon"]
print(fruits)
print(type(fruits))
print(id(type(fruits)))

# accesing list data items/elements/members
# indexing : accessing elements of a list/collection using index values
# index values : integers ranging from -x to +x / room number
# index values for first item is always 0
# index values for lat item is always -1
# list last item can also be accessed using index value = total_length of list - 1
fruits = ["mango", "apple", "guava", "watermelon"]
print(fruits[0])
print(type(fruits[0]))
print(id(fruits))
print(id(fruits[0]))
print(fruits[1])
print(fruits[2 - 1])
print(fruits[-1])

# len() -> gives the total size of a collection
# syntax : len(collection_name)

print(len(fruits))
print(fruits[len(fruits) - 1])

# tuple : list but immutable
# if we try to add anything to tuple, it will take different address
# represented using ()
# tuple() : gives a tuple from any collection or gives an empty tuple
# () -> empty tuple

meals = ()
print(meals)
print(type(meals))
print(len(meals))
print(id(meals))
meal = tuple()

print(meals)
print(type(meals))
print(len(meals))
print(id(meals))

meals = 10,

print(meals)
print(type(meals))
print(len(meals))
print(id(meals))

meals = ("south", "north", 100, 150, "veg", 500, "sattvic", 900.9, True)

print(meals)
print(type(meals))
print(len(meals))
print(id(meals))

meals = ("south", "north", 100, 150, "veg", 500, "sattvic", 900.9, True, False)

print(meals)
print(type(meals))
print(len(meals))
print(id(meals))

# accessing tuple items
# indexing, similar to list

print(meals[0])
print(meals[1])
print(meals[-1])

# range
# special data type
# it produces a sequence of numbers
# immutable
# syntax : range(start_value,end_value)
# syntax : range(end_value)
# syntax : range(start_value,end_value,step_size)
# defaults : start_value = 0, step size = 1

print(range(10))
print(range(0, 10))
print(range(5, 10))
print(range(0, 10, 2))
print(type(range(0, 10, 2)))

# how to see data in range()
# using for loop\
# or by converting range() to list

even_numbers = list(range(0, 20, 2))
print(even_numbers)

numbers_list = list(range(0, 20))  # always gives 0 to n-1, n=end-value
print(numbers_list)

# set
# bag
# insertion order is not preserved
# duplicates are not allowed
# indexing is not allowed
# mutable collection
# growable
# syntax : set()
# represented using {}
# {} => IS NOT AN EMPTY SET, IT IS EMPTY DICTIONARY/MAP/K-V PAIR
# set() => this is actually empty set
# used in discrete maths operations

data_set = {"hello", 123, "True", True, False, 10.9, 10.9, 10.9, True, True, False, "hello", "HELLO", "hELLO", "Hello"}
print(data_set)
print(type(data_set))
print(id(data_set))

# frozenset
# immutable set
# syntax : frozenset(set())

data_frozen_set = frozenset(data_set)

print(data_frozen_set)
print(type(data_frozen_set))

# use case : remove duplicates from a list

fruits = ["mango", "apple", "apple", "apple", "mango", "guava", "guava", "peach"]
print(fruits)
fruits_unique = set(fruits)
print(fruits_unique)
fruits = list(fruits_unique)
print(fruits)

# dict
# key : value type of data
# key : can be any data type , mostly string or int
# value also can be any data type
# dict() or {}

mind_map = {}
mind_map = {
    "apple": "fruit",
    "time": "clock",
    "food": "sattvic"
}
print(mind_map)
print(type(mind_map))

# assignment

# 1. create list of employee details
# use same for all other collection
