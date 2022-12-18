from db_control_func import *


def UseSettings(command):
    settingsdb = database_control("import", "settings")

    for i in range(len(settingsdb)):
        if settingsdb[i][1] == command:
            return settingsdb[i][-1]