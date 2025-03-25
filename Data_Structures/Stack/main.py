class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def top(self):
        if(self.is_empty()):
            print("Stack is Empty")
            return -1
        return self.head.data
    
    def push(self,num):
        item = Node(num)
        item.next = self.head
        self.head = item
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return -1
        self.head = self.head.next
        self.size -= 1


def main():
    temp1 = Stack()
    temp1.pop()
    temp1.push(1)
    print(temp1.top())
    temp1.push(2)
    print(temp1.top())
    temp1.push(3)
    print(temp1.top())
    temp1.push(4)
    print(temp1.top())
    temp1.pop()
    print(temp1.top())
    temp1.pop()
    print(temp1.top())
    temp1.pop()
    print(temp1.top())
    temp1.pop()
    print(temp1.top())

if __name__ == "__main__":
    print("hello")
    main()



