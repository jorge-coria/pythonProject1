import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes',
    'Reply hazy ... try again',
    'Ask again later ...',
    'Concentrate ... ask again',
    'My reply is yes',
    'Outlook looking good',
    'Highly likely']

print(messages[random.randint(0, len(messages) - 1)])