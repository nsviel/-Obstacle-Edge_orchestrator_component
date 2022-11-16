#---------------------------------------------
from param import param_hu
from src import parser_json

import datetime


def format_prediction():
    # Load unformatted prediction
    path = "data/generic/pred_thresh_0.1_frame_5.json"
    json = parser_json.load_data_from_file(path)

    # Format prediction
    pred = {
        "Timestamp": int(datetime.datetime.now().timestamp()),
        "Position": {
        "Longitude": 23.84,
        "Latitude": 8.48,
        "Speed": 50,
        "Direction": "ToFrance"
        },
        "Label": json["detections"][0]["name"],
        "Dimension":{
            "Width": round(json["detections"][0]["dimensions"][0], 3),
            "Length": round(json["detections"][0]["dimensions"][1], 3),
            "Heigth": round(json["detections"][0]["dimensions"][2], 3),
            "Direction": round(json["detections"][0]["heading"], 3)
        },
        "Accuracy": 49
    }

    # Save formatted prediction into state file
    parser_json.upload_file(param_hu.path_state_pred, pred)
