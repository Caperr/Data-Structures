# Binary tree implementation using object composition
# This implementation only supports int node values, but
# could easily be adapted for other datatypes.
# Written by Jasper Law
# ISSUE: tree printing skips nodes! 3, 6 and 7 not printed


# The principle behind this implementation is to store nodes as objects with:
# - The node's value
# - Containers for the nodes to the left and right of that node

# I'm containing my child nodes inside of the parent nodes, which
# gives my tree an inherant structure.
# This means that I don't need to store any other data to track the
# structure of the tree. For example,
# another common implementation is to store the tree in a dictionary.


# Tree container class.
# Contains a reference to the root node, and methods that
# manipulate the entire tree, rather than single nodes.
class Tree():
    # The root of the tree
    root = None

    # Class constructor. Required argument: the desired VALUE of the root.
    def __init__(self, _rootValue):
        # Initialize 
        self.root = Node(None, _rootValue)

    # Add a node to the tree
    # Does this by traversing the tree, essentially performing
    # a search for where the node should be (based on its value),
    # until an empty slot is found.
    def addNode(self, value):
        # Track the current nodes that are being checked
        currentNode = self.root
        currentParent = None
        # Track wether or not the node has been found, already in the tree
        nodeFound = False
        # For once an empty slot has been found.
        # Was it on the left or right of the parent?
        goLeft = False

        # Until an empty node is found...
        while currentNode != None:
            # Check if this node is equal to the one we want to add
            if currentNode.getValue() == value:
                # Stop searching. Trees cannot contain duplicates
                nodeFound = True
                break
            
            # Search the current node's children
            currentParent = currentNode
            # If our node should go on the left of this node,
            # set the next iteration to check the left child
            if currentNode.getValue() < value:
                currentNode = currentNode.right
                goLeft = False
            # If our node should go on the right of this node,
            # set the next iteration to check the right child
            else:
                currentNode = currentNode.left
                goLeft = True

        # The iteration ended. Therefore, either an empty node was found,
        # or our node was found.
        # If our node wasn't found, we must have found an empty slot.
        if not nodeFound:
            # Initialise our new node into the child of our current node
            if goLeft:
                currentParent.left = Node(currentParent, value)
            else:
                currentParent.right = Node(currentParent, value)

    # [to be written]
    # Remove a node from the tree
    def popNode(self,_value):
        pass

    # [to be written]
    # Print out the tree in an easy-to-read way,
    # I.e with each layer on a seperate line, with lines linking
    # the nodes as appropriate.
    # One method could be to use an algorithm similar to getHeight,
    # unwrapping and printing each layer of the tree.
    def printTree(self):
        # This could probably all be done in a single loop. Just add intermediary layers to the matrix for connecting lines.
        treeHeight = self.getHeight() + 1
        if treeHeight % 2 == 0:
            treeHeight += 1
        # Ideally the width (x) of the matrix would be calculated based on the maximum width of the tree
        matrix = [[None for x in range(treeHeight)] for y in range(treeHeight)]
        matrix[0][(treeHeight+1)//2] = self.root
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                # Pretty sure items are getting overwritten here.
                # Need to precalculate the amount of screen space needed for each pair of children
                # and divide the amount of space between the pairs
                # this would make printing difficult though
                if matrix[y][x] != None:
                    if matrix[y][x].left != None:
                        matrix[y+1][x-1] = matrix[y][x].left
                    if matrix[y][x].right != None:
                        matrix[y+1][x+1] = matrix[y][x].right
        
        for y in matrix:
            for x in y:
                if x == None:
                    print(" ",end="")
                else:
                    print(x.value,end="")
            print()
            for x in range(len(y)):
                if x != max(range(len(y))) and y[x+1] != None and y[x+1].left != None:
                    print("/",end="")
                elif y[x-1] != None and y[x-1].right != None:
                    print("\\",end="")
                else:
                    print(" ",end="")
            print()

    # [to be written]
    # Search the tree to check the existance of a node.
    # will probably be done with a similar algorithm to addNode
    def binarySearch(self):
        pass

    # Return the result of an in order traversal, as a list
    def inOrder(self):
        # Start traversing the tree from the root, and return the result
        return self.root.inOrder()

    # Return the result of a pre order traversal, as a list
    def preOrder(self):
        # Start traversing the tree from the root, and return the result
        return self.root.preOrder()

    # Return the result of a post order traversal, as a list
    def postOrder(self):
        # Start traversing the tree from the root, and return the result
        return self.root.postOrder()

    # Return the height of the tree
    # Unwrap the tree layer by layer, counting the layers at each stage
    def getHeight(self):
        # Start at the top of the tree. We already know that the top
        # layer will contain only the root.
        layer = [self.root]
        layersCounter = 0
        # Until the end of the tree has been reached
        while layer != []:
            # we haven't reached the end of the tree yet, so
            # increment the layers counter
            layersCounter += 1
            # A container for the next layer while it is being unwrapped.
            # Clear this container at each iteration
            nextLayer = []
            # for every node in the current layer
            for currentNode in layer:
                # add its children to the next layer
                if currentNode.left != None:
                    nextLayer.append(currentNode.left)
                if currentNode.right != None:
                    nextLayer.append(currentNode.right)
            # Set the next iteration to scan the next layer
            layer = nextLayer
        return layersCounter

    def height(self):
        return self.root.height()
                
        
# The class for a node.
class Node():
    # A REFERENCE to the the parent of this node.
    # NB: This isn't actually used in my code.
    # I just thought i should add it because it could be useful.
    # I could easily modify addNode and/or getHeight to use this efficiently
    parent = None
    # A CONTAINER for the node to the left of this node
    left = None
    # A CONTAINER for the node to the right of this node
    right = None
    # The value of this node
    value = 0

    # Class constructor.
    # Save the node's value and parent reference to attributes
    def __init__(self, _parent, _value):
        self.parent = _parent
        self.value = _value

    # Return the value of the node.
    # I really need to use this more.
    def getValue(self):
        return self.value

    # Return the result of in order traversal as a list,
    # starting from this node.
    # ---
    # This is a recursive algorithm that will mostly start from
    # the root, in the tree class. However, it's the exact same
    # algorithm, so it could just as easily be called from ANY node
    # to return the traversal of this node's subtree.
    # ---
    # One improvement I could make would be to store the three functions
    # in this method (left, visit, and right) as seperate functions.
    # Then, store references to them in a list, and then call those
    # references from the inOrder, preOrder, and postOrder methods in the
    # right order. for that traversal. This would reduce redundancy.
    def inOrder(self):
        # Track the result of the traversal
        result = []
        # Traverse the left subtree first
        if self.left != None:
            result += self.left.inOrder()
        # Then visit this node
        result += [self.value]
        # Then traverse the right subtree
        if self.right != None:
            result += self.right.inOrder()
        # and finally, return the result
        return result

    # Pre-order traversal. See notes for inOrder
    def preOrder(self):
        result = [self.value]
        if self.left != None:
            result += self.left.preOrder()
        if self.right != None:
            result += self.right.preOrder()
        return result

    # Post-order traversal. See notes for inOrder
    def postOrder(self):
        result = []
        if self.left != None:
            result += self.left.postOrder()
        if self.right != None:
            result += self.right.postOrder()
        result += [self.value]
        return result

    # Linear tree height by leaf
    def height(self):
        # if a child doesn't exist, return 0 as that child's height
        if self.left is None:
            if self.right is None:
                return 0
            # if a child does exist, return its height (plus 1 for this node)
            return self.right.height() + 1
        # the same
        if self.right is None:
            return self.left.height() + 1
        # if both children exist, only return the biggest height (plus 1 for this node)
        return max(self.left.height(), self.right.height()) + 1
        

# And that's the implementation!
# Now, let's take a look at an example.

# First, I initialize a tree called "myTree", with the value of the root being 4.
myTree = Tree(4)
# Add some nodes to the tree.
# Yes, I could have done this with a loop.
# I've added the nodes in this order to make the tree layout more interesting.
myTree.addNode(2)
myTree.addNode(8)
myTree.addNode(1)
myTree.addNode(10)
myTree.addNode(5)
myTree.addNode(7)
myTree.addNode(9)
myTree.addNode(3)
myTree.addNode(6)

# Print the traversals of the tree.
# Note that these methods return lists.
print("in order:",myTree.inOrder())
print("pre order:",myTree.preOrder())
print("post order:",myTree.postOrder())

# And finally, this is where you come in...
# Print the tree in a more easily understood way.
#myTree.printTree()
print("height:",myTree.height())
