import sys
import cv2
import imutils
import numpy as np
import glob

resize_size = (120, 180)
resize_area = resize_size[0] * resize_size[1]


def png2white(image):
    alpha_channel = image[:, :, 3]
    _, mask = cv2.threshold(alpha_channel, 254, 255,
                            cv2.THRESH_BINARY)
    color = image[:, :, :3]
    image = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))
    return image


def background_color(image):
    counts = np.bincount(image.flatten())
    return np.argmax(counts)


def image_preproccess(image):
    '''Grayscale image and put a treshold on it'''
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    back_color = background_color(gray_image)
    _, thresh = cv2.threshold(
        gray_image, 10, 255, cv2.THRESH_BINARY if back_color < 127 else cv2.THRESH_BINARY_INV)

    # cv2.imshow("debug", thresh)
    # cv2.waitKey(0)

    '''Find contours'''
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    for number in contours:
        '''Crop contour rectangle and find contour'''
        x, y, w, h = cv2.boundingRect(number)
        origin, size, degree = cv2.minAreaRect(number)
        cropped_number = thresh[y: y+h, x: x+w]
        # cv2.imshow("debug", thresh)
        # cv2.waitKey(0)

        '''Rotate image if contour is rotated with min area rectangle'''
        rotated_number = imutils.rotate_bound(cropped_number, -degree)
        # cv2.imshow("debug2", rotated_number)
        # cv2.waitKey(0)

        '''Find rotated contour again '''
        rotated_contours, _ = cv2.findContours(
            rotated_number, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_contour = max(rotated_contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(num_contour)

        '''Crop rotated contour to have the shape vertical'''
        res_number = rotated_number[y: y+h, x: x+w]
        if h < w:
            res_number = imutils.rotate_bound(res_number, -90)
        # cv2.imshow("debug2", res_number)
        # cv2.waitKey(0)

        '''Add result picture to results array'''
        res_number = cv2.resize(res_number, resize_size)
        results.append(res_number)

    return results


def sampler():
    result = []
    for i in range(10):
        image = cv2.imread("good/%d.PNG" % i, cv2.IMREAD_UNCHANGED)
        image = png2white(image)
        number = image_preproccess(image)[0]
        result.append(number)
    return result


number_masks = sampler()


def digit_recognize(image):
    image = png2white(image)
    numbers = image_preproccess(image)
    result = []
    for number in numbers:
        max_count, max_index = 0, 0
        for index, mask in enumerate(number_masks):
            for num in [number, imutils.rotate(number, 180)]:
                masked_img = cv2.bitwise_not(cv2.bitwise_xor(num, mask))
                # masked_img = cv2.bitwise_and(num, mask)
                tmp_count = np.count_nonzero(masked_img)
                if tmp_count > max_count:
                    max_count = tmp_count
                    max_index = index

        accuracy = max_count / resize_area
        result.append({
            "number": max_index if (accuracy > 0.8) else -1,
            "accuracy": accuracy
        })
    return result


def main(address):
    image = cv2.imread(address, cv2.IMREAD_UNCHANGED)
    h, w, c = image.shape
    if h == 0 or w == 0:
        raise("Invalid image path or file")
    return digit_recognize(image)


if __name__ == "__main__":
    try:
        print(main(sys.argv[1]))
    except Exception as error:
        raise error

    # for image in glob.glob("numbers/*"):
    #     print(image.split("\\")[1], "=>",
    #           sorted(main(image), key=lambda x: x["number"], reverse=True))
    cv2.destroyAllWindows()
