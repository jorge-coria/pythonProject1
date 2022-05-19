import pprint
message = 'It was a bright cold day in April.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count) # pretty-text as string val: print(pprint.pformat(count))