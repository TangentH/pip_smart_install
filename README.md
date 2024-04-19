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


