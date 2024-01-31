
import pygame
from grid_env import GridEnvironment
from game_factory import GameFactory

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Let's init the grid object filled with some rand position item")


    #Now i need to build the renderer
    game = GameFactory(grid_size=(6, 6), num_agents=4)

    running = True
    while running:

        game.run_game()

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
