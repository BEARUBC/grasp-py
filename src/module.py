from abc import abstractmethod


class Module:

    @abstractmethod
    def process(self, input_json: dict) -> dict:
        pass

    def run(self, json_str: str) -> str:
        # parse the json str into a dictionary
        # convert dictionary back into a json string
        return self.process(input_json)