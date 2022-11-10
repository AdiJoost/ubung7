def sumNumbers(n: int) -> int:
    if n < 0:
        return
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

testers = (0,1,2,3,4, -1, -25)
for n in testers:
    print(sumNumbers(n))