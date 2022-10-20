print('Utazási költségtérítés\n')

ut:float = float(input('Add meg a megtett utat Km-ben: '))
fogy:float = float(input('Add meg az autó fogyasztását 100 Km-re literben: '))
ar:float = float(input('Add meg az üzemanyag árát Ft-ban: '))

uzemanyagar = ut * fogy * ar / 100
if ut <= 100:
    print(f'\nköltségtérítés: {round(uzemanyagar)} Ft')
else:
    print(f'\nköltségtérítés: {round(uzemanyagar + 25 * ut)} Ft')