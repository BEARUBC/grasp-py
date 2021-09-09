import cv2

from src.grip_select.selector import GripSelector


class CropCNNSelector(GripSelector):
    def classify_image(self, image):
        pass

    def _crop_center_bbox(self, img, contours):
        for cntr in contours:
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
