def spam():
    global eggs
    eggs = 'lsd'

eggs = 'global'
spam()
print(eggs)