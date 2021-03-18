import numpy as np



##create samples
output=[]
for i in range(0,1000):
    pi_obs = np.random.dirichlet([1,1,1,1],1)[0].tolist()
    pi_max = max(pi_obs)
    k = pi_obs.index(pi_max)

    output.append([pi_max,k])


zs = list(map(lambda x:x[0],output))

import matplotlib.pyplot as plt

plt.hist(zs)

ys = list(map(lambda x:np.random.poisson(x[1]))