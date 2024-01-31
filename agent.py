from enum import Enum
from entities import Entity
class Policy(Enum):
    ALWAYS_DEFECT = 1
    ALWAYS_COOPERATE = 2
    TIT_FOR_TAT = 3
    REPUTATION = 4

class Agent:
    def __init__(self, id, start_position, policy, render_entity):
        self.id = id
        self.position = start_position
        self._policy = policy
        self.render_entity = render_entity


        #movement: make a random move. Ask factory if is it ok. If true make the move.
        # Ask if there is interaction. If so, see agent and make interaction. Call entity for refresh

