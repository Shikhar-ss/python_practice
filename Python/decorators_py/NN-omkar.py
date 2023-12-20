import numpy as np


class Neuron:
    
    def __init__(self,input_value1,input_value2):
        self.input_value1 = input_value1
        self.input_value2 = input_value2
        self.lam = 0.8
        W = np.random.randn()
        b = np.ones([1])
        
        
    def V_fun(self,W,b):
        V1 = self.input_value1*W + self.input_value2*W+b
        V2 = self.input_value1*W + self.input_value2*W+b
        V3 = self.input_value1*W + self.input_value2*W+b
        V4 = self.input_value1*W + self.input_value2*W+b
        return V1,V2,V3,V4
    
    def sigmoid(x):
            return 1 /(1 + np.exp(-x))
                    
                    
nn = Neuron()


h1 = nn.sigmoid(V_fun) 
h2 = sigmoid(V2)
h3 = sigmoid(V3)
h4 = sigmoid(V4)

print()    

        