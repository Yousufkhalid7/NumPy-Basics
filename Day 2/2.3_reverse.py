import numpy as np

array = np.arange(10, 30)
#Using colon operator
#print(f'Reversed array: {array[::-1]}')

#Using built-in .flip() function
print(f'Reversed array: {np.flip(array)}')