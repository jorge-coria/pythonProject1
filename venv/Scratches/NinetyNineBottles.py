# Press Ctrl-C to stop the program.
# Line 21: Change the number to decrease by that amount next iteration
# Line 14: Change compare operator to bypass loop and play last stanza

import sys, time

print('Ninety-Nine Bottles')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99 # starting number of bottles.
PAUSE = 2    # change to 0 to see the full song at once.

try:
    while bottles > 1: # Loop and dislay lyrics
        print(bottles, 'bottles of juice on the wall,')
        time.sleep(PAUSE)
        print(bottles, 'bottles of juice,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1
        print(bottles, 'bottles of juice on the wall!')
        time.sleep(PAUSE)
        print() # Newline

# Display the last stanza:
    print('1 bottle of juice on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of juice,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of juice on the wall!')
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C : end the program.

