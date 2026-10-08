Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import permutations
... 
... word1 = "SEND"
... word2 = "MORE"
... result = "MONEY"
... 
... letters = set(word1 + word2 + result)
... 
... for p in permutations(range(10), len(letters)):
...     d = dict(zip(letters, p))
... 
...     # First letters cannot be zero
...     if d['S'] == 0 or d['M'] == 0:
...         continue
... 
...     SEND = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
...     MORE = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
...     MONEY = 10000*d['M'] + 1000*d['O'] + 100*d['N'] + 10*d['E'] + d['Y']
... 
...     if SEND + MORE == MONEY:
...         print("Solution found:")
...         print("SEND =", SEND)
...         print("MORE =", MORE)
...         print("MONEY =", MONEY)
