from abc import abstractmethod
import json


class Module:

    @abstractmethod
    def process(self, input_json: dict) -> dict:
        pass

    def run(self, json_str: str) -> str:
        return json.dumps(self.process(json.loads(json_str)))
