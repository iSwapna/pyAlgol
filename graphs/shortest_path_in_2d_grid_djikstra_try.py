# Trial with Djikstras - is there a way to improve from BFS brute force?
#   1. When a Gate is found without a key, how can you minimally back track
#   2. Djikstra is useful only when there are wts to reduce the relative
#      distance due to wt-ed edges
#
#
def is_ground(cell):
    return cell is '.' or cell is '+'

def print_aList(a_list):
    for item in a_list:
        print(item)

    


def is_gate(cell):
    return 'A' <= cell <= 'Z'

def is_key(cell):
    return 'a' <= cell <= 'z'
    
    
from heapq import *
def find_shortest_path(grid):
    heap = []
    #print(grid)
    dist = [[9999 for col in row] for row in grid]
    keys = [[set() for col in row] for row in grid]
    parent = [[list() for col in row] for row in grid]
    
    def get_path(row, col):
        res = []
        while grid[row][col] is not '@':
            res.append([row,col])
            print(parent[row][col])
            print(res)
            row, col = parent[row][col]
        res.append([row, col])
        res.reverse()
        return res
            
    def get_near(row, col):
        max_r, max_c = len(grid), len(grid[0])
        res = []
        if row + 1 < max_r:
            res.append([row + 1, col])
        if row:
            res.append([row -1, col])
        if col:
            res.append([row, col - 1])
        if col + 1 < max_c:
            res.append([row, col + 1])
            
        return res
    
    def has_key(cell, row, col):
        return cell in keys[row][col]
    
    def relax(cell, row, col):
        for near in get_near(row, col):
            n_r, n_c = near
            near_cell = grid[n_r][n_c]
            print("near:")
            print(near)
            if is_ground(near_cell) or is_key(near_cell) or (is_gate(near_cell) and has_key(near_cell, row, col)):
                if dist[row][col] + 1 < dist[n_r][n_c]:
                    dist[n_r][n_c] = dist[row][col] + 1
                    print("reduced dist: " + str(n_r) + ":" + str(n_c))
                    print(dist[n_r][n_c])
                    
                    keys[n_r][n_c] = keys[row][col]
                    heappush(heap, (dist[n_r][n_c], n_r, n_c))
                    parent[n_r][n_c] = [row, col]
                    #print(keys[n_r][n_c])
                    
            if is_key(near_cell):
                keys[n_r][n_c].add(near_cell.upper())

            
    #init pq
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem is "@":
                heappush(heap, (0, i, j))
                dist[i][j] = 0
            if elem is "." or elem is '+':
                heappush(heap, (9999, i, j)) # has a comparable with int, like MAX_INT?
    
    #print(heap)
    while heap:
        dis, row, col = heappop(heap)
        print("from pq: row: " + str(row) + " :col: " + str(col) + " :dis: " + str(dis))
        cell = grid[row][col]
        
        if cell is '+':
            print(dis)
            return get_path(row, col)
        relax(cell, row, col)
                







