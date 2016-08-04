import numpy as np

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
        # Array holding theoretical shortest distance from (x,y) to destination.
        self.heuristic_map = np.zeros((M,N))    

        # Variable to represent farthest distance for current search. 
        # Change to whatever number represent "infinity" distance.
        self.furthest_distance = 255 

        # Array holding the shortest distance from start_pos to (x,y). 
        # Initialized to be "infinity (big enough num)", updated along with the searching algo. 
        self.distance_map = np.zeros((M,N)) + self.furthest_distance

        # Array holding link pointer to previous position leads to current 
        # position on shortest path from start to destination, in coordinates.
        # Init all entries to destination position coordinates. 
        # Single entry example: camefrom_map[2,3] = (2,2)
        self.camefrom_map = [] 

        # Frontier dictionary holds pos:distance_map[pos] pairs, representing
        # every outstanding candidate position at frontier to try.
        # Note: cannot use distance_map[pos] as key as it is not unique.
        self.frontier = {}

        # footprint list contains all tuples of coordinates that we already searched.
        footprint = []

    def add_neighbors(self, pos, distance)
        """
        Add neighbors to frontier dictionary.

        Input:
        pos: Tuple holding (x,y) coordinates of current position.
        distance: Value of self.distance_map[pos[0],pos[1]]
        """
        x = pos[0]
        y = pos[1]

        if x-1>=0:
            self.frontier.update({(pos[0]-1,pos[1]):distance+1})
        if y-1>=0: 
            self.frontier.update({(pos[0],pos[1]-1):distance+1})
        if x+1<M: 
            self.frontier.update({(pos[0]+1,pos[1]):distance+1})
        if y+1<N:
            self.frontier.update({(pos[0],pos[1]+1):distance+1})


    def findpath(self, start_pos, end_pos, obstacles)
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
         for row in range(0,M-1):
            for col in range(0,N-1):
                self.heuristic_map[row,col] = abs(start_pos[0]-tgt_pos[0]) + \
                        abs(start_pos[1]-tgt_pos[1])

        # Init the camefrom_map to destination position.
        for row in range(0,M-1):
            for col in range(0,N-1):
                self.camefrom_map[row,col] = tgt_pos

        # Start frontier dictionary with start_pos.
        self.distance_map[start_pos[0],start_pos[1]] = 0
        self.frontier.update({start_pos:0})

        # Main loop
        while True:

            # If frontier is not empty
            if not self.frontier:
                # Sort according to the recorded distances, start with the candidate
                # with current shortest distance witnessed as it is most promising. 
                sorted_list = sorted(self.frontier.values())
                # Co-ordinates of current candidate
                cur_pos = sorted_list[0] 

                # Remove cur_pos from frontier
                del self.frontier[cur_pos]
                # Add cur_pos neighbors to frontier
                add_neighbors(cur_pos, self.frontier[cur_pos])

                return True

            # Run out of frontier candidates - no path exists!
            else:
                return False

       
    def drawpath(self)
        """
        Print out the shortest path just found.
        """
