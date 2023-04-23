'''
OPERATORS / OPERATIONS IN PYTHON
==================================
OPERATION => A SMALL SPECIFIC ACTIVITY OR TASK OR COMPONENT OF A BIGGER EXECUTION.

OPERATOR => SYMBOL THAT PERFORMS CERTAIN OPERATIONS

1. ARITHMETIC
2. RELATIONAL
3. LOGICAL
4. BIT-WISE
5. ASSIGNMENT
6. SPECIAL OPERATORS

==========================================
1. ARITHMETIC OPERATORS:

+ => ADDITION

- => MINUS

* => PRODUCT

/ => QUOTIENT

% => REMAINDER / Modular Division / Modulus

1. in p%q, the max remainder you can get is p
2. if p < q, then % will always return p

// => FLOOR DIVISION

** => EXPONENT
================================================

2. RELATIONAL

<  - Less than
>  - greater than
>= - GTE
<= - LTE
== - Equals To
!= - Not Equals

note: relational operators or comparison operators always return boolean value (True/False)

# Chained Operations

10<20 => True
10<20<30 => True
10<20<30<40 => True
10<20<30<40>50 => False
10<20<30<40<30 => False
10 > 20 < 30 > 40 < 30 => False

================================================
3. LOGICAL

does logical operation on two entities.

AND => True if both are True
OR => True if one is True
NOT => Complement

# for Boolean values:
True AND True => True
True OR False => True
NOT True => False

# for non boolean value

0 => means False,
non-zero => True,

empty string => False,
Non-Empty (string) => True

SHORT-CIRCUIT OPERATION:
========================

WE COMPARE THE SUFFICIENT CONDITION AND MOVE FORWARD, IF REQUIRED.

TRUE AND TRUE => TRUE, AFTER EVALUATING 2ND CONDITION
TRUE OR FALSE => TRUE, AFTER EVALUATING, 1ST CONDITION, NOT EVEN BOTHERED ABOUT 2ND ONE

=============================================
'''

value_1 = 10
value_2 = 20

value_3 = value_1 + value_2
value_3 = value_1 - value_2
value_3 = value_2 - value_1
value_3 = value_2 - value_2

value_3 = value_1 * value_2

value_3 = value_1 / value_2
value_3 = value_2 / value_1

value_2 = 0

# Exception : ZeroDivisionError: division by zero
# value_3 = value_1 / value_2

value_2 = 22
value_1 = 7

value_3 = value_2 / value_1

value_2 = 90
value_1 = 100
# 0, 0, 1, 2, 0, 4, 3, 2, 1, 0, 10, 10

value_3 = value_2 % value_1
print(value_3)
value_1 = 15
value_3 = value_1 % 2

value_2 = 99.3
value_1 = 4.5

value_3 = value_2 // value_1

print(value_2, "//", value_1, "=", value_3)

value_2 = 10
value_1 = 6

value_3 = value_2 ** value_1

print(value_3)

print(type(value_1))
print(type(value_2))
print(type(value_3))

# relational ops
# value_2 = True
# value_1 = 10

value_2 = 200
value_1 = 300
value_3 = value_2 > value_1
print(value_3)

value_3 = value_2 < value_1
print(value_3)

value_3 = value_2 >= value_1
print(value_3)

value_3 = value_2 <= value_1
print(value_3)

value_3 = value_2 == value_1
print(value_3)

value_3 = value_2 != value_1
print(value_3)

value_3 = 10 < 20 < 30 < 40 < 30
print(value_3)

value_3 = 10 > 20 < 30 > 40 < 30
print(value_3)

value_2 = 10 < 5
value_1 = 11 > 5

value_3 = value_2 and value_1
print(value_3)

value_3 = value_2 or value_1
print(value_3)

value_3 = not value_1
print(value_3)

value_3 = not value_2
print(value_3)

value_2 = 100
value_1 = 200

value_3 = value_2 > value_1
print(value_3)

value_1 = ""
value_2 = "Hanish1234"

value_3 = value_2 and value_1
print(value_3)

value_3 = value_1 or value_2
print(value_3)

value_3 = not value_1
print(value_3)
