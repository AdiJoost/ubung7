def getParams(s: str):
    length = len(s)
    sumLower = 0
    sumUpper = 0
    for i in s:
        if i.islower():
            sumLower += 1
        if i.isupper():
            sumUpper += 1
    return length, sumLower, sumUpper

testers = (
    "Hello",
    "134395",
    "",
    "£!èàé`?",
    "GUTEN TAG",
    "asdfbd"
)
for test in testers:
    print(getParams(test))