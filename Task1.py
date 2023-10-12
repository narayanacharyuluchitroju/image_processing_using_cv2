import cv2

try:
    # Load the image
    input_image = cv2.imread("Lena.png")

    # Convert the image into a grayscale image
    output_grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # save the image
    cv2.imwrite('grayscale.png', output_grayscale_image)

    # display the original and grayscale converted images
    cv2.imshow('Original Image', input_image)
    cv2.imshow('GrayScale Image', output_grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")

