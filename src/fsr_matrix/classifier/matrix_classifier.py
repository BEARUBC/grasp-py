import tensorflow as tf
import numpy as np

from src.definitions import SETTINGS

output_map = [
    "Nothing",
    "Foam Sphere",
    "Wood Cube",
    "Wood cylinder"
]


class MatrixClassifier:
    def __init__(self):
        self.settings = SETTINGS["fsr_matrix"]
        self.input_shape = (SETTINGS["columns"] * SETTINGS["rows"],)
        print(self.input_shape)
        print(type(self.input_shape))
        self.model = self.build_model()

    def build_model(self):
        layers = [
            tf.keras.layers.Flatten(input_shape=self.input_shape),
            tf.keras.layers.Dense(120, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(50, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(self.settings["classifier"]["output_size"], activation=tf.nn.softmax)
        ]

        model = tf.keras.models.Sequential()
        for layer in layers:
            model.add(layer)
        return model

    def train_model(self):
        pass

    # Take inputs, return expected shape
    def classify_inputs(self, inputs: np.ndarray, english=False):
        if inputs.shape != self.input_shape:
            print("Input shape does not match expected input shape")
            return
        prediction = self.model.predict(inputs).argmax()
        if english:
            return output_map[prediction]
        else:
            return prediction
