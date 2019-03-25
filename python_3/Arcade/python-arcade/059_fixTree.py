def fixTree(tree):
    return list(map(lambda x : ' '*(x.count(' ')//2) + '*'*x.count('*') + ' '*(x.count(' ')//2) ,tree))
