import subprocess
import sys
import os
from importlib.metadata import version, PackageNotFoundError

def install_packages(requirements_path):
    # Check if in a Conda environment
    if 'CONDA_PREFIX' in os.environ:
        print(f"Running in a Conda environment located at: {os.environ['CONDA_PREFIX']}")
    elif hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
        print(f"Running in a virtual environment located at: {sys.prefix}")
    else:
        print("Not running in a virtual environment.")

    # Check for requirements.txt in the current directory
    if not os.path.exists(requirements_path):
        print("No requirements.txt found in the current directory.")
        return
    else:
        user_input = input("Found requirements.txt.\nDo you want to continue with the installation? [y/n]: ")
        if user_input.lower() != 'y':
            print("Installation aborted by the user.")
            return

    with open(requirements_path, "r") as file:
        lines = file.readlines()

    installed_packages = {}
    failed_packages = []

    for line in lines:
        line = line.strip()
        if line.startswith('#') or not line:
            continue  # Skip comments and empty lines

        parts = line.split('==')
        package_name = parts[0].strip()
        requested_version = parts[1].strip() if len(parts) > 1 else 'not specified'

        try:
            # Try installing the specific version or just the package if no version specified
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', line])
            actual_version = version(package_name)
            installed_packages[package_name] = (actual_version, requested_version)
        except subprocess.CalledProcessError:
            try:
                # If specific version fails, try installing the package without version specification
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
                actual_version = version(package_name)
                installed_packages[package_name] = (actual_version, requested_version)
            except subprocess.CalledProcessError:
                failed_packages.append(package_name)
        except PackageNotFoundError:
            failed_packages.append(package_name)

    # Print installed packages and their versions
    print("\nInstalled Packages and Versions:")
    print(f"{'Package':<30}{'Version Installed':<20}{'Version Requested':<20}")
    print('-' * 70)
    for package, versions in installed_packages.items():
        actual_version, requested_version = versions
        print(f"{package:<30}{actual_version:<20}{requested_version:<20}")

    # Print failed installations
    if failed_packages:
        print("\nFailed to Install:")
        for package in failed_packages:
            print(package)
        print()

if __name__ == "__main__":
    requirements_path = 'requirements.txt'  # Assume default path
    install_packages(requirements_path)
