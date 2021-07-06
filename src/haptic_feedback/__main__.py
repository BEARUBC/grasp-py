from src.haptic_feedback.haptic_module import HapticFeedback
from src.haptic_feedback.randomwalk_generator import RandomWalkGenerator


def main():
    haptic_feedback = HapticFeedback()
    test_randomwalk = RandomWalkGenerator()
    test_randomwalk.generator()
    rw_list = test_randomwalk.randomwalk
    haptic_feedback.process({"fsr_strengths": rw_list})


main()

# temporary --------------------------------------
# from src.haptic_feedback.randomwalk_generator import RandomWalkGenerator


# def main():
# randomwalk = RandomWalkGenerator()
# randomwalk.generator()
# randomwalk.plotter()


# main()
