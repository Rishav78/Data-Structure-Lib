import queue;

class BinarySearchTree:
    class Node:
        def __init__(self, data, left = None, right = None):
                self.__right = right
                self.__left = left
                self.__data = data

        def getLeft(self):
            return self.__left

        def getRight(self):
            return self.__right

        def getElement(self):
            return self.__data

        def setLeft(self, left):
            self.__left = left
        
        def setRight(self, right):
            self.__right = right
        
        def setElement(self, data):
            self.__data = data
        

    def __init__(self):
        self.__root = None
        
    def insert(self, value):
        node = BinarySearchTree.Node(value)
        if self.__root == None:
            self.__root = node
        else:
            root = self.__root
            while True:
                if(root.getElement() > value):
                    if not root.getRight():
                        root.setRight(node)
                        break
                    else:
                        root = root.getRight()
                else:
                    if not root.getLeft():
                        root.setLeft(node)
                        break
                    else:
                        root = root.getLeft()
    @staticmethod
    def __print(root, size=0):
        if not root:
            return size
        else:
            print(root.getElement())
            s = BinarySearchTree.__print(root.getLeft(), size+1)
            return BinarySearchTree.__print(root.getRight(), s)

    def __str__(self):
        return "Total Nodes Triverse " + str(BinarySearchTree.__print(self.__root))
    
    def LevelOrderTriversing(self, value):
        if self.__root == None:
            return None
        nodeQueue = queue.Queue()
        nodeQueue.push(self.__root);
        while not nodeQueue.isEmpty():
            q = nodeQueue.pop()
            print(q.getElement())
            if(q.getElement() == value):
                return True
            left = q.getLeft()
            right = q.getRight()
            left and nodeQueue.push(left)
            right and nodeQueue.push(right)
        return False

    # @staticmethod
    # def isBinarySearchTree(root):
    #     if root.get

    @staticmethod
    def __preorder(root):
        if not root:
            return
        print(root.getElement())
        BinarySearchTree.__preorder(root.getLeft())
        BinarySearchTree.__preorder(root.getRight())
    
    @staticmethod
    def __inorder(root):
        if not root:
            print(root.getElement())
            return
        BinarySearchTree.__preorder(root.getLeft())
        BinarySearchTree.__preorder(root.getRight())

    @staticmethod
    def __postorder(root):
        if not root:
            print(root.getElement())
            return
        BinarySearchTree.__preorder(root.getRight())
        BinarySearchTree.__preorder(root.getLeft())

    def preorder(self):
        BinarySearchTree.__preorder(self.__root)
    
    def inorder(self):
        BinarySearchTree.__inorder(self.__root)
    
    def postorder(self):
        BinarySearchTree.__postorder(self.__root)


    


tree = BinarySearchTree()
string = input('Enter number seprated by space: ').split()
for i in string:
    tree.insert(int(i))

# find = int(input('Enter number to be found: '))

# print(tree.LevelOrderTriversing(find))

tree.inorder()