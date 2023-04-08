from src.grasp_analytics.modules.grip_select.mobilenet.objects import OBJECT_GRIP_MAP, GripType


def get_grip_type(label):
    if label in OBJECT_GRIP_MAP.keys():
        return OBJECT_GRIP_MAP[label]
    else:
        return GripType.POWER