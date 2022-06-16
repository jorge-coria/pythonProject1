import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:400])

# Failed download not a dealbreaker for your program, wrap with try+except to handle without crashing
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# Check for errors, raises an exception if failed to download, does nothing if download successful
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()