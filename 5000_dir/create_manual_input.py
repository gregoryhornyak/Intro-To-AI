from settingsControl import UseSettings
from db_control_func import *

def create_inputs_by_manual():
    num_o_lines = UseSettings("Number_Of_Inputs")
    num_of_sets = int(input("How many training sets? "))
    c = ','
    db01=[]
    print("There are " + str(num_o_lines*num_of_sets) + " number of inputs.")
    for i in range(num_o_lines):
        for set in range(num_of_sets):
            value = input("Value for input " + str(i + 1) + ": ")
            db01.append(["i",set,0,i,value])
    return db01
