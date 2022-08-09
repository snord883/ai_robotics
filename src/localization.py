import numpy as np

n = 5
p = [1/n]*n

green = 'green'
red = 'red'
world = np.array([green, red, red, green, green])
measurements = [red, red]
motion = [1, 1]
pHit = 0.6
pMiss = 0.2

pUndershot = 0.1
pExact = 0.8
pOvershot = 0.1


########### SENSE #################
def sense(p, Z):
    temp = np.array(p)
    temp[world == red] = pHit*temp[world == red] if Z == red else pMiss*temp[world == red]
    temp[world == green] = pHit*temp[world == green] if Z == green else pMiss*temp[world == green]
    return temp/sum(temp)


# print(sense(p))

y = p
for m in measurements:
    y = sense(y, m)

# print(y)

######## MOTION ###################
# def move(p, U):
#     return np.roll(p, U)


def move(p, U):
    n = len(p)
    q = [0]*n
    for i in range(len(p)):
        q[i] += (pUndershot * p[(i-(U - 1)) % n])
        q[i] += (pExact     * p[(i-(U + 0)) % n])
        q[i] += (pOvershot  * p[(i-(U + 1)) % n])
    return q


# print(move([0, 0.5, 0, 0.5, 0], 2))

x = [1, 0, 0, 0, 0]
for i in range(100):
    x = move(x, 1)


# print(x)


########## ENTROPY ################

def entropy(p, S, M):
    temp = p
    for i in range(min(len(S), len(M))):
        temp = sense(temp, S[i])
        temp = move(temp, M[i])
    return temp

print(entropy(p, measurements, motion))
