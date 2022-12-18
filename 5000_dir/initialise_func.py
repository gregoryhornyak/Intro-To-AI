from create_dbs import *
from randomise_weights import *
from db_control_func import *

def Initialise():
    database_control("export","weights",database=randomise_weights(create_weights()))  #  1 if random numbers
