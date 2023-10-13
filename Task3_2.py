import cv2

# Load the image
input_image = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

# Apply Canny-edge detector
edge_filtered_canny_l2_normalized = cv2.Canny(image=input_image,
                                threshold1=100,
                                threshold2=200,
                                apertureSize=3,
                                L2gradient=True)

edge_filtered_canny = cv2.Canny(image=input_image,
                                threshold1=100,
                                threshold2=200,
                                apertureSize=3,
                                L2gradient=False)

#save the output image
cv2.imwrite("Task3_2_Canny_Edge_Detection_L2_Normalized.png", edge_filtered_canny_l2_normalized)
cv2.imwrite("Task3_2_Canny_Edge_Detection.png", edge_filtered_canny)

# Display the Canny-edge detection result
cv2.imshow("Canny Edge Detection L2 Noramalized", edge_filtered_canny_l2_normalized)
cv2.imshow("Canny Edge Detection", edge_filtered_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
