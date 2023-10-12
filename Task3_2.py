import cv2

# Load the image
input_image = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

# Apply Canny-edge detector
edges_canny = cv2.Canny(image=input_image,
                        threshold1=100,
                        threshold2=200,
                        apertureSize=3,
                        L2gradient=True)

# Display the Canny-edge detection result
cv2.imshow("Canny Edge Detection", edges_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
