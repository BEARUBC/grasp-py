from src.haptic_feedback.randomwalk_generator import RandomWalkGenerator
from src.module import Module


class HapticFeedbackModule(Module):

    def process(self, input_json: dict) -> dict:
        test_randomwalk = RandomWalkGenerator()
        test_randomwalk.generator()
        test_randomwalk.plotter()
        rw_list = test_randomwalk.randomwalk

        new_list = [element * 2 for element in rw_list]
        new_randomwalk = RandomWalkGenerator()
        new_randomwalk.rw_setter(new_list)
        new_randomwalk.plotter()

        return {"haptic feedback random walk": new_randomwalk}
