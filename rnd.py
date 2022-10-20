import random

# [0, 1) -> float számot állít elő 
r1 = random.random()

# [a, b] -> egész szám (a < b)
r2 = random.randint(a=-30, b=40)

# [start, stop) 'step-esével' előállított intervallomból választ egy véletlen számot
r3 = random.randrange(start=0, stop=101, step=2)