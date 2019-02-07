from datetime import datetime 

from guizero import App, Text, Window
from random import randint


font = "FreeMono"
font_size = 60
colors = ['#aaaaa9', '#c1973e','white','#a5c13e']
main_font_color = "#ff4f1f"


number_to_char_map = {
    2: 'a',
    3: 'd',
    4: 'g',
    5: 'j',
    6: 'm',
    7: 'p',
    8: 't',
    9: 'w',
    10: ' ' 
}

char_map = {
    'a': 2,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 3,
    'f': 3,
    'g': 4,
    'h': 4,
    'i': 4,
    'j': 5,
    'k': 5,
    'l': 5,
    'm': 6,
    'n': 6,
    'o': 6,
    'p': 7,
    'r': 7,
    's': 7,
    't': 8,
    'u': 8,
    'v': 8,
    'w': 9,
    'x': 9,
    'y': 9,
    ' ': 10
}

class Player:
    index = 0
    count = 0
    message = ''
    target_message = ''
    on_hook = True
    start = datetime.now()
    app = None
    is_winner = False
    is_complete = False
        
    def __init__(self, index, app, target_message):
        self.index = index
        self.target_message = target_message
        
        self.app = app
        self.player_name_text = Text(app, text="Player {}".format(index + 1), size=font_size, font=font, color=colors[index], grid=[0,(index +1) * 2, 3,1], align='left') 
        self.text = Text(app, text="", size=font_size, font=font, color=colors[index], grid=[0,((index +1) * 2) + 1, 3,1],align='left') 
        
        

    def phone_on_hook(self, on_hook, can_win_game):
        if self.is_complete:
            return
        
        
        self.on_hook = on_hook
        if self.on_hook:
            end = datetime.now()
            completed_time = end - self.start
            print("Player " + str(self.index) + " is DONE with { " + self.message + " } in " + "{}".format(completed_time) + " seconds")
            self.text.value = self.message
            
            if self.target_message.lower() == self.message.lower() and can_win_game:
                self.is_winner = True
                self.player_name_text.value = self.player_name_text.value + "(WINNER) "
                self.is_complete = True
                
            if self.target_message.lower() == self.message.lower() and not can_win_game:
                self.is_winner = False
                self.is_complete = True
            
        else:
            print("Player " + str(self.index) + " is STARTING!")
            self.start = datetime.now()
            self.text.value = self.message + "_"
        
    def digit_received(self):
        if self.on_hook:
            print('Phone must be off hook, bro!')
            return

        digit = self.count
        self.count = 0

        if digit == 1:
            self.character_received(None)
            return self.message
        
        char = self.calculate_character(digit)
        print("char: " + str(char))
        self.character_received(char)
        return self.message
        
    def character_received(self, char):
        if char == None:
            #remove last character
            self.message = self.message[:-1]
            self.text.value = self.message + "_"
            return
        
        self.message = self.message + char
        print("message: " + self.message)
        self.text.value = self.message + "_"
        

    def count_digit(self):
            self.count += 1

    def calculate_character(self, digit):
        if digit <= 0 or digit > 10:
            return " "
        
        if len(self.message) >= len(self.target_message):
            return number_to_char_map[digit]
        else:
            next_expected_char = self.target_message[len(self.message):][0].lower()
            next_expected_char_digit = char_map[next_expected_char]

        if digit == next_expected_char_digit:
            return next_expected_char

        if digit == 1:
            return

        return number_to_char_map[digit]
      
    