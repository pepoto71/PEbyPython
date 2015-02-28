def censor(text,word):
    '''
    Replace some sequence from given text 
    with */using state mashines/ in linear time O(n)
    '''
    states=len(word)
    current_state=0
    temp_buffer=''
    builder=''
    for char in text:        
        if char=='.' or char==',' or char=='!':
            builder +=char
            continue
        else:
            if char.lower==word[current_state].lower:
                current_state +=1
            else:
                current_state=0
                builder +=temp_buffer
                temp_buffer=''
            if current_state==0:
                builder +=char
            else:
                temp_buffer +=char
            if current_state==states:
                builder +='*'*states
                temp_buffer=''
                current_state=0
    return builder
            
print censor('Hi i am new for this amazing pyhon programing language. This is my new chalange.','a')
