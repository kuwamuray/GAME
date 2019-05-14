import numpy
import random

M = 20
N = 10

end_flag = 0
field =  [[65307 for j in range(N)] for i in range(M)]
field[int(M/2) - 1][int(N/2) - 1] = 9632
field[int(M/2)    ][int(N/2)    ] = 9632
field[int(M/2) - 1][int(N/2)    ] = 9633
field[int(M/2)    ][int(N/2) - 1] = 9633
BWT = 9633

def CheckPositionVacant(S,X,Y):
    L = []
    MM = list(S)
    L.append(ord(MM[0]) - 65)
    L.append(ord(MM[1]) - 97)
    print(L)
    block_position = []
    if X == 0 :
        if Y % 2 == 0 :
            for i in range(4):
                block_position.append([L[0] + i, L[1]])
        else :
            for i in range(4):
                block_position.append([L[0], L[1] + i])
    elif X == 1 :
        for i in range(2):
            for j in range(2):
                block_position.append([L[0] + i, L[1] + j])
    elif X == 2 :
        block_position.append([L[0]    , L[1]    ])
        block_position.append([L[0] + 1, L[1]    ])
        block_position.append([L[0] - 1, L[1]    ])
        block_position.append([L[0]    , L[1] + 1])
        block_position.append([L[0]    , L[1] - 1])
        if Y % 4 == 0 :
            block_position.remove([L[0] + 1, L[1]    ])
        elif Y % 4 == 1 :
            block_position.remove([L[0]    , L[1] - 1])
        elif Y % 4 == 2 :
            block_position.remove([L[0] - 1, L[1]    ])
        else :
            block_position.remove([L[0]    , L[1] + 1])
    elif X == 3 :
        if Y % 4 == 0 :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0] - 1, L[1]    ])
            block_position.append([L[0]    , L[1] + 1])
            block_position.append([L[0]    , L[1] + 2])
        elif Y % 4 == 1 :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0]    , L[1] + 1])
            block_position.append([L[0] + 1, L[1]    ])
            block_position.append([L[0] + 2, L[1]    ])
        elif Y % 4 == 2 :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0] + 1, L[1]    ])
            block_position.append([L[0]    , L[1] - 1])
            block_position.append([L[0]    , L[1] - 2])
        else :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0]    , L[1] - 1])
            block_position.append([L[0] - 1, L[1]    ])
            block_position.append([L[0] - 2, L[1]    ])
    elif X == 4 :
        if Y % 4 == 0 :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0] - 1, L[1]    ])
            block_position.append([L[0]    , L[1] - 1])
            block_position.append([L[0]    , L[1] - 2])
        elif Y % 4 == 1 :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0]    , L[1] + 1])
            block_position.append([L[0] - 1, L[1]    ])
            block_position.append([L[0] - 2, L[1]    ])
        elif Y % 4 == 2 :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0] + 1, L[1]    ])
            block_position.append([L[0]    , L[1] + 1])
            block_position.append([L[0]    , L[1] + 2])
        else :
            block_position.append([L[0]    , L[1]    ])
            block_position.append([L[0]    , L[1] - 1])
            block_position.append([L[0] + 1, L[1]    ])
            block_position.append([L[0] + 2, L[1]    ])
    elif X == 5 :
        block_position.append([L[0]    , L[1]    ])
        block_position.append([L[0] + 1, L[1]    ])
        if Y % 2 == 0 :
            block_position.append([L[0]    , L[1] + 1])
            block_position.append([L[0] + 1, L[1] - 1])
        else :
            block_position.append([L[0]    , L[1] - 1])
            block_position.append([L[0] - 1, L[1] - 1])
    else :
        block_position.append([L[0]    , L[1]    ])
        block_position.append([L[0]    , L[1] - 1])
        if Y % 2 == 0 :
            block_position.append([L[0] + 1, L[1]    ])
            block_position.append([L[0] + 1, L[1] + 1])
        else :
            block_position.append([L[0] - 1, L[1]    ])
            block_position.append([L[0] + 1, L[1] - 1])
    print(block_position)
    for i in range(4):
        if block_position[i][0] < 0 or block_position[i][0] >= M or block_position[i][1] < 0 or block_position[i][1] >= N or field[block_position[i][0]][block_position[i][1]] != 65307 :
            return 0
    return block_position

