
import pygame
from grid_env import GridEnvironment
from renderer import GameRenderer

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Let's init the grid object filled with some rand position item")

    grid = GridEnvironment((6, 6))

    #Now i need to build the renderer

    renderer = GameRenderer(grid, 'Prova')

    running = True
    while running:

        renderer.render_on_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pass

    """

    ar = AbstractRenderer('prova')

    running = True
    while running:

        ar.render_on_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    """
