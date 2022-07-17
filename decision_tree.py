'''
decision_tree.py
Description:
A module to implement a classfication tree algorithm for data analysis
Author:
    Brandon Niles (180946050)
Purpose:
    To determine a hierarchy of columns for a particular dataset given a classifier
Instructions:
    Import where needed
'''

#Imports

from tree_dataclasses import Split, LeafNode, InternalNode
from data_loading import make_tree_data
import numpy as np
from sklearn.model_selection import train_test_split

#Globals
node_count = 0

#Methods

'''
gini_impurity(node)
Calculates a gini impurity score for an input
Arguments:
    node -> data: node to examine
Returns:
    gini_index -> float: corresponding gini score
'''
def gini_impurity(node):
    possible_labels = np.unique(node) #either true or false

    gini_index = 0
    for label in possible_labels:
        probability = len(node[node == label]) / len(node)
        gini_index = gini_index + (probability * probability)
    gini_index = 1 - gini_index
    return gini_index

'''
information_gain(node, right, left)
Calculates the information gain of a specific node and children
Arguments:
    node -> data: node to examine
    right -> data: right child
    left -> data: left child
Returns:
    information -> float: information gained
'''
def information_gain(node, right, left):
    right_weight = len(right) / len(node) #ratio of child to parent
    left_weight = len(left) / len(node)
    information = gini_impurity(node) - (right_weight * gini_impurity(right)) - \
        (left_weight * gini_impurity(left))

    return information

'''
find_split(data, columns)
Determines the best possible split for a given dataset
Arguments:
    data -> data: current data instance
    columns -> int: current number of columns
Returns:
    best_split -> dict: dictionary representation of the best split
'''
def find_split(data, columns):
    best_split = Split() #create new Split object
    best_info =  -1.0 #pick the split with most information gain
    for column_index in range(columns):
        col_values = data[:, column_index] #fetch entries in a column
        unique_values = np.unique(col_values) #possibly saves time if there are duplicates

        for threshold in unique_values:
            right, left = split_tree(data, threshold, column_index) #try every split to compare
            if(len(left) and len(right)):
                node = data[:, -1]
                right_branch = right[:, -1]
                left_branch = left[:, -1]

                information = information_gain(node, right_branch, left_branch)
                if(information >= best_info): #populate/update split object
                    best_split.info_gain = information
                    best_split.right = right
                    best_split.left = left
                    best_split.column_index = column_index
                    best_split.threshold = threshold
                    best_info = information #new criteria
    return best_split

'''
create_class_tree(data, depth, max_depth)
Recursively creates the classification tree
Arguments:
    data: data: current data instance
    depth -> int: current depth
    max_depth -> int: maximum allowed depth
Returns:
    node -> LeafNode or InternalNode: resultant node object
Outputs:
    Text based on how many times the function has been called
'''
                
def create_class_tree(data, depth, max_depth):
    global node_count
    node_count += 1
    print("Generating node: #{}".format(node_count)) #handy output to keep user aware that the program is functioning
    classes = data[:, -1]

    _, columns = np.shape(data[:, :-1]) #get column size info

    if depth <= max_depth:
        split = find_split(data, columns)
        if(split.info_gain > 0): #otherwise no reason to split
            #recurive calls
            right = create_class_tree(split.right, depth + 1, max_depth)
            left = create_class_tree(split.left, depth + 1, max_depth)
            return InternalNode(split.column_index, split.threshold, split.info_gain, right, left)
    return LeafNode(leaf_label(classes))

'''
split_tree(data, threshold, index)
Splits a dataset into a left and right split based on a comparison value between
the corresponding value at an index and a threshold splitting value
Arguments:
    data -> DataFrame: current data instance
    threshold -> float: splitting value
    index -> int: index of column to conduct the split
Returns:
    right_split -> array: array of items in the right split (greater than or equal to threshold)
    left_split -> array: array of items in the left split (less than threshold)
'''
def split_tree(data, threshold, index):
    right_split = np.array([entry for entry in data if entry[index] >= threshold])
    left_split = np.array([entry for entry in data if entry[index] < threshold])
    return right_split, left_split

'''
leaf_label(leaf)
Determines the label value of a leaf.
Useful for when a leaf may have values of several labels, chooses the label with highest count.
Arguments:
    leaf -> data: leaf data to be examined
Returns:
    label -> string: the determined label of a leaf
'''
def leaf_label(leaf):
    array = list(leaf)
    label = max(array, key = array.count) #label that occurs the most
    return label

'''
train_tree(filename)
Starts the tree training/construction process
Arguments:
    filename -> string: file to be opened
Returns:
    None
Output:
    Information based on status of the process
'''
def train_tree(filename):
    print("Starting tree process on {}".format(filename))
    data = make_tree_data(filename)

    samples = data.iloc[:, :-1].values
    labels = data.iloc[:, -1].values.reshape(-1,1) #labels, convert to a column
    train_samples, _, train_labels, _ = train_test_split(samples, labels, test_size=.2) #not interested in test data

    dataset = np.concatenate((train_samples, train_labels), axis=1) #align into a single matrix, sample column is last column
    root = create_class_tree(dataset, 0, 200) #construct tree and return root

    print("\n\n Resulting Tree: \n")
    print_tree(root, data) #visualize

'''
print_tree(node, data, spacer)
Recursively prints the string representation of the tree
Arguments:
    node -> Node: current node (start with root)
    data -> data: data for referencing column names
    spacer -> string: current space between messages
Returns:
    None
Output:
    Text based on current node
'''
def print_tree(node, data, depth=0):

    spacer = (depth + 1) * "  " #increase spacing for each recursive call to show depth

    print("D:{} ".format(depth), end="") #start by printing depth

    if isinstance(node, LeafNode): #leaf label
        print(node.value)

    else: #internal node, condition
        print("{} >= {} Gain: {}".format(data.columns[node.index], node.threshold, node.gain))
        print("{}left:".format(spacer), end="")
        print_tree(node.left, data,  depth + 1)
        print("{}right:".format(spacer), end="")
        print_tree(node.right, data, depth + 1)
    
