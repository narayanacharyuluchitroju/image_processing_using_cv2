import cv2
import numpy as np

try:
    # Load the grayscale image
    image = cv2.imread("Lines.jpeg", cv2.IMREAD_GRAYSCALE)

    # Get the image's height and width
    h, w = image.shape

    # Create an empty image for the filtered result, with the same size as the original
    filtered_image_dy = np.zeros((h, w), dtype=np.uint8)

    # Define a filter for detecting horizontal edges
    dy_kernel = np.array([[-1, -1, -1],
                          [0, 0, 0],
                          [1, 1, 1]], dtype=np.float32)

    # Go through each pixel in the image
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # Capture a small area around the pixel
            neighborhood = image[i - 1:i + 2, j - 1:j + 2]

            # Apply the horizontal-edge detection filter to the area
            gradient_y = np.sum(neighborhood * dy_kernel)

            # Ensure the pixel values stay within the valid color range (0-255)
            gradient_y = np.clip(gradient_y, 0, 255)

            # Update the corresponding pixel in the filtered image
            filtered_image_dy[i, j] = np.uint8(gradient_y)

    # Save the output image
    cv2.imwrite("Task5_2_Horizontal_Edge_Detection.png", filtered_image_dy)

    # Show the original grayscale image
    cv2.imshow("Input Image", image)

    # Show the result of horizontal edge detection
    cv2.imshow("Horizontal Edge Detection", filtered_image_dy)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
