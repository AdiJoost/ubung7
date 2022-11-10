def isPrime(n: int):
    amountOfdivisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            amountOfdivisors += 1
    return True if amountOfdivisors == 2 else False

def primNumbers(n: int):
    amountOfPrime = 0
    for i in range(n):
        if isPrime(i):
            amountOfPrime += 1
    return amountOfPrime

testers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for test in testers:
    print(f"{test} is Prime? {isPrime(test)}")

for test in testers:
    print(f"{test} has how many Primes below? {primNumbers(test)}")

print("______________________")
print(f"For n=10'000, there are {primNumbers(10000)} prim-numbers m, where m < 10'000")