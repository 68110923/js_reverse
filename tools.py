import json

from typing import Union, Dict, List


class Tools:
    @staticmethod
    def jsonp(text, callback) -> Union[Dict, List]:
        start_idx = text.index(callback + '(') + len(callback) + 1
        end_idx = text.rfind(')')
        data = json.loads(text[start_idx:end_idx])
        return data
