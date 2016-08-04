import numpy as np
from collections import OrderedDict

class AStar(object):
    """
        AStar shortest path searching algorithm. 
        Good intro to the algo.: http://www.redblobgames.com/pathfinding/a-star/introduction.html

    """

    def __init__(self, M, N):
        """
        Initialize variables required.

        Inputs:
        M: Horizontal width of searching area.
        N: Vertical height of searching area.

        """
        # Dimension of boundaries.
        self.M = M
        self.N = N

        # Array holding theoretical shortest distance from (x,y) to destination.
        self.heuristic_map = np.zeros((M,N))    

        # Variable to represent farthest distance for current search. 
        # Change to whatever number represent "infinity" distance.
        self.furthest_distance = 255 
        # Array holding the shortest distance from start_pos to (x,y). 
        # Initialized to be "infinity (big enough num)", updated along with the searching algo. 
        self.distance_map = np.zeros((M,N)) + self.furthest_distance

        # Dictionary holding link pointer to previous position leads to current 
        # position on shortest path from start to destination, in coordinates.
        # Init all entries to destination position coordinates. 
        # Single entry example: camefrom_map[(2,3)] = (2,2)
        self.camefrom_map = {} 

        # Frontier dictionary holds pos:guestimate_distance[pos] pairs, representing
        # every outstanding candidate position at frontier to try.
        # Note: cannot use guestimate_distance[pos] as key as it is not unique.
        #       Guestimate_distance[pos] = distance_map[pos] + heuristic_map[pos]
        self.frontier = {}

        # footprint list contains all tuples of coordinates that we already searched.
        self.footprint = []

    def add_neighbors(self, pos, distance, obstacles):
        """
        Add neighbors to frontier dictionary.

        Input:
        pos: Tuple holding (x,y) coordinates of current position.
        distance: Value of self.distance_map[pos[0],pos[1]]
        """
        
        neighbor_list = [(pos[0]-1,pos[1]), (pos[0]+1,pos[1]), \
                (pos[0],pos[1]-1), (pos[0], pos[1]+1)]
        # Processing each neighbor.
        for (x,y) in neighbor_list:
            if x>=0 and y>=0 and x<self.M and y<self.N:   # Out from boundary?
                if (x,y) not in obstacles:
                    if (x,y) not in self.footprint: # Already in done list?
                        new_distance = distance + 1 + self.heuristic_map[x,y]
                        if (x,y) not in self.frontier.keys():       # A new candidate to add to frontier set.
                            self.frontier.update({(x,y):new_distance})
                            self.distance_map[x,y] = distance + 1
                            self.camefrom_map[(x,y)] = pos
                        elif new_distance < self.frontier[(x,y)]:   # A short path reached this neighbor.
                            self.frontier[(x,y)] = new_distance
                            self.distance_map[x,y] = distance + 1
                            self.camefrom_map[(x,y)] = pos


    def findpath(self, start_pos, end_pos, obstacles):
        """
        Finding the path.

        Inputs:
        start_pos: Tuple holding (x,y) coordinates of starting position.
        end_pos: Tuple holding (x,y) coordinates of destination position.
        obstacles: A list of tuples holding obstacles coordinates.

        Returns:
        True if path finding is successful. 
        False if otherwise, say, obstacles in the way that no such path exists.
        """
        # Init the heuristic_map.
        for row in range(0,self.M):
            for col in range(0,self.N):
                self.heuristic_map[row,col] = abs(row-end_pos[0]) + \
                    abs(col-end_pos[1])
        print(self.heuristic_map)

        # Init the camefrom_map to destination position.
        for row in range(0,self.M-1):
            for col in range(0,self.N-1):
                self.camefrom_map[(row,col)] = end_pos
        print(self.camefrom_map)

        # Start frontier dictionary with start_pos.
        self.distance_map[start_pos[0],start_pos[1]] = 0 
        guestimate_distance = 0 + self.heuristic_map[start_pos[0],start_pos[1]]
        self.frontier.update({start_pos:guestimate_distance})
        print(self.distance_map)
        print(self.frontier)
        print(self.footprint)

        # Main loop
        while True:

            # If frontier is not empty
            if bool(self.frontier):
                # Sort according to the recorded distances, start with the candidate
                # with current shortest distance witnessed as it is most promising. 
                sorted_list = sorted(self.frontier, key=self.frontier.get)
                # Co-ordinates of current candidate
                cur_pos = sorted_list[0] 

                # At the target position!
                if cur_pos == end_pos:
                    print("Succeed!")
                    return True

                # Add cur_pos neighbors to frontier
                self.add_neighbors(cur_pos, self.distance_map[cur_pos[0],cur_pos[1]], obstacles)

                # Remove cur_pos from frontier, and add to done list
                del self.frontier[cur_pos]
                self.footprint.append(cur_pos)

                #self.debugprint(cur_pos)


            # Run out of frontier candidates - no path exists!
            else:
                print("Failed to find path!")
                return False

       
    def debugprint(self, cur_pos):
        """
        Print out the debug info.
        """    
        print("cur_pos = ", cur_pos)
        print("Distance map:")
        print(self.distance_map)
        print("Frontier:")
        print(sorted(self.frontier.items(), key=lambda x:x[1] ))
        print("Footprint:")
        print(self.footprint)
        print("--------------")

    def drawpath(self,obstacles):
        """
        Print out the shortest path just found.
        """
        for i in obstacles:
            self.distance_map[i[0],i[1]]=44
        print("Distance map")
        print(self.distance_map)
        for i in self.footprint:
            self.distance_map[i[0],i[1]]=88
        print("Evaluated path")
        print(self.distance_map)

astar = AStar(13,12)
start_pos = (12,7)
end_pos = (1,4)
obstacles=[(1,2),(2,2),(2,3),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(8,5),(8,6),(8,7),(7,7),(6,7),(5,7),(5,6)]
astar.findpath(start_pos, end_pos, obstacles)
astar.drawpath(obstacles)

