import cv2
import numpy as np

try:
    # Load the image
    image = cv2.imread("Lena.png")

    # Get the dimensions of the image
    h, w = image.shape[:2]
    # print(h,w)
    # cv2.imshow("input_image", image)

    # Create an empty filtered image of the same size as the original image
    gaussian_filtered_image = np.zeros_like(image, dtype=np.float32)
    # print(gaussian_filtered_image)

    # Define a 5x5 Gaussian filter kernel
    gaussian_kernel = np.array([[1, 4, 6, 4, 1],
                                [4, 16, 24, 16, 4],
                                [6, 24, 36, 24, 6],
                                [4, 16, 24, 16, 4],
                                [1, 4, 6, 4, 1]], dtype=np.float32) / 256

    # Reshape the Gaussian kernel to match the neighborhood shape
    gaussian_kernel = gaussian_kernel[:, :, np.newaxis]

    # Iterate over each pixel in the image
    for i in range(2, h - 2):
        for j in range(2, w - 2):
            # Define a larger neighborhood region around the pixel
            neighborhood = image[i - 2:i + 3, j - 2:j + 3]

            # Apply the filter kernel to the neighborhood
            filtered_pixel = np.sum(neighborhood * gaussian_kernel, axis=(0, 1))

            # Ensure that pixel values are within the valid color range (0-255)
            filtered_pixel = np.clip(filtered_pixel, 0, 255)

            # Update the corresponding pixel in the filtered image
            gaussian_filtered_image[i, j] = filtered_pixel

    # Convert the filtered image to uint8 and save it
    gaussian_filtered_image = np.round(gaussian_filtered_image).astype(np.uint8)

    # Save the shifted image
    cv2.imwrite('gaussian_filtered_image.png', gaussian_filtered_image)

    # Display the original and filtered images
    cv2.imshow("input_image", image)
    cv2.imshow("gaussian_filtered_image", gaussian_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")

