# IP: 187000
# OP: 2 nap 3 óra 56 perc 40 mp

uzemido = int(input('üzemidő: '))

day = uzemido // (3600 * 24)
uzemido %= (3600 * 24)
hour = uzemido // 3600
uzemido %= 3600
minute = uzemido // 60
sec = uzemido % 60

print(f'átváltva: {day}.{hour}:{minute}:{sec}')