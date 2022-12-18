from create_dbs import *
from db_control_func import*

def Structure():

    database_control("export", "outputs", database=create_outputs())
    database_control("export", "weight", database=create_weights())
    database_control("export", "hidden_neurons", database=create_hns())
