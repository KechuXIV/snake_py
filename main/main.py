#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import collections
import pygame as pg

from Control import Control

try:
    import Queue as queue
except ImportError:
    import queue

LEVELS = None
FONT = None
CAPTION = "Snake"
SCREEN_SIZE = (544, 544)
PLAY_RECT = pg.Rect(16, 16, 512, 512)
CELL = pg.Rect(0, 0, 16, 16)
BOARD_SIZE = (PLAY_RECT.w//CELL.w, PLAY_RECT.h//CELL.h)
GROWTH_PER_APPLE = 3


COLORS = {"background" : (30, 40, 50), "walls" : pg.Color("lightslategrey"),
          "snake" : pg.Color("limegreen"), "head" : pg.Color("darkgreen"),
          "apple" : pg.Color("tomato")}

DIRECT_DICT = {"left" : (-1, 0), "right" : ( 1, 0),
               "up" : ( 0,-1), "down" : ( 0, 1)}

OPPOSITES = {"left" : "right", "right" : "left",
             "up" : "down", "down" : "up"}

KEY_MAPPING = {(pg.K_LEFT, pg.K_a) : "left", (pg.K_RIGHT, pg.K_d) : "right",
               (pg.K_UP, pg.K_w) : "up", (pg.K_DOWN, pg.K_s) : "down"}

def draw_cell(surface, cell, color, offset=(0,0)):
    """Draw a single cell at the desired size with an offset."""
    pos = [cell[i]*CELL.size[i] for i in (0,1)]
    rect = pg.Rect(pos, CELL.size)
    rect.move_ip(*offset)
    surface.fill(color, rect)


def make_levels():
    """Make a few levels.  Hardcoded and ugly.  Don't do this."""
    w, h = BOARD_SIZE
    r = range
    levels = [
        ({(w//2,i) for i in r(h//2-3)}|{(w//2,i) for i in r(h//2+3,h)}),
        ({(w//4,i) for i in r(3*h//5)}|{(3*w//4,i) for i in r(2*h//5,h)}),
        ({(w//2,i) for i in r(5,h-5)}|{(i,h//2) for i in r(3,w//2-3)}|
            {(i+w//2+3, h//2) for i in r(3,w//2-3)})]
    return levels


def main():
    """
    Prepare pygame, our screen, some basic loading, and start the program.
    """
    global FONTS, LEVELS
    os.environ["SDL_VIDEO_CENTERED"] = "True"
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    FONTS = {"BIG" : pg.font.SysFont("helvetica", 100, True),
             "SMALL" : pg.font.SysFont("helvetica", 50, True)}
    LEVELS = make_levels()
    Control().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()