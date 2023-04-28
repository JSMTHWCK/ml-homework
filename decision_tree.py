import random as rng
import math

class Node:
    def __init__(self,id,data_points):
        self.id = id #int
        self.data_points = data_points #array of arrays
        self.split_value = None
        self.left_split = None #id
        self.right_split = None #id 

                    
class Tree:
    def __init__(self):
        self.nodes_by_id = {}

    def sort_data(self,data,axis):
        for a in range (0,len(data)):
            for i in range(1,len(data)):
                if data[i][axis] < data[i - 1][axis]:
                    data[i],data[i - 1] = data[i - 1],data[i]
        return (data)
    def calc_splitpoints(self,points,axis):
        split_points = []
        sorted_points = self.sort_data(points,axis)
        for i in range(0,len(sorted_points)-1):
            if sorted_points[i][axis] != sorted_points[i+1][axis]:
                split = sorted_points[i][axis] + (sorted_points[i+1][axis] - sorted_points[i][axis])/2
                split = round(split,3)
                split_points.append(split)
        return list(set(split_points))

    def gini(self,purity):
        return 1 - purity ** 2 - (1 - purity)**2
    def purity(self,data,object):
        purity = 0
        for point in data:
            if point[0] == object:
                purity += 1
        return purity / len(data)

    def split_data(self,data,best_splitpoint):
        left_split = []
        right_split = []
        axis = best_splitpoint[1]
        splitpoint = best_splitpoint[0]
        for point in data:
            if point[axis + 1] < splitpoint:
                left_split.append(point)
            else:
                right_split.append(point)
        return left_split,right_split
    
    def find_bestsplitpoint(self,data,splitpoints):
        G = []
        for axis in range(0,len(splitpoints)):
            for split in splitpoints[axis]:
                left_split,right_split = self.split_data(data,[split,axis])
                purity_point = data[0][0]
                G_before = self.gini(self.purity(data,purity_point))
                left_purity = self.purity(left_split,purity_point)
                G_after_left = len(left_split)/len(data) * self.gini(left_purity)
                right_purity = self.purity(right_split,purity_point)
                G_after_right = len(right_split)/len(data) * self.gini(right_purity)
                G_after = G_after_left + G_after_right
                G.append(G_before - G_after)
        max_g = max(G)
        max_g_index = G.index(max_g)
        #max g index is like 4th point is blank
        i = 0
        while True:
            if len(splitpoints[i]) > max_g_index:
                return [splitpoints[i][max_g_index],i]
            else:
                max_g_index -= len(splitpoints[i])
                i += 1
                
    def most_frequent(self,data):
        types = []
        scores = []
        types_with_location = []
        for i in range(0,len(data)):
            if data[i] in types:
                scores += 1
            else:
                scores.append(1)
                types_with_location.append([i,data[i]])
        max_score = scores.index(max(scores))
        return types_with_location[max_score][1]

    def fit(self,data, min_size = 2, remaining_depth = 10,node = 0):
        if self.purity(data,data[0][0]) < 1 and remaining_depth > 0 and len(data) >= min_size:
            splitpoints = []
            for i in range(1,len(data[0])):
                splitpoints.append(self.calc_splitpoints(data,i))
            best_splitpoint = self.find_bestsplitpoint(data,splitpoints)
            left_split,right_split = self.split_data(data,best_splitpoint)

            last_node = len(self.nodes_by_id)

            if node == 0:
                self.nodes_by_id[0] = Node(0,data)
            self.nodes_by_id[node].split_value = best_splitpoint
            self.nodes_by_id[node].left_split = last_node + 1
            self.nodes_by_id[node].right_split = last_node + 2
            self.nodes_by_id[last_node + 1] = Node(last_node + 1, left_split)
            self.nodes_by_id[last_node + 2] = Node(last_node + 2, right_split)
            current_depth = remaining_depth
            self.fit(left_split,min_size, current_depth - 1, last_node + 1)
            self.fit(right_split,min_size, current_depth - 1, last_node + 2)
        #create self.nodes_by_id_system here
        if len(self.nodes_by_id) == 0:
            self.nodes_by_id[0] = Node(0,data)

    def fit_forest(self,data,forest_size,min_size = 2,max_depth = 10):
        forest = []
        for i in range(forest_size):
            sub_data = []
            for i in range(math.ceil(len(data) * 0.8)):
                sub_data.append(data[rng.randint(0,len(data) - 1)])
            self.nodes_by_id = {}
            self.fit(sub_data,min_size,max_depth,0)
            forest.append(self.nodes_by_id)
        self.forests = forest
 
    def find_highest(self,data):
        types = [] #array of arrays [0,"shortbread"]
        types_w_location = []
        populations = []
        for i in range(len(data)):
            if data[i][0] in types:
                populations[types.index(data[i][0])] += 1
            else:
                types_w_location.append([i,data[i][0]])
                types.append(data[i][0])
                populations.append(0)
                populations[types.index(data[i][0])] += 1
        greatest_field = populations.index(max(populations))
        type_of_field = types_w_location[greatest_field]
        return type_of_field


    def predict(self,data_point,forest = False,forest_data = None):
        if forest != False:
            self.nodes_by_id = forest_data
        tree_top = self.nodes_by_id[0]
        current_node = tree_top
        while True:
            if current_node.left_split == None:
                #just grabbing the first point as all are the same
                current_data = current_node.data_points
                type_of_field = self.find_highest(current_data)
                return type_of_field[1]
            else:
                axis = current_node.split_value[1] + 1
                value = current_node.split_value[0]
                if data_point[axis] < value:
                    current_node = self.nodes_by_id[current_node.left_split]
                else:
                    current_node = self.nodes_by_id[current_node.right_split]    
    def predict_forest(self,data_point):
        general_votes = []
        for tree in self.forests:
            general_votes.append(self.predict(data_point,True,tree))
        winner = self.most_frequent(general_votes)
        return winner

