from settingsControl import *
from useful_functions import*
from import_export import*

def PrintOut():
    weights_db = importAnything("weights")
    inputs_db = importAnything("inputs")
    hns_db = importAnything("hidden_neurons")
    output_db = importAnything("outputs")
    num_o_lyrs = LayerItemCounter()
    print(num_o_lyrs)
    which_set = int(UseSettings("Which_Training_Set"))
    for layer in range(len(num_o_lyrs)):
        if layer == 0:
            print("(Input) Layer one")
            for neuron in range(len(inputs_db)):
                if int(inputs_db[neuron][-2]) == which_set:
                    #print(inputs_db[neuron])
                    for w in range(len(weights_db)):
                        if      int(weights_db[w][2]) == int(inputs_db[neuron][2]) and \
                                int(weights_db[w][1]) == int(inputs_db[neuron][1]) and \
                                int(weights_db[w][3]) == which_set:# and \
                                #int(weights_db[w][1] == layer):
                            print(str(inputs_db[neuron][2]) + ". input: " + str(inputs_db[neuron][-1]), end=" > ")
                            print(str(w+1) + ". weight: " + str( round( float(weights_db[w][-1]),2 ) ))
        elif layer > 0 and layer <= (len(num_o_lyrs)-2):
            print("Layer " + str(layer+1))
            #for neuron in range(len(hns_db)):
            for neuron in range(len(hns_db)): # 12 3 4 5 2
                for w in range(len(weights_db)):
                    if int(weights_db[w][2]) == int(hns_db[neuron][2]) and int(weights_db[w][1]) == int(hns_db[neuron][1]) and int(weights_db[w][1]) == layer and int(hns_db[neuron][1]) == layer:
                        print(str(neuron + 1) + ". h_neuron on layer "+str(layer+1)+": " + str(hns_db[neuron][-1]), end=" > ")
                        print(str(w+1) + ". weight: " + str( round( float(weights_db[w][-1]),2 ) ))
        else:
            print("(Output) Layer " + str(layer + 1))
            for neuron in range(num_o_lyrs[layer]):
                print(str(neuron + 1) + ". output on layer " + str(layer + 1) + ": " + str(output_db[neuron][-1]))

    print("Success 06 !")