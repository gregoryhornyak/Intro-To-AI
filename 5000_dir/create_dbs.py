#from settingsControl import *
from useful_functions import *
import random

def create_outputs():
    output_database = []
    num_o_lines = int(UseSettings("Number_Of_Outputs"))
    layer_num = LayerCounter()
    for op in range(num_o_lines):
        value = 0
        output_database.append(["op",layer_num-1,op,value])
    return output_database

def create_weights():
    output_database = []
    num_of_sets = int(UseSettings("Number_Of_Training_Sets"))
    layer_items_LIST = LayerItemCounter()
    for layer in range(len(layer_items_LIST)-1):
        for hn_i in range(int(layer_items_LIST[layer])):
            for hn in range(int(layer_items_LIST[layer+1])):
                # ['w','domain_layer','domain_ser_num','domain_epoch','range_ser_num','value']
                if layer == 0: # input layer
                    for set in range(num_of_sets):
                        output_database.append(["w",layer,hn_i,set,hn,0])
                else:
                    output_database.append(["w",layer,hn_i,99,hn,0])
    return output_database

def create_hns():
    output_database = []
    hn_layer_items_LIST = UseSettings("Number_Of_Hidden_Neurons_List")
    for layer in range(len(hn_layer_items_LIST)):
        for hn in range(int((hn_layer_items_LIST[int(layer)]))):
            value = 0
            output_database.append(["hn",layer+1,hn,value]) # + extras
    return output_database
