# Complete the calculate_sizes_of_basins function below.
def calculate_sizes_of_basins(elevation_map):
    if not len(elevation_map):
        return
    
    MAX_ROW = len(elevation_map) - 1
    MAX_COL = len(elevation_map[0]) - 1
    
    def get_neighbors(row, col):
        neighbors = []
        if row < MAX_ROW:
            neighbors.append([row + 1, col])
        if col < MAX_COL:
            neighbors.append([row, col + 1])
        if row:
            neighbors.append([row - 1, col])
        if col:
            neighbors.append([row, col - 1])
            
        return neighbors
    
    def get_lowest(row, col):
        lowest = elevation_map[row][col]
        low_rc = [row, col]
        for nxt in get_neighbors(row, col):
            nxt_r, nxt_c = nxt
            nxt_val = elevation_map[nxt_r][nxt_c]
            if nxt_val < lowest:
                low_rc = [nxt_r, nxt_c]
                lowest = nxt_val
                
        return [lowest, low_rc]
    
    visited = [[False for col in row] for row in elevation_map]
    adj_list = [[[] for col in row] for row in elevation_map]
    to_visit = set((r, c) for r in range(MAX_ROW + 1) for c in range(MAX_COL + 1))
    def connect_cells():
        for row in range(MAX_ROW + 1):
            for col in range(MAX_COL + 1):
                
                # if not sink, connect to lowest
                lowest, [low_r, low_c] = get_lowest(row, col)
                if lowest != elevation_map[row][col]:
                    adj_list[row][col].append([low_r, low_c])
                    adj_list[low_r][low_c].append([row, col])
    count = []
    
    def dfs(node):
        global cells_in_basin
        visited[node[0]][node[1]] = True
        cells_in_basin += 1
        for nxt in adj_list[node[0]][node[1]]:
            if not visited[nxt[0]][nxt[1]]:
                dfs(nxt)

    connect_cells()
    print("adj_list")
    print(adj_list)
    for row in range(MAX_ROW + 1):
        for col in range(MAX_COL + 1):
            if not visited[row][col]:
                global cells_in_basin
                cells_in_basin = 0
                dfs([row, col])
                count.append(cells_in_basin)
                cells_in_basin = 0

    return count


if __name__ == "__main__":
    matrix = [[1, 5, 2], [2, 4, 7], [3, 6, 9]]

    print(matrix)
    result = calculate_sizes_of_basins(matrix)
    print("Result: " + str(result))
    

        
