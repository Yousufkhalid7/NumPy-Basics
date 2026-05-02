import numpy as np

#4x2 matrix
m1 = np.array([[1,3],
                [0,1],
                [6,2],
                [9,7]])

#2x3 matrix
m2 = np.array([[3, 4, 7],
               [1, 4, 8]])

#Result will be 4x3 matrix
print(np.matmul(m1, m2))