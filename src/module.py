from abc import abstractmethod


class Module:

    @abstractmethod
    def run(self, input_json: str) -> str:
        pass
