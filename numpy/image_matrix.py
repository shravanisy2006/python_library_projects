import numpy as np
import matplotlib.pyplot as plt

image = np.array([
    [255, 200, 150],
    [100, 50, 0],
    [180, 220, 90]
])

plt.figure(figsize=(4, 4))
plt.subplot(1 , 2 ,1)
plt.imshow(image, cmap = 'gray')
plt.title("Original Image")
plt.axis('off')

inverted = 255 - image
plt.figure(figsize=(4, 4))
plt.subplot(1 , 2 , 2)
plt.imshow(inverted , cmap= 'gray')
plt.title("Inverted image")
plt.axis('off')

bright = image + 50
bright = np.clip(bright, 0, 255)
plt.figure(figsize=(4, 4))
plt.subplot(1 , 2 , 1)
plt.imshow(bright , cmap= 'gray')
plt.title("Brightened image")
plt.axis('off')

cropped = image[0:2, 0:2]
plt.figure(figsize=(4, 4))
plt.subplot(1 , 2 , 2)
plt.imshow(cropped , cmap= 'gray')
plt.title("cropped image")
plt.axis('off')

rotated = np.rot90(image)
plt.figure(figsize=(4, 4))
plt.subplot(1 , 2 , 1)
plt.imshow(rotated , cmap= 'gray')
plt.title("Rotated image")
plt.axis('off')
plt.show()
