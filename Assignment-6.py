n = int(input())
A = list(map(int,input().split()))
def bottle(x):
    B = []
    C = []
    from copy import deepcopy
    E = deepcopy(x)
    for i in range(len(x)):
        for j in range(1,len(x)):
            if x[i] < x[j] and x[j] not in B and x[i] not in C:
                C.append(x[i])
                B.append(x[j])
                E.remove(x[i])
                break
            elif x.count(x[i]) > 1 and (x[i] in C or x[i] in B):
                if x[i] in C:
                    C.remove(x[i])
                elif x[i] in B:
                    B.remove(x[i])

    return E,B,C
out,b,c = bottle(A)
if out[-1] != max(A) and out[-1] not in b and max(A) not in c:
    out.pop()
print(len(out))

