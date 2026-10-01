import time
count =  0
def hanoi_solve(n, source, target, auxiliary,display_progres):
    global count
    global A,B,C
    
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        hanoi_solve(n - 1, source, auxiliary, target,display_progres)

        # Move the last disk from source to target
        target.append(source.pop())

        # Count our iterations
        count += 1
        # Display our progress
        if display_progres:
            print ("%d ############" % count)
            print ("A", A)
            print ("B", B)
            print ("C", C)
        
        # Move the n - 1 disks that we left on auxiliary onto target, using source as auxiliary
        hanoi_solve(n - 1, auxiliary, target, source,display_progres)
        
    return count

print ("hanoi_solve Defined")



count = 0
size = 3
A = list(range(size,0,-1))
B = []
C = []
print (f"Hanoi Problems solved in {hanoi_solve(size, A, C, B,True)} steps")


hanoi_t = []
hanoi_s = []

for size in range(2,25):
    count = 0     
    A = list(range(size,0,-1))
    B = []
    C = []
    t0 = time.time()
    count = hanoi_solve(size, A, C, B,False)
    e_t = time.time() - t0
    hanoi_t.append(count)
    hanoi_s.append(size)

    print ("Solving Hanoi of size %d takes %d iterations and %.4f secs" % ( size,count, e_t))
    