import cv2
import numpy as np

# Load the image
input_image = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detector
gradient_x = cv2.Sobel(src=input_image,
                       ddepth=cv2.CV_64F,
                       dx=1,
                       dy=0,
                       ksize=3)
gradient_y = cv2.Sobel(src=input_image,
                       ddepth=cv2.CV_64F,
                       dx=0,
                       dy=1,
                       ksize=3)

# The gradient_x is the horizontal gradient component
cv2.imwrite("Task3_1_gradient_x.png", np.uint8(gradient_x))
cv2.imshow("gradient_x", np.uint8(gradient_x))

# The gradient_y is the vertical gradient component
cv2.imwrite("Task3_1_gradient_y.png", np.uint8(gradient_y))
cv2.imshow("gradient_y", np.uint8(gradient_y))

# Calculate the magnitude of the gradient
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

# Convert to uint8 for visualization
edge_filtered_sobel = np.uint8(gradient_magnitude)

# save the output
cv2.imwrite("Task3_1_Sobel_Edge_Detection.png", edge_filtered_sobel)

# Display the Sobel-edge detection result
cv2.imshow("Task3_1_Sobel_Edge_Detection", edge_filtered_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
