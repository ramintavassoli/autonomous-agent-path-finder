def MDP(dim,rMat,fMat,treasure_site):
    dim_wall = dim + 2
    V = [[0.0]*dim_wall for n in range(dim_wall)]
    V[0][0:dim_wall] = ['wall' for n in range (dim_wall)]
    V[dim_wall-1][0:dim_wall] = ['wall' for n in range(dim_wall)]
    for row in range(dim_wall):
        V[row][0] = 'wall'
        V[row][dim_wall-1] = 'wall'
    V[treasure_site[0]+1][treasure_site[1]+1] = +1.0
    for r_row in range(len(rMat)):
        V[rMat[r_row][0]+1][rMat[r_row][1]+1] = 'wall'
    for f_row in range(len(fMat)):
        V[fMat[f_row][0]+1][fMat[f_row][1]+1] = -1.0
    return V