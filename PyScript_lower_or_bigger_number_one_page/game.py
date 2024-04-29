from js import document, window
from random import randint

sn = 5
c = 0

def update_display(num, msg=""):
    document.getElementById("number_display").innerText = str(num)
    document.getElementById("message_display").innerText = msg
    # Update this to correctly define buttons in Python
    global buttonBigger, buttonLower
    buttonBigger = document.getElementById("bigger")
    buttonLower = document.getElementById("lower")

def bigger(*args):
    global sn, c
    n = randint(1, 10)
    while n == sn:
        n = randint(1, 10)

    if n > sn:
        update_display(n)
        sn = n
        c += 1
    else:
        update_display(n, "The number is lower")
        end_game()

def lower(*args):
    global sn, c
    n = randint(1, 10)
    while n == sn:
        n = randint(1, 10)

    if n < sn:
        update_display(n)
        sn = n
        c += 1
    else:
        update_display(n, "The number is bigger")
        end_game()

def end_game():
    global sn, c, buttonBigger, buttonLower
    document.getElementById("final_message").style.display = "block"  # Make the final message visible
    if c == 0:
        final_msg = "Ups! You had {} hits! <br>You seem to be a great lover!<br>Would you like to play a new game?".format(c)
    else:
        final_msg = "Congratulations!<br>You had {} hits!<br>Would you like to play a new game?".format(c)
    document.getElementById("end_message").innerHTML = final_msg
    
    # Disable buttons by removing event listeners
    buttonBigger.removeEventListener("click", bigger)
    buttonLower.removeEventListener("click", lower)
    
    # Optionally, you can also directly disable the buttons using the disabled property
    buttonBigger.disabled = True
    buttonLower.disabled = True

    # Ensure reset button is shown to allow new game
    document.getElementById("reset").style.display = "inline-block"

def resetGame(*args):
    global sn, c, buttonBigger, buttonLower
    sn = 5  # Reset starting number
    c = 0  # Reset counter
    update_display(sn)  # Update display with initial number

    # Hide the final message div and enable buttons
    document.getElementById("final_message").style.display = "none"
    buttonBigger.disabled = False
    buttonLower.disabled = False

    # Re-add event listeners if removed previously
    buttonBigger.addEventListener("click", bigger)
    buttonLower.addEventListener("click", lower)

# Expose functions to JavaScript
window.bigger = bigger
window.lower = lower
window.resetGame = resetGame
