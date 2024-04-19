import subprocess
import sys

def install_packages(requirements_path):
    with open(requirements_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        try:
            # install the specified version
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', line.strip()])
            print(f"Successfully installed {line.strip()}")
        except subprocess.CalledProcessError:
            # get the package name if the specified version failed
            package_name = line.split('==')[0]
            try:
                # if failed to install the specified version, install the default version
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
                print(f"Specified version failed, installed default version of {package_name}")
            except subprocess.CalledProcessError:
                print(f"Failed to install any version of {package_name}")

if __name__ == "__main__":
    requirements_path = 'requirements.txt'  # or other requirements.txt path
    install_packages(requirements_path)
