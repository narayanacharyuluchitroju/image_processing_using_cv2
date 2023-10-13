import cv2
import numpy as np

try:
    # Load the image
    image = cv2.imread("Lena.png")

    # Get the image's height and width
    h, w = image.shape[:2]

    # Create an empty image for the filtered result, with the same size as the original
    gaussian_filtered_image = np.zeros_like(image, dtype=np.float32)

    # Define a 7x7 smoothing filter to reduce noise and make the image smoother
    gaussian_kernel = np.array([[1, 1, 2, 2, 2, 1, 1],
                                [1, 2, 2, 4, 2, 2, 1],
                                [2, 2, 4, 8, 4, 2, 2],
                                [2, 4, 8, 16, 8, 4, 2],
                                [2, 2, 4, 8, 4, 2, 2],
                                [1, 2, 2, 4, 2, 2, 1],
                                [1, 1, 2, 2, 2, 1, 1]], dtype=np.float32) / 140

    # Prepare the smoothing filter for use
    gaussian_kernel = gaussian_kernel[:, :, np.newaxis]

    # Go through each pixel in the image
    for i in range(3, h - 3):
        for j in range(3, w - 3):
            # Capture a larger area around the pixel
            neighborhood = image[i - 3:i + 4, j - 3:j + 4]

            # Apply the smoothing filter to the area
            filtered_pixel = np.sum(neighborhood * gaussian_kernel, axis=(0, 1))

            # Ensure the pixel values stay within the valid color range (0-255)
            filtered_pixel = np.clip(filtered_pixel, 0, 255)

            # Update the corresponding pixel in the smoothed image
            gaussian_filtered_image[i, j] = filtered_pixel

    # Convert the smoothed image to 8-bit format and save it
    gaussian_filtered_image = np.round(gaussian_filtered_image).astype(np.uint8)
    cv2.imwrite('Task4_gaussian_filtered_image.png', gaussian_filtered_image)

    # Show the original and smoothed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian filtered image", gaussian_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