class Tests:
    def __init__(self,tree,data):
        self.tree = tree
        self.data = data
    def loocv(self, min_split,max_depth):
        data = self.data
        accuracy = 0
        for index_left_out in range(0,len(data)):
            modified_data = list(data)
            del modified_data[index_left_out]
            self.tree.nodes_by_id = {}
            self.tree.fit(modified_data,min_split,max_depth)
            if self.tree.predict(data[index_left_out]) == data[index_left_out][0]:
                accuracy += 1
        return accuracy/len(data)

    def min_split_tests(self):
        sizes = [i for i in range(0,11)]
        results = []
        for size in sizes:
            results.append(self.loocv(size,10))
        return results
            
            
    def max_depth_test(self):
        depth_sizes = [i for i in range(1,10)]
        results = []
        for depth in depth_sizes:
            results.append(self.loocv(1,depth))
        return results
        

    def loocv_forest(self,min_split,max_depth):
        tree_sizes = [i for i in range(0,4)]
        results = []
        for size in tree_sizes:
            data = self.data
            accuracy = 0
            for index_left_out in range(0,len(data)):
                modified_data = list(data)
                del modified_data[index_left_out]
                self.tree.nodes_by_id = {}
                self.tree.fit_forest(modified_data,10 ** size,min_split,max_depth)
                if self.tree.predict_forest(data[index_left_out]) == data[index_left_out][0]:
                    accuracy += 1
            results.append(accuracy/len(data))
        return results






data = [
    ["Shortbread",0.15,0.2],
    ["Shortbread",0.15,0.3],
    ["Shortbread",0.2,0.25],
    ["Shortbread",0.25,0.4],
    ["Shortbread",0.3,0.35],
    ["Sugar",0.05,0.25],
    ["Sugar",0.05,0.35],
    ["Sugar",0.1,0.3],
    ["Sugar",0.15,0.4],
    ["Sugar",0.25,0.35]
]
a = Tree()

test = Tests(a,data)
print(test.max_depth_test())

 