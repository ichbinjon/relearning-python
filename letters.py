#! python3
#makes things copied in clipboard lower or uppercase

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py letters.py [upper/lower] - copy account password')
    sys.exit()

case = sys.argv[1].lower()

if case == 'lower':
    text = pyperclip.paste().lower()
    pyperclip.copy(text)
    print('lowercase copied')
    sys.exit()

elif case == 'upper':
    text = pyperclip.paste().upper()
    pyperclip.copy(text)
    print('uppercase copied')
    sys.exit()
else:
    print('Usage: py letters.py [upper/lower] - copy account password')
    sys.exit()
