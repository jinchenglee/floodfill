import numpy as np
from copy import deepcopy

golden_path = []

def fill(cur_distance=0, cur_pos=(0,0), tgt_pos=(1,1), obstacles=[], path_map=[], tmp_best_distance=255, tmp_path=[]): 
    """
    Shortest path finding using flood-fill algorithm. Recursive calling, distance 
    increments 1 for every call. Path_map records the distances for every position.

    Parameters:
    ----------
    cur_distance: integer to represent distance of cur_pos to start position. Start with 0.
    cur_pos: Tuple of coordinates (x,y) of current standpoint.
    tgt_pos: Tuple of coordinates of target position.
    obstacles: A list of coordinates tuples of obstacles that path has to get around. 
    path_map: A MxN array to hold distance from each (x,y) position to starting point.
    tmp_best_distance: Current the best distance during searching. Passing between recursive calls.
    tmp_path: Current shortest path to target. Passing between recursive calls.

    Returns:
    ---------
    distance: Shortest distance till current call. 
    golden_path: Final shortest path after all searches. 
    """

    global golden_path

    # Get boundaries of search
    M,N = path_map.shape
    # Pos
    x = cur_pos[0]
    y = cur_pos[1]
    tgt_x = tgt_pos[0]
    tgt_y = tgt_pos[1]

    # Update path map
    path_map[x,y] = cur_distance
    # Distance update
    nxt_distance = cur_distance + 1
    # Debug print
    #print("(x,y)=(",x,",", y,") cur_distance =", cur_distance, "best_distance =", tmp_best_distance)

    # At the target already!
    if (cur_pos == tgt_pos):
        print("At the target! Best_distance = ", cur_distance)
        golden_path = deepcopy(tmp_path)
        #print(path_map)
        #print(golden_path)
        return cur_distance,golden_path

    if tmp_best_distance > nxt_distance:

        # West
        if x-1 >= 0:
            if path_map[x-1,y]>nxt_distance and ((x-1,y) not in obstacles):
                tmp_path.append((x,y))
                tmp_best_distance,golden_path = fill(nxt_distance, (x-1,y), tgt_pos, obstacles, path_map, tmp_best_distance, tmp_path)
                tmp_path.pop()
        #else:
        #    print("Hit wall! West side")

        # East 
        if x+1 < M:
            if path_map[x+1,y]>nxt_distance and ((x+1,y) not in obstacles):
                tmp_path.append((x,y))
                tmp_best_distance,golden_path = fill(nxt_distance, (x+1,y), tgt_pos, obstacles, path_map, tmp_best_distance, tmp_path)
                tmp_path.pop()
        #else:
        #    print("Hit wall! East side")

        # North
        if y-1 >= 0:
            if path_map[x,y-1]>nxt_distance and ((x,y-1) not in obstacles):
                tmp_path.append((x,y))
                tmp_best_distance,golden_path = fill(nxt_distance, (x,y-1), tgt_pos, obstacles, path_map, tmp_best_distance, tmp_path)
                tmp_path.pop()
        #else:
        #    print("Hit wall! North side")

        # South
        if y+1 < N:
            if path_map[x,y+1]>nxt_distance and ((x,y+1) not in obstacles):
                tmp_path.append((x,y))
                tmp_best_distance,golden_path = fill(nxt_distance, (x,y+1), tgt_pos, obstacles, path_map, tmp_best_distance, tmp_path)
                tmp_path.pop()
        #else:
        #    print("Hit wall! South side")

    return tmp_best_distance,golden_path


# Boundary of search
M,N = 15, 12
start_pos = (10,3)
tgt_pos = (6,6)
obstacles=[(1,2),(2,2),(2,3),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(5,7),(5,6)]
path_map = np.zeros((M,N)) + 255
tmp_path = []
distance = 255

distance,golden_path = fill(0, start_pos, tgt_pos, obstacles, path_map, 255, tmp_path)

path_map[tgt_pos[0], tgt_pos[1]] = -1
print("start (",start_pos[0], start_pos[1],"), end (", tgt_pos[0], tgt_pos[1], ")")
print(path_map)
print(golden_path)

for pos in golden_path:
    path_map[pos] = 111
for pos in obstacles:
    path_map[pos] = 888


print(path_map)
