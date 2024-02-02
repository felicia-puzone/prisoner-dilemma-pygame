from enum import Enum
from entities import Entity
class Policy(Enum):
    ALWAYS_DEFECT = 1
    ALWAYS_COOPERATE = 2
    TIT_FOR_TAT = 3
    REPUTATION = 4

class Action(Enum):
    DEFECTED = 1
    COOPERATED = 2
    AVOIDED = 3

class Agent:
    def __init__(self, id, start_position, policy, render_entity, init_score = 0):
        self.id = id
        self.position = start_position
        self._policy = policy
        self.render_entity = render_entity
        self.score = 0
        self.reputation = 0
        self.last_action = None

        #movement: make a random move. Ask factory if is it ok. If true make the move.
        # Ask if there is interaction. If so, see agent and make interaction. Call entity for refresh

    def set_position(self, new_pos):
        self.position = new_pos

        self.render_entity.update_rect(new_pos)

    def get_position(self):
        return self.position

