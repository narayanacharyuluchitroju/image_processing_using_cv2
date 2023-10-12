import Task1
import Task2_3
import cv2

img = cv2.imread('4.1.03.tiff')

Task = "Task2_2"

if Task == "Task1":
    # rgb_to_grayScale
    dst = Task1.img_color_to_grey(img)
    # Display the result
    cv2.imshow('Original Image', img)
    cv2.imshow('GrayScale Image', dst)
    print(dst.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if Task == "Task2_1":
    # shift_img_to_left
    dst = Task2.left_shift(img)
    # Display the result
    cv2.imshow('Original Image', img)
    cv2.imshow('Left Shifted Image', dst)
    print(dst.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if Task == "Task2_2":
    # shift_image_to_right
    dst = Task2.right_shift(img)
    # Display the result
    cv2.imshow('Original Image', img)
    cv2.imshow('Right Shifted Image', dst)
    print(dst.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
