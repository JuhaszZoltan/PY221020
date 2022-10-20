termek = input('termék megnevezése: ')
egysegar = int(input('termék egységára (Ft): '))
db = int(input('vásárolni kívánsz darabszám: '))
penz = int(input('ennyi pénz van nálad (Ft): '))

ar = egysegar * db
if ar <= penz:
    print(f'Meg tudod vásárolni a {db} {termek}-t!')
    if ar == penz:
        print('nem marad nálad pénz')
    else:
        print(f'{penz - ar} Ft a visszajáró')
else:
    if penz < egysegar:
        print(f'Nem tudsz egy db {termek}-t sem venni...')
    else:
        print(f'Maximum {penz // egysegar} db {termek}-ra/re van nálad elég pénz!')