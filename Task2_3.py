import cv2
import numpy as np

try:

    # Load the image
    input_image = cv2.imread('Lena.png')


    # Note: We are defining the right shift filter as of the left shift because the filter2D function flips the kernel
    # 180 degrees.

    # Define the right shift filter (7x7 filter) to shift the image to right by 3 pixels
    right_shift_filter = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]], dtype=np.float32)

    # Convolution of input_image and right_shift_filter using cv2.filter2D
    right_shifted_image = cv2.filter2D(
        src=input_image,
        ddepth=-1,
        kernel=right_shift_filter,
        borderType=cv2.BORDER_CONSTANT)

    # Save the right_shifted_image
    cv2.imwrite('right_shifted_image.png', right_shifted_image)
    cv2.imshow('right_shifted_image.png', right_shifted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")