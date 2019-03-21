def steps_hanoi(num_disks):
    #
    # Write your code here.
    #
    A, B, C = [], [], []
    A.extend(range(1, num_disks+1))
    def move(n, src, dst, tmp):
        if n > 0:
            # move n - 1 disks from src to tmp, so they are out of the way
            move(n - 1, src, tmp, dst)
            # move the nth disk from src to dst
            dst.append(src.pop())
            # Display our progress
            print(A, B, C, '##############', sep = '\n')
            
            # move the n - 1 disks that we left on tmp onto dst
            move(n - 1, tmp, dst, src)
    
    # initiate call from src A to dst C with tmp B
    move(num_disks, A, C, B)
steps_hanoi(3)
