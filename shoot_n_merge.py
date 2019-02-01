import numpy as np
import random
import sys

END = 0
M = 3
N = 3
field = np.zeros((M,N))
step = 1
            
while END == 0 :
    add_num = random.randrange(65,70) # ascii
    for k in range(M-1):
        for j in range(N):
            for i in range(M-1):
                if field[i][j]==0 and field[i+1][j]!=0 :
                    field[i][j] = field[i+1][j]
                    field[i+1][j] = 0
    print()
    for i in range(M):
        for j in range(N):
            # print(field[i][j])
            if field[i][j] == 0:
                sys.stdout.write("; ")
            else:
                sys.stdout.write(str(chr(int(field[i][j]))) + " ")
        print()
    print("next block is " + str(chr(add_num)))
    add_pst = int(input(str(step) + " step : "))
    i = 0
    while i < M and field[i][add_pst - 1] != 0:
        i += 1
    step += 1
    if i == M :
        if field[i-1][add_pst-1] == add_num:
            field[i-1][add_pst-1] += 1
            ni = i - 1
            nj = add_pst - 1
        else:
            print("Please select null space.")
            step -= 1
    else :
        field[i][add_pst-1] = add_num
        ni = i
        nj = add_pst - 1
    OK = 0
    while OK == 0 :
        f1, f2, f3 = 0, 0, 0
        if nj>0 and field[ni][nj]==field[ni][nj-1]:
            f1 = 1
        if ni>0 and field[ni][nj]==field[ni-1][nj]:
            f2 = 1
        if nj<N-1 and field[ni][nj]==field[ni][nj+1]:
            f3 = 1
        if f1 + f2 + f3 == 0 :
            OK = 1
        elif f1 + f2 + f3 == 3 :
            field[ni-1][nj] += 3
            field[ni][nj-1]  = 0
            field[ni][nj  ]  = 0
            field[ni][nj+1]  = 0
            ni -= 1
        elif f1 + f2 == 2 :
            field[ni-1][nj] += 2
            field[ni][nj-1]  = 0
            field[ni][nj  ]  = 0
            ni -= 1
        elif f2 + f3 == 2 :
            field[ni-1][nj] += 2
            field[ni][nj  ]  = 0
            field[ni][nj+1]  = 0
            ni -= 1
        elif f1 + f3 == 2 :
            field[ni][nj] += 2
            field[ni][nj-1]  = 0
            field[ni][nj+1]  = 0
        elif f1 == 1 :
            k = random.randrange(2)
            field[ni][nj-k  ] += 1
            field[ni][nj+k-1]  = 0
            nj -= k
        elif f2 == 1 :
            field[ni-1][nj] += 1
            field[ni  ][nj]  = 0
            ni -= 1
        elif f3 == 1 :
            k = random.randrange(2)
            field[ni][nj-k+1] += 1
            field[ni][nj+k  ]  = 0
            nj = nj - k + 1
    if 0 not in field :
        END = 1
        score = 0
        for i in range(M):
            for j in range(N):
                score += pow(2, field[i][j] - 64)
        print()
        print("Your score is " + str(score))
        print()
