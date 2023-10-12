import cv2
import numpy as np

try:
    # Load the image
    image = cv2.imread("vh_detection.jpeg")

    # Ensure the image is in grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Sobel filter for horizontal edge detection
    filtered_image_dy = cv2.Sobel(gray_image, cv2.CV_8U, 0, 1, ksize=3)

    # Display the original image
    cv2.imshow("Input Image", image)

    # Display horizontal edge detection result
    cv2.imshow("Horizontal Edge Detection", filtered_image_dy)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
