# escape characters
# used for text print formatting
# NOTES :
'''
# escape characters

print("STRING")

if we want to give special meaning to our output on screen, we can use escape characters.

Escape Character = it escapes the natural meaning of a string.

New Line

Newline Character : \n
Tab Space : gives 8 spaces between the strings : \t
Backspace : \b
Single quote escape : \'
Double quote escape : \"
Slash escape : \\

'String' : '', "", """ """ are not allowed
"String" : "", """ """ are not allowed
"""String""" : """ """ are not allowed

\Hello World\
'''

print("Hello World")
print("Hello\nWorld\nHello")
print("Hello\tWorld")
print("Hello\t\tWorld")

# Use Case
# Print a Menu Box
'''

 ++++++++++++++++++++++++++
 +          MENU          +
 ++++++++++++++++++++++++++

'''

for i in range(21):
    print("-", end='')  # by default print executes a new line after each time of printing

print("\n|\t\tMENU\t\t|")

for i in range(21):
    print("-", end='')

# Use case of \b
# Masked aadhar : 1234 8999 8XXX XXXX

aadhar_number = "1234 5678 1234 9090"

print("\nMASKED AADHAR NUMBER : ", aadhar_number, "\b\b\b\b\b\bX XXXX")
print(aadhar_number)

# quotes escaping
# ' "hello world" ' not possible
# " "HEllo WORLD" " NOT POSSIBLE
# """ """HEllo WORLD""" """ NOT POSSIBLE

# USe case
# ' 'Hello World' '
print('\'Hello World\'')
print('Chethan\'s bucket')
print("Chethan's Bucket")

# ""Chethan's Bucket""

print("\"Chethan's Bucket\"")
print("\"\"\"Chethan's Bucket\"\"\"")

# "Chethan's Bucket"
print('\"Chethan\'s Bucket\"')

# 'Chethan's BUcket'
# "Chethan's Bucket"

print("""'Chethan's Bucket'""")
print(""" "Chethan's Bucket" """)
print(""" "Chethan's Bucket" """)

# use case
# \hello world\

print("\\Hello World\\")
