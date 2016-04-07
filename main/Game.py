#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg
import random

from main import LEVELS
from main import BOARD_SIZE
from main import COLORS
from main import draw_cell
from main import PLAY_RECT
from _Scene import _Scene
from Snake import Snake
from Apple import Apple

class Game(_Scene):
    """This scene is active during the gameplay phase."""
    def __init__(self):
        _Scene.__init__(self, "DEAD")
        self.reset()

    def reset(self):
        """Prepare for next run."""
        _Scene.reset(self)
        self.snake = Snake()
        self.walls = self.make_walls()
        self.apple = Apple(self.walls, self.snake)

    def make_walls(self):
        """Make the borders, and load a random level."""
        walls = set()
        for i in range(-1, BOARD_SIZE[0]+1):
            walls.add((i, -1))
            walls.add((i, BOARD_SIZE[1]))
        for j in range(-1, BOARD_SIZE[1]+1):
            walls.add((-1, j))
            walls.add((BOARD_SIZE[0], j))
        walls |= random.choice(LEVELS)
        return walls

    def get_event(self, event):
        """Pass any key presses on to the snake."""
        if event.type == pg.KEYDOWN:
            self.snake.get_key_press(event.key)

    def update(self, now):
        """Update the snake and check if it has died."""
        _Scene.update(self, now)
        self.snake.update(now)
        self.snake.check_collisions(self.apple, self.walls)
        if self.snake.dead:
            self.done = True

    def draw(self, surface):
        """Draw the food, snake, and walls."""
        surface.fill(COLORS["background"])
        draw_cell(surface, self.apple.position,
                  self.apple.color, PLAY_RECT.topleft)
        for wall in self.walls:
            draw_cell(surface, wall, COLORS["walls"], PLAY_RECT.topleft)
        self.snake.draw(surface, offset=PLAY_RECT.topleft)
