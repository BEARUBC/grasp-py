import argparse
import numpy as np
import pandas as pd
from pathlib import Path

from src.definitions import ROOT_PATH, SETTINGS

parser = argparse.ArgumentParser(description="Generate FSR data")
parser.add_argument("out_path", type=str, help="Relative path to output directory")
parser.add_argument("--mode", type=str, default="random",
                    help="Read from a file with a specified path relative to the root directory")
parser.add_argument("--size", type=int, default=1000, help="Number of frames of data to generate")

args = parser.parse_args()


def generate_random_frame() -> np.ndarray:
    return np.random.rand(*SETTINGS["fsr_matrix"]["dims"])


generation_modes = {
    "random": generate_random_frame
}

print("Generating", args.size, "frames using", args.mode)
generation_function = generation_modes.get(args.mode, lambda: "random")
generated_data = np.array([np.ndarray.flatten(generation_function()) for _ in range(args.size)])
data_df = pd.DataFrame(generated_data)

output_path = Path(args.out_path)
print("Saving data to", output_path)
data_df.to_csv(output_path)
