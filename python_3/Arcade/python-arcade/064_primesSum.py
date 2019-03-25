def primesSum(a, b):
    return sum([i for i in range(a, b+1) if (0 not in [i%j for j in range(2,int(i**0.5)+1) ] ) and i!=1 ])
