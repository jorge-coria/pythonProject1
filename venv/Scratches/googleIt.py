# Launch a search query on Google with your browser
# Uses a search query from the clipboard or the command line

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get search query from command line
    search_query = ' '.join(sys.argv[1:])
else:
    # Get search query from clipboard.
    search_query = pyperclip.paste()

webbrowser.open('https://www.google.com/search?q=' + search_query)