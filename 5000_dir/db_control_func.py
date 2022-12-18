from import_export import*


def database_control(process, datatype, **arguments):
    db=[]
    newdb =[]
    if arguments.get("database"):
        db = arguments.get("database")
    if process == "import":
        importdb = importAnything(datatype)
        #print(importdb)

        # basic datasets
        if datatype in ["inputs", "outputs", "hidden_neurons", "weights"]:
            # print(importdb)
            for a in range(len(importdb)):
                newdb.append(importdb[a].split(","))
                for b in range(len(newdb[a]) - 2):
                    newdb[a][b + 1] = int(newdb[a][b + 1])
                newdb[a][-1] = float(newdb[a][-1])
            #return (newdb)
        # training dataset
        elif datatype == "training_data":
            for a in range(len(importdb)):
                newdb.append(importdb[a].split(","))
                for b in range(len(newdb[a])):
                    newdb[a][b] = int(newdb[a][b])
            importdb = newdb
            c = ","
            newdb = []
            for rows in range(len(importdb)):
                for cols in range(len(importdb[rows])):
                    newdb.append(["i", 0, (cols), (rows), (importdb[rows][cols])])
            #return (newdb)
        elif datatype == "target_outputs":
            for a in range(len(importdb)):
                importdb[a] = int(importdb[a])
                newdb.append(["top", 99, a, importdb[a]])
        # setting dataset
        elif datatype == "settings":
            # print(importdb)
            for a in range(len(importdb)):
                if "[" in importdb[a] and "[" in importdb[a]:
                    tempdb = []
                    firstHalf = True
                    string_half01 = ""
                    string_half02 = ""
                    for letter in range(len(importdb[a])):
                        if firstHalf == True:
                            if importdb[a][letter] != "[":
                                string_half01 += importdb[a][letter]
                            else:
                                firstHalf = False
                        if firstHalf == False:
                            string_half02 += importdb[a][letter]
                    tempdb = string_half01[:-1].split(",")
                    string_half02 = string_half02.strip("[]").split(",")
                    map_object = map(int, string_half02)
                    list_of_integers = list(map_object)
                    tempdb.append(list_of_integers)
                    # print(list_of_integers)
                    newdb.append(tempdb)
                else:
                    newdb.append(importdb[a].split(","))
                    if len(newdb[a][-1]) == 1:
                        newdb[a][-1] = int(newdb[a][-1])
                    try:
                        if newdb[a][-1][1] == ".":
                            newdb[a][-1] = float(newdb[a][-1])
                    except:
                        pass
        #print(newdb)

        return newdb

    elif process == "export":
        exportAnything(db, datatype)

