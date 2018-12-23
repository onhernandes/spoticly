import yaml
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
config_filepath = os.path.join(current_dir, "config.yaml")

with open(config_filepath, "r") as conf:
    y = yaml.load(conf)

def get(k):
    return y.get(k)

def set(data):
    for k, v in y.items():
        if data.get(k, None) is None:
            data[k] = v
    with open(config_filepath, "w") as outfile:
        return yaml.dump(data, outfile, default_flow_style=False)

def get_all():
    return y