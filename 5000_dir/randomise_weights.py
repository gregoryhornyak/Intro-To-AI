import random

def randomise_weights(weights=list):
    output_database = []
    #temp_line = []
    for w in range(len(weights)):
        weights[w][-1] = str(random.uniform(-1, 1))
    return weights