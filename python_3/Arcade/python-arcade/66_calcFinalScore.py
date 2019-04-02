def calcFinalScore(scores, n):
    gen = iter([k**2 for j,k in enumerate(sorted(scores)[::-1])])

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
