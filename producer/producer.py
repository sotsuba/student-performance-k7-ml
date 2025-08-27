import argparse
import json
from time import sleep
try:
    from utils import connect_to_rabbitmq, teardown_queue
except:
    from producer.utils import connect_to_rabbitmq, teardown_queue
import pandas as pd
import pika
from core.queue import Queue
from core.cli   import common_parent

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="cmd", required=True)
parser = sub.add_parser('consume', parents=[common_parent()], help='Run producer')
parser.add_argument(
    "-m",
    "--mode",
    default="setup",
    choices=["setup", "teardown"],
    help="Whether to setup or teardown a RabbitMQ queue with driver stats events. Setup will teardown before beginning emitting events.",
)

args = parser.parse_args()

def create_streams(mq: Queue):
    df = pd.read_csv('producer/data_sample.csv')

    while True:
        for _, record in df.iterrows():
            record = record.to_dict()              
            print(record)
            body = json.dumps(record).encode("utf-8")
            mq.send(body)
        sleep(1)

if __name__ == "__main__":
    parsed_args = vars(args)
    mode        = parsed_args["mode"]
    server      = parsed_args["rabbitmq_server"]
    queue_name  = parsed_args["queue_name"]
    
    print("Tearing down all existing queues!")
    try:
        teardown_queue(f"{queue_name}", server)
    except Exception as e:
        print(f"Queue {queue_name} does not exist. Skipping...!")

    if mode == "setup":
        connection, channel = connect_to_rabbitmq(server)
        mq = Queue(queue_name, connection)
        create_streams(mq)