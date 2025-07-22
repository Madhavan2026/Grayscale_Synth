import cv2
import matplotlib.pyplot as plt

def create_xerox_effect(image_path, threshold_value=128):
    try:
        # Load the Image
        original_image = cv2.imread(image_path)

        if original_image is None:
            raise FileNotFoundError(f"Error: Could not open or find the image at {image_path}")

        # Display the original image (optional)
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title("Original Image")
        plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')

        # Convert to Grayscale
        grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Apply Thresholding
        ret, binary_image = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)

        # Display the processed image
        plt.subplot(1, 2, 2)
        plt.title(f"Xerox Effect (Threshold={threshold_value})")
        plt.imshow(binary_image, cmap='grey')
        plt.axis('off')
        plt.show()

        return binary_image

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_path = 'Enter your image path'
    xeroxed_image = create_xerox_effect(image_path, threshold_value=120)
    print(xeroxed_image)

    if xeroxed_image is not None:
        cv2.imwrite("xeroxed_output.png", xeroxed_image)
        print("Xeroxed image saved as xeroxed_output.png")
