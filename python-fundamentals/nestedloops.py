import time 
start_time = time.time()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
#outer loop
for x in list1: # runs 9 times
    count += 1
    #inner loop
    for y in list2: # runs 9 time for each iteration of the outer loop so 9 * 9 = 81
        count += 1
print(count)


for i in range(10): 
    #inner loop
    for j in range(10):
        print(0, end=' ')
    print()  # New line after each inner loop completes

    for i in range(100000000): 
    #inner loop
     for j in range(1000000):
        print(0, end=' ')
    print()  # New line after each inner loop completes

    print(round(time.time() - start_time, 2))

    #^ track the amount of time it takes to run the code to display 
    # how run time is affected as our values get larget