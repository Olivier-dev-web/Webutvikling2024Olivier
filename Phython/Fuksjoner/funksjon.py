import random
def funksjon():
    return

def skriv_hei():
    print("---------")
    print("---hei---")
    print("---------")
    return

skriv_hei()

def gi_et_tileldig_tall(startverdi, stoppverdi):
    tilfeldig_tall = random.randrange(startverdi, stoppverdi )
    return tilfeldig_tall

nytt_tall = gi_et_tileldig_tall(30, 100)
print(nytt_tall)

print(gi_et_tileldig_tall(100, 1000))
