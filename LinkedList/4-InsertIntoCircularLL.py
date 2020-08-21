class Node:
  def __init__(self,data):
    self.data = data    
    self.next = None 

def insertNodeBeg(head, newNode):
    curr = head
    while True:
        curr =curr.next
        if curr.next==head:
            break
    curr.next = newNode
    newNode.next = head
    head = newNode
    return head


def printList(head):
    temp = head
    while True:
        print(temp.data)
        temp = temp.next
        if temp==head:
            break

head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = head

printList(head)
head = insertNodeBeg(head, Node('z'))
print("**************************")
printList(head)