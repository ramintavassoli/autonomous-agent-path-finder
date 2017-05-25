def qfinder1(Grid,a,b):
    if isinstance(Grid[a][b],float) == False:
        return Grid[a + 1][b]
    else:
        return Grid[a][b]