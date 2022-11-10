def duplexList(myList: list):
    sorted = myList.copy()
    sorted.sort()
    reversed = sorted.copy()
    reversed.reverse()
    return sorted + reversed


testers = [
    [1,3,4,5,6,2],
    [1.1, 1.4, 1.2, 1.2, -1.2, -0.3],
    ["Barack", "Trump", "Hillary", "Max"]
]

for test in testers:
    print (duplexList(test))