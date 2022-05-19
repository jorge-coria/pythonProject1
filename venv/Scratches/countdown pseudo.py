# infinite loop without base case
#def countdown(i):
#    print(i)
#    countdown(i-1)
#
#countdown(5)

# recursive function: base case and the recursive case
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

countdown(5)
