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
     
##created a function that will take the values    

    def insert_values(self, data_list):
        self.head = None ## making sure to restting the linked list 
        for data in data_list:
            self.insert_at_end(data)
    

## function to find length of a linked list
    
    def ll_length(self):
        counter=0
        itr = self.head
        while itr:
            counter=counter+1
            itr=itr.next
        return counter
    
## function to remove element from linked list at a given index

    def remove(self, index):
        if index<0  or index > self.ll_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0 
        itr = self.head
        
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next                      
            count = count+1
            
    def insert_after_value(self, data_after, data_to_insert):
        
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
        while itr:
           if itr.data == data_after:
               itr.next = Node(data_to_insert, itr.next)
               break 
           itr=itr.next
            
        
        
    
    
    
    def remove_by_value(self, data):
        
        if self.head is None: ## if list is empty 
            return 

        ## if head element is only the element we want to remove then
        
        if self.head.data == data: 
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data==data:
                itr.next = itr.next.next
                break
            itr = itr.next
                    
if __name__=='__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "oranges"])
    ll.print()
    ll.insert_after_value("mango","3")
    ll.print()
    ll.remove(3)
    ll.remove_by_value("mango")
    ll.print()
    print("length:" ,ll.ll_length())