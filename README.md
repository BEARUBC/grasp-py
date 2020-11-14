# Grasp-py
Python portion of GRASP control

## Setup
How to install and setup the RPi software on a pi or desktop


### Installation

Prerequisites:
- Anaconda
- Python 3.7
- [PortAudio](http://portaudio.com/) for PyAudio


```bash
git clone git@gitlab.com:UBCBear/grasp-rpi.git
cd grasp-py
conda env create --file environment.yaml
conda activate grasp-py

python -m install pygame
```

[Add pytorch to your conda environment](https://pytorch.org/get-started/locally/)

Be sure to select `Conda` as your package.
If you have a powerful GPU, it's also recommended to install and use CUDA. Once that's done be sure to select the correct version to use with pytorch. Right now all of the pytorch is written to use CUDA 10.1, so that is the recommended version right now.

## Updating the Environment
 
In the case of an update that adds, removes, or updates packages, run:
```bash
conda env update --file environment.yaml
```
