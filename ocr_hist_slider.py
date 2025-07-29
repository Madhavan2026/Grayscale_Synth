import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

original_image = None
grayscale_image = None
binary_image_display = None
threshold_slider = None
fig = None
ax_binary = None
hist_threshold_line = None
ax_hist = None

def update_image(val):
    """
    Callback function for the slider to update the binary image and histogram line in real-time.
    """
    global binary_image_display, ax_binary, grayscale_image, threshold_slider, hist_threshold_line, ax_hist

    if grayscale_image is None:
        print("Grayscale image not loaded yet.")
        return

    # Get the current threshold value from the slider
    new_threshold = int(threshold_slider.val)

    # Apply new threshold to the image
    ret, updated_binary_image = cv2.threshold(grayscale_image, new_threshold, 255, cv2.THRESH_BINARY)

    # Update the displayed binary image
    binary_image_display.set_data(updated_binary_image)
    ax_binary.set_title(f"Xerox Effect (Threshold={new_threshold})")

    # Update the position of the vertical line on the histogram
    if hist_threshold_line: # Check if the line object exists
        hist_threshold_line.set_xdata([new_threshold, new_threshold]) # Set new X coordinates
        hist_threshold_line.set_label(f'Threshold = {new_threshold}') # Update label

    # Re-draw the legend to reflect the new label
    if ax_hist:
        ax_hist.legend(loc='upper right') # Re-create the legend with updated labels, specify location if needed

    # Redraw the canvas to reflect all changes
    fig.canvas.draw_idle()

def create_xerox_effect_interactive(image_path):
    """
    Simulates a Xerox machine's black and white output with an interactive slider
    for thresholding.
    """
    global original_image, grayscale_image, binary_image_display, threshold_slider, fig, ax_binary, hist_threshold_line, ax_hist

    try:
        original_image = cv2.imread(image_path)

        if original_image is None:
            raise FileNotFoundError(f"Error: Could not open or find the image at {image_path}")

        # Convert to Grayscale
        grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Calculate histogram for the grayscale image
        hist_grayscale = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256])

        # Initial threshold value
        initial_threshold_value = 128

        # Apply initial thresholding
        ret, initial_binary_image = cv2.threshold(grayscale_image, initial_threshold_value, 255, cv2.THRESH_BINARY)

        # Setup the Matplotlib Figure and Subplots
        fig, axes = plt.subplots(1, 3, figsize=(18, 7))
        plt.subplots_adjust(bottom=0.25)

        # 1. Original Image Plot
        ax_original = axes[0]
        ax_original.set_title("Original Image")
        ax_original.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        ax_original.axis('off')

        # 2. Grayscale Histogram Plot
        ax_hist = axes[1] # Assign to global ax_hist for update_image to access
        ax_hist.plot(hist_grayscale, color='black')
        ax_hist.set_title("Grayscale Histogram")
        ax_hist.set_xlabel("Pixel Intensity")
        ax_hist.set_ylabel("Number of Pixels")
        ax_hist.set_xlim([0, 256])
        ax_hist.grid(True)
        # Store the line object returned by axvline (no [0] needed)
        hist_threshold_line = ax_hist.axvline(x=initial_threshold_value, color='r', linestyle='--', label=f'Threshold = {initial_threshold_value}')
        ax_hist.legend()


        # 3. Xerox Effect (Binary Image) Plot
        ax_binary = axes[2]
        ax_binary.set_title(f"Xerox Effect (Threshold={initial_threshold_value})")
        binary_image_display = ax_binary.imshow(initial_binary_image, cmap='gray')
        ax_binary.axis('off')

        # --- Create the Slider ---
        ax_slider = plt.axes([0.25, 0.1, 0.50, 0.03], facecolor='lightgoldenrodyellow')
        threshold_slider = Slider(ax_slider, 'Threshold', 0, 255, valinit=initial_threshold_value, valstep=1)

        # Register the update function with the slider
        threshold_slider.on_changed(update_image)

        plt.show()

        # Return the last state of the binary image when the window is closed
        ret, final_binary_image = cv2.threshold(grayscale_image, int(threshold_slider.val), 255, cv2.THRESH_BINARY)
        return final_binary_image

    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# --- How to use the function ---
if __name__ == "__main__":
    image_path = 'Enter your path to image.jpeg'
    final_processed_image = create_xerox_effect_interactive(image_path)

    if final_processed_image is not None:
        cv2.imwrite("final_xeroxed_output_after_interactive_session.png", final_processed_image)
        print("Final processed image (when window was closed) saved as final_xeroxed_output_after_interactive_session.png")
