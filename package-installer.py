import os.path
import subprocess
import sys


def install_package(packages):
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"Failed to install package {package}")


def read_requirements(file_path):
    requirements = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # 주석이나 빈 줄은 무시
                line = line.strip()
                if line and not line.startswith("#"):
                    requirements.append(line)

        return requirements

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []


requirements_path = os.path.join(os.path.curdir, "requirements.txt")
requirement_packages = read_requirements(requirements_path)
install_package(requirement_packages)