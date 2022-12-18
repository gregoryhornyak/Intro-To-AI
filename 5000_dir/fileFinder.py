import glob, os


def FileFinder(file_to_find):
    file_exists = False
    filename = file_to_find + ".txt"
    # searches if a file exists already
    for file in glob.glob("*.txt"):
        if file == filename or file == filename.capitalize():
            file_exists = True
            break

    return file_exists