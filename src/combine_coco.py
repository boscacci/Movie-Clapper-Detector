# Courtesy of Alex Strick van Linschoten
# https://gist.github.com/strickvl/e4bb9341ce1c83f67a531791bddf4cbd

import json
import os
from datetime import datetime


BASE_ANNOTATIONS_DIRECTORY = (
    "/Users/rob/repos/film-slate-detector/data/annotations"
)

ANNOTATIONS_COCO_FILE_A = f"{BASE_ANNOTATIONS_DIRECTORY}/first_50_images.json"

ANNOTATIONS_COCO_FILE_B = (
    f"{BASE_ANNOTATIONS_DIRECTORY}/finalized_pseudo_labels.json"
)


FILENAME_DATETIME_PREFIX = "%Y-%m-%d-%H:%M:%S"


def get_annotations(annotations_obj):
    return annotations_obj["annotations"]


def get_images(annotations_obj):
    return annotations_obj["images"]


def get_combined_obj(prodigy_annotations, synthetic_annotations):
    base_obj = None
    synthetic_obj = None
    with open(prodigy_annotations) as json_file:
        base_obj = json.load(json_file)

    with open(synthetic_annotations) as json_file:
        synthetic_obj = json.load(json_file)

    synthetic_annotations = get_annotations(synthetic_obj)
    synthetic_images = get_images(synthetic_obj)

    for annotation in synthetic_annotations:
        base_obj["annotations"].append(annotation)
    for image in synthetic_images:
        base_obj["images"].append(image)

    return base_obj


def save_object_as_json(object, file_path):
    json_string = json.dumps(object)
    with open(file_path, "w") as jsonFile:
        jsonFile.write(json_string)


if __name__ == "__main__":
    combined_obj = get_combined_obj(
        ANNOTATIONS_COCO_FILE_A,
        ANNOTATIONS_COCO_FILE_B,
    )

new_filename = os.path.join(
    BASE_ANNOTATIONS_DIRECTORY,
    f"{datetime.today().strftime(FILENAME_DATETIME_PREFIX)}-combined_redactions.json",
)

save_object_as_json(combined_obj, new_filename)
