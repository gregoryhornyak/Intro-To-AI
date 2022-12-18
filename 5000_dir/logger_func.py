from useful_functions import*

def logger(message):
    try:
        file01 = open("logs.txt", "a")
    except:
        file01 = open("logs.txt", "w")

    file01.write(str(LineCounter("logs.txt")) +" "+ message)
    file01.close()