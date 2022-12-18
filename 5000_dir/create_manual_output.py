from settingsControl import UseSettings
from useful_functions import LayerCounter
from db_control_func import *

def create_outputs_by_manual():
    num_o_lines = UseSettings("Number_Of_Outputs")
    num_of_layers = LayerCounter()
    db01=[]
    for op in range(num_o_lines):
        value = input("Value for output " + str(op + 1) + ": ")
        db01.append(["op",num_of_layers-1,op,value])
    return db01
