local random = math.random
local os_time = os.time
local kb = require("keyboard")
local mouse = require("mouse")

local moves = {"up", "down", "left", "right", "v", "s", "a", "b", "L", "R"}
local count = 0
local go = true

local start_time = os_time()  -- Record the start time

function on_click(x, y, button, pressed)
    if not pressed and button == 2 then  -- Button 2 represents the right mouse button
        go = false
        print("Number of moves:", count)
        print("Program was running for:", os.date("!%X", os_time() - start_time))  -- Print duration
    end
end

-- Register the mouse listener
mouse.on("click", on_click)

-- Main loop
while go do
    local rand = moves[random(#moves)]  -- Choose a random move from the list
    kb.press(rand)
    print(rand)  -- Just to see the random move, you can remove this in actual implementation
    count = count + 1

    -- Perform your action here
    -- kb.press(rand)  -- You can include this to simulate keyboard press

     -- Wait for 0.1 seconds between each move
end
