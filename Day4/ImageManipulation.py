import numpy as np
import matplotlib.pyplot as plt

img = np.random.randint(0, 255, ( 256, 256, 3), dtype=np.uint8)

#convert image into black and white using a Linear Formula
# Y = 0.2126R + 0.7152G + 0.0722B
#However, this formula only works if our red, green and blue values are between 0 and 1 - namely in sRGB format. Currently the values in our img range from 0 to 255.

#So:
sRGB_array = img/255 # Divide all the values by 255 to convert them to sRGB.

grey_values = np.array([0.2126, 0.7152, 0.072])
img_gray = np.matmul(sRGB_array, grey_values) # Multiply the sRGB array by the grey_vals array (provided) to convert the image to grayscale.

plt.imshow(img_gray, cmap='gray') # Finally use Matplotlib's .imshow() with the colormap parameter set to gray cmap=gray to display the result.
#The cmap parameter is important here. If we leave it out the function will not know that is dealing with a black and white image.
plt.show()