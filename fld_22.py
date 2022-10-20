szam:float = float(input('írj be egy számot: '))

if szam >= -30 and szam <= 40:
    print(f'a {szam} a [-30; 40] intervallumon belül van')
else:
    print(f'a {szam} a [-30; 40] intervallumon kívül esik')