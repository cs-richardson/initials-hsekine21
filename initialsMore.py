'''
This programs takes a name from the user and prints the initials of that name
in capital letters

Hina Sekine 
'''

# Greeting
print('This program will give the initials of the name you enter.\n')

# User Input
name = input('Enter your name: ')

# Splits string into a list, separated by ' '
partName = name.split(' ')

# Removes empty strings from the list 
while '' in partName:
    partName.remove('')

# Takes the first letter of each string in the list and puts them into a string 
initials = ''
for i in partName:
    initials = initials + i[0]

# Converts everything inside the list into uppercase and adds new line
initials = initials.upper() + '\n'

# Displays initials for the user 
print(initials)