def CheckReverse(X,Y,Z):
    I,J = 1,0
    OK, NG = 0, 0
    OK_COUNT = 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if X+I == M or field[X+I][Y] == 65307 :
            NG = 1
        elif field[X+I][Y] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            I += 1
    if OK == 1 :
        OK_COUNT += 1
        for i in range(1,I):
            field[X+i][Y] = 10000
    I,J = 1,0
    OK, NG = 0, 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if X-I < 0 or field[X-I][Y] == 65307 :
            NG = 1
        elif field[X-I][Y] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            I += 1
    if OK == 1 :
        OK_COUNT += 1
        for i in range(1,I):
            field[X-i][Y] = 10000
    I,J = 0,1
    OK, NG = 0, 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if Y+J == N or field[X][Y+J] == 65307 :
            NG = 1
        elif field[X][Y+J] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            J += 1
    if OK == 1 :
        OK_COUNT += 1
        for j in range(1,J):
            field[X][Y+j] = 10000
    I,J = 0,1
    OK, NG = 0, 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if Y-J < 0 or field[X][Y-J] == 65307 :
            NG = 1
        elif field[X][Y-J] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            J += 1
    if OK == 1 :
        OK_COUNT += 1
        for j in range(1,J):
            field[X][Y-j] = 10000
    I,J = 1,1
    OK, NG = 0, 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if X+I == M or Y+J == N or field[X+I][Y+J] == 65307 :
            NG = 1
        elif field[X+I][Y+J] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            I += 1
            J += 1
    if OK == 1 :
        OK_COUNT += 1
        for j in range(1,J):
            i = j
            field[X+i][Y+j] = 10000
    I,J = 1,1
    OK, NG = 0, 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if X+I == M or Y-J < 0 or field[X+I][Y-J] == 65307 :
            NG = 1
        elif field[X+I][Y-J] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            I += 1
            J += 1
    if OK == 1 :
        OK_COUNT += 1
        for j in range(1,J):
            i = j
            field[X+i][Y-j] = 10000
    I,J = 1,1
    OK, NG = 0, 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if X-I < 0 or Y+J == N or field[X-I][Y+J] == 65307 :
            NG = 1
        elif field[X-I][Y+J] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            I += 1
            J += 1
    if OK == 1 :
        OK_COUNT += 1
        for j in range(1,J):
            i = j
            field[X-i][Y+j] = 10000
    I,J = 1,1
    OK, NG = 0, 0
    vacant_flag = 0
    ally_flag = 0
    enemy_flag = 0
    while OK == 0 and NG == 0 :
        if X-I < 0 or Y-J < 0 or field[X-I][Y-J] == 65307 :
            NG = 1
        elif field[X-I][Y-J] == Z :
            if enemy_flag == 0 :
                NG = 1
            else :
                OK = 1
        else :
            enemy_flag = 1
            I += 1
            J += 1
    if OK == 1 :
        OK_COUNT += 1
        for j in range(1,J):
            i = j
            field[X-i][Y-j] = 10000
    if OK_COUNT == 0 :
        return 0
    else :
        return 1

def OutputField():
    print(chr(12288), end="")
    for j in range(N):
        print(chr(j + 65345), end="")
    print()
    for i in range(M):
        print(chr(i + 65313), end="")
        for j in range(N):
            print(chr(field[i][j]), end="")
        print()

