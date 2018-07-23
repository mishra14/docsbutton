import os
from notebook.base.handlers import IPythonHandler

class LiveShareRequestHandler(IPythonHandler):

    def get(self):
        response_json=dict()
        response_json['title']='Jupyter LiveShare'
        response_json['body']='Jupyter LiveShare request received. LiveShare Url: http://unit.test'
        self.write(response_json)
        self.flush()