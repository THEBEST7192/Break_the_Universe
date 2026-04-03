import math

from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle
from pyglet.graphics import Batch
from pyglet import clock


def hex_to_rgba(hex_color):
    return (
        int(hex_color[1:3], 16),
        int(hex_color[3:5], 16),
        int(hex_color[5:7], 16),
        255
    )


class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Solar System (Spawning Planets)")
        self.batch = Batch()

        self.cx, self.cy = 320, 320
        self.sun = Circle(self.cx, self.cy, 25, color=hex_to_rgba("#F9F871"), batch=self.batch)

        # Planets we *will* spawn later (specs only, no Circles yet)
        self.planet_specs = [
            # distance, speed, radius, color
            (70, 0.4, 7,  "#FACCFF"),  # Venus
            (100, 0.3, 10, "#00D2FC"), # Earth
            (140, 0.2, 6,  "#C34A36"), # Mars
            (280, 0.1, 16, "#FFC75F"), # Jupiter
        ]

        # Spawned planets live here: list of (distance, speed, Circle)
        self.planets = []

        self.angle = 0.0

        # Spawning control
        self.spawn_interval = 20.0   # seconds between spawns
        self.spawn_timer = 0.0
        self.next_to_spawn = 0       # index into planet_specs

        # Optional: spawn the first planet immediately
        # self.spawn_next_planet()

    def spawn_next_planet(self):
        if self.next_to_spawn >= len(self.planet_specs):
            return  # all spawned

        distance, speed, radius, color_hex = self.planet_specs[self.next_to_spawn]

        # start position on the +x axis for simplicity
        planet = Circle(
            self.cx + distance, self.cy,
            radius,
            color=hex_to_rgba(color_hex),
            batch=self.batch
        )

        self.planets.append((distance, speed, planet))
        self.next_to_spawn += 1

    def on_update(self, dt):
        self.angle += dt

        # Spawn logic
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer -= self.spawn_interval  # keeps timing stable
            self.spawn_next_planet()

        # Update only the planets that exist
        for distance, speed, planet_circle in self.planets:
            planet_circle.x = self.cx + distance * math.cos(self.angle * speed)
            planet_circle.y = self.cy + distance * math.sin(self.angle * speed)

    def on_draw(self):
        self.clear()
        self.batch.draw()


renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1 / 60)

run()
