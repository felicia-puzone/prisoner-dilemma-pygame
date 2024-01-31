import numpy as np
from enum import Enum
class Init_type(Enum):
    RANDOM = 1


class GridEnvironment:
    def __init__(self, grid_size, list_agents, init_type):
        """
        :param grid_size: A (W, H) tuple corresponding to the grid dimensions. Better if H=W
        """
        self._grid_size = grid_size

        #NP Array: 0 is empty space, 1-N are Agents' id

        self._grid = np.zeros(grid_size, dtype=np.int8)

        #some rand init for testing

        self._grid[2, 2] = 1






    """
    Properties
    """

    @property
    def GRID_DIMENSIONS(self):
        return self.GRID_W, self.GRID_H

    @property
    def GRID_W(self):
        return int(self._grid_size[0])

    @property
    def GRID_H(self):
        return int(self._grid_size[1])