#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

from main import COLORS
from main import queue
from main import KEY_MAPPING
from main import DIRECT_DICT
from main import OPPOSITES
from main import draw_cell
from main import GROWTH_PER_APPLE

class Snake(object):
    """Green and snakey."""
    def __init__(self):
        self.color = COLORS["snake"]
        self.speed = 8 # Cells per second
        self.direction = "up"
        self.vector = DIRECT_DICT[self.direction]
        self.body = [(10, 25), (10,24)]
        self.body_set = set(self.body)
        self.growing = False
        self.grow_number = 0
        self.timer = 0
        self.dead = False
        self.direction_queue = queue.Queue(5)

    def update(self, now):
        """Add new cell for the head.  If not growing, delete the tail."""
        if not self.dead and now-self.timer >= 1000.0/self.speed:
            self.timer = now
            self.change_direction()
            next_cell = [self.body[-1][i]+self.vector[i] for i in (0,1)]
            self.body.append(tuple(next_cell))
            if not self.growing:
                del self.body[0]
            else:
                self.grow()
            self.body_set = set(self.body)

    def change_direction(self):
        """
        Check direction queue for a new direction.  Directions parallel
        to the snakes current movement are ignored.
        """
        try:
            new = self.direction_queue.get(block=False)
        except queue.Empty:
            new = self.direction
        if new not in (self.direction, OPPOSITES[self.direction]):
            self.vector = DIRECT_DICT[new]
            self.direction = new

    def grow(self):
        """Increment grow number and reset if done."""
        self.grow_number += 1
        if self.grow_number == GROWTH_PER_APPLE:
            self.grow_number = 0
            self.growing = False

    def check_collisions(self, apple, walls):
        """Get apples and collide with body and walls."""
        if self.body[-1] == apple.position:
            apple.collide_with(self)
            self.growing = True
        elif self.body[-1] in walls:
            self.dead = True
        elif any(val > 1 for val in collections.Counter(self.body).values()):
            self.dead = True

    def get_key_press(self, key):
        """
        Add directions to the direction queue if key in KEY_MAPPING is pressed.
        """
        for keys in KEY_MAPPING:
            if key in keys:
                try:
                    self.direction_queue.put(KEY_MAPPING[keys], block=False)
                    break
                except queue.Full:
                    pass

    def draw(self, surface, offset=(0,0)):
        """Draw the whole body, then the head."""
        for cell in self.body:
            draw_cell(surface, cell, self.color, offset)
        draw_cell(surface, self.body[-1], COLORS["head"], offset)