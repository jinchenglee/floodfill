import numpy as np

def fill(cur_distance=0, cur_pos=(0,0), tgt_pos=(1,1), obstacles=[], path_map=[], best_distance=255): 
    """
    Shortest path finding using flood-fill algorithm. Recursive calling, distance 
    increments 1 for every call. Path_map records the distances for every position.

    Parameters:
    ----------
    cur_distance: integer to represent distance of cur_pos to start position. Start with 0.
    cur_pos: Tuple of coordinates (x,y) of current standpoint.
    tgt_pos: Tuple of coordinates of target position.
    obstacles: A list of coordinates tuples of obstacles that path has to get around. 

    Returns:
    ---------
    Shortest distance till current call. 
    In the meantime, ``path_map`` records are updated lively.
    """
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
    print("(x,y)=(",x,",", y,") cur_distance =", cur_distance, "best_distance =", best_distance)

    # At the target already!
    if (cur_pos == tgt_pos):
        print("At the target! Best_distance = ", cur_distance)
        print(path_map)
        return cur_distance


    if best_distance > nxt_distance:
        # West
        if x-1 >= 0:
            if path_map[x-1,y]>nxt_distance:
                best_distance = fill(nxt_distance, (x-1,y), tgt_pos, obstacles, path_map, best_distance)
        else:
            print("Hit wall! West side")
        # East 
        if x+1 < M:
            if path_map[x+1,y]>nxt_distance:
                best_distance = fill(nxt_distance, (x+1,y), tgt_pos, obstacles, path_map, best_distance)
        else:
            print("Hit wall! East side")
        # North
        if y-1 >= 0:
            if path_map[x,y-1]>nxt_distance:
                best_distance = fill(nxt_distance, (x,y-1), tgt_pos, obstacles, path_map, best_distance)
        else:
            print("Hit wall! North side")
        # South
        if y+1 < N:
            if path_map[x,y+1]>nxt_distance:
                best_distance = fill(nxt_distance, (x,y+1), tgt_pos, obstacles, path_map, best_distance)
        else:
            print("Hit wall! South side")

    return best_distance


# Boundary of search
M,N = 10, 10
start_pos = (2,8)
tgt_pos = (9,0)
obstacles=[]
path_map = np.zeros((M,N)) + 255

fill(0, start_pos, tgt_pos, obstacles, path_map, 255)

path_map[tgt_pos[0], tgt_pos[1]] = -1
print("start (",start_pos[0], start_pos[1],"), end (", tgt_pos[0], tgt_pos[1], ")")
print(path_map)
