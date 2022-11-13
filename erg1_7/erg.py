
""" ́Ενα νόμισμα ρίχνεται επανειλημμένα και η κορώνα έχει πιθανότητα εμφάνισης p σε
κάθε ρίψη. 
Ποια είναι η πιθανότητα να εμφανισθεί η Κορώνα για δεύτερη φορά στην ρίψη k ;"""
import random
import numpy as np
import matplotlib.pyplot as plt
import binomialDist
import matplotlib.animation as anim

print("------Experiment starting-------")

k = 9 #up to how many tosses are specified here
p = 0.005 #probability of heads
p0 = p

coin = ['K','G']
trials = 1000
writer = anim.PillowWriter(fps=30)
fig = plt.figure()

def printData(data,k):
    print(f"Success Rate: {data} | (k = {k}, p = {p})")

def trial(k):
    toss_sequence = []
    w = [p,1-p]
    for toss in range(k):
        toss_sequence.append(random.choices(coin,weights=w)[0])
    if toss_sequence.count('K') == 2 and toss_sequence[-1] == 'K':
        return True
    return False

def experiment(k):
    successes = 0
    for i in range(trials):
        if trial(k): successes += 1
    return successes

def averageExperiment(k): #do experiment 4 times and return the average success rate
    sr = []
    for exp in range(4):
        sr.append(experiment(k)/trials)
    return np.average(sr)

totalProbs = []
with writer.saving(fig,"probs_loop.gif",dpi=256):
    while p < 1:
        xrange = range(2,k+1)
        x = np.array(xrange) #x = k
        probs = []
        for i in xrange:
            e = averageExperiment(i)
            printData(e,i)
            probs.append(e)
        totalProbs.append(probs)
        plt.ylim(0,1)
        plt.plot(xrange,probs,label='Success Rate (Program Result)',color='g')
        plt.plot(xrange,(x-1)*((1-p)**(x-2))*(p**2),label="(k-1) * (1-p)^(k-2) * p^2 (Mathematical Result)",color='firebrick')
        plt.title(f"2 Heads in k Tosses, With kth Toss Being a Head -- P(Head) = {round(p,2)}")
        plt.xlabel("k")
        plt.ylabel("Probability of 2 Heads and Toss k Being Head")
        plt.legend()
        writer.grab_frame()
        plt.cla()
        p = round(p+p0,5)
    totalProbs.reverse()
    for prob in totalProbs:
        xrange = range(2,k+1)
        x = np.array(xrange)
        plt.ylim(0,1)
        plt.plot(xrange,prob,label='Success Rate (Program Result)',color='g')
        plt.plot(xrange,(x-1)*((1-p)**(x-2))*(p**2),label="(k-1) * (1-p)^(k-2) * p^2 (Mathematical Result)",color='firebrick')
        plt.title(f"2 Heads in k Tosses, With kth Toss Being a Head -- P(Head) = {round(p,2)}")
        plt.xlabel("k")
        plt.ylabel("Probability of 2 Heads and Toss k Being Head")
        plt.legend()
        writer.grab_frame()
        plt.cla()
        p = round(p-p0,5)


#experiment: 2 heads in k tosses, with kth toss being a head
#binomial: 2 heads in k tosses


