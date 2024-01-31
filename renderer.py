import pygame as pg
from entities import Entity

"""
Constants
"""
BACKGROUND_COLOR = (11, 11, 69)
GRID_LINE_COLOR = (50, 205, 50, 50)
CLEAR = (0, 0, 0, 0)
TILE_SIZE = 100


class GameRenderer:
    def __init__(self, grid_size, window_title):
        """
        :param grid: Class-based representation of the game state. Feeds all the information necessary to the renderer
        :param window_title: What we set as the window caption
        :param screen_size: The size of the virtual display on which we will be rendering stuff on
        """

        pg.init()  # initialize pygame
        pg.display.set_caption(window_title)  # set the window caption

        self._clock = pg.time.Clock()  # create clock object
        self._grid = grid_size
        self._screen = None  # temp screen attribute
        grid_size = grid_size
        game_surface_size = TILE_SIZE * grid_size[0] + 2, TILE_SIZE * grid_size[1] + 2

        self._screen_size = game_surface_size

        self._screen = pg.display.set_mode(
            self._screen_size
        )

        # Create a background
        self._background = pg.Surface(
            game_surface_size
        ).convert()  # here we create and fill all the surfaces
        self._background.fill(BACKGROUND_COLOR)
        # Create a layer for the grid
        self._grid_layer = pg.Surface(game_surface_size).convert_alpha()
        self._grid_layer.fill(CLEAR)
        self._draw_grid()
        #Create a layer for the entities
        self._entity_layer = pg.Surface(game_surface_size).convert_alpha()
        self._entity_layer.fill(CLEAR)
        #Create the entities (agents)
        self.list_entities = []

        self._draw_entities()


    def _init_display(self):
        self._screen = pg.display.set_mode(
            self._screen_size
        )  # instantiate virtual display


    def render_on_display(self):
        """
        Renders the current frame on the virtual display.
        :return:
        """
        self._screen.blit(self._background, (0, 0))
        self._background.blit(self._grid_layer, (0, 0))
        self._background.blit(self._entity_layer, (0, 0))
        pg.display.flip()


    def _draw_grid(self):
        """
        Draws the grid lines to the grid layer surface.
        :return:
        """

        # drawing the horizontal lines
        for y in range(self.GRID_H + 1):
            pg.draw.line(
                self._grid_layer,
                GRID_LINE_COLOR,
                (0, y * TILE_SIZE),
                (self.SCREEN_W, y * TILE_SIZE),
                2
            )

        # drawing the vertical lines
        for x in range(self.GRID_W + 1):
            pg.draw.line(
                self._grid_layer,
                GRID_LINE_COLOR,
                (x * TILE_SIZE, 0),
                (x * TILE_SIZE, self.SCREEN_H),
                2
            )

    def _draw_entities(self):
        # Agents
        for entity in self.list_entities:
            self._entity_layer.blit(
                entity.IMAGE, (entity.rect.left, entity.rect.top))

    def update(self):
        self._draw_entities()

    """
    Properties
    """
    @property
    def SCREEN_SIZE(self):
        return tuple(self._grid)

    @property
    def SCREEN_W(self):
        return int(self._grid[1] * TILE_SIZE + 4)

    @property
    def SCREEN_H(self):
        return int(self._grid[0] * TILE_SIZE + 4)
    @property
    def GRID_W(self):
        return self._grid[1]

    @property
    def GRID_H(self):
        return self._grid[0]
