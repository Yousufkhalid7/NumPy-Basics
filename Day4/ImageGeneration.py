#Images are nothing other than a collection of pixels. And each pixel is nothing other than value for a colour. And any colour can be represented as a combination of red, green, and blue (RGB).
import numpy as np
import matplotlib.pyplot as plt

#for image (0-255) pixels, (256,256,3) shape of the array, stores each value as 8-bit integer(0-255)
img = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

print(f'Shape of the image is {img.shape}')
print(f'Image has {img.ndim} dimensions')
print(f'Data type of image is {type(img)}')

plt.imshow(img) #show the image
plt.show()