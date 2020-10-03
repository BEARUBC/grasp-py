# GRASP-RPi
The main software for the Raspberry Pi

## Setup
How to install and setup the RPi software on a pi or desktop

### Requirements

- [PortAudio](http://portaudio.com/) for PyAudio
- Python 3.6

Desktop only:

- Virtualenv

### Installation
Step-by-step installation instructions for various platforms

#### Windows

1. Setup a virtual environment in the root directory of the project. This can either be [done in your IDE](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html), or like so:
   
    ```
    cd <path-to-grasp-rpi>\grasp-rpi
    virtualenv --python=<path_to_python3.6> venv
    venv\Scripts\activate.bat
    ``` 
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

#### Mac/Linux

1. Setup a virtual environment in the root directory of the project. This can either be [done in your IDE](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html), or like so:
    ```
    cd <path-to-grasp-rpi>/grasp-rpi
    virtualenv --python=<path_to_python3.6> venv
    source venv/bin/activate
    ```
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```


#### Pi
We don't bother with a development environment on a pi, because we're not doing any development. Simply install the requirements:
```
pip install -r requirements.txt
```