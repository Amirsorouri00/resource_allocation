import random
import math


def selectsort(Demand):
    A = Demand
    # Traverse through all array elements 
    for i in range(len(A)): 
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

def check_end(Demand):
    for i in range(0, len(Demand)):
        if Demand[i] == 0:
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
    print(freed_num, g1_counter)
    return g1_counter, freed_num

def put(Alloc, idd, num):
    flag = False
    fflag = False
    counter = 0
    g1_counter = 0
    freed = 0


    for row in range(0,9):
        g1_counter, freed =  analyze_vector(Alloc[row], g1_counter, freed)
        print(g1_counter, freed)
        if 0 == freed:
            continue
        print(check_group(idd))
        if 1 == check_group(idd):
            if(g1_counter == 15):
                continue
        for column in range(0,23):
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
    return flag

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
        print(idd)
        index.remove(index[index.index(idd)])
        print(index)

        need = math.ceil(element/10)
        users_count = users_count+1
        
        while True:
            flag = put(Alloc, idd, need)
            if flag == False:
                print("LOOP Detected")
                break
            if need != 0:
                break
        Demand[Demand.index(idd)] = 0
        print("Alloc[{0}]".format(round))
        print(Alloc)
        break
    return check_end(Demand)

def main():
    Demand = []
    Alloc = []
    # print(Alloc)
    i = 0
    myround = 0
    for i in range(0,9):
        Demand.append(random.randint(1,250))
        i = i+1
    
    while True:
        Alloc = [[-1 for item in range(0,24)] for item in range(0,9)]
        Allocate(myround,Demand, Alloc)
        myround+=1
        if check_end != False:
            break
    return

main()