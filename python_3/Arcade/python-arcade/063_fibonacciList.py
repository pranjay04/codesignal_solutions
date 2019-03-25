def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda i,x: i + [i[-1]+i[-2]] , range(2,n), [0,1])]