def OutputNextBlock(X,Y,Z):
    if X == 0 :
        if Y % 2 == 0 :
            print(chr(12288) + chr(Z + 101))
            for i in range(3):
                print(chr(12288) + chr(Z))
        else :
            print(chr(12288) + chr(Z + 101) + chr(Z) + chr(Z) + chr(Z))
    elif X == 1 :
        print(chr(12288) + chr(Z + 101) + chr(Z))
        print(chr(12288) + chr(Z) + chr(Z))
    elif X == 2 :
        if Y % 4 == 0 :
            print(chr(12288) + chr(12288) + chr(Z))
            print(chr(12288) + chr(Z) + chr(Z + 101) + chr(Z))
        elif Y % 4 == 1 :
            print(chr(12288) + chr(Z))
            print(chr(12288) + chr(Z + 101) + chr(Z))
            print(chr(12288) + chr(Z))
        elif Y % 4 == 2 :
            print(chr(12288) + chr(Z) + chr(Z + 101) + chr(Z))
            print(chr(12288) + chr(12288) + chr(Z))
        else :
            print(chr(12288) + chr(12288) + chr(Z))
            print(chr(12288) + chr(Z) + chr(Z + 101))
            print(chr(12288) + chr(12288) + chr(Z))
    elif X == 3 :
        if Y % 4 == 0 :
            print(chr(12288) + chr(Z))
            print(chr(12288) + chr(Z + 101) + chr(Z) + chr(Z))
        elif Y % 4 == 1 :
            print(chr(12288) + chr(Z + 101) + chr(Z))
            print(chr(12288) + chr(Z))
            print(chr(12288) + chr(Z))
        elif Y % 4 == 2 :
            print(chr(12288) + chr(Z) + chr(Z) + chr(Z + 101))
            print(chr(12288) + chr(12288) + chr(12288) + chr(Z))
        else :
            print(chr(12288) + chr(12288) + chr(Z))
            print(chr(12288) + chr(12288) + chr(Z))
            print(chr(12288) + chr(Z) + chr(Z + 101))
    elif X == 4 :
        if Y % 4 == 0 :
            print(chr(12288) + chr(12288) + chr(12288) + chr(Z))
            print(chr(12288) + chr(Z) + chr(Z) + chr(Z + 101))
        elif Y % 4 == 1 :
            print(chr(12288) + chr(Z))
            print(chr(12288) + chr(Z))
            print(chr(12288) + chr(Z + 101) + chr(Z))
        elif Y % 4 == 2 :
            print(chr(12288) + chr(Z + 101) + chr(Z) + chr(Z))
            print(chr(12288) + chr(Z))
        else :
            print(chr(12288) + chr(Z) + chr(Z + 101))
            print(chr(12288) + chr(12288) + chr(Z))
            print(chr(12288) + chr(12288) + chr(Z))
    elif X == 5 :
        if Y % 2 == 0 :
            print(chr(12288) + chr(12288) + chr(Z + 101) + chr(Z))
            print(chr(12288) + chr(Z) + chr(Z))
        else :
            print(chr(12288) + chr(Z))
            print(chr(12288) + chr(Z) + chr(Z + 101))
            print(chr(12288) + chr(12288) + chr(Z))
    else :
        if Y % 2 == 0 :
            print(chr(12288) + chr(Z) + chr(Z + 101))
            print(chr(12288) + chr(12288) + chr(Z) + chr(Z))
        else :
            print(chr(12288) + chr(12288) + chr(Z))
            print(chr(12288) + chr(Z) + chr(Z + 101))
            print(chr(12288) + chr(Z))

missed_count = 0
while end_flag == 0 and missed_count < 1000 :
    OutputField()
    if missed_count == 0 :
        next_block_int = random.randrange(7)
    turn_count = 0
    print()
    OutputNextBlock(next_block_int, turn_count, BWT)
    print()
    turn_flag = 1
    if BWT == 9633 : 
        while turn_flag == 1 :
            T = input("TURN ? : ")
            while len(T) != 1 :
                T = input("TURN ? : ")
            if ord(T) == 80 :
                BWT = 19265 - BWT
                missed_count = - 1
                turn_flag = 0
            elif ord(T) == 89 :
                turn_count += 1
                OutputField()
                print()
                OutputNextBlock(next_block_int, turn_count, BWT)
                print()
            else :
                turn_flag = 0
    else :
        turn_count = random.randrange(4)
    if BWT == 9633 :
        put_position_input = input("PUT POSITION : ")
    elif missed_count >= 0 :
        put_position_input = chr(65 + random.randrange(M)) + chr(97 + random.randrange(N))
    if missed_count >= 0 :
        print(put_position_input)
        put_position = CheckPositionVacant(put_position_input, next_block_int, turn_count)
        print(put_position)
    else :
        put_position = 0
    if put_position == 0 :
        missed_count += 1
    else :
        reverse_flag = []
        for i in range(4):
            reverse_flag.append(CheckReverse(put_position[i][0], put_position[i][1], BWT))
        if 1 not in reverse_flag :
            print("YOU CANT PUT THERE !!")
            missed_count += 1
            field = numpy.array(field)
            field = numpy.where(field == 10000, 19265 - BWT, field)
            field = field.tolist()
        else :
            for i in range(4):
                field[put_position[i][0]][put_position[i][1]] = BWT
                field = numpy.array(field)
                field = numpy.where(field == 10000, BWT, field)
                field = field.tolist()
            for i in range(M):
                if 65307 not in field[i] :
                    field[i] = [65307 for j in range(N)]
            BWT = 19265 - BWT
            missed_count = 0
    BC = 0
    WC = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 9633 :
                BC += 1
            elif field[i][j] == 9632 :
                WC += 1
    if BWT == 9633 :
        print()
        print("YOUR SCORE : " + str(BC))
        print(" CPU SCORE : " + str(WC))
        print()

print()
print("YOUR SCORE : " + str(BC))
print(" CPU SCORE : " + str(WC))
print()
