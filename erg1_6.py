import random
import numpy as np
import matplotlib.pyplot as plt

trials = 15
avg = []
for i in range(trials):
    prizes = []
    for i in range(250000):
        s = 0
        while random.choices(['H','T'],weights=(50,50))[0] == 'T':
            s += 1
        prizes.append(2**s)
    avg.append(np.average(prizes))
print(np.average(avg))