class LinkList:
    class Node:
        def __init__(self, data, next):
            self.__data = data
            self.__next = next

        def getElement(self):
            return self.__data

        def getNext(self):
            return self.__next
        
        def setNext(self, next):
            self.__next = next
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0

    def insertAtBegnning(self, value):
        self.insertInBetween(value, 0);

    def reverse(self):
        current = self.__head
        prev = None
        next = None
        while current:
            next = current.getNext()
            current.setNext(prev)
            prev = current
            current = next
        else:
            self.__head = prev

    def p(self):
        a = self.__head
        while a != None:
            print(a.getElement())
            a = a.getNext()

    def insertAtEnd(self,value):
        self.insertInBetween(value, self.__size)
    
    def size(self):
        return self.__size
       
    def remove(self, value, all = False):
        head = self.__head
        prev = None
        while head:
            if head.getElement() == value:
                self.deleteElement(prev, head)
                if all:
                    return
            prev = head
            head = head.getNext()


    def unLink(self, index):
        if self.size() >= index:
            prev = None
            head = self.__head
            while head.getNext() and index >= 0:
                prev = head
                head = head.getNext()
                index -= 1
            else:
                self.deleteElement(prev, head)
        else:
            print('Out Of Bound')

    def deleteElement(self, prev, current):
        if prev == None:
            self.__head = current.getNext()
        else:
            prev.setNext(current.getNext())

    def insertInBetween(self, value, index):
        if self.__size >= index:
            self.__size += 1
            head = self.__head
            if index == 0:
                node = LinkList.Node(value, head)
                self.__head = node
            else:
                while head.getNext() != None and index > 1 :
                    head = head.getNext()
                    index -= 1
                else:
                    node = LinkList.Node(value, head.getNext())
                    head.setNext(node)
        else:
            print('Out Of Bound')
    
    @staticmethod
    def mergeList(list1, list2):
        head1 = list1.__head
        head2 = list2.__head
        newList = LinkList()
        while head1 and head2:
            value1 = head1.getElement()
            value2 = head2.getElement()
            if value1 < value2:
                newList.insertAtEnd(value1)
                head1 = head1.getNext()
            else:
                newList.insertAtEnd(value2)
                head2 = head2.getNext()
        while head1:
            value1 = head1.getElement()
            newList.insertAtEnd(value1)
            head1 = head1.getNext()
        while head2:
            value2 = head2.getElement()
            newList.insertAtEnd(value2)
            head2 = head2.getNext()

        return newList
