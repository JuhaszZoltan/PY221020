import random
szamok:list[int] = []

futasok_szama = 0
while len(szamok) < 5:
    r = random.randint(1, 90)
    if r not in szamok:
        szamok.append(r)
    futasok_szama += 1

print(szamok)
print(f'ciklus iterációinak száma: {futasok_szama}')