## Davlarlar orasida visa card bo'lganlarini chiqarish
with open('karta.txt') as f:
    visa = []
    for i in f.read().split('\n'):
        card = i.split(',')
        if card[1] == 'visa' and card[-1] not in visa:
            visa.append(card[-1])

visa.sort()
for i in visa:
    print(i)