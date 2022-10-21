import json
from src.grasp_analytics.modules.grip_select.mobilenet import objects

with open("coco_labels.json", "r") as f:
    data = json.load(f)

"""
# TODO
1. build a dictionary that takes us from old category id -> old category name (iterate over categories to build this)
2. use the OBJECT_GRIP_MAP to convert old category names to new category enums 
3. convert new category enums into their int IDs
"""


def clean_categories(df):
    df["new_category"] = [
        {"supercategory": "grip", "id": 0, "name": "tip"},
        {"supercategory": "grip", "id": 1, "name": "lateral"},
        {"supercategory": "grip", "id": 2, "name": "tripod"},
        {"supercategory": "grip", "id": 3, "name": "spherical"},
        {"supercategory": "grip", "id": 4, "name": "power"},
        {"supercategory": "grip", "id": 5, "name": "extension"}
    ]
    df["temp_annotations"] = df['annotations'].copy()
    mask = [category["name"] in objects.OBJECT_GRIP_MAP.keys() for category in df["categories"]]
    masked_cat = [cat for cat, msk in zip(df["categories"], mask) if msk]
    df["masked_cat"] = masked_cat
    for category in df["masked_cat"]:
        for anot in df["temp_annotations"]:
            if anot["category_id"] == category["id"]:
                anot["new_category_id"] = objects.OBJECT_GRIP_MAP[category["name"]].value
    df["new_annotations"] = [an for an in df["temp_annotations"] if ("new_category_id" in an.keys())]


def clean_annotations(df: list) -> None:
    """
    Cleans up annotations
    Args:
        df: Data

    Returns:None

    """
    for item in df["new_annotations"]:
        del item["category_id"]
        item["category_id"] = item["new_category_id"]
        del item["new_category_id"]
    del df["masked_cat"]
    del df["temp_annotations"]
    df["categories"] = df["new_category"]
    df["annotations"] = df["new_annotations"]
    del df["new_annotations"]
    del df["new_category"]


clean_categories(data)
clean_annotations(data)


def check_range(df, key):
    acc = []
    for i in df[key]:
        acc.append(i["category_id"])
    print(f"Category ranges from {min(acc)} to {max(acc)}")


check_range(data, "annotations")
