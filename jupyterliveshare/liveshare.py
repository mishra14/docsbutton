import os
from notebook.base.handlers import IPythonHandler

class LiveShareRequestHandler(IPythonHandler):

    def get(self):
        response_json=dict()
        response_json['title']='This is jupyter LiveShare'
        response_json['body']='Jupyter LiveShare request received.'
        self.write(response_json)
        self.flush()