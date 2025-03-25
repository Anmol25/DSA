class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Queue:
    def __init__(self):
        self.frontnode = None
        self.lastnode = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def front(self):
        if self.is_empty():
            print("Queue Empty")
            return -1
        return self.frontnode.data

    def enqueue(self, item: int):
        if self.is_empty():
            self.frontnode = Node(item)
            self.lastnode = self.frontnode
        else:
            self.lastnode.next = Node(item)
            self.lastnode = self.lastnode.next
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            print("Queue empty")
            return -1
        self.frontnode = self.frontnode.next
        self.size -= 1
        if self.frontnode is None:
            self.lastnode = None
    


def main():
    temp1 = Queue()
    temp1.dequeue()
    temp1.enqueue(1)
    temp1.enqueue(2)
    temp1.enqueue(3)
    temp1.enqueue(4)
    print(temp1.front())
    temp1.dequeue()
    print(temp1.front())
    temp1.dequeue()
    print(temp1.front())
    temp1.dequeue()
    print(temp1.front())
    temp1.dequeue()
    print(temp1.front())
    

if __name__ == "__main__":
    print("hello")
    main()



