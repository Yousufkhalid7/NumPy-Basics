import numpy as np

array = np.arange(10,30)
#slicing technique
print(f'Last three values of the array {array[-3:]}')
print(f'4th, 5th and 6th element of the array are {array[3:6]}')
print(f'Elements except the first 12: {array[12:30]}')
print(f'Even elements: {array[::2]}')