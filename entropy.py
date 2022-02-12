import numpy as np


def ent(x):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x==x_value].shape[0])/x.shape[0]
        logp = np.log2(p)
        ent -=p*logp

    return ent