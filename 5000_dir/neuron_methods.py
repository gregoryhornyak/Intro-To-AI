
class Neuron_from_list:

    # arguments are lists: inputs and weights, plus 0 if sigmoid act. func. or 1 if step act. func.
    # step 1: input call in
    def __init__(self, input_list):
        self.inputs_list = input_list
        self.summ=0
        self.output=0.0

    # step 2: sum up input
    def sumUp(self):
        self.summ = 0
        for i in range(len(self.inputs_list)):
            self.summ += float(self.inputs_list[i])


    # step 3a: use sigmoid act. func.
    #def sigmoid(self, x):
    def sigmoid(self):
        e = 2.7182
        return 1/ ( 1 + e**( -1*(2*self.summ) ) )

    # step 3b: use step act. func.
    def step(self, threshold):
        if self.summ >= threshold:
            return 1
        else:
            return 0

    # step 4: return output
    def printOutput(self):
        return self.summ


# end of neuron_list class