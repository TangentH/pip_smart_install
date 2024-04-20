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
