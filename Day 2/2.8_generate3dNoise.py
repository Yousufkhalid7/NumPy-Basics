from numpy.random import random
import matplotlib.pyplot as plt

#generate noise
noise = random((128, 128, 3))

#display image
print(noise.shape)
plt.imshow(noise)
plt.show()