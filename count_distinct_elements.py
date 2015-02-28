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
