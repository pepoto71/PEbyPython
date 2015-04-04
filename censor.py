text='Hi i am new for this amazing pyhon programing language. This is my new chalange.'
words=['new','a','hi','hi i am']

def censor(text,word):
    '''
    Replace some sequence from given text 
    */using state mashines/ in linear time O(n)
    '''
    states=len(word)
    current_state=0
    temp_buffer=''
    builder=''
    signs=('.',',','!','?',';',':')#add more punctuation
    for char in text:         
        if char in signs:
            builder +=char
            continue
        else:            
            if char.lower()==word[current_state].lower():
                current_state +=1
                temp_buffer +=char
            else:
                current_state=0
                builder +=temp_buffer
                temp_buffer=''            
                builder +=char               
            if current_state==states:
                builder +='*'*states
                temp_buffer=''
                current_state=0        
    return builder

def test_cases(text,words):
    print "-=Test cases=-"
    for word in words:
        print '='*len(text)    
        print "Censored word: %s" %word
        print text
        print censor(text,word)

test_cases(text,words)       
