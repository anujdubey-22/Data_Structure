'''
Expected Time Complexity: O(1) for push() and O(N) for pop() (or vice-versa).
Expected Auxiliary Space: O(1) for both push() and pop().
'''


'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
   ''' 
count=1
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    global count
    
    if count%2!=0:
        queue_1.append(x)
    else:
        queue_2.append(x)
        
    count+=1
    return
    # code here


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    global count
    if count>1:
        count-=1
    else:
        count=1
        return -1
    if count%2!=0 and len(queue_1)>0:
        return queue_1.pop()
    elif count%2==0 and len(queue_2)>0:
        return queue_2.pop()
    else:
        return -1


#################################### by  using 2  Queues ##################################################################

def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    queue_1.append(x)
    while len(queue_2)!=0:
        value=queue_2.pop(0)
        queue_1.append(value)
        
    temp=queue_1
    queue_1=queue_2
    queue_2=temp

#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    if len(queue_2)>0:
        return queue_2.pop(0)
    else:
        return -1
    
#################################################### by using 1 Queue ########################################################

def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    queue_1.append(x)
    n=len(queue_1)-1
    for i in range(n):
        value=queue_1.pop(0)
        queue_1.append(value)
        


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    if len(queue_1)>0:
        return queue_1.pop(0)
    else:
        return -1 
        