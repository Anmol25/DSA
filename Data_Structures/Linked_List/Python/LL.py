class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item):
        if (self.head == None):
            temp = Node(item)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(item)
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    def insert(self, num: int, place: int):
        # If LinkedList is empty
        if self.head == None:
            self.append(num)
        else:
            temp = Node(num)
            # At Head
            if place == 0:
                temp.next = self.head
                self.head = temp
            # At Tail
            elif place == self.size:
                self.tail.next = temp
                self.tail = temp
            # Middle
            else:
                front = self.head
                back = self.head.next
                for i in range(0, place-1):
                    front = front.next
                    back = back.next
                temp.next = back
                front.next = temp
            self.size += 1

    def delete(self, place: int):
        if self.head == None:
            print("LinkedList is Empty")
        elif (place < 0 or place >= self.size):
            print("List Index Out of Bounds")
        else:
            # Delete Head
            if place == 0:
                self.head = self.head.next
            elif place == self.size-1:
                front = self.head
                back = self.head.next
                while (back != self.tail):
                    front = front.next
                    back = back.next
                front.next = None
            else:
                count = 1
                front = self.head
                todelete = self.head.next
                while (count != place):
                    front = front.next
                    todelete = todelete.next
                    count += 1
                # Delete
                front.next = todelete.next
                todelete.next = None
            self.size -= 1

    def search(self, num):
        count = 0
        temp = self.head
        while (temp.data != num):
            if temp.next == None:
                count = -1
                return count
            temp = temp.next
            count += 1
        return count

    def __len__(self):
        return self.size

    def __str__(self):
        temp = self.head
        string = ""
        while temp != None:
            string += f"{temp.data}->"
            temp = temp.next
        string += "None"
        return string


def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print(ll)
    print(len(ll))

    ll.insert(20, 5)
    print(ll)
    print(len(ll))

    ll.delete(4)
    print(ll)
    print(len(ll))

    print("Location of 3:", ll.search(3))


if __name__ == "__main__":
    main()
