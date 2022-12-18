from neuron_methods import Neuron_from_list

class Neuron:
    def __init__(self, inList):
        # pushes the datas through a neuron

        self.neuron01 = Neuron_from_list(inList)
        self.neuron01.sumUp()

    def ret(self):

        return self.neuron01.sigmoid()
        #return self.neuron01.step(1.6)

    def __del__(self):
        pass
