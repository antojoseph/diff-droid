import banner
import logger_modules
import attack_modules
import updater


def menu():
    print "(1)  View Logging Modules"
    print "(2)  View Attack Modules"
    print "(3)  Update "


def show_banner():
    banner.horizontal("DIFF-DROID")


def read_user_input():
    option = raw_input("Please enter your choice :")
    if (int(option) == 1):
        logger_modules.print_list()
    elif (int(option) == 2):
        attack_modules.print_list()
    elif (int(option) == 3):
        updater.update()


show_banner()
menu()
read_user_input()
