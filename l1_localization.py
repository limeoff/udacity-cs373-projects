
p=[0.2, 0.2, 0.2, 0.2, 0.2] #prior uniform distribution
#p = [0, 1, 0, 0, 0]  # for movement quiz
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']  # making n measurements
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, z):
    q = []
    for index, item in enumerate(world):
        if item == z:
            q.append(p[index] * pHit)
        else:
            q.append(p[index] * pMiss)

            # one more variant
            # q.append(p[index] * (hit * pHit + (1 - hit) * pMiss))
    # normalizing distribution after measurement - entries in q should sum to one.
    q = [i / sum(q) for i in q]
    return q


# shift probabolities in p to the right for U num of steps
def move(p, u):
    q = []
    for i , v in enumerate(p):
        s = pExact * p[(i - u) % len(p)]
        s = s + pOvershoot * p[(i - u - 1) % len(p)]
        s = s + pUndershoot * p[(i - u + 1) % len(p)]
        #print(s)
        q.append(s)
    return q


# updating p after each measurement
# for measure in measurements:
#    p = sense(p,measure)

for i in range(len(measurements)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])

print(p)