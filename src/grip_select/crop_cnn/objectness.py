import cv2

from src.definitions import SETTINGS, ROOT_PATH


def run_bounding_boxes(source_image):
    centre(contours_numbers(find_contour(source_image)))


# this is inside 1
def find_contour(img1):
    grey = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(grey, 128, 255, cv2.THRESH_BINARY)[1]
    return cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# inside 2
def contours_numbers(contours):
    if len(contours) == 2:
        return contours[0]
    else:
        return contours[1]


# inside 3
def centre(contours_num):
    for cntr in contours_num:
        x, y, w, h = cv2.boundingRect(cntr)
        cx = x + w // 2
        cy = y + h // 2
        cr = max(w, h) // 2
        dim = (200, 200)
        dr = 10
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cropped = img[y: y + h, x: x + w]
        cv2.imshow("cropped", img)
        r = cr + 1 * dr
        if cy - r < 0 or cy + r >= img.shape[0] or cx - r < 0 or cx + r >= img.shape[1]:
            continue
        resized_cropped = img[cy - r:cy + r, cx - r:cx + r]
        resized_cropped = cv2.resize(resized_cropped, dim)
        # cv2.imshow("resized_cropped", resized_cropped)


if __name__ == "__main__":
    img_path = ROOT_PATH / SETTINGS["grip_select"]["data_dir"] / "images/cup/cup_001.jpg"
    img = cv2.imread(str(img_path))

    # cv2.imshow("source", img.copy())
    run_bounding_boxes(img)
    cv2.waitKey()
    cv2.destroyAllWindows()

# convert to grayscale
# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold
# thresh = cv2.threshold(grey, 128, 255, cv2.THRESH_BINARY)[1]

# get contours
# result = img.copy()
# contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours = contours[0] if len(contours) == 2 else contours[1]
# for cntr in contours:
#    x, y, w, h = cv2.boundingRect(cntr)
#    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
#    cropped = img[y: y+h, x: x+w]
#    cv2.imshow("cropped", cropped)

# centre and radius
# cx = x+w//2
# cy = y+h//2
# cr = max(w, h)//2

# dim = (200, 200)
# make larger region in cropped
# dr = 10
# for i in range(0, 1):
#    r = cr+1*dr
#    cv2.rectangle(result, (cx-r, cy-r), (cx+r, cy+r), (0, 255, 0), 1)
#    cropped = img[cy-r:cy+r, cx-r:cx+r]
#    resizeandcrop = cv2.resize(cropped, dim)
#    cv2.imshow("resizeandcrop{}".format(i), resizeandcrop)

# resize cropped1 to be proper pixels

# show
# cv2.imshow("source", result)
# cv2.waitKey()
# cv2.destroyAllWindows()
