import matplotlib.pyplot as plt 
import numpy as np
import random
from time import time
import seaborn

state = ['S','NS'] #S = Sick , NS = Not Sick
def experiment():
    mom, = random.choices(state,weights=(1,99))
    dad, = random.choices(state,weights=(1,99))

    #determine weights on probability of sickness for children based on parents condition
    if (mom == "S") ^ (dad == "S"): #MomSick XOR DadSick
        child1, = random.choices(state,weights=(2,98))
        child2 ,= random.choices(state,weights=(2,98))
    elif (mom == "S") and (dad == "S"):
        child1, = random.choices(state,weights=(50,50))
        child2, = random.choices(state,weights=(50,50))
    else:
        child1 = child2 = 'NS'
    return {
        'M': mom,
        'D': dad,
        'C1': child1,
        'C2':child2
    }

trials = 1000000
iters = 50
data = []
ps = 0
print("Program running...")
for i in range(iters):
    s = time() #store time for each iter
    if i == 0: ps = s #store loop start time
    D = M = C1 = C2 = A = B = 0

    C1andC2GivenB = 0
    C1andC2 = 0
    MxorDgivenC1andC2 = 0
    MandDgivenC1andC2 = 0
    for trial in range(trials):
        e = experiment()
        if e['M'] == 'S': M += 1
        if e['D'] == 'S': D += 1
        if (e['M'] == 'S') ^ (e['D'] == 'S'): 
            B += 1
            if (e['C1'] == 'S') and (e['C2'] == 'S'):
                C1andC2GivenB += 1 #Question 1 [Sample Space: B]
        if (e['M'] == 'S') and (e['D'] == 'S'): A += 1
        if e['C1'] == 'S': C1 += 1
        if e['C2'] == 'S': C2 += 1
        if (e['C1'] == 'S') and (e['C2'] == 'S'):
            C1andC2 += 1 #Question 2 [Sample Space: Ω]
            if (e['M'] == 'S') ^ (e['D'] == 'S'): 
                MxorDgivenC1andC2 += 1 #Question 3 [Sample Space: C1andC2]
            if (e['M'] == 'S') and (e['D'] == 'S'):
                MandDgivenC1andC2 += 1 #Question 4 [Sample Space: C1andC2]
    te = time() - s
    print(f"Iteration {i+1} complete:  time remaining: {round((iters-(i+1))*te,1)}s")
    data.append([C1andC2GivenB/B,C1andC2/trials,MxorDgivenC1andC2/C1andC2,MandDgivenC1andC2/C1andC2])

print(f"Program completed in {time() - ps} seconds")
data = np.array(data) #Organize data into numpy array
x = range(1,iters+1) #Define x-axis for plots

#Log Plot
for k in range(1,5):
    logq = np.log10(data[:,k-1])
    plt.plot(x,logq,label=f'log10Q{k}')
plt.title("Logarithmic represantation of probabilities")
plt.ylabel("Probabilities log10")
plt.xlabel("Iteration #")
plt.legend()
plt.savefig("./erg1_4/log.jpg")

#Normal Plot
plt.clf()
for k in range(1,5):
    plt.plot(x,data[:,k-1],label=f'Q{k}')
plt.title("Normal represantation of probabilities")
plt.ylabel("Probabilities")
plt.xlabel("Iteration #")
plt.legend()
plt.savefig("./erg1_4/normal.jpg")

#Bar Plots
palette = seaborn.color_palette('flare',n_colors=iters).as_hex()
for k in range(1,5):
    plt.clf()
    plt.bar(x,data[:,k-1],color=palette)
    plt.plot(x,[np.average(data[:,k-1]) for a in range(iters)],color='#ecf931')
    plt.title(f"Question {k} probabilities")
    plt.ylabel("Probability")
    plt.xlabel("Iteration #")
    plt.savefig(f"./erg1_4/bar_Q{k}.jpg")

#Print out averages for each question
print("---------------------------")
for i in range(1,5):
    print(f"Q{i} average value: {np.average(data[:,i-1])}")
