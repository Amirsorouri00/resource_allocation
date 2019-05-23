import random
import math


def selectsort(Demand):
    X = Demand
    for i in range(len(X)):
     min_index = i
     for j in range(i+1, len(X)):
       if X[min_index] > X[j]:
         min_index = j
     X[i], X[min_index] = X[min_index], X[i]
    return X

def check_end(Demand):
    for i in range(0, len(Demand)):
        if Demand[i] != 0:
            return False
    return True

def check_group(indexelem):
    return (indexelem % 2) 

def analyze_vector(current_row, g1_counter, freed_num):
    g1_counter = 0
    freed_num = 0
    for i in range(0,len(current_row)):
        if -1 == current_row[i]:
            freed_num = freed_num+1
        else:
            if check_group(current_row[i]):
                g1_counter+=1
    return g1_counter, freed_num

def put(Alloc, idd, num):
    flag = False
    fflag = False
    counter = 0
    g1_counter = 0
    freed = 0

    for row in range(0,9):
        g1_counter, freed =  analyze_vector(Alloc[row], g1_counter, freed)
        if 0 == freed:
            continue
        if 1 == check_group(idd):
            if(g1_counter == 15):
                continue
        for column in range(0,24):
            if(Alloc[row][column] == -1 and counter < num):
                flag = True
                Alloc[row][column] = idd
                if check_group(idd) == 1:
                    g1_counter+=1
                    if g1_counter == 15:
                        fflag = True
                        break
                counter+=1
            elif counter == num:
                fflag = True
                break
        if fflag == True:
            break
    num = num - counter
    
    return flag, num

def Allocate(round, Demand, Alloc):
    need = 0
    element = 0
    max_users = 5
    users_count = 0
    flag = False

    sorted = Demand[:]
    tmp = sorted[:]
    index = selectsort(tmp)
    while(0 != len(sorted)):
        if users_count >= max_users:
            break
        element = sorted[-1]
        sorted.remove(sorted[sorted.index(element)])

        idd = index[-1]
        index.remove(index[index.index(idd)])

        need = math.ceil(element/10)
        users_count = users_count+1
        cnt = 0
        while True:
            flag, need = put(Alloc, idd, need)
            if flag == False:
                print("LOOP Detected")
                break
            if need == 0:
                break
        Demand[Demand.index(idd)] = 0
        print("Alloc[{0}]".format(round), Alloc)
        # break
    return check_end(Demand)

def main():  
    myround = 0
    Demand = []
    Alloc = []  
    for i in range(0,9):
        Demand.append(random.randint(1,250))
    while True:
        print("Demand before: ", Demand)
        Alloc = [[-1 for item in range(0,24)] for item in range(0,9)]
        Allocate(myround,Demand, Alloc)
        myround+=1
        print("Demand after: ", Demand)
        print("check_end: ", check_end(Demand))
        print("-----------------------------------------------------------------------------------------------------")
        if check_end(Demand) != False:
            break
    return

main()