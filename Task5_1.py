import cv2
import numpy as np

try:
    # Load a grayscale image
    image = cv2.imread("Lines.jpeg", cv2.IMREAD_GRAYSCALE)

    # Get the image's height and width
    h, w = image.shape

    # Create an empty image for the filtered result, with the same size as the original
    filtered_image_dx = np.zeros((h, w), dtype=np.uint8)

    # Define a filter for detecting vertical edges
    dx_kernel = np.array([[-1, 0, 1],
                          [-1, 0, 1],
                          [-1, 0, 1]], dtype=np.float32)

    # Go through each pixel in the image
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # Capture a small area around the pixel
            neighborhood = image[i - 1:i + 2, j - 1:j + 2]

            # Apply the vertical-edge detection filter to the area
            gradient_x = np.sum(neighborhood * dx_kernel)

            # Ensure the pixel values stay within the valid color range (0-255)
            gradient_x = np.clip(gradient_x, 0, 255)

            # Update the corresponding pixel in the filtered image
            filtered_image_dx[i, j] = np.uint8(gradient_x)

    # Save the image
    cv2.imwrite("Task5_Vertical_Edge_Detection.png", filtered_image_dx)

    # Show the original grayscale image
    cv2.imshow("Input Image", image)

    # Show the result of vertical edge detection
    cv2.imshow("Vertical Edge Detection", filtered_image_dx)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
