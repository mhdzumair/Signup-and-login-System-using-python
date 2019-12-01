from sys import exit
from time import sleep
import string

print("Welcome to Hacking World!!!")
sleep(5)


def validator(password):
    for l in string.ascii_lowercase:
        for u in string.ascii_uppercase:
            for d in string.digits:
                if 5 <= len(password) <= 15 and l in password and u in password and d in password:
                    return True
    return False


while True:
    hackingInterest = input("Do you wish to hack other's system? \n please input your choice (Y)es or (N)o :")
    if hackingInterest.lower() == "y":
        break
    elif hackingInterest.lower() == "n":
        exit("You'r such a good boy ... \n Go and drink mommy milk :-) ..")
    else:
        print("input is invalid type y / n \n please try again...")

print("Please be patient...")
sleep(5)
print("In order to hack you must login to our server. \n if you don't have an account please create an account")
credential = {}
while True:
    choiceLS = input("Enter your choice (S)ignup (L)ogin :")
    if choiceLS.lower() == "l":
        print("System is loading...")
        sleep(3)
        while True:
            userName = input("Enter Your user name :")
            sleep(3)
            password = input("Enter your Password :")
            try:
                with open("userdata.txt", "r") as file:
                    for data in file:
                        (key, value) = data.split()
                        credential[key] = value
                    if not f"{userName}" in credential:
                        print("Invalid user name. \nPlease try again...")
                    else:
                        print("checking password ...")
                        sleep(5)
                        checkPassword = credential.get(f"{userName}")
                        if password == checkPassword:
                            print("You are succesfully login to hacking 2.0 ...")
                            print("System is loading...")
                            sleep(10)
                            print("sorry!!! can't connect to the server right now.. \n server is under "
                                  "construction... \n you will hack other's system in future. Thanks for participate")
                            sleep(3)
                            exit("system going to shut down")
                        else:
                            print("Your entered password is invalid. \n please try again.")
                            sleep(5)
            except FileNotFoundError:
                print("You don't have an account please signup for an account...!")
                sleep(5)
                break

    elif choiceLS.lower() == "s":
        print("warning!!! \nI'm not responsible for any illegal activity. \nThis Software only for Educational purpose")
        sleep(10)
        while True:
            userName = input("Please enter user name :")
            try:
                with open("userdata.txt", "r") as file:
                    for data in file:
                        (key, value) = data.split()
                        credential[key] = value
                if not f"{userName}" in credential:
                    with open("userdata.txt", "a") as file:
                        file.write(f"{userName} ")
                        break
                else:
                    print("username is already taken. please enter another user name.")
                    sleep(5)
            except FileNotFoundError:
                with open("userdata.txt", "w") as file:
                    file.write(f"{userName} ")
                    break

        while True:
            password = input("Enter a strong password :")
            if validator(password):
                with open("userdata.txt", "a") as file:
                    file.write(f"{password}\n")
                    break
            else:
                print(
                    "Your password must be under this rules \n 1) Password should contain atleast 1 upper case. \n 2) Password should contain atleast one lower case. \n 3) Password should contain atleast one numaric value. \n 4) your password must be 5 - 15 characters. \n Try again with strong password...")
                sleep(5)

        print("You are successfully create an account...")
        print("please login to system...")
        sleep(5)
        while True:
            userChoice = input("Do you wish to (L)ogin or (E)xit system :")
            if userChoice.lower() == "l":
                print("please wait...\n loading...")
                sleep(10)
                break
            elif userChoice.lower() == "e":
                print("Thank you for using my software... Good bye...!")
                sleep(5)
                exit("system begin shutdown...n")
            else:
                print("invalid input type l / e \n Try again..")
                sleep(3)

    else:
        print("invalid input type s / l \n Try again..")
        sleep(5)
