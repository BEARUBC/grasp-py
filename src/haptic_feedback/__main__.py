from src.haptic_feedback.randomwalk_generator import RandomWalkGenerator


def main():
    randomwalk = RandomWalkGenerator()
    randomwalk.generator()
    randomwalk.plotter()


main()
