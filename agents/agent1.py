import random
from .base_agent import BaseAgent
from common.move import Move

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["112233", "445566"]


class Agent(BaseAgent):
    def get_move(self):
        """
        Called regularly called to get the next move for your train. Implement
        an algorithm to control your train here. You will be handing in this file.

        For now, the code simply picks a random direction between UP, DOWN, LEFT, RIGHT

        This method must return one of moves.MOVE
        """

        moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        return random.choice(moves)

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["000001", "000002", "000003"]

BASE_DIRECTIONS = [
    (0, -1),  # Up
    (1, 0),  # Right
    (0, 1),  # Down
    (-1, 0),  # Left
]