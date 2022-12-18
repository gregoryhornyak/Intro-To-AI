from settingsControl import *


def LineCounter(filename=str):
    if not isinstance(filename,str):
        raise Exception("Argument is not string")
    if filename[-4] != ".": # outputs . t x t
        filename += ".txt"
    try:
        file01 = open(str(filename), "r")
    except:
        raise FileNotFoundError
    line_count = 0
    for line in file01:
        if line != "\n":
            line_count += 1
    file01.close()
    return line_count

def LayerCounter():
    hns_lyrs = UseSettings("Number_Of_Hidden_Neurons_List")
    num_of_lyrs = 2 + len(hns_lyrs)
    return num_of_lyrs

def LayerItemCounter():
    hns_lyrs = UseSettings("Number_Of_Hidden_Neurons_List")
    i_lyr = int(UseSettings("Number_Of_Inputs"))
    op_lyr = int(UseSettings("Number_Of_Outputs"))
    num_of_lyrs=[]
    num_of_lyrs.append(i_lyr)
    # print("Inputs are :" + str(i_lyr))
    for hn in hns_lyrs:
        num_of_lyrs.append(int(hn))
    num_of_lyrs.append(op_lyr)
    return num_of_lyrs
