import subprocess
import sys
import pkg_resources

def install_packages(requirements_path):
    with open(requirements_path, "r") as file:
        lines = file.readlines()

    installed_packages = {}
    failed_packages = []

    for line in lines:
        parts = line.strip().split('==')
        package_name = parts[0]
        requested_version = parts[1] if len(parts) > 1 else None
        
        try:
            # install the specified version
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', line.strip()])
            print(f"Successfully installed {line.strip()}")
            installed_packages[package_name] = requested_version
        except subprocess.CalledProcessError:
            try:
                # if failed to install the specified version, install the default version
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
                print(f"Specified version failed, installed default version of {package_name}")
                installed_packages[package_name] = 'default'  # Mark as default installed
            except subprocess.CalledProcessError:
                print(f"Failed to install any version of {package_name}")
                failed_packages.append(package_name)

    # Print installed packages and their versions
    print("\nInstalled Packages and Versions:")
    for package, requested_version in installed_packages.items():
        actual_version = pkg_resources.get_distribution(package).version
        if requested_version and requested_version != actual_version:
            print(f"{package}=={actual_version} (requested {requested_version})")  # version mismatch
        else:
            print(f"{package}=={actual_version}")

    # Print failed installations
    if failed_packages:
        print("\nFailed to Install:")
        for package in failed_packages:
            print(f"{package} - installation failed")

if __name__ == "__main__":
    requirements_path = 'requirements.txt'  # or other requirements.txt path
    install_packages(requirements_path)
