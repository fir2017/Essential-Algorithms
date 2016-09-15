class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


    def FindLargestCell(top):
        if top.next == None:
            return None
        top = top.next
        best_cell = top
        best_value = best_cell.value
        top = top.next
        while top != None:
            if top.value > best_value:
                best_cell = top
                best_value = top.value
            top = top.next
        return best_cell

    def FindCell(top, target):
        while top != None:
            # print top.value
            if top.value == target:
                return top
            top = top.next
        return None

    def FindCellBefore(top, target):
        if top == None:
            return None
        while top.next != None:
            if top.next.value == target:
                return top
            top = top.next
        return None

mynode1 = Node("first")
mynode2 = Node("second")
mynode3 = Node("third")
new_cell = Node("new")


mynode1.next = mynode2
mynode2.next = mynode3
list_ = [3,4,5,1,88,4]

print Node.FindLargestCell(mynode1)
