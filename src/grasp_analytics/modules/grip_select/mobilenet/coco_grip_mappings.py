import json
from src.grasp_analytics.modules.grip_select.mobilenet  import objects

from itertools import compress
print(objects.OBJECT_GRIP_MAP)

with open("coco_labels.json", "r") as f:
    data = json.load(f)

#data_cat = data["categories"]

# Verifying that there are two locations in the dataframe with the same category info
# print(data_cat == data["info"]["categories"])
"""
The aim is to create an extra key called GripType in the labels' category thats for the griptype

THE ALGORITHM:
    - import objects.py (Having problems with that)
    - for every element i in data["categories"]:
        - if i["name"] is a key in OBJECT_GRIP_MAP:
            - add OBJECT_GRIP_MAP[i["name"]] to i["GripType"]
        - else:
            - Add None? or skip? confirm with James
            
# TODO
1. build a dictionary that takes us from old category id -> old category name (iterate over categories to build this)
2. use the OBJECT_GRIP_MAP to convert old category names to new category enums 
3. convert new category enums into their int IDs
"""
data["new_category"] = [
    {"supercategory": "grip", "id": 0, "name": "tip"},
    {"supercategory": "grip", "id": 1, "name": "lateral"},
    {"supercategory": "grip", "id": 2, "name": "tripod"},
    {"supercategory": "grip", "id": 3, "name": "spherical"},
    {"supercategory": "grip", "id": 4, "name": "power"},
    {"supercategory": "grip", "id": 5, "name": "extension"}
]
data["temp_annotations"] = data['annotations'].copy()
# data["category_copy"] = data["categories"]
# acc = 0
mask = [category["name"] in objects.OBJECT_GRIP_MAP.keys() for category in data["categories"]]
masked_cat = [cat for cat,msk in zip(data["categories"],mask) if msk]
data["masked_cat"] = masked_cat
for category in data["masked_cat"]:
    for anot in data["temp_annotations"]:
        if anot["category_id"] == category["id"]:
                anot["new_category_id"] = objects.OBJECT_GRIP_MAP[category["name"]].value


data["new_annotations"] = [an for an in data["temp_annotations"] if ("new_category_id" in an.keys())]

def clean_annotations(df: list):
    for item in df["new_annotations"]:
        del item["category_id"]
        item["category_id"] = item["new_category_id"]
        del item["new_category_id"]
    del df["masked_cat"]
    del df["temp_annotations"]
clean_annotations(data)

# del data["category_copy"]
# del data["masked_cat"]
# del data["temp_annotations"]


#rndm = {"a": 32, "b": 2321}
#del rndm["a"]
def check_range(df):
    acc = []
    for i in df["new_annotations"]:
        acc.append(i["category_id"])
    print(f"Category ranges from {min(acc)} to {max(acc)}")
check_range(data)
data["categories"] = data["new_category"]
data["annotations"] = data["new_annotations"]
del data["new_annotations"]
del data["new_category"]

