def qfinder2(Grid,a,b):
    if isinstance(Grid[a][b], float) == False:
        return Grid[a][b + 1]
    else:
        return Grid[a][b]
