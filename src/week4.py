#week 4
#fuctions
#print 'hello' n times
def print_hello(times):
    print times*" hello "
#return string
def return_hello(times):
    return times*" hello "
#to swap to objects
def swap(a,b):
    return(b,a)
def computepay(hours,rate):
    if (hours and rate) :
        if hours>40:
            return (hours-40)*rate*1.5+40*rate
        else:
            return hours*rate
        end
    else:
        return False    
    end
def inp_hours():
    inp=raw_input("Enter hours: ")
    try:
        hours=int(inp)
        return hours
    except:
        print "Uncorrect input valus"
        return False
def inp_rate():
    inp=raw_input("Enter rate: ")
    try:
        rate=int(inp)
        return rate
    except:
        print "Uncorrect input valus"
        return False  
       

print_hello(10)
print_hello(2)
print return_hello(3)
print swap(3,7)
print swap("hello","good bye")
print computepay(45,10)

hours=inp_hours()
print hours
rate=inp_rate()
print rate
payment=computepay(hours, rate)
print payment if payment else "Uncorrect input values"

