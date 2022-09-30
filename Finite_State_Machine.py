# Allowed number inputs

class FSM:
    def __init__(self):
        self.handlers = {}

    def add_state(self, name, handler):
        self.handlers[name] = handler

    def run(self, startingState, cargo):
        handler = self.handlers[startingState]
        while True:
            (newState, cargo) = handler(cargo)
            if newState == "END":
                print("END reached")
                break
            handler = self.handlers[newState]

num = FSM()
def start_handler(cargo):
    
    if cargo == '':
        print('Invalid number')
        return ('END', cargo)
    elif cargo[0] == '-':
        return ('Minus', cargo[1:])
    elif type(cargo[0]) == int:
        return ('Second Dig', cargo[1:])
    else: 
        print("Invalid number")
        return ('END', cargo)

def after_minus_handler(cargo):
    
    if cargo[0].isnumeric():
        return ('Second Dig', cargo[1:])
    else:
        print('Invalid number')
        return ('END', cargo)

def second_dig_handler(cargo):
    
    if cargo == '':
        return ('END', cargo)
    elif cargo[0].isnumeric():
        return ('Second Dig', cargo[1:])
    elif cargo[0] == '.':
        return ('After dot', cargo[1:])
    else:
        print('Invalid number')
        return ('END', cargo)

def after_dot_handler(cargo):
    
    if cargo == '':
        print('Invalid number')
    elif cargo[0].isnumeric():
        return ('Mantissa', cargo[1:])
    else:
        print('Invalid number')
        return ('END', cargo)
        
def mantissa_handler(cargo):
    
    if cargo == '':
        return ('END', cargo)
    elif cargo[0].isnumeric():
        return ("Mantissa", cargo[1:])
    else:
        print('Invalid number')
        return ('END', cargo)

def end_handler(cargo):
    pass

    
num.add_state("Start", start_handler)

num.add_state('Minus', after_minus_handler)

num.add_state('Second Dig', second_dig_handler)

num.add_state('After dot', after_dot_handler)

num.add_state('Mantissa', mantissa_handler)

num.add_state('END', end_handler)

# Test
num.run('Start', '-26.45z')

num.run('Start', '-26.45')

num.run('Start', '--26.45')

num.run('Start', '3.')

num.run('Start', '.45')