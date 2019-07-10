'''TRAVERSING A SINGLY LINKED LIST'''

class Node(object):
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None
        
        
class SLinkedList(object):              #SLL is actually the head value pointer
    def __init__(self):
        self.headval = None
    
    def printval(self):
        printval = self.headval         #set printval to headval pointer
        while printval != None:
            print (printval.dataval)    #print data from current node
            printval = printval.nextval #set printval to next node using nextval pointer
    
    def atbeginning(self, new_data):
        NewNode = Node(new_data)        #NewNode is a global variable
        NewNode.nextval = self.headval
        self.headval = NewNode
        
    def atend(self, new_data):
        NewNode = Node(new_data)
        if self.headval == None:
            self.headval = NewNode
            return
        lastPtr = self.headval             #always remember to use a new variavle to traverse
        while lastPtr.nextval != None:
            lastPtr = lastPtr.nextval
        lastPtr.nextval = NewNode          #attach new node at the end of SLL
            
    def atmiddle(self, middle_node, new_data):
        if middle_node == None:
            print("middle_node does not exist.")
        NewNode = Node(new_data)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
        
    def remove_node(self, remove_key):     #if the first node contains the key
        temp = self.headval
        if temp != None:
            if temp.dataval == remove_key:
                self.headval = temp.nextval #point head to node after temp
                temp = None     # delete temp
                return
        
        while temp != None:
            if temp.dataval == remove_key: #if this node contains the key, jump to line 57
                break
            prev = temp          #keep moving prev and temp forward      
            temp = temp.nextval
            
        if temp == None:        #if you get to the end and it is empty, end program
            return
        prev.nextval = temp.nextval #delete node
        temp = None
        
e2, e3 = Node('Tues'), Node('Wed')

list1 = SLinkedList()
list1.headval = Node('Mon')     #set the head to point to the first node in SLL

list1.headval.nextval = e2      #set the pointer in first node to point to node 2
e2.nextval = e3                 #set nextval ptr to node 3

list1.printval()

list1.atbeginning('Sun')

list1.printval()

list1.atend('Thurs')
list1.atmiddle(e2, 'Saturday')
list1.printval()
list1.remove_node('Thurs')
list1.printval()