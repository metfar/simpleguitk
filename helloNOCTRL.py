# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

try:
	import simpleguitk as simplegui;

except:
	import simplegui;

import subprocess;
message = "Welcome!";

# Handler for mouse click
def click():
    global message;
    message = "Fine!";

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [1,20], 12, "#538457");

def strrev(x):
    return(x[::-1]);

def timex():
    global message;
    message=subprocess.check_output(["uptime"]);
    message=message.split('p',2)[1];
    message=strrev(strrev(message).split(',',4)[4]);
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 50, 20);
frame.set_canvas_background("#dddddd");
frame.set_draw_handler(draw);
timer = simplegui.create_timer(500, timex);
timer.start();

# Start the frame animation
frame.start()
