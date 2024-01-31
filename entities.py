import os

from pygame import image, Rect, transform
from pygame.sprite import DirtySprite

TILE_SIZE = 100

entity_path = os.path.join(os.getcwd(), "assets")

sprite_dict = {
    "a_agent": os.path.join(entity_path, "agent_miku.png"),
    "b_agent": os.path.join(entity_path, "red_agent.png"),
}



def load_img(path):
    """
    :param path: Location of the image to load.
    :return: A loaded sprite with the pixels formatted for performance.
    """
    return image.load(path).convert_alpha()


def get_gui_window_icon():
    """
    :return: The icon to display in the render window.
    """
    return image.load(sprite_dict["game_icon"])


class Entity(DirtySprite):
    def __init__(self, entity_type, location):
        """
        :param entity_type: String specifying which sprite to load from the sprite dictionary (sprite_dict)
        :param location: [X, Y] location of the sprite. We calculate the pixel position by multiplying it by cell_sizes
        """
        DirtySprite.__init__(self)
        self._image = transform.scale(  # Load, scale and record the entity sprite
            load_img(sprite_dict[entity_type]), (TILE_SIZE, TILE_SIZE)
        )
        self.update_rect(location)  # do the initial rect update

    def update_rect(self, new_loc):
        """
        :param new_loc: New [X, Y] location of the sprite.
        :return: Nothing, but the sprite updates it's state so it is rendered in the right place next iteration.
        """
        self.rect = Rect(
            new_loc[0] * TILE_SIZE, new_loc[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE
        )

    @property
    def IMAGE(self):
        return self._image
