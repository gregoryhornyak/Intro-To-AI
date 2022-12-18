from single_neuron import*
#from db_control_func import*
from useful_functions import*
from weighting_inputs import*
#from settingsControl import*

def calculate_output(i,w,hn,o):

    weights_db = w
    inputs_db = i
    hns_db = hn
    output_db = o

    num_o_lyrs = LayerItemCounter()
    #print("Number of layers: "+str(num_o_lyrs))
    num_o_weights = LineCounter("weights.txt")
    which_train_set = int(UseSettings("Which_Training_Set"))
    training_set=0
    #            WEIGHTING
    for layer in range(len(num_o_lyrs)-1): # weights are inbetween
        for neuron in range(int(num_o_lyrs[layer+1])): # dont skip layer zero
            # domain layer is input layer aka. layer zero
            if layer == 0:
                for hn in range(len(hns_db)): # find relevant hn
                    if int(hns_db[hn][1]) == layer + 1:  # target neuron
                        if int(hns_db[hn][2]) == neuron: # to be updated
                            neuron01 = Neuron(weighting_Inputs(layer, inputs_db, weights_db, neuron,training_set))  # activate the neuron
                            hns_db[hn][-1] = (float(neuron01.ret())) # update
                            del neuron01 # delete
                            break
            # domain layer is hn layer
            #    enter hns                exit hns
            elif layer >=1 and layer <= len(num_o_lyrs)-3:
                for hn in range(len(hns_db)):  # find relevant hn
                    if int(hns_db[hn][1]) == layer + 1:  # target layer neuron
                        if int(hns_db[hn][2]) == neuron:  # to be updated
                            neuron01 = Neuron(weighting_Inputs(layer, hns_db, weights_db, neuron,training_set))  # activate the neuron
                            hns_db[hn][-1] = float(neuron01.ret())  # update
                            del neuron01  # delete
                            break  # no need for further loops
            # domain layer is last hn layer
            else:
                for op in range(len(output_db)):  # find relevant op
                    if int(output_db[op][1]) == layer + 1:  # target layer
                        if int(output_db[op][2]) == neuron:  # to be updated
                            neuron01 = Neuron(weighting_Inputs(layer, hns_db, weights_db, neuron,training_set))  # activate the neuron
                            output_db[op][-1] = float(neuron01.ret())  # update
                            del neuron01  # delete
                            break  # no need for further loops

    return hns_db,weights_db,output_db
