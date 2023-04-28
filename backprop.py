import numpy as np
class NeuralNetwork:
    def __init__(self,points,weights,bias):
        self.outputs_by_layer = []
        self.sigma_by_layer = []
        self.rss_dh_by_layer = []
        self.rss_da_by_layer = []
        self.rss_db_by_layer = []
        self.points = points
        self.weights = weights
        self.bias = bias


    def sigmoid(self,values):
        sigmoid_values = []
        for value in values:
            sigmoid_values.append(1/((1 + np.e**(-1 * value))))
        return sigmoid_values
    
    def dSigmoid(self,values):
        sigmoid_values = []
        for value in values:
            sigmoid_values.append((np.e ** (-1 * value))/((1 + np.e ** (-1 * value)) ** 2))
        return sigmoid_values
        
    def forwardprop(self):
        self.outputs_by_layer.append([np.array([[0]])])
        self.sigma_by_layer.append([np.array([0])])
        for i in range(len(self.weights)): 
            prod = np.matmul(self.weights[i],self.outputs_by_layer[i])
            self.sigma_by_layer.append(prod + self.bias[i])
            self.outputs_by_layer.append(self.sigmoid(self.sigma_by_layer[-1]))
        print(self.outputs_by_layer[-1])


    def backprop(self):
        self.rss_dh_by_layer.append(2 * (self.outputs_by_layer[-1][0] - 0))
        for i in range(len(self.weights),1,-1):
            transpose = np.asmatrix(self.weights[i - 1]).transpose()
            transpose = np.asarray(transpose)
            product = np.multiply(self.rss_dh_by_layer[0], self.dSigmoid(self.sigma_by_layer[i]))
            self.rss_dh_by_layer.insert(0,np.matmul(transpose, product))
        print(self.rss_dh_by_layer[0])

    def expansion(self):
        for i in range(len(self.sigma_by_layer) - 1):
            #rssdb
            dSigmoid = self.dSigmoid(self.sigma_by_layer[-i - 1])
            self.rss_db_by_layer.append(np.multiply(self.rss_dh_by_layer[-1-i],dSigmoid))
            #rssda
            self.rss_da_by_layer.append(np.outer(self.rss_db_by_layer[-1-i], self.outputs_by_layer[-i-2]))
        print(self.rss_db_by_layer)
        
a = NeuralNetwork(
    #points#
    [
    (0,0), (0.25,1), (0.5,0.5),(0.75,1),(1,0)
    ]
    ,
    #weights#
    [
    np.array([[5],[-5],[5],[-5]])
    ,np.array([[10,10,0,0],[0,0,10,10]])
    ,np.array([10,10])
    ]
    ,
    #bias#
    [
    np.array([[-0.75],[1.75],[-3.25],[4.25]]),
    np.array([[-12.5],[-12.5]]),
    np.array([[-2.5]])
    ])

a.forwardprop()
a.forwardprop()

print('done')