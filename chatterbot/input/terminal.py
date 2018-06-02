from __future__ import unicode_literals
from chatterbot.input import InputAdapter
from chatterbot.conversation import Statement
from chatterbot.utils import input_function

import sys

class TerminalAdapter(InputAdapter):

    def __init__(self, **kwargs):
        super(TerminalAdapter, self).__init__(**kwargs)
        self.user = kwargs['user']

    def process_input(self, *args, **kwargs):
        sys.stdout.write('[' + self.user + '] : ')
        sys.stdout.flush()
        user_input = input_function()
        return Statement(user_input)
