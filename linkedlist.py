class Node:
    def __init__(self, data = None, next = None):
        self.data=data
        self.next=next
        
class LinkedList:
    def __init__(self):
        self.head=None


#data inserting
    def inset_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node
    
    #printing liked list    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        
        while itr:
            llstr = llstr + str(itr.data) + '-->'
            itr=itr.next
        print(llstr)
        
        #Inserting at the end
        
    def insert_at_end(self, data):
        if self.head is None:  ## check if list is empty. if it is empty add new node and sets its next pointer to none as it is only element
            self.head = Node(data,None)
        
        itr=self.head       
        while itr.next:
            itr = itr.next
            
        itr.next=Node(data,None)
            
        
if __name__=='__main__':
    ll = LinkedList()
    ll.inset_at_begin(10)
    ll.inset_at_begin(78)
    ll.insert_at_end(9)
    ll.insert_at_end(108)
    ll.print()