def exportAny(db,filename):
    file01 = open(str(filename+".txt"),"w")
    for i in range(len(db)):
        temp_list = ",".join(db[i])
        temp_list = ",".join(map(str, db[i]))
        file01.write(temp_list +"\n")
    file01.close()

myList = [ ["w,0,0,0,0.56"],["w,0,2,5,0.056"],["w,1,0,8,0.998"],["w,1,2,0,0.8989"] ]
exportAny(myList,"weights")

def importAny(filename):
    file01 = open(str(filename+".txt"),"r")
    tempdb = []
    for i in range(4):
        tempdb.append(file01.readline().strip("\n").split(","))
    return tempdb

myList02 = []
myList02 = (importAny("weights"))

print(myList02[2])
