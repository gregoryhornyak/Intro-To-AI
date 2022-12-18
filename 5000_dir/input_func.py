from db_control_func import*
from create_manual_input import *
from create_manual_output import *


def Input(manual_or_import=str):
    if manual_or_import == "manual":
        database_control("export", "training_data", database=create_inputs_by_manual())
        database_control("export", "target_outputs", database=create_outputs_by_manual())
    if manual_or_import == "import":
        sought_file = "training_data" #input("Type in the name of the database: ")
        try:
            # raw_input_db = exportAnything(importAnything(sought_file),"input")
            database_control("export", "inputs", database=database_control("import", sought_file))
        except:
            raise Exception("Error: Could not find the database with name "+sought_file)
        sought_file02 = "target_outputs"
        try:
            # raw_input_db = exportAnything(importAnything(sought_file),"input")
            database_control("export", "toutputs", database=database_control("import", sought_file02))
        except:
            raise Exception("Error: Could not find the database with name "+sought_file02)

