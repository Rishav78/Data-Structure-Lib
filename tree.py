class Tree:
    class Node:
        def __init__(self, element, left, right):
            self.__element = element
            self.__left = left
            self.__right = right

        def getLeft(self):
            return self.__left

        def getRight(self):
            return self.__right

        def setLeft(self, left):
            self.__left = left

        def setRight(self, right):
            self.__right = right

        def getElement(self):
            return self.__element

    def __init__(self):
        self.__root = None
        self.__size = 0
    
    def getRoot(self):
        return self.__root
    
    @staticmethod
    def __insert(root, value):
        if root.getElement() > value:
            if root.getLeft() == None:
                root.setLeft(Tree.Node(value, None, None))
            else:
                Tree.__insert(root.getLeft(), value)
        else:
            if root.getRight() == None:
                root.setRight(Tree.Node(value, None, None))
            else:
                Tree.__insert(root.getRight(), value)

    def insert(self, value):
        if not self.__root:
            self.__root = Tree.Node(value, None, None)
        else:
            Tree.__insert(self.__root, value)

    @staticmethod
    def __print(root):
        if not root:
            return
        else:
            print(root.getElement())
            Tree.__print(root.getLeft())
            Tree.__print(root.getRight())
    
    @staticmethod
    def __remove(value, prev, root):
        if not root:
            return root
        if root.getElement() > value:
            root.setLeft(Tree.__remove(root.getLeft()))
        elif root.getElement() < value:
            root.setRight(Tree.__remove(root.getRight()))
        else:
            if not root.getLeft() and not root.getRight():
                return None
            elif not root.getLeft():
                return root.getRight()
            elif not root.getRight():
                return root.getLeft()
            else:
                min = Tree.__min(root.getRight())

    @staticmethod
    def __min(root):
        if not root.getLeft():
            return root
        return Tree._min(root.getLeft())

    def remove(self, value):
        pass
        