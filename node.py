'''THIS SCRIPT IS INTENDED TO TEST
AND IMPLEMENT A LINKED LIST DATA STRUCTURE'''

class Node:                             #create Node class and initialize parameters
    def __init__(self, dataval):  #class accepts one parameter
        self.dataval = dataval
        self.nextval = None     #pointer to next node initialized as None
        
        
e1, e2, e3 = Node('Mon'), Node('Tues'), Node('Wed')

e1.nextval = e2    #link the nodes
e2.nextval = e3

thisvalue = e1

while thisvalue != None:   #print the data values contained in each node
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval
