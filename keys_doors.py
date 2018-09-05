# bfs based solution
# 
from collections import deque
def find_shortest_path(grid):
    
    def is_door(ch):
        return 'A' <= ch <= 'J'
    
    def is_key(ch):
        return 'a' <= ch <= 'j'
    
    def is_start(ch):
        return ch is '@'
    
    def is_goal(ch):
        return ch is '+'
    
    def is_land(ch):
        return ch is '.'
    
    def can_open_door(door, keys):
        return keys >> (ord(door) - ord('A')) & 1
    
    #to keep track of
    # 1. distance grid - distance from start to this cell, for this route
    #                  - this route is characterised by a unique set of keys
    # 2. parent grid - parent from which this state was reached in the distance grid
    # 3. Visited grid
    MAX_KEYS  = 10
    MAX_MASK, MAX_ROW, MAX_COL = 1 << MAX_KEYS, len(grid), len(grid[0])
    INF = MAX_ROW * MAX_COL * MAX_MASK + 1 
    
    def neighbors(row, col):
        result = []
        
        if row + 1 < MAX_ROW:
            result.append([row + 1, col])
        if col + 1 < MAX_COL:
            result.append([row, col + 1])
        if row:
            result.append([row - 1, col])
        if col:
            result.append([row, col - 1])
        
        return result
    # 
    distance = [[[INF for ch in range(MAX_MASK)] for col in range(MAX_COL)] for row in range(MAX_ROW)]
    parent = [[[list() for ch in range(MAX_MASK)] for col in range(MAX_COL)] for row in range(MAX_ROW)]
    
    # ALGORITHM
    # scan grid and find start and goal cells
    # do bfs (dfs should work too)
    #         - every move creates a new potential path to the goal which could be the shortest (brute force -backtrack)
    #         - adding a ground/gate/water node does not change the current path in any way- a normal bfs move
    #         - adding a new key, adds new possible future paths where a corresponding Gate could be crossed.
    #         - adding a new key, could also travel through already explored nodes to find a Gate that is now cross-able.
    #         - following from the above, we only need to keep track of path changes where the combinations of keys are uniq
    # find out shortest path in candidates
    # build path from back pointers and return
    
    def bfs():
        
        distance[start[0]][start[1]][0] = 0
        q = deque()
        q.appendleft([start, 0])
        
        while q:
            frm = q.pop()
            frm_r, frm_c = frm[0][0], frm[0][1]
            frm_ch, frm_keys = grid[frm_r][frm_c], frm[1]
            
            # need to be in queue to have been processed when discovered to update distance
            if is_goal(frm_ch):
                continue
                
            for nxt in neighbors(frm_r, frm_c):
                to_r, to_c, to_ch = nxt[0], nxt[1], grid[nxt[0]][nxt[1]]
                
                if is_land(to_ch) or is_goal(to_ch) or is_start(to_ch) or \
                (is_door(to_ch) and can_open_door(to_ch, frm_keys)) or is_key(to_ch):
                    
                    new_keys = frm_keys
                    if is_key(to_ch):
                        new_keys = frm_keys | 1 << (ord(to_ch) - ord('a'))
                 
                    if not parent[to_r][to_c][new_keys]:
                        parent[to_r][to_c][new_keys] = frm
                        distance[to_r][to_c][new_keys] = distance[frm_r][frm_c][frm_keys] + 1
                        q.appendleft([[to_r, to_c], new_keys])          
    
    def get_start_and_goal():
        for r in range(MAX_ROW):
            for c in range(MAX_COL):
                if grid[r][c] is '@':
                    start = [r, c]
                if grid[r][c] is '+':
                    goal = [r, c]
                    
        return (start, goal)
            
    
    start, goal = get_start_and_goal()
    bfs()
    
    shortest_path_keyset = 0
    distance_to_goal = distance[goal[0]][goal[1]][:]
    distance = None # release memory?
    min_distance = distance_to_goal[0]
    
    for keyset, dist in enumerate(distance_to_goal):
        if dist < min_distance:
            min_distance = dist
            shortest_path_keyset = keyset
            
    #build path to goal
    path = [goal]
    prnt = [[goal[0], goal[1]], shortest_path_keyset]
    while prnt[0] is not start:
        prnt = parent[prnt[0][0]][prnt[0][1]][prnt[1]]
        path.append(prnt[0])
        
    path.reverse()
    return path

if __name__ == '__main__':

    grid1 = [['.', '.', '.', 'B'], \
             ['.', 'b', '#', '.'], \
             ['@', '#', '+', '.']]
    
    result = find_shortest_path(grid1)
    print(result)
    assert(result == [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [2, 2]])
    

