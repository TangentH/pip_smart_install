# pip_smart_install
Automatically resolve version problem when using pip install -r requirements.txt

Smoothly install all dependencies in your requirements.txt even if pip cannot find the specified version (then the default version will be installed).

**Usage:**

```
cd /path/to/requirements.txt
git clone https://github.com/Tangent-H/pip_smart_install.git
conda activate <env_name> # enter conda environment if needed
python smart_install.py
```

**Alternatively** (even an easier approach):

1. `cd` the directory with a requirements.txt
2. `conda activate <env>` if needed
3. make sure there is no such a file named `smart_install.py` in this directory because the following command tried to remove this file after installing all the requirements

```
wget https://raw.githubusercontent.com/Tangent-H/pip_smart_install/main/smart_install.py && python smart_install.py ; rm smart_install.py
```

**Example:**

```
cd test
conda activate test
wget https://raw.githubusercontent.com/Tangent-H/pip_smart_install/main/smart_install.py && python smart_install.py ; rm smart_install.py
```

if the requirements.txt looks something like this:

```
# default installation
numpy
# wrong version
pillow==1.2.3.4
# correct version
matplotlib==3.8.0
# package not exist
NoSuchPackage
```

The output of the script looks something like this:

```
Running in a Conda environment located at: /home/tan/anaconda3/envs/test
Found requirements.txt.
Do you want to continue with the installation? [y/n]: y

...
# pip install standard output
...

Installed Packages and Versions:
Package             Version Installed   Version Requested   
------------------------------------------------------------
numpy               1.26.4              not specified       
pillow              10.3.0              1.2.3.4             
matplotlib          3.8.0               3.8.0               

Failed to Install:
NoSuchPackage

```

If you think this repo is useful, consider giving me a ⭐, thx!
