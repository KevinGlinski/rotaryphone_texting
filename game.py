from datetime import datetime 

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
        
    def __init__(self, index, target_message):
        self.index = index
        self.target_message = target_message

    def phone_on_hook(self, on_hook):
        self.on_hook = on_hook
        if self.on_hook:
            end = datetime.now()
            completed_time = end - self.start
            print("Player " + str(self.index) + " is DONE with { " + self.message + " } in " + "{}".format(completed_time) + " seconds")
            self.message = ""
        else:
            print("Player " + str(self.index) + " is STARTING!")
            self.start = datetime.now()
        
    def digit_received(self):
        if self.on_hook:
            print('Phone must be off hook, bro!')
            return

        digit = self.count
        self.count = 0

        if digit == 1:
            self.character_received(None)
            return
        
        char = self.calculate_character(digit)
        print("char: " + str(char))
        self.character_received(char)
        return self.message
        
    def character_received(self, char):
        if char == None:
            #remove last character
            self.message = self.message[:-1]
            return
        
        self.message = self.message + char
        print("message: " + self.message)

    def count_digit(self):
            self.count += 1

    def calculate_character(self, digit):
        next_expected_char = self.target_message[len(self.message):][0].lower()
        next_expected_char_digit = char_map[next_expected_char]

        if digit == next_expected_char_digit:
            return next_expected_char

        if digit == 1:
            return

        return number_to_char_map[digit]

        # if digit == 2:
        #     return 'a'
        # if digit == 3:
        #     if not self.message:
        #         return 'f'
        #     elif self.message.endswith("l"):
        #         return 'd'
        #     return 'e'
        # if digit == 4:
        #     if self.message:
        #         if self.message.endswith("t") or self.message.endswith("g"):
        #             return 'h'
        #         return 'g'
        #     elif len(self.message) == 1:
        #         return 'i'
        #     return 'h'
        # if digit == 5:
        #     if self.message.endswith("n"):
        #         return 'k'
        #     return 'l'
        # if digit == 6:
        #     if self.message:
        #         if self.message.endswith("a"):
        #             return 'n'
        #         return 'o'
        #     return 'm'
        # if digit == 7:
        #     if self.message:
        #         if self.message.endswith("o"):
        #             return 'r'
        #         return 's'
        #     return 'p'
        # if digit == 8:
        #     if self.message:
        #         return 'u'
        #     return 't'
        # if digit == 9:
        #     if len(self.message.split()) == 1:
        #         return 'w'
        #     return 'y'
        # if digit == 10:
        #     return " "
        
# message = 'test message'

# player = Player(1, message)
# #h
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.on_hook = True
# player.digit_received()
# #e
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.on_hook = True
# player.digit_received()
# #l
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.on_hook = True
# player.digit_received()
# #l
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.on_hook = True
# player.digit_received()
# #0
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.on_hook = True
# player.digit_received()
# #10
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.count_digit()
# player.on_hook = True
# player.digit_received()
# input("")