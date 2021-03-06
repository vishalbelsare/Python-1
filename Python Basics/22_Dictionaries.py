# dictionary has a Key-Value pair, like Name-Age in the below example
NameAge = {'Prateek':27, 'Mayank':25, 'Utkarsh':21}
print('Dictionary:',NameAge)

# Key is case sensitive, that means 'Prateek' with capital P and 'prateek' are different keys
print('Age of Prateek:',NameAge['Prateek'])

NameAge['Dheeraj'] = 25 # adding a new key-value pair to the dictionary
print('\nAdding Dheeraj in the dictionary..')

print('Dictionary:',NameAge)

del NameAge['Prateek'] # deleting a key-value pair from the dictionary
print('\ndeleting Prateek from the dictionary..')
print('Dictionary:',NameAge)


# you can also create lists in a dictionary to store complex data

DateOfBirth = {'Prateek':[1,'May',1990], 'Mayank':[12,'Feb',1992], 'Utkarsh':[10,'Oct',1995]}
print('\nDateOfBirth dictionary:',DateOfBirth)
print("Prateek's DOB:",DateOfBirth['Prateek'])
print('len of DOB dictionary:',len(DateOfBirth))

print('Mayank was born in month:',DateOfBirth['Mayank'][1])



squares = {} # empty dictionary
for x in range(1,10):
    squares[x] = x**2

#print(squares.items())

for key, value in squares.items() : # Dictionary.items() gives key-value sets which can be enumerated.
    print("Square of {0} is {1}".format(key, value))
