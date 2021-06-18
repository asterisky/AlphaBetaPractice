# *****  Author: Katie Pizziketti, 6.17.21 *****
# Generate a basic tree with random values to practice alpha-beta pruning concepts.
# ***** Acknowledgements *****
# Thank you to Nicole Chiou for significant contributions to this program.

import math
import random

class Node(object):

    def __init__(self, value):
        self.value = value
        self.alpha = -(math.inf)
        self.beta = math.inf

class Tree(Node):

    def __init__(self):
        root = Node(None)
        lChild = Node(None)
        mChild = Node(None)
        rChild = Node(None)
        lGChild1 = Node(random.randint(1, 50))
        lGChild2 = Node(random.randint(1, 50))
        lGChild3 = Node(random.randint(1, 50))
        mGChild1 = Node(random.randint(1, 50))
        mGChild2 = Node(random.randint(1, 50))
        mGChild3 = Node(random.randint(1, 50))
        rGChild1 = Node(random.randint(1, 50))
        rGChild2 = Node(random.randint(1, 50))
        rGChild3 = Node(random.randint(1, 50))

        self.tree = {'r': root, 'lC': lChild, 'mC': mChild, 'rC': rChild, 'lGC1': lGChild1, 'lGC2': lGChild2, 'lGC3': lGChild3, 'mGC1':mGChild1,
            'mGC2': mGChild2, 'mGC3': mGChild3, 'rGC1': rGChild1, 'rGC2':rGChild2, 'rGC3': rGChild3}

#prints a visual representation of a 3-ply tree
def print_t(Tree):
    print('\n\n\n')
    print("                                   ", "A:", Tree.tree['r'].alpha, "B:", Tree.tree['r'].beta, "          \n")
    print("     ", "A:", Tree.tree['lC'].alpha, "B:", Tree.tree['lC'].beta,   "                  ", "A:", Tree.tree['mC'].alpha,
    "B:", Tree.tree['mC'].beta, "                              ",  "A:", Tree.tree['rC'].alpha, "B:", Tree.tree['rC'].beta, "     \n")
    print(Tree.tree['lGC1'].value, "  ", Tree.tree['lGC2'].value, "   ", Tree.tree['lGC3'].value, "                       ", Tree.tree['mGC1'].value, "   ",
     Tree.tree['mGC2'].value, "   ", Tree.tree['mGC3'].value, "                     ", Tree.tree['rGC1'].value, "   ", Tree.tree['rGC2'].value, "   ", Tree.tree['rGC3'].value)

#propagate the alpha-beta values through the tree
def solve(Tree):
    #left grandchild alpha-beta
    Tree.tree['lC'].beta = min([Tree.tree['lGC1'].value, Tree.tree['lGC2'].value, Tree.tree['lGC3'].value])
    Tree.tree['lC'].alpha = min([Tree.tree['lGC1'].value, Tree.tree['lGC2'].value, Tree.tree['lGC3'].value])

    #prune middle grandchildren
    if(Tree.tree['mGC1'].value < Tree.tree['lC'].alpha):
        Tree.tree['mGC2'].value = 'P'
        Tree.tree['mGC3'].value = 'P'
    if(Tree.tree['mGC2'].value != 'P'):
        if (Tree.tree['mGC2'].value < Tree.tree['lC'].alpha):
            Tree.tree['mGC3'].value = 'P'
    #middle grandchild alpha-beta
    mGCValues = [v for v in [Tree.tree['mGC1'].value, Tree.tree['mGC2'].value, Tree.tree['mGC3'].value] if v != 'P']
    Tree.tree['mC'].beta = min(mGCValues)
    Tree.tree['mC'].alpha = min(mGCValues)
    
    #prune right grandchildren
    if (Tree.tree['rGC1'].value < Tree.tree['lC'].alpha) or (Tree.tree['rGC1'].value < Tree.tree['mC'].alpha):
        Tree.tree['rGC2'].value = 'P'
        Tree.tree['rGC3'].value = 'P'
    if(Tree.tree['rGC2'].value != 'P'): 
        if ((Tree.tree['rGC2'].value < Tree.tree['lC'].alpha) or (Tree.tree['rGC2'].value < Tree.tree['mC'].alpha)):
            Tree.tree['rGC3'].value = 'P'
    #right grandchild alpha-beta
    rGCValues = [v for v in [Tree.tree['rGC1'].value, Tree.tree['rGC2'].value, Tree.tree['rGC3'].value] if v != 'P']
    Tree.tree['rC'].beta = min(rGCValues)
    Tree.tree['rC'].alpha = min(rGCValues)

    #root alpha-beta
    Tree.tree['r'].alpha = max([Tree.tree['lC'].beta, Tree.tree['mC'].beta, Tree.tree['rC'].beta])
    Tree.tree['r'].beta = Tree.tree['r'].alpha

t = Tree()
print_t(t)
solve(t)
print("\nHit enter when ready for answer.")
input()
print_t(t)


