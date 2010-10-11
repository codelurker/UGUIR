SPRITE_SIZE = 32

WINDOW_W, WINDOW_H = 1024, 768
VIEWPORT_W, VIEWPORT_H = 25, 20

MAP_W, MAP_H = VIEWPORT_W * SPRITE_SIZE, VIEWPORT_H * SPRITE_SIZE
DEFAULT_MAP_CELLS_X, DEFAULT_MAP_CELLS_Y = 300, 300

MSGBOX_W, MSGBOX_H = MAP_W, WINDOW_H - MAP_H
MSGBOX_X, MSGBOX_Y = 0, MAP_H

OUTLINE_W, OUTLINE_H = 224, 400
OUTLINE_X, OUTLINE_Y = MAP_W, MAP_H - OUTLINE_H

MSGBOX_LINES = 7

DUNGEON_WALL = 0
DUNGEON_FLOOR = 1

CLOSE_TO_EDGE = 164

#MAP GENERATION STUFF
MINIMUM_ROOM_SIZE = 4
BSP_RECURSION_DEPTH = 10

DEFAULT_MSGSTYLE = dict(font_name='Arial', font_size=10, color=(255,255,255,255))

bonus = {
         "1": -6,
         "2": -5,
         "3": -5,
         "4": -4,
         "5": -4,
         "6": -3,
         "7": -3,
         "8": -2,
         "9": -2,
         "10": -1,
         "11": 0,
         "12": 0,
         "13": 0,
         "14": 1,
         "15": 2,
         "16": 4,
         "17": 5,
         "18": 6
         }
