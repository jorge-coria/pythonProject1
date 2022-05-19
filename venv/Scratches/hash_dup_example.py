voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out hehe")
    else:
        voted[name] = True
        print("let them votee")

check_voter('adam')
check_voter('mike')
check_voter('mike')
check_voter('mike')
check_voter('adam')

# dictionary is a good way to prevent duplicate entries

'''
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
'''