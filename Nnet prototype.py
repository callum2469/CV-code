import math
import random

class neuron():
    nextNum = 0
    def __init__(self,layer,net):
        self.num = neuron.nextNum
        neuron.nextNum += 1
        self.bias = random.randint(0,10)
        self.net = net
        self.layer = layer
        self.connections = []
        self.activation = random.random()
        if self.layer == 0:
            pass
        else:
            self.connections = [i.num for i in self.net if i.layer == self.layer-1]
            self.temp = []
            for i in self.connections: self.temp.append([i,random.randint(0,10)])
            self.connections = self.temp

    def calculate_activation(self):
        if self.layer == 0:
            pass
        else:
            self.activation = 0
            for i in self.connections: self.activation += i[1] * self.net[i[0]].activation
            self.activation -= self.bias
            self.activation = self.sigmoid(self.activation)

    def sigmoid(self,x):
        if x >= 0:
            z = math.exp(-x)
            return 1 / (1 + z)
        else:
            z = math.exp(x)
            return z / (1 + z)
        
    def __str__(self):
        st = "neuron: " + str(self.num) + " layer: " + str(self.layer) + " bias: " + str(self.bias) +" activation: " + str(self.activation) + " connections: "
        if self.connections == []:
            st += "null"
        else:
            for i in self.connections: st += str(i) + " "
        return(st)

class neural_net():
    def __init__(self,inputs,outputs,layers,layerSize):
        self.inputs = inputs
        self.outputs = outputs
        self.layers = layers
        self.layerSize = layerSize
        self.net = []
        for i in range(0,inputs):self.net.append(neuron(0,self.net))
        for i in range(0,layers):
            for o in range(0,layerSize): self.net.append(neuron(i+1,self.net))
        for i in range(0,outputs):self.net.append(neuron(layers+1,self.net))

    def calculate_outputs(self):
        for i in self.net: i.calculate_activation()
        self.temp = self.net[-self.outputs:]
        self.temp2 = []
        for i in self.temp:
            self.temp2.append(i.activation)
        return(self.temp2)
        
    def input_values(self,inputValues):
        for i in range(0,self.inputs):
            self.net[i].activation = inputValues[i]

    def __str__(self):
        st = ""
        for i in self.net: st += str(i) + "\n"
        return(st)

net1 = neural_net(2,2,2,2)
print(net1)
net1.input_values([3,7])
print(net1)
print(net1.calculate_outputs())
print(net1)
    
