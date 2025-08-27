from argparse import ArgumentParser

def common_parent():
    p = ArgumentParser(add_help=False)
    p.add_argument("-b", "--rabbitmq_server", default="localhost")
    p.add_argument("-q", "--queue_name",default="alicpp_records")
    return p