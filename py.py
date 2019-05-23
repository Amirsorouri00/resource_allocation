import random
import math

def sort(Demand):
    X = Demand
    for i in range(len(X)):
     min_index = i
     for j in range(i+1, len(X)):
       if X[min_index] > X[j]:
         min_index = j
     X[i], X[min_index] = X[min_index], X[i]
    return X

def check_end(DTS):
    for i in range(0, len(DTS)):
        if DTS[i] != 0:
            return False
    return True

def fivelimitcheck(UAB, maze, counterperslot, cntperslot):
    for i in range(0, len(cntperslot)):
        if cntperslot[i] == 1:
            counterperslot[i]+=1

    for j in range(0, len(counterperslot) - 1):
        if counterperslot[j] == 5:
            counter = 0    
            for k in range(j*25, j*25+9):
                # print(j, k)
                if maze[j][counter] == -1:
                    maze[j][counter] = -9
                    UAB.remove(k)
                counter+=1
                

def userallocator(block_need, UAB, maze):
    cntperslot = [-1 for i in range(0,10)]
    # print("cntpslot", cntperslot)
    userblocks = []
    row = -1
    col = -1
    for j in range(0, block_need):
        block_num = random.choice(tuple(UAB))
        if cntperslot[math.floor(block_num/25)] == -1:
            cntperslot[math.floor(block_num/25)] = 1
        row = math.floor(block_num/25)
        col = block_num%25
        if maze[row][col] == -1:
            maze[row][col] = j
            UAB.remove(block_num)
            userblocks.append([row, col])
            block_need -= 1
    return cntperslot, userblocks, block_need

def Allocator(maze, UAB, UCPSGS, UDS, round):
    counterperslot = [-1 for i in range(0,10)]
    usersblocks = []
    flag = True
    for i in range(0,9):
        amount = UDS[i]
        block_need = math.ceil(amount/10)
        print(block_need)
        cntpslot, userblocks, block_need = userallocator(block_need, UAB, maze)
        usersblocks.append(userblocks)
        UDS[i] = (block_need*10)
        print(block_need)
        fivelimitcheck(UAB, maze, counterperslot, cntpslot)
        print("-----------------------------------------------------------------------------------------------")
    return flag


def main():
    UsersDataToSend = []
    for i in range(0,9):
        UsersDataToSend.append(random.randint(1,250))
    cnt = 0
    while True:
        print("UsersDataToSend before: ", UsersDataToSend)
        UnAllocatedBlocks = set()
        UnAllocatedBlocks.update([i for i in range(0,10*25)])
        print(UnAllocatedBlocks)
        UsersCounterPerSlotGlobState = [0 for i in range(0,10)]
        maze = [[-1 for item in range(0,25)] for item in range(0,10)]
        Allocator(maze, UnAllocatedBlocks,UsersCounterPerSlotGlobState, UsersDataToSend, cnt)
        cnt+=1
        if check_end(UsersDataToSend) != False:
            print(maze)
            break
    return


main()