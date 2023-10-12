import cv2
import numpy as np

try:
    # Load the image
    image = cv2.imread("vh_detection.jpeg", cv2.IMREAD_GRAYSCALE)

    # Get the dimensions of the image
    h, w = image.shape

    # Create an empty filtered image of the same size as the original image
    filtered_image_dy = np.zeros((h, w), dtype=np.uint8)

    # Define the horizontal edge detection kernel
    dy_kernel = np.array([[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]], dtype=np.float32)

    # Iterate over each pixel in the image
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # Define a neighborhood region around the pixel
            neighborhood = image[i - 1:i + 2, j - 1:j + 2]

            # Apply the horizontal-edge detection kernel to the neighborhood
            gradient_y = np.sum(neighborhood * dy_kernel)

            # Ensure that pixel values are within the valid color range (0-255)
            gradient_y = np.clip(gradient_y, 0, 255)

            # Update the corresponding pixel in the filtered image
            filtered_image_dy[i, j] = np.uint8(gradient_y)

    # Display the original image
    cv2.imshow("Input Image", image)

    # Display horizontal edge detection result
    cv2.imshow("Horizontal Edge Detection", filtered_image_dy)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
