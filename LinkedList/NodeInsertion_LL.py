class Node:
  def __init__(self,data):
    self.data = data    
    self.next = None 

def insertNodeBeg(head, newNode):
  newNode.next = head
  head = newNode
  return head

def insertmiddle(head, targetNode, newNode):
  cur = head
  while(cur.data != targetNode.data):
    cur = cur.next
  newNode.next = cur.next 
  cur.next = newNode
  return head

def insertEnd(head, newNode):
  cur = head
  while(cur.next !=None):
    cur = cur.next
  newNode.next = None
  cur.next = newNode 
  return head

def printList(head):
    temp = head
    while (temp):
        print(temp.data)
        temp = temp.next

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

printList(head)

head = insertNodeBeg(head, Node('z'))

print("***List after inserting z(In the Beg)***")

printList(head)

print("***List after inserting p(In the middle)***")

head = insertmiddle(head, nodeD, Node('p'))
printList(head)


print("***List after inserting M(In the end)***")

head = insertEnd(head, Node('m'))
printList(head)