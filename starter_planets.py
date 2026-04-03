import math
from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle
from pyglet.graphics import Batch
from pyglet import clock


# Simple color helper (RGB only)
def hex_to_rgb(hex_color):
    return (
        int(hex_color[1:3], 16),
        int(hex_color[3:5], 16),
        int(hex_color[5:7], 16),
    )


class SolarSystem(Window):
    def __init__(self):
        super().__init__(640, 640, "Mini Solar System")

        self.batch = Batch()

        # Center of the screen
        self.cx, self.cy = 320, 320

        # Sun
        self.sun = Circle(self.cx, self.cy, 25,
                          color=hex_to_rgb("#F9F871"),
                          batch=self.batch)

        # Planets (EDIT THESE!)
        # (x_distance, y_distance, speed, size, color)
        self.planets = [
            (80, 80, 1.0, 8, "#00D2FC"),   # Planet 1
            (80, 80, 1.0, 8, "#00D2FC"),  # Planet 2
            (140, 140, 0.5, 10, "#FFC75F"), # Planet 3
            (200, 200, 0.2, 12, "#C34A36"), # Planet 4

            # Nucelear Reactor 
            (100, 100, 1000.0, 5, "#FFFFFF"),  # Core 1
            (120, 120, 1000.0, 5, "#FFFFFF"),  # Core 2
            (140, 140, 1000.0, 5, "#FFFFFF"), # Core 3
            (160, 160, 1000.0, 5, "#FFFFFF"),  # Core 4
            (180, 180, 1000.0, 5, "#FFFFFF"),  # Core 5
            (200, 200, 1000.0, 5, "#FFFFFF") # Core 6 
        ]

        # Create planet objects
        self.planet_circles = []
        for x_distance, y_distance, speed, size, color in self.planets:
            circle = Circle(self.cx + x_distance, self.cy + y_distance,
                            size,
                            color=hex_to_rgb(color),
                            batch=self.batch)
            self.planet_circles.append((x_distance, y_distance, speed, circle))

        self.angle = 0

    def update(self, dt):
        self.angle += dt

        # Move planets in circles
        for x_distance, y_distance, speed, circle in self.planet_circles:
            circle.x = self.cx + x_distance * math.cos(self.angle * speed)
            circle.y = self.cy + y_distance * math.sin(self.angle * speed)

    def on_draw(self):
        self.clear()
        self.batch.draw()


game = SolarSystem()
clock.schedule_interval(game.update, 1 / 60)

run()
