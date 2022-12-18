from input_func import*
from parameters_func import*
from structure_func import*
from initialise_func import*
from introduce_func import*


Parameters(7,[8,12,5],3, 3,"sigmoid",0.1) # 1
print("Parameters DONE")
Input("import") # 2
print("Inputs DONE")
Structure() # 3
print("Structure DONE")
Initialise() # 4
print("Initialise DONE")
Introduced() # 5
print("Introduced DONE")

# HAVE TO SOLVE TRAINING SET PROBLEM

#PrintOut()


# Problem: when exporting, unnecessary upper commas are added


'''


Introduced()
    to repeatedly introduce one training sample at a time at the input layer.
Output()
    to calculate
WeightUpdate()
Print()

DONE:   Input() to insert data by manual or from database

Parameters(Number_Of_Inputs, Number_Of_Hidden_Neurons, Number_Of_Outputs, Number_Of_Epochs, Activation_Function, Learning_Rate)

Structure() to create the structure

Initialise() to produce random weight values between 0 and 1 for the weights
'''
