import random as ran
from pynput import mouse
import time as t
import keyboard as kb
moves = ["up", "down", "left", "right", "v", "s", "a", "b", "L", "R"]
rand = ran.choice(moves)
count = 0

kb.wait("k")
go = True

start_time = t.time()  # Record the start time

def on_click(x, y, button, pressed):
    global go
    if not pressed and button == mouse.Button.right:
        go = False
        print(count)
        print("Program was running for:", t.strftime("%H:%M:%S", t.gmtime(t.time() - start_time)))

# Create a listener for mouse clicks
listener = mouse.Listener(on_click=on_click)
listener.start()

while go:
    rand = ran.choice(moves)
    kb.press(rand) 
    print(rand) # Just to see the random move, you can remove this in actual implementation
    count += 1
    
    # Perform your action here
    # kb.press(rand) # You can include this to simulate keyboard press
    # Assuming you want to end when 'i' key is pressed
    # if kb.is_pressed("i"):
    #     print(count)
    #     break

# Stop the listener after loop ends
listener.stop()
