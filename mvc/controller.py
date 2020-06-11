import string
from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model("dedsec", "pZ35Cd5BSgH8y9s", "mvc", "credential")
        self.view = View()

    def validator(self, password):
        for l in string.ascii_lowercase:
            for u in string.ascii_uppercase:
                for d in string.digits:
                    if 5 <= len(password) <= 15 and l in password and u in password and d in password:
                        return True
        return False

    def wishToHack(self):
        self.view.wishToHack()
        self.hackingInterest = input()
        if self.hackingInterest.lower() == "y":
            return
        elif self.hackingInterest.lower() == "n":
            self.view.goodBoy()
            Controller.exitMethod()
        else:
            View.invalidInput("input")
            self.wishToHack()

    def choice(self):
        self.view.patient(5)
        self.view.noteMessage()
        self.view.userChoice()
        self.userChoice = input()
        choiceLower = self.userChoice.lower()
        if choiceLower == "s":
            self.signup()
        elif choiceLower == "l":
            self.login()
        elif choiceLower == "e":
            Controller.exitMethod()
        else:
            View.invalidInput("input")
            self.choice()

    def signup(self):
        self.view.patient(3)
        self.view.warning()
        username = self.getUsername("signup")
        password = self.getPassword("signup")
        self.model.signup(username, password)

    def getUsername(self, method):
        self.view.userName()
        self.username = input()
        result = self.model.usernameCheck(self.username)
        if method == "signup":
            if result:
                self.view.userNameExist()
                self.getUsername("signup")
            else:
                return self.username
        elif method == "login":
            if result:
                return self.username
            else:
                View.invalidInput("username")
                self.getUsername("login")

    def getPassword(self, method):
        if method == "signup":
            self.view.passwordRules()
        self.view.password()
        self.password = input()
        if method == "signup":
            valid = self.validator(self.password)
            if valid:
                return self.password
            else:
                View.invalidInput("password")
                self.getPassword("signup")
        elif method == "login":
            return self.password

    def login(self):
        self.view.patient(3)
        username = self.getUsername("login")
        password = self.getPassword("login")
        validate = self.model.passwordCheck(username, password)
        if validate:
            self.view.loginSucces()
            Controller.exitMethod()
        else:
            View.invalidInput("username or password")
            self.login()

    @classmethod
    def exitMethod(cls):
        View.exitMethod()
        exit()
