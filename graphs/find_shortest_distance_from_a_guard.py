#
# Complete the find_shortest_distance_from_a_guard function below.
#
from collections import deque
def find_shortest_distance_from_a_guard(grid):
    #
    # Write your code here.
    #
    grid = ['OOOOG', 'OWWOO', 'OOOWO', 'GWWWO', 'OOOOG']
    #grid = ['OOOOG']
    R, C = len(grid), len(grid[0])
    def get_n(r,c):
        choice = [(r-1,c), (r+1,c), (r,c-1), (r, c+1)]
        n =[]
        for r_, c_ in choice:
            if 0 <= r_ < R and 0 <= c_ < C:
                n.append((r_,c_))
        return n
            
   
    q = deque()
    res = [[0]* C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'W':
                res[r][c] = -1
            elif grid[r][c] == 'G':
                res[r][c] = 0
                q.append([r,c,0])
            else:
                res[r][c] = -2
    while q:
        r_, c_, dist_ = q.popleft()
        n_ = get_n(r_,c_)
        for r, c in n_:
            if res[r][c] == -2:
                res[r][c] = dist_ + 1
                q.append([r,c,dist_+1])
    return res
                
