print('Bankjegyautomata\n')
print('A legkisebb címlet 1000 Ft,\na maximálisan felvehető összeg 300.000 Ft\n')

osszeg = int(input('adja meg mekkora összeget kíván felvenni! '))

if osszeg % 1000 != 0 or osszeg > 300000:
    print('hibás összeget adtál meg!')
else:
    # 179000
    tizezres = osszeg // 10000
    osszeg = osszeg % 10000
    otezres = osszeg // 5000
    osszeg = osszeg % 5000
    egyezres = osszeg // 1000
    print('\nA kiadott bankjegyek:\n')
    print(f'{tizezres} * 10.000 = {tizezres * 10000}')
    print(f' {otezres} *  5.000 =   {otezres * 5000}')
    print(f' {egyezres} *  1.000 =   {egyezres * 1000}')
    print('_____________________')
    print(f'Összeg:       {tizezres * 10000 + otezres * 5000 + egyezres * 1000}')
