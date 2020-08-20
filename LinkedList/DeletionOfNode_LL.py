class Node:
  def __init__(self,data):
    self.data = data    
    self.next = None

def deleteStart_Node(head):
  if(head==None):
    return
  if(head.next==Node):
    head = None
    return
  head = head.next
  return head


def deleteMed_Node(head, targetNode):
  cur = head
  while(cur.next.data!=targetNode.data):
    cur = cur.next
  cur.next = cur.next.next
  return head

def deleteEnd_Node(head):
  cur = head
  while(cur.next.next!=None):
    cur = cur.next
  print("Node = ",cur.data)
  cur.next = cur.next.next
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
print("*"*18)
head = deleteStart_Node(head)
printList(head)

print("*"*18)

head = deleteMed_Node(head, nodeE)
printList(head)

print("*"*18)

head = deleteEnd_Node(head)
printList(head)
