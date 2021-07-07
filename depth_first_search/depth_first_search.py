# given a node class that has name and an array of children nodes
# implement the depthFirstSearch method which takes in an empty array,
# traverse the tree and return the array which contains all of the nodes' names
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)

        return array

# test:
# {
#   "graph": {
#     "nodes": [
#       {"children": ["B", "C", "D"], "id": "A", "value": "A"},
#       {"children": ["E", "F"], "id": "B", "value": "B"},
#       {"children": [], "id": "C", "value": "C"},
#       {"children": ["G", "H"], "id": "D", "value": "D"},
#       {"children": [], "id": "E", "value": "E"},
#       {"children": ["I", "J"], "id": "F", "value": "F"},
#       {"children": ["K"], "id": "G", "value": "G"},
#       {"children": [], "id": "H", "value": "H"},
#       {"children": [], "id": "I", "value": "I"},
#       {"children": [], "id": "J", "value": "J"},
#       {"children": [], "id": "K", "value": "K"}
#     ],
#     "startNode": "A"
#   }
# }

# Time: O(V + E), we traverse every vertex, so this is the O(V) part, but on top of that, every vertex has E number of edges
# and we call the depthFirstSearch function. Each depthFirstSearch method has a for loop with E iteration, 
# therefore, the time complexity is O(V + E)
# Space: O(V), each node calls depthFirstSearch method, but the method won't be resolved until we resolve all
# the depthFirstSeartch calls from the children node.
# In this case, we are creating V frames on the stack, therefore the space complexity is O(V), where V is the number
# of vertices.
