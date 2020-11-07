from src.definitions import TORCH_DEVICE
from src.fsr_matrix.classifier.matrix_classifier import MatrixClassifier

matrix_classifier = MatrixClassifier().to(TORCH_DEVICE)
