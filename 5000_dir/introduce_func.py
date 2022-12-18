from output_func import*
from weight_update_func import*

def Introduced():

    trainingNum=0
    databases = [[],[],[],[]]
    inputs_db = database_control("import","inputs") # only current training set needed
    for i in range(len(inputs_db)):
        if inputs_db[i][-2] == trainingNum:
            databases[0].append(inputs_db[i])
    databases[1] = database_control("import","hidden_neurons")
    databases[2] = database_control("import","weights")
    databases[3] = database_control("import","outputs")
    print(databases[0])
    print(databases[1])
    print(databases[2])
    print(databases[3])

    for setNum in range(trainingNum):
        for i in range(len(inputs_db)):
            if inputs_db[i][-2] == setNum:
                databases[0].append(inputs_db[i])
        databases = calculate_output(databases[0],databases[1],databases[2],databases[3])  # i,hn,w,o

    db_types = ["hidden_neurons","weights","outputs"]
    print(databases[0])
    print(databases[1])
    print(databases[2])
    print(databases[3])
    #for item in range(len(db_types)-1):
        #database_control("export",db_types[item+1],database=databases[item])

    '''
        weights_db = database_control("import","weights")
        inputs_db = database_control("import","inputs")
        hns_db = database_control("import","hidden_neurons")
        output_db = database_control("import","outputs")
        databases = calculate_output(inputs_db, weights_db, hns_db, output_db)  # hn,w,o
        for i in range(3):
              newdatabases = calculate_output(inputs_db, weights_db, hns_db, output_db)
    '''