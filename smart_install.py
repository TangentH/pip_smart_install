import subprocess
import sys
import pkg_resources

def install_packages(requirements_path):
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
        requested_version = parts[1].strip() if len(parts) > 1 else None
        
        try:
            # Install the specified version
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', line])
            print(f"Successfully installed {line}")
            installed_packages[package_name] = (requested_version, requested_version)
        except subprocess.CalledProcessError:
            try:
                # If failed to install the specified version, install the default version
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
                print(f"Specified version failed, installed default version of {package_name}")
                installed_packages[package_name] = (pkg_resources.get_distribution(package_name).version, requested_version)
            except subprocess.CalledProcessError:
                print(f"Failed to install any version of {package_name}")
                failed_packages.append(package_name)

    # Print installed packages and their versions
    print("\nInstalled Packages and Versions:")
    print(f"{'Package':<20}{'Version Installed':<20}{'Version Requested':<20}")
    print('-' * 60)
    for package, (actual_version, requested_version) in installed_packages.items():
        print(f"{package:<20}{actual_version:<20}{requested_version:<20}")

    # Print failed installations
    if failed_packages:
        print("\nFailed to Install:")
        for package in failed_packages:
            print(f"{package} - installation failed")

if __name__ == "__main__":
    requirements_path = 'requirements.txt'  # or other requirements.txt path
    install_packages(requirements_path)
