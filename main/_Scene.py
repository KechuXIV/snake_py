#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg

class _Scene(object):
    """Overly simplified Scene."""
    def __init__(self, next_state=None):
        self.next = next_state
        self.done = False
        self.start_time = None
        self.screen_copy = None

    def startup(self, now):
        """Set present time and take a snapshot of the display."""
        self.start_time = now
        self.screen_copy = pg.display.get_surface().copy()

    def reset(self):
        """Prepare for next time scene has control."""
        self.done = False
        self.start_time = None
        self.screen_copy = None

    def get_event(self, event):
        """Overload in child."""
        pass

    def update(self, now):
        """If the start time has not been set run necessary startup."""
        if not self.start_time:
            self.startup(now)