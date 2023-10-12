import cv2
import numpy as np

# Load the image
input_image = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detector
gradient_x = cv2.Sobel(src=input_image,
                       ddepth=cv2.CV_64F,
                       dx=1, dy=0,
                       ksize=3)
gradient_y = cv2.Sobel(src=input_image,
                       ddepth=cv2.CV_64F,
                       dx=0,
                       dy=1,
                       ksize=3)

# Calculate the magnitude of the gradient
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

# Convert to uint8 for visualization
edges_sobel = np.uint8(gradient_magnitude)

# Display the Sobel edge detection result
cv2.imshow("Sobel Edge Detection", edges_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
