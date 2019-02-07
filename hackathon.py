import pigpio
import game

from guizero import App, Text, Window, Box
from random import randint

phrases = [
    #"Four furious friends fought for the p",
    
    'hi how r u today',
    'bonjour said Olivier',    
    #"If Im not back in five minutes just wait longer",
    "Four furious friends fought",
    "Tie twine to three tree twigs",
    "Green glass globes glow greenly",
    "Six slimy snails sailed silently",
    "I wish to wash my Irish wristwatch",
    "He threw three free throws",
    #"Its a nice night for a white rice fight",
    "I shot the city sheriff",
    #"Shut up the shutters and sit in the shop",
    "A pessimistic pest exists amidst us",
    "She sees cheese",
    "Thin grippy thick slippery"
]

phrases = [
'bonjour said Olivier'
]

PLAYER0_HOOK_PIN = 22
PLAYER0_DIALING_STATE = 17
PLAYER0_DIGIT_PIN = 27

PLAYER1_HOOK_PIN = 11
PLAYER1_DIALING_STATE = 10
PLAYER1_DIGIT_PIN = 9

PLAYER2_HOOK_PIN = 13
PLAYER2_DIALING_STATE = 5
PLAYER2_DIGIT_PIN = 6

PLAYER3_HOOK_PIN = 4
PLAYER3_DIALING_STATE = 15
PLAYER3_DIGIT_PIN = 18

def is_game_over():
    try:
        
        if players is None:
            return False
    
        for player in players:
            if player.is_winner:
                return True
        
        return False
    except:
        return False
    
    
def phone_on_hook(g, L, t):
    
    print("hook")
    player = get_player(g)
    if player == None:
        return
    
    # print("Player {}".format(player.index))
    if L == 1 and not is_game_over():
        # print("HIGH")
        player.phone_on_hook(False, not is_game_over())
    else:
        # print("LOW")
        player.phone_on_hook(True, not is_game_over())
        
def dialing_state(g, L, t):
    print("dialing state")
    if is_game_over():
        return
    
    # print("state")
    player = get_player(g)
    if player == None:
        return
    # print("Player {}".format(player.index))
    if L == 1:
        message = player.digit_received()
        print(message)

def count_digits(g, L, t):
    print("count digits")
    if is_game_over():
        return
    
    
    # print("digits")
    player = get_player(g)
    if player == None:
        return
    # print("Player {}".format(player.index))
    if L == 0:
        player.count_digit()

def get_player(argument):
    try:
        print("get player {}".format(argument))
        switcher = {
            PLAYER0_HOOK_PIN: 0, 
            PLAYER0_DIALING_STATE: 0, 
            PLAYER0_DIGIT_PIN: 0,
            PLAYER1_HOOK_PIN: 1, 
            PLAYER1_DIALING_STATE: 1, 
            PLAYER1_DIGIT_PIN: 1,
            PLAYER2_HOOK_PIN: 2, 
            PLAYER2_DIALING_STATE: 2, 
            PLAYER2_DIGIT_PIN: 2,
            PLAYER3_HOOK_PIN: 3, 
            PLAYER3_DIALING_STATE: 3, 
            PLAYER3_DIGIT_PIN: 3
        } 

     
        idx =  switcher.get(argument, None)
    
        if (players is None) or len(players) <= idx:
            return None
        
        return players[idx]
    except:
        return None

pi = pigpio.pi()
#PLAYER 1
pi.set_mode(PLAYER0_HOOK_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER0_HOOK_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER0_HOOK_PIN, 10000)

pi.set_mode(PLAYER0_DIALING_STATE, pigpio.INPUT)
pi.set_pull_up_down(PLAYER0_DIALING_STATE, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER0_DIALING_STATE, 10000)

pi.set_mode(PLAYER0_DIGIT_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER0_DIGIT_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER0_DIGIT_PIN, 10000)

pi.callback(PLAYER0_DIALING_STATE, pigpio.EITHER_EDGE, dialing_state)
pi.callback(PLAYER0_HOOK_PIN, pigpio.EITHER_EDGE, phone_on_hook)
pi.callback(PLAYER0_DIGIT_PIN, pigpio.EITHER_EDGE, count_digits)

#PLAYER 2
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

#PLAYER 3
pi.set_mode(PLAYER2_HOOK_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER2_HOOK_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER2_HOOK_PIN, 10000)

