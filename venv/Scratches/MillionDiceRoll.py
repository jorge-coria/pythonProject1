# A simulation of 1 million dice rolls.
# Using SystemRandom() in my implementation -> Takes longer

import random, time

print('''Million Dice Roll Stats Simulator
Enter how many six-sided dice you want to roll:''')
numberOfDice = int(input('> '))

# Dictionary to store each dice roll result
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# Simulate dice rolls
print('Simulating 1,000,000 rolls of {} dice...'.format(numberOfDice))
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print('{}% done...'.format(round(i / 10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.SystemRandom().randint(1, 6)
    results[total] = results[total] + 1

# Display results
print(' TOTAL - ROLLS - PERCENTAGE ')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(' {} - {} rolls - {}%'.format(i, roll, percentage))
