import numpy as np
consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"

def cons():
    return "".join(np.random.choice([c for c in consonants], size=8, replace=True))

def vows():
    return "".join(np.random.choice([v for v in vowels], size=4, replace=True))

c = cons()
v = vows()
planet = c[0]+v[0]+c[1]+c[2]+v[1]+c[3]+"-"+c[4]+v[2]+c[5]+c[6]+v[3]+c[7]
print("cons: ", c)
print("vows: ", v)
print("planet: ~"+planet)

