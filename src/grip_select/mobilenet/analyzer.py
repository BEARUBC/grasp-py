import cv2
from typing import List

from src.definitions import ROOT_PATH
from src.grip_select.mobilenet.result import MobileNetResult


class MobileNetAnalyzer:
    def __init__(self, classes_path: str = None, config_path: str = None, weights_path: str = None):
        self._path = ROOT_PATH / "grip_select/mobilenet/"

        self._classes_path = classes_path if classes_path else self._path / "coco.names"
        self._config_path = config_path if config_path else self._path / "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        self._weights_path = weights_path if weights_path else self._path / "frozen_inference_graph.pb"

        with open(str(self._classes_path), 'rt') as f:
            self._class_names = f.read().rstrip('\n').split('\n')

        self._model = self._create_model()

    def _create_model(self):
        net = cv2.dnn_DetectionModel(self._weights_path, self._config_path)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)
        return net

    def _analyze_image(self, image) -> None:
        height, width, channels = image.shape
        top_left = (240, 160)
        bottom_right = (400, 320)
        cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), thickness=1)

        classIds, confs, bbox = self._model.detect(image, confThreshold=0.5)
        box_sizes = []
        box_data = zip(classIds.flatten(), confs.flatten(), bbox)
        i = 0
        for classId, confidence, box in box_data:
            # cv2.rectangle(img, tuple(square_tl), tuple(square_br), color=(0, 255, 0), thickness=2)
            # cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            box_offset = (box[0] + 1 / 2 * box[2], box[1] + 1 / 2 * box[3])
            box_sizes.append(box[2] * box[3])

            # if (box_offset[0] > top_left[0] and box_offset[0] < bottom_right[0] and box_offset[1] > top_left[1] and box_offset[
            #     1] < bottom_right[1]):
            #     cv2.rectangle(img, box, color=(0, 255, 255), thickness=2)
            #     cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
            #                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            # i += 1

        box_data = list(zip(classIds.flatten(), confs.flatten(), bbox, box_sizes))
        min_size = 100000
        selected_box = None

        square_tl = [0, 0]
        square_br = [50, 50]
        for i in range(len(box_data)):
            box = box_data[i][2]
            box_offset = (box[0] + 1 / 2 * box[2], box[1] + 1 / 2 * box[3])
            if box_sizes[i] < min_size and top_left[0] < box_offset[0] < bottom_right[0] and top_left[1] < box_offset[
                1] < \
                    bottom_right[1]:
                selected_box = box_data[i]
                min_size = box_sizes[i]
                square_box = selected_box[2]

                x_diff = square_box[2]
                y_diff = square_box[3]

                square_tl = [square_box[0], square_box[1]]
                square_br = [square_box[0] + square_box[2], square_box[1] + square_box[3]]

                if x_diff == y_diff:
                    square_box = box
                elif x_diff > y_diff:
                    square_tl[1] = int(square_box[1] - (x_diff - y_diff) / 2)
                    square_br[1] = int(square_box[1] + square_box[3] + (x_diff - y_diff) / 2)
                else:
                    square_tl[0] = int(square_box[0] - (y_diff - x_diff) / 2)
                    square_br[0] = int(square_box[0] + square_box[2] + (y_diff - x_diff) / 2)

        cv2.rectangle(image, tuple(square_tl), tuple(square_br), color=(255, 255, 0), thickness=2)
        cv2.putText(image, self._class_names[selected_box[0] - 1].upper(),
                    (selected_box[2][0] + 10, selected_box[2][1] + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        cv2.imshow("Output", image)
        cv2.waitKey(0)

    def _analyze_video(self, video) -> List[MobileNetResult]:
        pass


# img = cv2.imread('img_8.png')



