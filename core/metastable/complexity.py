import numpy as np
import math

def lempel_ziv(ts):

    ts = np.array(ts)

    s = "".join(['1' if x > np.median(ts) else '0' for x in ts])

    n = len(s)

    i, u, v, w, c = 1, 1, 1, 1, 1

    while v + w <= n:

        if s[i:i+v] == s[i+w:i+v+w]:
            v += 1
        else:
            w += 1
            c += 1
            v = 1

    return (c * math.log2(n)) / n
