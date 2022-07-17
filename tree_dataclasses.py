'''
tree_dataclasses.py
Description:
A module to define Python dataclasses
Author:
    Brandon Niles (180946050)
Purpose:
    To provide useful dataclasses for the purposes of generating decision trees
Instructions:
    Import where needed
'''

#DataClasses

'''
LeafNode
Dataclass representation of a leaf node.
Stores a reference to the count of each label in a particular set of values
Attributes:
    value -> string: Label (True or False)
Methods:
    __init__(values): Constructor
'''

class LeafNode():
    def __init__(self, value):
        self.value = value


'''
InternalNode
Dataclass representation of an internal node (decision node).
Stores a reference to both true and false branches, as well as other data
Attributes:
    index -> int: index of column
    threshold -> float: splitting value
    information -> float: information gain
    true_branch -> LeafNode or InternalNode: right child
    false_branch -> LeafNode or InternalNode: left child
Methods:
    __init__(values): Constructor
'''
class InternalNode():
    def __init__(self, index, threshold, information, true_branch, false_branch):
        self.index = index
        self.threshold = threshold
        self.gain = information
        self.right = true_branch
        self.left = false_branch

'''
DecisionTree
Dataclass representation of a decision tree.
Attributes:
Methods:
    __init__(min_split, max_depth): Constructor
'''
class DecisionTree():
    def __init__(self):
        self.root = None

'''
Split
Dataclass representation of a given split
Attributes:
    info_gain -> float: information gain from split
    right -> Node: right child
    left -> Node: left child
    column_index -> int: index of column to be split
    threshold -> float: splitting point
Methods:
    __init__(self, info_gain, right, left, column_index, threshold): Constructor
'''
class Split():
    def __init__(self, info_gain=0, right=None, left=None, column_index=None, threshold=None):
        self.info_gain = info_gain
        self.right = right
        self.left = left
        self.column_index = column_index
        self.threshold = threshold