import cv2
import glob
import numpy as np

# Pass image read into an array in the 'froatate' function; openCV used here; any other library like SKimage, Pillow can be used too
# Rotates an image anticlockwise by 90°


def frotate90(image):

    # finding length and breadth of the image
    l, b, _ = image.shape

    # Blank array of the shape of rotated image
    imR = np.zeros((b, l, 3), dtype='uint8')

    # Seggregating the three colour channels of the image into seperate arrays
    im1 = image[:, :, 0]
    im2 = image[:, :, 1]
    im3 = image[:, :, 2]

    # Taking transpose of each array, to rotate the image channels
    im1 = im1.transpose()
    im2 = im2.transpose()
    im3 = im3.transpose()

    # In addition to rotating the arrays, taking transpose will also filp the channels vertically
    # Therefore the channels shall be vertically flipped again, to achieve perfect roatation

    # Vertically flipping each channel:

    # A for loop is run till half the length of rotated image channels,
    # and i'th row of a channel is interchanged with the i'th from the bottom
    # all till the central row.

    for i in range(int(b / 2)):
        # Saving the i'th row from bottom in a temporary arrays
        [k1, k2, k3] = [k[b - 1 - i, :] for k in [im1.copy(), im2.copy(), im3.copy()]]

        # Saving values of i'th rows at the positions of i'th rows from bottoms
        im1[b - 1 - i, :] = im1[i, :]
        im2[b - 1 - i, :] = im2[i, :]
        im3[b - 1 - i, :] = im3[i, :]

        # Saving the temporarily stored values in the i'th rows' positions
        im1[i, :] = k1
        im2[i, :] = k2
        im3[i, :] = k3

    # Feeding each rotated channel at their respective position in the new blank array
    imR[:, :, 0] = im1
    imR[:, :, 1] = im2
    imR[:, :, 2] = im3

    return(imR)


# enter path of image to be rotated's file kept in the computer.
# in the format 'filename.jpg' or any other image format
path = ''
im = cv2.imread(path)
# rotated image is saved here
image_rotated = frotate90(im)

# User to enter the filename by which name the rotated image shall be saved
naam = ''

# saving the rotated image as the filename entered above, in the computer.
cv2.imwrite(naam + '.jpg', image_rotated)
