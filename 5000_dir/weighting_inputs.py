#from settingsControl import *

def weighting_Inputs(domainLayer, inputs_list, weights_list, hn_serial_number, training_set):
    weighted_inputs_list=[] # returning
    serNum = training_set
    # hidden neurons are inputs
    for i in range(len(inputs_list)):
        for w in range(len(weights_list)):
            if int(inputs_list[i][1]) == int(weights_list[w][1]): # same layer
                if int(inputs_list[i][2]) == int(weights_list[w][2]):  # same dom serial number
                    if int(inputs_list[i][1]) == domainLayer: # layer of input is same as given layer
                        if int(weights_list[w][4]) == hn_serial_number: # to correct hn

                            if inputs_list[i][0] == "i": # if input, not hn
                                if int(inputs_list[i][-2]) == serNum: # correct training set
                                    if int(weights_list[i][3]) == serNum: # correct training set
                                        weighted_inputs_list.append(float(inputs_list[i][-1]) * float(weights_list[w][-1])) # store only the value

                            else: # if hn, not input
                                weighted_inputs_list.append(float(inputs_list[i][-1]) * float(weights_list[w][-1])) # store only the value

    return weighted_inputs_list
