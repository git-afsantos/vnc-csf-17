#!/usr/bin/env python

from math import pi
from pyguki import simulator
from . import desafio

WIDTH = 9
HEIGHT = 4
OX = 0.2
OY = 0.32
OA = pi/4
OBSTACLES = [(3, 0), (3, 1), (3, 2), (2, 1),
             (0, 3), (0, 4), (0, 5), (1, 4),
             (3, 7), (3, 8), (2, 8)]

simulator.run(width = WIDTH, height = HEIGHT, ox = OX, oy = OY, oa = OA,
              obstacles = OBSTACLES,
              goal = (1.92, 0, 0.96, 1.28),
              callbacks = {
                "init":         getattr(desafio, "quando_inicia"),
                "bump_center":  getattr(desafio, "quando_bate_na_frente", None),
                "bump_left":    getattr(desafio, "quando_bate_na_esquerda", None),
                "bump_right":   getattr(desafio, "quando_bate_na_direita", None),
                "walk_done":    getattr(desafio, "andar_feito", None),
                "rotate_done":  getattr(desafio, "rodar_feito", None)
              })
