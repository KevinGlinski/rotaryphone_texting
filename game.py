import pyxel
from guizero import App, Text, Window
from random import randint

phrases = [
    'hi how r',
    'hi how r u today',
    'bonjour said Olivier',
    
    "If I'm not back in five minutes just wait longer",
    # "If Stu chews shoes should Stu choose the shoes he chews",
    "Four furious friends fought for the phone",


]


font = "FreeMono"
font_size = 60
phrase_color = "lightblue"
colors = ['white', '#a5c13e','#c1973e','#aaaaa9']
main_font_color = "#ff4f1f"


class Player:
    index = 0
    message = ''
    target_message = ''
    on_hook = True
        
    def __init__(self, index, target_message, digit_gpio_pin, hook_gpio_pin):
        self.index = index
        self.target_message = target_message

        self.text = Text(app, text="Player {}".format(index + 1), size=font_size, font=font, color=colors[index], grid=[0,(index +1) * 2, 3,1], align='left') 
        self.text = Text(app, text=phrases[0]+ "_", size=font_size, font=font, color=colors[index], grid=[0,((index +1) * 2) + 1, 3,1],align='left') 
        
        
    def digit_received(self, digit):
        if on_hook:
            return
        
        if digit == 1:
            self.character_received(None)
            return
        
        #TODO calculate character
        char = 'a'
        self.character_received(self, char) 
        
    def character_received(self, char):
        if char == None:
            #TODO: remove char
            return
        
        self.message = self.message + char
        print(self.message)
        
    def on_hook(self):
        print('on hook')
        self.on_hook = True
    
    def off_hook(self):
        print('off hook')
        self.on_hook = False
        
    def __del__(self):
        self.text.set("die")

     
message = 'test message'


app = App("Hello World", bg='black', width=800, height=600, layout="grid")
players = []

def start_game(player_count):
    clear_screen()

    message_index = randint(0, len(phrases) - 1)
    message = phrases[message_index]

    Text(app, text=message, size=font_size, font=font, color=phrase_color, grid=[0,0, 3,1],align='top')
    Text(app, text="1 - Undo     0 - Space", size=int(font_size/2), font=font, color=phrase_color, grid=[2,10],align='bottom')


    for i in range(player_count):
        players.append(Player(i, message, 1,1))

def clear_screen():
    for child in app.children:
        child.clear()
        child.hide()
        del child
    
    app.children.clear()

def show_start_screen():
    clear_screen()
    Text(app, text="Welcome to Rotary Phone Texting", size=65, font=font, grid=[0,0] , color=main_font_color,align='center')

def clicked(key):
    print(key.key)
    if key.key == 'q':
        show_start_screen()
        return

    if key.key == '1' or key.key == '2' or key.key == '3' or key.key == '4':
        start_game(int(key.key))
        return


app.when_key_pressed = clicked
show_start_screen()
app.display()
