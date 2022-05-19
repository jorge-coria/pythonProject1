def spam():
    print(eggs)     # ERROR !
    eggs = 'spam local'

eggs = 'global'
spam()

# Python does not fall back to using global eggs