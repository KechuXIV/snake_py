#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg

from _Scene import _Scene
from main import PLAY_RECT
from main import FONTS

class AnyKey(_Scene):
    """A state for the start and death scene."""
    def __init__(self, title):
        _Scene.__init__(self, "GAME")
        self.blink_timer = 0.0
        self.blink = False
        self.make_text(title)
        self.reset()

    def make_text(self, title):
        """Pre-render text."""
        self.main = FONTS["BIG"].render(title, True, pg.Color("white"))
        self.main_rect = self.main.get_rect(centerx=PLAY_RECT.centerx,
                                            centery=PLAY_RECT.centery-150)
        text = "Press any key"
        self.ne_key = FONTS["SMALL"].render(text, True, pg.Color("white"))
        self.ne_key_rect = self.ne_key.get_rect(centerx=PLAY_RECT.centerx,
                                                centery=PLAY_RECT.centery+150)

    def draw(self, surface):
        """Draw primary text and blinking prompt if necessary."""
        surface.blit(self.screen_copy, (0,0))
        surface.blit(self.main, self.main_rect)
        if self.blink:
            surface.blit(self.ne_key, self.ne_key_rect)

    def update(self, now):
        """Update blinking prompt."""
        _Scene.update(self, now)
        if now-self.blink_timer > 1000.0/5:
            self.blink = not self.blink
            self.blink_timer = now

    def get_event(self, event):
        """Switch to game on keydown."""
        if event.type == pg.KEYDOWN:
            self.done = True