pi.set_mode(PLAYER2_DIALING_STATE, pigpio.INPUT)
pi.set_pull_up_down(PLAYER2_DIALING_STATE, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER2_DIALING_STATE, 10000)

pi.set_mode(PLAYER2_DIGIT_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER2_DIGIT_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER2_DIGIT_PIN, 10000)

pi.callback(PLAYER2_DIALING_STATE, pigpio.EITHER_EDGE, dialing_state)
pi.callback(PLAYER2_HOOK_PIN, pigpio.EITHER_EDGE, phone_on_hook)
pi.callback(PLAYER2_DIGIT_PIN, pigpio.EITHER_EDGE, count_digits)

#PLAYER 4
pi.set_mode(PLAYER3_HOOK_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER3_HOOK_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER3_HOOK_PIN, 10000)

pi.set_mode(PLAYER3_DIALING_STATE, pigpio.INPUT)
pi.set_pull_up_down(PLAYER3_DIALING_STATE, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER3_DIALING_STATE, 10000)

pi.set_mode(PLAYER3_DIGIT_PIN, pigpio.INPUT)
pi.set_pull_up_down(PLAYER3_DIGIT_PIN, pigpio.PUD_DOWN)
pi.set_glitch_filter(PLAYER3_DIGIT_PIN, 10000)

pi.callback(PLAYER3_DIALING_STATE, pigpio.EITHER_EDGE, dialing_state)
pi.callback(PLAYER3_HOOK_PIN, pigpio.EITHER_EDGE, phone_on_hook)
pi.callback(PLAYER3_DIGIT_PIN, pigpio.EITHER_EDGE, count_digits)

''''''''''''''''' 
      UI
'''''''''''''''''
font = "FreeMono"
font_size = 60
phrase_color = "red"
main_font_color = "#ff4f1f"
sub_font_color = "#acadaf"

app = App("Rotary T9", bg='black', width=800, height=600, layout="grid")
app.tk.attributes('-fullscreen', True)
players = []

def start_game(player_count):
    players.clear()
    
    print("start game {} {} {} {}".format(pi.read(PLAYER0_HOOK_PIN),pi.read(PLAYER1_HOOK_PIN),pi.read(PLAYER2_HOOK_PIN),pi.read(PLAYER3_HOOK_PIN)))
    if (pi.read(PLAYER0_HOOK_PIN) == 1) or \
        (pi.read(PLAYER1_HOOK_PIN) == 1) or \
        (pi.read(PLAYER2_HOOK_PIN) == 1) or \
        (pi.read(PLAYER3_HOOK_PIN) == 1):
            Text(app, text="All Phones Must Be On HOOK", size=65, font=font, grid=[0,2] , color=main_font_color,align='center')
            return
    
    clear_screen()

    message_index = randint(0, len(phrases) - 1)
    message = phrases[message_index]

    Text(app, text=message, size=font_size, font=font, color=phrase_color, grid=[0,0, 3,1],align='left')
    Text(app, text="1 - Undo     0 - Space", size=int(font_size/2), font=font, color=phrase_color, grid=[2,10],align='bottom')

    for i in range(player_count):
        print("creating player {}".format(i))
        players.append(game.Player(i, app, message))
    
    print("player count {}".format(len(players)))

def clear_screen():
    for child in app.children:
        try:
            child.clear()
        except:
            pass
        child.hide()
        del child
    
    app.children.clear()

def show_start_screen():
    clear_screen()
    Text(app, text="Welcome to Rotary Phone Texting", size=65, font=font, grid=[0,0] , color=main_font_color,align='center')
    Box(app, height=150, grid=[0,1])
    Text(app, text="Using the rotary phone, T9 text the message at the top of the screen", size=25, font=font, grid=[0,2], color=sub_font_color,align='center')
    Text( app, text="E.g. for 's', dial 7 once", size = 25, font=font, grid=[0,3], color=sub_font_color,align='center')
    Text( app, text="1 - Undo last character", size = 25, font=font, grid=[0,4], color=sub_font_color,align='center')
    Text( app, text="0 - Space", size = 25, font=font, grid=[0,5], color=sub_font_color,align='center')
    
def clicked(key):
    print("starting game with {} players".format(key.key))
    if key.key == 's':
        show_start_screen()
        return

    if key.key == '1' or key.key == '2' or key.key == '3' or key.key == '4':
        start_game(int(key.key))
        return
    
    if key.key == 'q':
        app.destroy()

app.when_key_pressed = clicked
show_start_screen()
app.display()
print("stopping")
pi.stop()