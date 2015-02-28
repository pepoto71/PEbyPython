def count(sequence,item):
    '''
    Count object in sequence/list
    in linear time O(n)
    '''
    visited={}
    for element in sequence:
        key=str(element)
        if key in visited:
            visited[key] +=1
        else:
            visited[key]=1
    if str(item) in visited:
        return visited[str(item)]
    else:
        return 0
    
item={}
arr=[1,2,[],{},3,2,2,2,2,3,0]
print 'item %s ,exist in sequence %d times' %(str(item),count(arr,{}))

#############################################

def remove_duplicates(lst):
    '''
    Remove duplicates in linear time O(n)
    '''
    temp={}
    result=[]
    for item in lst:
        if str(item) in temp:
            continue
        else:
            temp[str(item)]=True
            result.append(item)        
    return result
    
lst=[1,2,2,2,1,{},{},[],3,-4,-4,-4,0,0,'qwerty','qwerty']
print remove_duplicates(lst)

def median(lst):
    lst.sort()
    if len(lst)%2==1:
     return lst[len(lst)/2]
    else:
        return (lst[len(lst)/2-1]+lst[len(lst)/2])/2.0
print median([4,5,5,4])
