def convertDB(database=list):  # , output_type=str):
    if not isinstance(database,list):
        raise Exception("Argument01 has wrong data type")
    # if not isinstance(output_type,str):
    #   raise Exception("Argument02 has wrong data type")

    output_db = []
    print(database)
    # if output_type in ["hn", "hidden_neuron", "i", "input", "op", "output", "w", "weight"]:
    for line in range(len(database)):
        output_db.append(database[line])
    # elif output_type in ["settings", "stg"]:

    return output_db