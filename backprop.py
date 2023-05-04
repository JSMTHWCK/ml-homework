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

    """ HELPERS FUNCTIONS"""

    def addarrays(self,arr1,arr2):
        arr_sum = []
        for i in range(0,len(arr1)):
            arr_sum.append(np.array(arr1[i]) + np.array(arr2[i]))
        return arr_sum
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
    

    """ ACTUAL FUNCTIONS """
    def forwardprop(self,point):
        outputs_by_layer = [np.array([[point[0]]])]
        sigma_by_layer = [np.array([point[1]])]

        for i in range(len(self.weights)): 
            prod = np.matmul(self.weights[i],outputs_by_layer[i])
            sigma_by_layer.append(prod + self.bias[i])
            outputs_by_layer.append(self.sigmoid(sigma_by_layer[-1]))
        self.outputs_by_layer.append(np.array(outputs_by_layer,dtype=object))
        self.sigma_by_layer.append(np.array(sigma_by_layer,dtype=object))
    def backprop(self):
        index = len(self.outputs_by_layer) - 1
        rss_dh_by_layer = []
        rss_dh_by_layer.append(2 * (self.outputs_by_layer[index][-1][0] - 0))
        for i in range(len(self.weights),1,-1):
            transpose = np.asmatrix(self.weights[i - 1]).transpose()
            transpose = np.asarray(transpose)
            product = np.multiply(rss_dh_by_layer[0], self.dSigmoid(self.sigma_by_layer[index][i]))
            rss_dh_by_layer.insert(0,np.matmul(transpose, product))
        self.rss_dh_by_layer.append(np.array(rss_dh_by_layer))

    def expansion(self):
        rss_da_by_layer = []
        rss_db_by_layer = []
        index = len(self.rss_dh_by_layer) - 1
        for i in range(len(self.sigma_by_layer)):
            #rssdb
            dSigmoid = self.dSigmoid(self.sigma_by_layer[index][-i - 1])
            rss_db_by_layer.append(np.multiply(self.rss_dh_by_layer[index][-i],dSigmoid))
            #rssda
            rss_da_by_layer.append(np.outer(rss_db_by_layer[-1-i], self.outputs_by_layer[index][-i-2]))
        self.rss_da_by_layer.append(rss_da_by_layer)
        self.rss_db_by_layer.append(rss_db_by_layer)
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

for point in a.points:
    a.forwardprop(point)
print(a.sigma_by_layer[0])
print(a.sigma_by_layer[1])
print()
print(a.addarrays(a.sigma_by_layer[0],a.sigma_by_layer[1]))