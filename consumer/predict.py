from pathlib import Path 
import argparse 
import joblib # type: ignore
import pandas as pd # type: ignore
import json
from consumer.utils import ensure_features 
from core.queue import Queue 
from core.custom_feature import CreateCustomFeatures
from core.cli   import common_parent

import sys
this_mod = sys.modules[__name__]
setattr(this_mod, "CreateCustomFeatures", CreateCustomFeatures)

FOLDER_PATH = Path(__file__).resolve().parent.parent

MODEL_PATH = FOLDER_PATH / 'models' / 'final_model.joblib'

args = common_parent().parse_args()

# Load artifacts
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError as e:
    print(f"Error loading model artifacts: {e}.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred loading artifacts: {e}")
    exit()

    
def predict(data: pd.DataFrame):
    y_pred = model.predict(data)
    return {
        'student_id': int(data['StudentID'].iloc[0]) if 'StudentID' in data else 'N/A',
        'gpa_pred': y_pred[0]
    }

def callback(ch, method, properties, body):
    try: 
        msg = json.loads(body.decode('utf-8'))
        df = ensure_features(pd.DataFrame([msg]))
        gpa_pred = predict(df)
        
        log_entry = {'type': 'successful', 'prediction': gpa_pred}
        print(log_entry)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"{e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    

if __name__ == "__main__":
    parsed_args = vars(args)
    server = parsed_args["rabbitmq_server"]
    queue_name = parsed_args["queue_name"]
    mq = Queue(queue_name, callback_fn=callback)
    mq.consume()