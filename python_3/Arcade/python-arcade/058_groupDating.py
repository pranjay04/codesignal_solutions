def groupDating(male, female):
    return [[male[x] for x in range(len(male)) if male[x] != female[x]], [female[y] for y in range(len(female)) if male[y] != female[y]]]
