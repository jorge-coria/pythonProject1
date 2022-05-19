message = 'I LOVE MY LIFE >> THANK YOU GOD FOR EVERYTHING + EVERYONE PAST AND PRESENT'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)