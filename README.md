# Grasp-py
Python portion of GRASP control

## Installation

Prerequisites:
- Anaconda
- Python 3.7

```bash
git clone git@gitlab.com:UBCBear/grasp-rpi.git
cd grasp-py
conda env create --file environment.yaml
conda activate grasp-py
```

[Add pytorch to your conda environment](https://pytorch.org/get-started/locally/)

## Updating the Environment
 
In the case of an update that adds, removes, or updates packages, run:
```bash
conda env update --file environment.yaml
```
