import numpy as np
import matplotlib.pyplot as plt

image = np.array([
    [255, 200, 150],
    [100, 50, 0],
    [180, 220, 90]
])

plt.subplot(3 , 2 ,1)
plt.imshow(image, cmap = 'gray')
plt.title("Original Image")
plt.axis('off')

inverted = 255 - image
plt.subplot(3 , 2 , 2)
plt.imshow(inverted , cmap= 'gray')
plt.title("Inverted image")
plt.axis('off')

bright = image + 50
bright = np.clip(bright, 0, 255)
plt.subplot(3 , 2 , 3)
plt.imshow(bright , cmap= 'gray')
plt.title("Brightened image")
plt.axis('off')

cropped = image[0:2, 0:2]
plt.subplot(3 , 2 , 4)
plt.imshow(cropped , cmap= 'gray')
plt.title("cropped image")
plt.axis('off')

rotated = np.rot90(image)
plt.subplot(3 , 1 , 3)
plt.imshow(rotated , cmap= 'gray')
plt.title("Rotated image")
plt.axis('off')

plt.tight_layout()
plt.savefig("image_matrix_output.png")
plt.show()


# fig, axes = plt.subplots(1, 5, figsize=(15, 4))

# images = [image, inverted, bright, cropped, rotated]
# titles = ["Original Image", "Inverted Image", "Brightened Image", "Cropped Image", "Rotated Image"]

# for ax, img, title in zip(axes, images, titles):
#     ax.imshow(img, cmap='gray')
#     ax.set_title(title)
#     ax.axis('off')

# plt.tight_layout()
# plt.show()