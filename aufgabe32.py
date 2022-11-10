import math

def normalFactor(n) -> int:
    if n < 0:
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def stirling(n) -> int:
    if n < 0:
        return
    return math.sqrt(2*n*math.pi)*((n/math.e)**n)


def getDifferance(n):
    normal = normalFactor(n)
    sterli = stirling(n)
    differance = abs(normal - sterli)
    perc = differance / normal
    return (normal, sterli, differance, perc)

tester = (-1, 0, 1, 2, 3, 4, 5, 6, 7)
for n in tester:
    print(normalFactor(n))
    print(stirling(n))

results = []
for i in range(1,101):
    results.append(getDifferance(i))

#Prozentual wird die Differenz zwischen den beiden Funktionen kleiner

print(results[20])
print(results[99])
