L = [[1,2],[3,4],[5,]]

def flat(L):
    for sublist in L:
        for e in sublist:
            yield e

for num in flat(L):
    print(num)