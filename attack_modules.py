from os import listdir
from os.path import isfile, join


def pretty_print(list_of_files):
    print "Attack Modules !"
    for x in range(len(list_of_files)):
        print "\t"+"("+str(x)+") "+list_of_files[x]
    read_input(list_of_files)

def print_list():
    mypath = "attackers"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    pretty_print(onlyfiles)

def read_input(list_of_files):
    user_option = raw_input("Please enter your choice :")
    for x in range(len(list_of_files)):
        if (x == int(user_option)):
            print "your selection is: "+list_of_files[x]