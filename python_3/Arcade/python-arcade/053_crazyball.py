from itertools import combinations

def crazyball(players, k):
    return sorted(list( map(lambda i: sorted(i),list(combinations(players, k))) ))
