import os
import subprocess
import platform
import sys
from setuptools import setup, find_packages


class Setup:
    def __init__(self):
        self.path_virtualenv = "venv/"
        self.os_platform = platform.system()
        self.default()
        self.check_up()

    def check_up(self):
        if not self.check_pip_package():
            self.install_pip()
        if not self.check_virtualenv_package():
            self.install_virtualenv()
        if not self.check_venv_folder():
            self.create_venv()
        try:
            self.install_requirements()
        except Exception as e:
            print("Erro na instalação: ", e)

        # self.check_virtualenv_package()

    @staticmethod
    def check_pip_package():
        pip_exists = True
        try:
            import pip
        except ImportError:
            pip_exists = False

        return pip_exists

    @staticmethod
    def check_virtualenv_package():
        return os.getenv('VIRTUAL_ENV')

    def check_venv_folder(self):
        return os.path.exists(self.path_virtualenv)

    @staticmethod
    def install_pip():
        # instalar pip comandos
        return True

    @staticmethod
    def install_virtualenv():
        # instalar virtualenv comandos
        return True

    def create_venv(self):
        # criar venv comandos
        return True

    def install_requirements(self):
        pip_path = os.path.join(os.path.dirname(sys.executable), "", "pip.exe")
        # print(pip_path)
        # subprocess.run([pip_path, "list"])
        subprocess.run([pip_path, "install", "-r", "requirements.txt"])

    def default(self):
        setup(
            name="mika",
            version="0.0.23",
            author="Letícia Ellen Bernardo",
            author_email="leticiaellenbernardo@gmail.com",
            description="initial project of virtual assistant",
            packages=find_packages(),
            long_description=""
        )
