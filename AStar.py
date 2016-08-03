import numpy as np

class AStar(object):
    """
        AStar shortest path searching algorithm. 
        Good intro to the algo.: http://www.redblobgames.com/pathfinding/a-star/introduction.html

        Parameters:
        ----------
        M: Horizontal width of searching area.
        N: Vertical height of searching area.
        start_pos: Tuple holding (x,y) coordinates of starting position.
        end_pos: Tuple holding (x,y) coordinates of destination position.
    """

    def __init__(self, M, N):
        """
        Initialize variables required.

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


    def findpath(self, start_pos, end_pos)
        """
        Finding the path.
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
       
    def drawpath(self)
        """
        Print out the shortest path just found.
        """
