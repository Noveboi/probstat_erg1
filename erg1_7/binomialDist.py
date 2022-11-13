import itertools
#n choose k
def nCk(n,k):
    if k > n: 
        print("k cannot be larger than n!")
        return False
    return len(list(itertools.combinations(range(n),k)))

#Binomial random variable PMF with params n and p
# -- "Out of n independent trials, k trials are successful" --
#Returns: probability for every k successful trials out of n (k = 0,1,...,n)
#n = number of trials
#p = probability of success 
#indexing at index i returns the i amount of successful trials
def PMF(n,p):
    for k in range(n+1):
        yield nCk(n,k)*(p**k)*((1-p)**(n-k))
