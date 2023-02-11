# Raqanlarni tekshirish
#Karta_raqami,Karta_turi,Valyuta,Valyuta_kodi,Korxona,Davlat
from functools import reduce

with open('karta.txt') as f:
    for i in f.read().split('\n')[1::]:
        num = i.split(',')
        sum = reduce((lambda x, y: int(x) + int(y)), set(num[0]))
        if sum == 45:
            print(f"Karta raqam: {num[0]}\nDavlat: {num[-1]}\nValyuta: {num[-3]}\nKorxona: {num[-2]}\n\n")


