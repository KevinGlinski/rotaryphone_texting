import pigpio
import game

PLAYER1_HOOK_PIN = 14
PLAYER1_DIALING_STATE = 15
PLAYER1_DIGIT_PIN = 18
player1_message = "hello world"
player1 = game.Player(1, player1_message)

def phone_on_hook(g, L, t):
    # print("hook")
    player = get_player(g)

    if L == 1:
        # print("HIGH")
        player.phone_on_hook(False)
    else:
        # print("LOW")
        player.phone_on_hook(True)

def dialing_state(g, L, t):
    # print("state")
    player = get_player(g)

    if L == 1:
        message = player.digit_received()
        print(message)

def count_digits(g, L, t):
    # print("digits")
    player = get_player(g)

    if L == 0:
        player.count_digit()

def get_player(argument): 
    switcher = {
        PLAYER1_HOOK_PIN: player1, 
        PLAYER1_DIALING_STATE: player1, 
        PLAYER1_DIGIT_PIN: player1
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "nothing") 

pi = pigpio.pi()
pi.set_mode(PLAYER1_HOOK_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER1_HOOK_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER1_HOOK_PIN, 10000)

pi.set_mode(PLAYER1_DIALING_STATE, pigpio.INPUT)
pi.set_pull_up_down(PLAYER1_DIALING_STATE, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER1_DIALING_STATE, 10000)

pi.set_mode(PLAYER1_DIGIT_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER1_DIGIT_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER1_DIGIT_PIN, 10000)

pi.callback(PLAYER1_DIALING_STATE, pigpio.EITHER_EDGE, dialing_state)
pi.callback(PLAYER1_HOOK_PIN, pigpio.EITHER_EDGE, phone_on_hook)
pi.callback(PLAYER1_DIGIT_PIN, pigpio.EITHER_EDGE, count_digits)

input("")
pigpio.stop()