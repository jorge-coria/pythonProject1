def greet2(name):
    print('how you been, ' + name + '?')

def bye():
    print('alright, bye!')


def greet(name):
    print('hi ' + name + '!')
    greet2(name)
    print('about to head out, ' + name + '.')
    bye()

greet('Kamila C')