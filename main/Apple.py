#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from main import COLORS
from main import BOARD_SIZE

class Apple(object):
    """Something edible.  Causes unrestricted growth in some animals."""
    def __init__(self, walls, snake):
        self.position = self.respawn(snake.body_set|walls)
        self.walls = walls
        self.color = COLORS["apple"]

    def collide_with(self, snake):
        """If eaten find a new home."""
        self.position = self.respawn(snake.body_set|self.walls)

    def respawn(self, obstacles):
        """Don't land in a wall or inside the snake."""
        position = tuple(random.randrange(BOARD_SIZE[i]) for i in (0,1))
        while position in obstacles:
            position = tuple(random.randrange(BOARD_SIZE[i]) for i in (0,1))
        return position