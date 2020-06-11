from controller import Controller


def run():
    control = Controller()
    control.wishToHack()
    control.choice()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        Controller.exitMethod()
