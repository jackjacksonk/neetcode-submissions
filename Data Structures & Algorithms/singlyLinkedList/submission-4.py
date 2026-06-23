class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        current_index = 0
        while current:
            if current_index == index:
                return current.val
            current = current.next 
            current_index += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:

        current = self.head
        current_index = 0
        while current_index < index and current:
            current_index += 1
            current = current.next

        if current and current.next:
            if self.tail == current.next:
                self.tail = current
            current.next = current.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        result = []
        while current:
            result.append(current.val)
            current = current.next
        return result
