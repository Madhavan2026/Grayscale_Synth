import cv2
import matplotlib.pyplot as plt

# Loads in BGR format
org_img = cv2.imread("Enter the path to image")

if org_img is None:
    raise FileNotFoundError(f"Error: Could not open or find the image at {org_img}")

# Show the original image 
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Now convert into grayscale format
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(1,2,2)
plt.title("Grayscale Image")
plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.show()

# To write the grayscale image
#cv2.imwrite("gray_image.png", gray)

