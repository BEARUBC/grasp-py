# Grasp-py

Python portion of GRASP control

## Setup

How to install and setup the RPi software on a pi or desktop

### Installation

Prerequisites:

- Anaconda
- Python >= 3.7

```bash
git clone git@github.com:BEARUBC/grasp-py.git
cd grasp-py
conda env create --file environment.yaml
conda activate grasp_analytics
```

If you would like to enable linting as a pre-commit hook, run:

```
pre-commit install
```

[Add pytorch to your conda environment](https://pytorch.org/get-started/locally/)

Be sure to select `Conda` as your package.
If you have a GPU that is CUDA-enabled, it's also recommended to install and use CUDA. Once that's done be sure to select the correct version to use with pytorch.

## Updating the Environment

In the case of an update that adds, removes, or updates packages, run:

```bash
conda env update --file environment.yaml
```

## Installing Package Locally

Run the following command in the root directory of the repository:

```
pip install .
```
