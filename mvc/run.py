from controller import Controller
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def run():
    control = Controller()
    control.wishToHack()
    control.choice()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        Controller.exitMethod()
    except ImportError:
        install("pymongo")
