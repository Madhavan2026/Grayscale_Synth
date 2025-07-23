import cv2
import matplotlib.pyplot as plt

def create_xerox_effect(image_path, threshold_value=128):
    try:
        original_image = cv2.imread(image_path)

        if original_image is None:
            raise FileNotFoundError(f"Error: Could not open or find the image at {image_path}")

        # Convert to Grayscale
        grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Manual method to convert as Grayscale
        # B = original_image[:, :, 0]
        # G = original_image[:, :, 1]
        # R = original_image[:, :, 2]
        # grayscale_image = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)

        # Calculate histogram for the grayscale image
        hist_grayscale = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256])

        # Thresholding
        ret, binary_image = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)

        plt.figure(figsize=(18, 6))

        # Original Image
        plt.subplot(1, 3, 1) # 1 row, 3 columns, 1st plot
        plt.title("Original Image")
        plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')

        # Grayscale Histogram with Threshold Line
        plt.subplot(1, 3, 2) # 1 row, 3 columns, 2nd plot
        plt.plot(hist_grayscale, color='black')
        plt.axvline(x=threshold_value, color='r', linestyle='--', label=f'Threshold = {threshold_value}')
        plt.title("Grayscale Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Number of Pixels")
        plt.xlim([0, 256])
        plt.grid(True)
        plt.legend()

        # Xerox Effect (Binary Image)
        plt.subplot(1, 3, 3) # 1 row, 3 columns, 3rd plot
        plt.title(f"Xerox Effect (Binary Image)")
        plt.imshow(binary_image, cmap='gray')
        plt.axis('off')

        plt.tight_layout()
        plt.show()

        return binary_image

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Enter your image location
    image_path = '/path to your image.jpeg'
    xeroxed_image = create_xerox_effect(image_path, threshold_value=150)  # Assign your threshold value
    print(f"Processed image array shape: {xeroxed_image.shape}" if xeroxed_image is not None else "Image processing failed.")

    if xeroxed_image is not None:
        # To write the processed image
        cv2.imwrite("xeroxed_output_with_hist.png", xeroxed_image)
        print("Xeroxed image saved as xeroxed_output_with_hist.png")
