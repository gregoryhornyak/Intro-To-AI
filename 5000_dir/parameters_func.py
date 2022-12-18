from db_control_func import *
from useful_functions import*

def Parameters(Number_Of_Inputs=int, Number_Of_Hidden_Neurons_List=list, Number_Of_Outputs=int, Number_Of_Epochs=int, Activation_Function=str, Learning_Rate=float):
    if not isinstance(Number_Of_Inputs,int):
        raise Exception("Number_Of_Inputs" + " has wrong datatype")
    if not isinstance(Number_Of_Hidden_Neurons_List,list):
        raise Exception("Number_Of_Hidden_Neurons_List" + " has wrong datatype")
    if not isinstance(Number_Of_Outputs,int):
        raise Exception("Number_Of_Outputs" + " has wrong datatype")
    if not isinstance(Number_Of_Epochs,int):
        raise Exception("Number_Of_Epochs" + " has wrong datatype")
    if not isinstance(Learning_Rate,float):
        raise Exception("Learning_Rate" + " has wrong datatype")
    if not isinstance(Activation_Function,str):
        raise Exception("Activation Function" + " has wrong datatype")
    elif Activation_Function != "sigmoid" and Activation_Function != "step":
        raise Exception("Activation Function doesn't exists")

    if Activation_Function == "sigmoid":
        Activation_Function = 0
    elif Activation_Function == "step":
        Activation_Function = 1

    # new function for this
    Number_Of_Training_Sets=0
    try:
        file01 = open("training_data.txt", "r")
        oneline = file01.readline().strip("\n").split(",")
        Number_Of_Training_Sets = len(oneline)
        file01.close()
    except:
        pass

    Which_Training_Set = 0
    settings_db = [Number_Of_Inputs,Number_Of_Hidden_Neurons_List,Number_Of_Outputs,Number_Of_Epochs,
                   Activation_Function,Learning_Rate,Number_Of_Training_Sets,Which_Training_Set]
    settings_names_db = ["Number_Of_Inputs","Number_Of_Hidden_Neurons_List","Number_Of_Outputs","Number_Of_Epochs",
                   "act_func_0_SGM_1_STP","Learning_Rate","Number_Of_Training_Sets","Which_Training_Set"]

    newdb01 = []
    for i in range(len(settings_db)):
        newdb01.append(["stg", settings_names_db[i],str(settings_db[i])])

    database_control("export", "settings", database=newdb01)
