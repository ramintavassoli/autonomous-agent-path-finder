from qfinder1 import qfinder1
from qfinder2 import qfinder2
from qfinder3 import qfinder3
from qfinder4 import qfinder4


def MDPA(dim, Grid, rew, discount):
    qlist = []
    index_mat = [[0]*(dim+2) for n in range(dim+2)]
    for k in range(4):
        GridDup = [row[:] for row in Grid]
        row_num = 0
        col_num = 0
        for row in GridDup:
            for col in row:
                if isinstance(col,float) == True:
                    if col == 1.0:
                        qmax = 1.0
                        index_mat[row_num][col_num] = 5
                        Grid[row_num][col_num] = round(qmax, 2)
                    elif col == -1.0:
                        qmax = -1.0
                        index_mat[row_num][col_num] = -5
                        Grid[row_num][col_num] = round(qmax, 2)
                    else:
                        qN = (4/5)*(rew + discount**k*qfinder1(GridDup,row_num-1,col_num)) + (1/10)*(rew + discount**k*qfinder2(GridDup,row_num,col_num-1)) + (1/10)*(rew + discount**k*qfinder3(GridDup,row_num,col_num+1))
                        qS = (4/5)*(rew + discount**k*qfinder4(GridDup,row_num+1,col_num)) + (1/10)*(rew + discount**k*qfinder2(GridDup,row_num,col_num-1)) + (1/10)*(rew + discount**k*qfinder3(GridDup,row_num,col_num+1))
                        qW = (4/5)*(rew + discount**k*qfinder2(GridDup,row_num,col_num-1)) + (1/10)*(rew + discount**k*qfinder1(GridDup,row_num-1,col_num)) + (1/10)*(rew + discount**k*qfinder4(GridDup,row_num+1,col_num))
                        qE = (4/5)*(rew + discount**k*qfinder3(GridDup,row_num,col_num+1)) + (1/10)*(rew + discount**k*qfinder1(GridDup,row_num-1,col_num)) + (1/10)*(rew + discount**k*qfinder4(GridDup,row_num+1,col_num))
                        qlist.extend([qN, qS, qW, qE])
                        qmax = max(qlist)
                        index_mat[row_num][col_num] = qlist.index(qmax)+1 #7x7 matrix
                        Grid[row_num][col_num] = round(qmax, 2)
                        qlist = []
                col_num += 1
            col_num = 0
            row_num += 1

    col_num = 0
    row_num = 0

    returnINDEX = [[''] * (dim + 2) for n in range(dim + 2)]
    for row in index_mat:
        for col in row:
            if index_mat[row_num][col_num] == 1:
                returnINDEX[row_num][col_num] += 'N'
            if index_mat[row_num][col_num] == 2:
                returnINDEX[row_num][col_num] += 'S'
            if index_mat[row_num][col_num] == 3:
                returnINDEX[row_num][col_num] += 'W'
            if index_mat[row_num][col_num] == 4:
                returnINDEX[row_num][col_num] += 'E'
            col_num += 1
        col_num = 0
        row_num += 1

    col_num = 0
    row_num = 0

    returnGRID = [[''] * (dim + 2) for n in range(dim + 2)]
    for row in returnGRID:
        for col in row:
            returnGRID[row_num][col_num] = str(Grid[row_num][col_num]) + returnINDEX[row_num][col_num]
            col_num += 1
        col_num = 0
        row_num += 1

    return returnGRID