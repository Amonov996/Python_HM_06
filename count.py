## Davlatlar sonini chiarsh:
from pprint import pprint

with open('karta.txt') as f:
    dct = {}
    for i in f.read().split('\n')[1::]:
        country = i.split(',')
        if country[-1] not in dct:
            dct[country[-1]] = 1
        else:
            dct[country[-1]] += 1
pprint(dct)
# for key, val in dct.items():
#     print(key, val)