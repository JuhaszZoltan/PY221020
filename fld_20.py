szam:int = int(input('írj be egy számot: '))

if szam == 0:
    print('egyik sem')
elif szam < 0:
    print('negatív')
else:
    print('pozitív')