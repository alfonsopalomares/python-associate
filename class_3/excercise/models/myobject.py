import json

class MyObject(object):
    values = {}
    def __init__(self, **kargs):
        self.values = kargs

    def __str__(self):
        return  json.dumps(self.values)
        
