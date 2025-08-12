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
        
if __name__=='__main__':
    ll = LinkedList()
    ll.inset_at_begin(10)
    ll.inset_at_begin(78)
    ll.print()