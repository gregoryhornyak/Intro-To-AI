def importAnything(data_type=str):
    if not isinstance(data_type,str):
        raise Exception("Argument is not string")
    filename = data_type + ".txt"
    try:
        file01 = open(filename, "r")
    except:
        raise FileNotFoundError
    output_db = []
    line_count = 0
    for line in file01:
        if line != "\n":
            line_count += 1
    file01.close()
    file01 = open(filename, "r")
    for item in range(line_count):
        output_db.append(file01.readline().strip("\n"))  # .split(","))
    file01.close()
    return output_db

def exportAnything(database=list, data_type=str):
    if not isinstance(data_type,str):
        raise Exception("Argument is not string")
    if data_type[-1] != "s":
        #print("You probably missed an 's' from the end")
        data_type += "s"
    data_type = data_type + ".txt"
    file01 = open(data_type, "w")
    for i in range(len(database)):
        temp_list = map(str, database[i])
        line = ",".join(temp_list)
        file01.write(line +"\n")
    file01.close()
