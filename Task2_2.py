import cv2
import numpy as np

try:
    # Load the image
    input_image = cv2.imread('Lena.png')

    # Define the left shift filter (3x3 filter) to shift the image to left by 1 pixel
    left_shift_filter = np.array([[0, 0, 0],
                                  [0, 0, 1],
                                  [0, 0, 0]], dtype=np.float32)

    # Note: We are defining the right shift filter for the left shift because the filter2D function flips 180 degrees.
    # Convolution of input_image and left_shift_filter using cv2.filter2D
    left_shifted_image = cv2.filter2D(src=input_image,
                                      ddepth=-1,
                                      kernel=left_shift_filter,
                                      borderType=cv2.BORDER_CONSTANT)

    # Save the shifted image
    cv2.imwrite('left_shifted_image.png', left_shifted_image)
    cv2.imshow('left_shifted_image.png', left_shifted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
