import os
from notebook.base.handlers import IPythonHandler

class LiveShareRequestHandler(IPythonHandler):

    def get(self):
        self.write('This is a sample for jupyter liveshare')
        self.flush()