from ultralytics import YOLO
from comet_ml import Experiment
from comet_ml.integration.pytorch import log_model
from dotenv import dotenv_values
import torch
import torch.nn as nn
from torch.nn.utils import prune
import fiftyone as fo
import fiftyone.zoo as foz


def load_data():
    name = 'open-images-v7'
    label_type = ['detections'] # ("detections", "classifications", "relationships", "points", segmentations")
    classes = ['Laptop']
    
    dataset = foz.load_zoo_dataset(
        name,
        split="validation", # train, test, validation
        label_types=label_type,
        classes=classes,
        max_samples=50,
        shuffle=True,
    )
    return dataset
    


def custom_prune(model):
    parameters_to_prune = (
        (model.conv1, 'weight'),
        (model.fc1, 'weight'),
    )
    prune.global_unstructured(parameters_to_prune, pruning_method=prune.L1Unstructured, amount=0.2)
    prune.remove(model.conv1, 'weight')


def calculate_size(model):
    param_size = sum(p.numel() * p.element_size() for p in model.parameters())
    buffer_size = sum(b.numel() * b.element_size() for b in model.buffers())

    size_all_mb = (param_size + buffer_size) / (1024 ** 2)
    print('Model size: {:.3f} MB'.format(size_all_mb))


def main():
    # use gpu if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device)
    
    config = dotenv_values(".env")
    experiment = Experiment(
        api_key=config["COMET_API_KEY"],
        project_name="general",
        workspace="irisxu02"
    )
    
    # hyperparams
    num_epochs = 10
    learning_rate = 0.001
    batch_size = 64
    
    hyper_params = {
        "learning_rate": 0.5,
        "steps": 100000,
        "batch_size": 50,
    }
    experiment.log_parameters(hyper_params)
    
    # train and stuff here
    #model = YOLO("yolov8n.pt") # Model size: 12.085 MB
    model = YOLO("yolov8n-oiv7.pt") # Model size: 13.385 MB
    
    # Train the model on the Open Images V7 dataset
    results = model.train(data='open-images-v7.yaml', epochs=100, imgsz=640)
    
    # log to comet
    log_model(experiment, model, model_name="TheModel")
    

if __name__ == '__main__':
    main()