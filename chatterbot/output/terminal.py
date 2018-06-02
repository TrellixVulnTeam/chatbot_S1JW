from __future__ import unicode_literals
from .output_adapter import OutputAdapter

import sys
import time

class TerminalAdapter(OutputAdapter):

    def __init__(self, **kwargs):
        super(TerminalAdapter, self).__init__(**kwargs)
        self.name = kwargs['name']

    def process_response(self, statement, session_id=None):
        sys.stdout.write('[' + self.name + '] : ')
        for char in statement.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print('\r')
        return statement.text