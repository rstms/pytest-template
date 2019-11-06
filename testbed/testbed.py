
import json

def simple_func():
    return 'Ni!'

class TestBed:
    def __init__(self):
        self.state = 'init'
        self.cfg = {}

    def read_config(self, file):
        self.cfg = json.load(file)
