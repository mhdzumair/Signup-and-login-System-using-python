from time import sleep, perf_counter


class View(object):
    def __init__(self):
        print(
            '\n**************************************************************', end="")
        View.printEffect("\t\tWelcome to Hacking World!!!")
        print(
            '\n**************************************************************')

    @classmethod
    def printEffect(cls, words, newline=True):
        print("\r")
        for char in words:
            sleep(0.15)
            print(char, end='', flush=True)
        if newline:
            print()

    @classmethod
    def printDot(cls, time=None):
        startTime = perf_counter()
        while (perf_counter() - startTime) <= (5 if time == None else float(time)):
            for char in "...":
                sleep(0.4)
                print(char, end='', flush=True)
            print("\b\b\b   \b\b\b", end="")

        print()

    @classmethod
    def exitMethod(cls):
        View.printEffect(
            "\nThanks for using my programe. \nGood bye...!\nEnding the programe", newline=False)
        View.printDot()
        print("\n")

    def wishToHack(self):
        View.printEffect(
            "Do you wish to hack other's system? \n please input your choice \n\t(Y)es \t\t Type 'y' \n\t(N)o \t\t Type 'n'")

    def goodBoy(self):
        View.printEffect(
            "You'r such a good boy ... \n Go and drink mommy milk :-)", newline=False)
        View.printDot()

    @staticmethod
    def invalidInput(type):
        View.printEffect(f"invalid {type} \n please try again", newline=False)
        View.printDot()

    def noteMessage(self):
        View.printEffect(
            "In order to hack you must login to an Account. \nif you don't have an Account please create an Account.")

    def userChoice(self):
        View.printEffect(
            "Do you wish to \n\t(L)ogin \t\t Type 'l' \n\t(S)ignup \t\t Type 's' \n\t(E)xit \t\t\t Type 'e'\nthe system ")

    def patient(self, time=None):
        View.printEffect("System is loading", newline=False)
        View.printDot(time)

    def userName(self):
        View.printEffect("Enter the user name :")

    def password(self):
        View.printEffect("Enter the Password :")

    def passwordCheck(self):
        View.printEffect("checking password", newline=False)
        View.printDot()

    def loginSucces(self):
        View.printEffect("You are succesfully login to hacking 3.0")
        self.patient(10)
        View.printEffect("sorry!!! can't connect to the server right now.")
        View.printEffect(
            "server is under construction. you will hack other's system in future. Thanks for participating")

    def warning(self):
        View.printEffect(
            "warning!!! \nI'm not responsible for any illegal activity. \nThis Software only for Educational purpose")
        self.patient(8)

    def userNameExist(self):
        View.printEffect(
            "username is already taken. please enter another user name.")

    def passwordRules(self):
        View.printEffect("Your password must be under this rules \n 1) Password should contain atleast 1 upper case. \n 2) Password should contain atleast one lower case. \n 3) Password should contain atleast one numaric value. \n 4) your password must be 5 - 15 characters.")

    def signupSuccess(self):
        View.printEffect(
            "You are successfully create an account", newline=False)
        View.printDot()
