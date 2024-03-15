from engine import train_one_epoch, evaluate
import torch
from init_dataset import PennFudanDataset
from get_transform import get_transform
import utils
from finetune import get_model_instance_segmentation
from train import train
import time

# train on the GPU or on the CPU, if a GPU is not available
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

# our dataset has two classes only - background and person
num_classes = 2

# use our dataset and defined transformations
dataset = PennFudanDataset("data/PennFudanPed", get_transform(train=True))
dataset_test = PennFudanDataset("data/PennFudanPed", get_transform(train=False))

# split the dataset in train and test set
indices = torch.randperm(len(dataset)).tolist()
dataset = torch.utils.data.Subset(dataset, indices[:-50])
dataset_test = torch.utils.data.Subset(dataset_test, indices[-50:])

# define the evaluation data loader
data_loader_test = torch.utils.data.DataLoader(
    dataset_test,
    batch_size=1,
    shuffle=False,
    num_workers=0,  # no additional processes run in parallel
    collate_fn=utils.collate_fn,
)

# define training data loader using a Distributed Sampler
data_loader = torch.utils.data.DataLoader(
    dataset=dataset,
    batch_size=2,
    shuffle=True,
    num_workers=0,  # no additional processes run in parallel
    collate_fn=utils.collate_fn,
)

# get the model using our helper function in finetune.py
model = get_model_instance_segmentation(num_classes)

# share the memory of the model during multiprocessing
model.share_memory()

# move model to the right device
model.to(device)

# construct an optimizer
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)

# and a learning rate scheduler
lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

# let's train it just for 2 epochs
num_epochs = 2

# start timer
start_time = time.time()

# train the model
train(model, num_epochs, data_loader, device)

# end timer
end_time = time.time()

# evaluate on the test dataset
evaluate(model, data_loader_test, device=device)

# save the model to runs\train1.pt
torch.save(model, "runs/bench.pt")

print(f"That's it! \nThe training took {end_time - start_time} seconds to complete.")
