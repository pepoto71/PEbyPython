# "Stopwatch: The Game"

import simplegui

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def init():
    global stop_watch,counter_hits,counter_success,stop_watch_state
    stop_watch=0
    counter_hits=0
    counter_success=0
    stop_watch_state=False

def increase_counter_hits():
    global counter_hits,stop_watch_state
    if stop_watch_state:
        counter_hits +=1

def check_success():
    global stop_watch,counter_success,stop_watch_state
    if stop_watch_state:
        if stop_watch%10==0:
            counter_success +=1
        
def set_stop_watch_state(state):
    global stop_watch_state
    stop_watch_state=state

def format_stop_watch(t):    
    min=t/600
    min_to_str=str(min)
    seconds=(t-min*600)/10
    if seconds<10:
        seconds_to_str="0"+str(seconds)
    else:
        seconds_to_str=str(seconds)
    milseconds=t%10
    milseconds_to_str=str(milseconds)
    return min_to_str+":"+seconds_to_str+"."+milseconds_to_str

def format_counters():
    global counter_hits,counter_success
    return str(counter_success)+"/"+str(counter_hits)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    set_stop_watch_state(True)

def stop():    
    timer.stop()
    increase_counter_hits()
    check_success()
    set_stop_watch_state(False)
    
def reset():
    timer.stop()
    init()

# define event handler for timer with 0.1 sec interval
def tick():
    global stop_watch
    stop_watch +=1    

# define draw handler
def draw(canvas):    
    canvas.draw_text(format_counters(),[162,20],20,"Green")
    canvas.draw_text(format_stop_watch(stop_watch),[70,60],24,"Red")

    
# create frame
frame=simplegui.create_frame("Stop watch game",200,110)
button_start=frame.add_button("Start",start,100)
button_stop=frame.add_button("Stop",stop,100)
button_reset=frame.add_button("Reset",reset,100)

timer=simplegui.create_timer(100,tick)

# register event handlers
frame.set_draw_handler(draw)

# start frame
init()
frame.start()


# Please remember to review the grading rubric
