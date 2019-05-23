import random
import math

def print_result(l):
    result = []
    for i in range(0, len(l)):
        thisrow = l[i]
        row = []
        for j in range(0, len(thisrow)):
            if thisrow[j] >= 0:
                row.append([thisrow[j], j])
        result.append(row)
    cnt = 0
    for i in range(0, len(result)):
        print("slot{0}".format(cnt), result[i])
        cnt+=1

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
                if maze[j][counter] == -1:
                    maze[j][counter] = -9
                    UAB.remove(k)
                counter+=1
    return

def fifteenlimitcheck(UAB, maze, doublecntperslot):
    for j in range(0, len(doublecntperslot) - 1):
        if doublecntperslot[j] == 15:
            counter = 0    
            for k in range(j*25, j*25+9):
                if maze[j][counter] == -1:
                    maze[j][counter] = -9
                    UAB.remove(k)
                counter+=1
    return

def userallocator(block_need, UAB, maze, user):
    cntperslot = [-1 for i in range(0,10)]
    doublecntperslot = [0 for i in range(0,10)]
    userblocks = []
    row = -1
    col = -1
    for j in range(0, block_need):
        if j%2 == 1:
            fifteenlimitcheck(UAB, maze, doublecntperslot)
        block_num = random.choice(tuple(UAB))
        if cntperslot[math.floor(block_num/25)] == -1:
            cntperslot[math.floor(block_num/25)] = 1
        row = math.floor(block_num/25)
        col = block_num%25
        if maze[row][col] == -1:
            maze[row][col] = user
            UAB.remove(block_num)
            doublecntperslot[row] +=1
            userblocks.append([row, col])
            block_need -= 1
    return cntperslot, userblocks, block_need

def Allocator(maze, UAB, UCPSGS, UDS, round):
    counterperslot = [-1 for i in range(0,10)]
    usersblocks = []
    flag = True
    for i in range(0,10):
        print("-----------------------------------------------------------------------------------------------")
        print("Scheduling the user number: {0}".format(i))
        amount = UDS[i]
        block_need = math.ceil(amount/10)
        print("number of block resources this user needs equals to: {0}".format(block_need))
        cntpslot, userblocks, block_need = userallocator(block_need, UAB, maze, i)
        usersblocks.append(userblocks)
        UDS[i] = (block_need*10)
        fivelimitcheck(UAB, maze, counterperslot, cntpslot)
    return flag

def main():
    UsersDataToSend = []
    for i in range(0,10):
        if random.randint(1,2) == 2:
            UsersDataToSend.append(random.randint(1,250))
        else:
            UsersDataToSend.append(0)
    
    cnt = 0
    while True:
        print("UsersDataToSend before: ", UsersDataToSend)
        print("user_id/index: ", [i for i in range(0,10)])
        UnAllocatedBlocks = set()
        UnAllocatedBlocks.update([i for i in range(0,10*25)])
        UsersCounterPerSlotGlobState = [0 for i in range(0,10)]
        maze = [[-1 for item in range(0,25)] for item in range(0,10)]
        Allocator(maze, UnAllocatedBlocks,UsersCounterPerSlotGlobState, UsersDataToSend, cnt)
        cnt+=1
        if check_end(UsersDataToSend) != False:
            print("-----------------------------------------------------------------------------------------------\n")
            print("Scheduler Result")
            print("(tutorial:  for each [x, y] in each slot: \nx == user_id which would be between (0,9)    &&     y = block_resource_number would be between (0,24) \nin slot)\n")
            print_result( maze)
            print("UsersDataToSend after: ", UsersDataToSend)
            break
    return

main()