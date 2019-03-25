def correctLineup(athletes):
    return [b for a in zip(athletes[1::2],athletes[::2]) for b in a]
