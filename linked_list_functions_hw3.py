# Question 2
def FindLargestCell(top):
    if top.next == None:
        return None
    top = top.next
    best_cell = top
    best_value = best_cell.value
    top = top.next
    while top != None:
        if top.Value > best_value:
            best_cell = top
            best_value = top.value
        top = top.next
    return best_cell
# Question 3
def AddAtBeginning(top, new_cell):
    new_cell.next = top.next
    top.next = new_cell
    new_cell.next.prev = new_cell
    new_cell.prev = top

# Question 4
def AddAtEnd(bottom, new_cell):
    new_cell.prev = bottom.prev
    bottom.prev = new_cell
    new_cell.prev.next = new_cell
    new_cell.next = bottom
# Question 5
# singly list
def InsertCell(after_me, new_cell):
    new_cell.next = after_me.next
    after_me.next = new_cell

def AddAtBeginning(top, new_cell):
    InsertCell(top, new_cell)
def AddAtEnd(bottom, new_cell):
    InsertCell(bottom.prev, new_cell)
# Question 6
def DeleteCell(target_cell):
    target_cell.next.prev = target_cell.prev
    target_cell.prev.next = target_cell.next


# Question 7
# It depends according what the doubly list is sorted.
# Once we know the sort pattern, we can manage our search to
# start at the bottom sentinel. However, that would not change
# the BIG O run time, but could affect the coefficient of BIG O.


# Question 8
# doubly list
def InsertCell(top, new_cell):
    while top.next.value < new_cell.value:
        top = top.next
    new_cell.next = top.next
    top.next = new_cell
    new_cell.next.prev = new_cell
    new_cell.prev = top

# Question 9
def IsSorted(sentinel):
    if sentinel.next == None:
        return True
    if sentinel.next.next == None:
        return True
    sentinel = sentinel.next
    while sentinel.next != None:
        if sentinel.value > sentinel.next.value:
            return False
        sentinel = sentinel.next
    return True

# Question 10
# Selection sort takes longer because it has to search the whole list,
# and the insertion sort does not have to search the whole time always,
# it actually depends on the value it searches.
