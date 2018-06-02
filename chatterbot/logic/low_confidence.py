from __future__ import unicode_literals
from chatterbot.conversation import Statement
from .best_match import BestMatch


class LowConfidenceAdapter(BestMatch):

    def __init__(self, **kwargs):

        super(LowConfidenceAdapter, self).__init__(**kwargs)

        self.confidence_threshold = kwargs.get('threshold', 0.65)
        default_responses = kwargs.get(
            'default_response', "I'm sorry, I do not understand."
        )
        if isinstance(default_responses, str):
            default_responses = [
                default_responses
            ]
        self.default_responses = [
            Statement(text=default) for default in default_responses
        ]

    def process(self, input_statement):

        closest_match = self.get(input_statement)

        response = self.select_response(input_statement, self.default_responses)
        if closest_match.confidence > self.confidence_threshold:
            response.confidence = 1
        else:
            response.confidence = 0
        return response