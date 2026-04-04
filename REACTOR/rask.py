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


RAINBOW_COLORS = [
    '#FF0000', # Red
    '#FF7F00', # Orange
    '#FFFF00', # Yellow
    '#00FF00', # Green
    '#00FFFF', # Cyan
    '#0000FF', # Blue
    '#8B00FF', # Violet
    '#FF00FF'  # Magenta
]

class RAINBOW:
    def __init__(self, start_color, speed):
        self.start_color = start_color
        self.speed = speed

def rainbow(start_color, speed):
    return RAINBOW(start_color, speed)

def get_rainbow_color(start_index, speed, time):
    index = int(start_index + time * speed) % len(RAINBOW_COLORS)
    return hex_to_rgb(RAINBOW_COLORS[index])

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
        # (x_distance, y_distance, speed, size, color, phase)
        self.planets = [
            (80, 80, 1.0, 8, "#00D2FC", 0),  # Planet 2
            (140, 140, 0.5, 10, "#FFC75F", 0), # Planet 3
            (200, 200, 0.2, 12, "#C34A36", 0), # Planet 4

            # Nucelear Reactor 
            (100, 100, 1000.0, 5, "#FFFFFF", 0),  # Core 1
            (120, 120, 1000.0, 5, "#FFFFFF", 0),  # Core 2
            (140, 140, 1000.0, 5, "#FFFFFF", 0), # Core 3
            (160, 160, 1000.0, 5, "#FFFFFF", 0),  # Core 4
            (180, 180, 1000.0, 5, "#FFFFFF", 0),  # Core 5
            (200, 200, 1000.0, 5, "#FFFFFF", 0), # Core 6 

            # Other Reactor part
            (150, 150, 1.0, 20, RAINBOW(1, 10), 0),
            (150, 150, 1.0, 20, RAINBOW(2, 10), math.pi/2),
            (150, 150, 1.0, 20, RAINBOW(3, 10), math.pi),
            (150, 150, 1.0, 20, RAINBOW(4, 10), 3*math.pi/2)
        ]

        # Create planet objects
        self.planet_circles = []
        for planet_data in self.planets:
            x_distance, y_distance, speed, size, color, phase = planet_data

            # Handle rainbow colors
            if isinstance(color, RAINBOW):
                initial_color = get_rainbow_color(color.start_color, color.speed, 0)
            else:
                initial_color = hex_to_rgb(color)

            circle = Circle(self.cx + x_distance, self.cy + y_distance,
                            size,
                            color=initial_color,
                            batch=self.batch)
            self.planet_circles.append({
                'x_dist': x_distance,
                'y_dist': y_distance,
                'speed': speed,
                'phase': phase,
                'circle': circle,
                'color_info': color
            })

        self.angle = 0

    def update(self, dt):
        self.angle += dt

        # Move planets in circles
        for p in self.planet_circles:
            p['circle'].x = self.cx + p['x_dist'] * math.cos(self.angle * p['speed'] + p['phase'])
            p['circle'].y = self.cy + p['y_dist'] * math.sin(self.angle * p['speed'] + p['phase'])
            
            # Update rainbow colors
            if isinstance(p['color_info'], RAINBOW):
                p['circle'].color = get_rainbow_color(p['color_info'].start_color, p['color_info'].speed, self.angle)

    def on_draw(self):
        self.clear()
        self.batch.draw()


game = SolarSystem()
clock.schedule_interval(game.update, 1 / 60)

run()
