def prefSum(a):
    return functools.reduce(lambda i,x : i + [i[-1] +x], a[1:], [a[0]])
#functools.reduce(function, iterable[, initializer])
