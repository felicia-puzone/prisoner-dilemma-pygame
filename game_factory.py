from agent import Agent, Policy
from grid_env import GridEnvironment
from entities import Entity
from renderer import GameRenderer
import random
import time
from timer import RepeatedTimer
import logging


class GameFactory:
    def __init__(self, grid_size, num_agents, game_strategy=0, num_steps = 10):
        self._num_agents = num_agents
        self._num_steps = num_steps
        self._list_agents = []
        self._grid_size = grid_size
        self._num_pos = grid_size[0] * grid_size[1]
        self._renderer = GameRenderer(self._grid_size, 'Prova')
        self._game_strategy = game_strategy
        self._occupied_positions = {}
        self.init_agents()
        self.add_entities_to_renderer()
        self._renderer.update()
        self._timer = RepeatedTimer(1, self.move_step)
        self.global_total_score = 0


    # Random initialization
    def init_agents(self):
        for i in range(self._num_agents):
            max_iter = 100
            while max_iter > 0:
                start_position = (random.randrange(self._grid_size[0]), random.randrange(self._grid_size[1]))
                if self.position_available(start_position):

                    entity = Entity(
                        entity_type="normal_agent", location=start_position
                    )
                    agent = Agent(id=i + 1, start_position=start_position, policy=Policy.ALWAYS_DEFECT,
                                  render_entity=entity)
                    self._list_agents.append(agent)
                    self._occupied_positions.update({start_position: agent})
                    max_iter = 0


                else:
                    max_iter = max_iter - 1

        logging.info('%d Agents initialized.' % self._num_agents)

    def position_available(self, pos):
        if pos not in self._occupied_positions.keys():
            return True
        else:
            return False

    def add_entities_to_renderer(self):
        for elem in self._list_agents:
            self._renderer.list_entities.append(elem.render_entity)

    def _reset_entity_state(self):
        for entity in self._renderer.list_entities:
            entity.change_entity_state(entity_type="normal_agent")

    # Anticollision random spawn: same map as below. if not present => can spawn ----------- OK

    # Random movement with anticollision --------- OK

    # Movement functions -------- OK

    # Contention meeting: there is a map position-agent for all the occupied positions. An agent moves and we search if the
    # 4-connectivity positions are in that map. If so, we retrieve the corresponding agent and start the contention.

    # Adding clock and dynamic matplotlib update

    def _move_left(self, agent):
        current_pos = agent.get_position()
        new_pos = (current_pos[0] - 1, current_pos[1])

        # Border checking
        if self._grid_size[0] > new_pos[0] >= 0 and self._grid_size[1] > new_pos[1] >= 0:

            # anticollision
            if self.position_available(new_pos):
                agent.set_position(new_pos)
                del self._occupied_positions[current_pos]
                self._occupied_positions.update({new_pos: agent})
                # self._renderer.update()
            else:
                print("position already taken")
        else:
            print("position out of border")

    def _move_right(self, agent):
        current_pos = agent.get_position()
        new_pos = (current_pos[0] + 1, current_pos[1])

        # Border checking
        if self._grid_size[0] > new_pos[0] >= 0 and self._grid_size[1] > new_pos[1] >= 0:

            # anticollision
            if self.position_available(new_pos):
                agent.set_position(new_pos)
                del self._occupied_positions[current_pos]
                self._occupied_positions.update({new_pos: agent})
                # self._renderer.update()
            else:
                print("position already taken")
        else:
            print("position out of border")

    def _move_up(self, agent):
        current_pos = agent.get_position()
        new_pos = (current_pos[0], current_pos[1] - 1)

        # Border checking
        if self._grid_size[0] > new_pos[0] >= 0 and self._grid_size[1] > new_pos[1] >= 0:

            # anticollision
            if self.position_available(new_pos):
                agent.set_position(new_pos)
                del self._occupied_positions[current_pos]
                self._occupied_positions.update({new_pos: agent})
                # self._renderer.update()
            else:
                print("position already taken")
        else:
            print("position out of border")

    def _move_down(self, agent):
        current_pos = agent.get_position()
        new_pos = (current_pos[0], current_pos[1] + 1)

        # Border checking
        if self._grid_size[0] > new_pos[0] >= 0 and self._grid_size[1] > new_pos[1] >= 0:

            # anticollision
            if self.position_available(new_pos):
                agent.set_position(new_pos)
                del self._occupied_positions[current_pos]
                self._occupied_positions.update({new_pos: agent})
                # self._renderer.update()
            else:
                print("position already taken")
        else:
            print("position out of border")

    def _random_move(self, agent):
        seed = random.randrange(4)
        match seed:
            case 0:
                self._move_up(agent)
            case 1:
                self._move_down(agent)
            case 2:
                self._move_left(agent)
            case 3:
                self._move_right(agent)

    def _global_random_move(self):
        for agent in self._list_agents:
            self._random_move(agent)

    def move_step(self):

        self._reset_entity_state()
        self._global_random_move()
        logging.info('Round %d of random moving activated' % self._num_steps)
        self.check_contentions()
        self._renderer.update()

        self._num_steps = self._num_steps - 1

        if self._num_steps == 0:
            self.stop_game()

    """
    Contention Logic Functions
    """

    def check_contentions(self):
        # Defining all the contention agents
        already_fighted = []

        for pos in self._occupied_positions:
            if self._occupied_positions[pos] not in already_fighted:
                # computing the 4-connectivity positions
                pos_up = (pos[0], pos[1] - 1)
                pos_down = (pos[0], pos[1] + 1)
                pos_left = (pos[0] - 1, pos[1])
                pos_right = (pos[0] + 1, pos[1])

                if pos_up in self._occupied_positions.keys():
                    agent1 = self._occupied_positions[pos]
                    agent2 = self._occupied_positions[pos_up]

                    agent1.render_entity.change_entity_state(entity_type="contention_agent")
                    agent2.render_entity.change_entity_state(entity_type="contention_agent")

                    self._make_contention(agent1, agent2)
                    already_fighted.append(agent1)
                    already_fighted.append(agent2)

                elif pos_down in self._occupied_positions.keys():
                    agent1 = self._occupied_positions[pos]
                    agent2 = self._occupied_positions[pos_down]

                    agent1.render_entity.change_entity_state(entity_type="contention_agent")
                    agent2.render_entity.change_entity_state(entity_type="contention_agent")

                    self._make_contention(agent1, agent2)
                    already_fighted.append(agent1)
                    already_fighted.append(agent2)

                elif pos_left in self._occupied_positions.keys():
                    agent1 = self._occupied_positions[pos]
                    agent2 = self._occupied_positions[pos_left]

                    agent1.render_entity.change_entity_state(entity_type="contention_agent")
                    agent2.render_entity.change_entity_state(entity_type="contention_agent")

                    self._make_contention(agent1, agent2)
                    already_fighted.append(agent1)
                    already_fighted.append(agent2)

                elif pos_right in self._occupied_positions.keys():
                    agent1 = self._occupied_positions[pos]
                    agent2 = self._occupied_positions[pos_right]

                    agent1.render_entity.change_entity_state(entity_type="contention_agent")
                    agent2.render_entity.change_entity_state(entity_type="contention_agent")

                    self._make_contention(agent1, agent2)
                    already_fighted.append(agent1)
                    already_fighted.append(agent2)

        already_fighted = list(dict.fromkeys(already_fighted))
        logging.info("Agents that should have been fought:")
        for i in already_fighted:
            logging.info(i.id)

    def _make_contention(self, agent1, agent2):
        logging.info("Agent %d and Agent %d had fought" % (agent1.id, agent2.id))

    def run_game(self):
        return self._renderer.render_on_display()

    def stop_game(self):
        self._timer.stop()
