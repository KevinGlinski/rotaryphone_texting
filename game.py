
class Player:
    index = 0
    message = ''
    target_message = ''
    on_hook = True
        
    def __init__(self, index, target_message, digit_gpio_pin, hook_gpio_pin):
        self.index = index
        self.target_message = target_message
        
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
        

message = 'test message'

Player(1, message, 15, 14)
