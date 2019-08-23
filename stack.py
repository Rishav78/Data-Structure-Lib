class Stack:
    class Node:
        def __init__(self, data, prev = None, next = None):
            self.__prev = prev
            self.__next = next
            self.__data = data

        def setNext(self, next):
            self.__next = next

        def getData(self):
            return self.__data
        
        def getPrev(self):
            return self.__prev
        
        def getNext(self):
            self.__next

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def size(self):
        return self.__size

    def push(self, element):
        n = Stack.Node(element, self.__tail)
        self.__size = self.__size + 1
        if self.__head == None:
            self.__head = n
        else:
            self.__tail.setNext(n)
        self.__tail = n
    
    def pop(self):
        if self.__size == 0:
            return None
        else:
            current = self.__tail.getData()
            prev = self.__tail.getPrev()
            prev and prev.setNext(None)
            self.__tail = prev
            self.__size = self.__size - 1
            return current
            
    def __str__(self):
        a = self.__head
        string = ''
        while a:
            string = string + str(a.getData())
            a = a.getNext()
        return string;
    # def __str__(self):
    #     string = '['
    #     while not self.isEmpty():
    #         string = string + str(self.pop())
    #         if self.size() > 0:
    #             string = string + ', '
    #     return (string + ']')
            

    def isEmpty(self):
        return self.__size == 0