import numpy as np

array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

print(f'Array has {array.ndim} dimensions')
print(f'Shape {array.shape}')
print(array[2,0,3])