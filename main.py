import math
import random
from pyglet.window import Window, key
from pyglet.app import run
from pyglet.shapes import Circle
from pyglet.graphics import Batch
from pyglet import clock, text


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
        super().__init__(640, 640, "Kjernereaktor - Sith Code")

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
            (230, 220, 0.5, 8, "#00D2FC", 0),  # Planet 2
            (250, 240, 0.3, 10, "#FFC75F", math.pi/4), # Planet 3
            (300, 280, 0.2, 12, "#C34A36", 0), # Planet 4

            # Nucelear Reactor (5 sections of radial lines - rotated for 5-fold symmetry)
            # Section 1 (0 * 2pi/5 + pi/5 rad) - Dark Red
            (100, 100, 1.0, 5, "#8B0000", 0 * 2*math.pi/5 + math.pi/5),
            (120, 120, 1.0, 5, "#8B0000", 0 * 2*math.pi/5 + math.pi/5),
            (140, 140, 1.0, 5, "#8B0000", 0 * 2*math.pi/5 + math.pi/5),
            (160, 160, 1.0, 5, "#8B0000", 0 * 2*math.pi/5 + math.pi/5),
            (180, 180, 1.0, 5, "#8B0000", 0 * 2*math.pi/5 + math.pi/5),
            (200, 200, 1.0, 5, "#8B0000", 0 * 2*math.pi/5 + math.pi/5),
            # Section 2 (1 * 2pi/5 + pi/5 rad) - Orange Red
            (100, 100, 1.0, 5, "#FF4500", 1 * 2*math.pi/5 + math.pi/5),
            (120, 120, 1.0, 5, "#FF4500", 1 * 2*math.pi/5 + math.pi/5),
            (140, 140, 1.0, 5, "#FF4500", 1 * 2*math.pi/5 + math.pi/5),
            (160, 160, 1.0, 5, "#FF4500", 1 * 2*math.pi/5 + math.pi/5),
            (180, 180, 1.0, 5, "#FF4500", 1 * 2*math.pi/5 + math.pi/5),
            (200, 200, 1.0, 5, "#FF4500", 1 * 2*math.pi/5 + math.pi/5),
            # Section 3 (2 * 2pi/5 + pi/5 rad) - Dark Orange
            (100, 100, 1.0, 5, "#FF8C00", 2 * 2*math.pi/5 + math.pi/5),
            (120, 120, 1.0, 5, "#FF8C00", 2 * 2*math.pi/5 + math.pi/5),
            (140, 140, 1.0, 5, "#FF8C00", 2 * 2*math.pi/5 + math.pi/5),
            (160, 160, 1.0, 5, "#FF8C00", 2 * 2*math.pi/5 + math.pi/5),
            (180, 180, 1.0, 5, "#FF8C00", 2 * 2*math.pi/5 + math.pi/5),
            (200, 200, 1.0, 5, "#FF8C00", 2 * 2*math.pi/5 + math.pi/5),
            # Section 4 (3 * 2pi/5 + pi/5 rad) - Gold
            (100, 100, 1.0, 5, "#FFD700", 3 * 2*math.pi/5 + math.pi/5),
            (120, 120, 1.0, 5, "#FFD700", 3 * 2*math.pi/5 + math.pi/5),
            (140, 140, 1.0, 5, "#FFD700", 3 * 2*math.pi/5 + math.pi/5),
            (160, 160, 1.0, 5, "#FFD700", 3 * 2*math.pi/5 + math.pi/5),
            (180, 180, 1.0, 5, "#FFD700", 3 * 2*math.pi/5 + math.pi/5),
            (200, 200, 1.0, 5, "#FFD700", 3 * 2*math.pi/5 + math.pi/5),
            # Section 5 (4 * 2pi/5 + pi/5 rad) - Goldenrod
            (100, 100, 1.0, 5, "#DAA520", 4 * 2*math.pi/5 + math.pi/5),
            (120, 120, 1.0, 5, "#DAA520", 4 * 2*math.pi/5 + math.pi/5),
            (140, 140, 1.0, 5, "#DAA520", 4 * 2*math.pi/5 + math.pi/5),
            (160, 160, 1.0, 5, "#DAA520", 4 * 2*math.pi/5 + math.pi/5),
            (180, 180, 1.0, 5, "#DAA520", 4 * 2*math.pi/5 + math.pi/5),
            (200, 200, 1.0, 5, "#DAA520", 4 * 2*math.pi/5 + math.pi/5),
            
            # Other Reactor part (Rainbow circles)
            (150, 150, 1.0, 20, RAINBOW(1, 10), 0 * 2*math.pi/5),
            (150, 150, 1.0, 20, RAINBOW(2, 10), 1 * 2*math.pi/5),
            (150, 150, 1.0, 20, RAINBOW(3, 10), 2 * 2*math.pi/5),
            (150, 150, 1.0, 20, RAINBOW(4, 10), 3 * 2*math.pi/5),
            (150, 150, 1.0, 20, RAINBOW(5, 10), 4 * 2*math.pi/5)
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

            circle = Circle(self.cx + x_distance * math.cos(phase), 
                            self.cy + y_distance * math.sin(phase),
                            size,
                            color=initial_color,
                            batch=self.batch)
            
            # Offset position and velocity
            self.planet_circles.append({
                'x_dist': x_distance,
                'y_dist': y_distance,
                'speed': speed,
                'phase': phase,
                'circle': circle,
                'offset_x': 0.0,
                'offset_y': 0.0,
                'ovx': 0.0,
                'ovy': 0.0,
                'color_info': color
            })

        self.angle = 0

        # Asteroids
        self.asteroids = []
        self.asteroid_speed = 300.0

        # Text Label in top right
        self.label = text.Label('SPACE: Asteroids',
                                font_name='Arial',
                                font_size=12,
                                x=self.width - 10, y=self.height - 10,
                                anchor_x='right', anchor_y='top',
                                color=(255, 255, 255, 255),
                                batch=self.batch)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.spawn_asteroid()

    def spawn_asteroid(self):
        # Spawn asteroid at random position on the screen edge
        side = random.randint(0, 3)
        if side == 0: # Top
            x, y = random.randint(0, self.width), self.height
        elif side == 1: # Bottom
            x, y = random.randint(0, self.width), 0
        elif side == 2: # Left
            x, y = 0, random.randint(0, self.height)
        else: # Right
            x, y = self.width, random.randint(0, self.height)

        # Create asteroid
        ashp = Circle(x, y, 12, color=(128, 128, 128), batch=self.batch)
        
        # Calculate direction towards center
        dx, dy = self.cx - x, self.cy - y
        dist = math.hypot(dx, dy)
        vx = (dx / (dist or 1)) * self.asteroid_speed
        vy = (dy / (dist or 1)) * self.asteroid_speed

        self.asteroids.append({'shape': ashp, 'vx': vx, 'vy': vy})

    def update(self, dt):
        self.angle += dt

        # Move planets in circles with physics offset
        for p in self.planet_circles:
            # Apply offset velocity to offset position
            p['offset_x'] += p['ovx'] * dt
            p['offset_y'] += p['ovy'] * dt
            
            # Apply friction to offset velocity
            p['ovx'] *= 0.99
            p['ovy'] *= 0.99

            # Base orbital position
            base_x = self.cx + p['x_dist'] * math.cos(self.angle * p['speed'] + p['phase'])
            base_y = self.cy + p['y_dist'] * math.sin(self.angle * p['speed'] + p['phase'])
            
            # Final position is base + offset
            p['circle'].x = base_x + p['offset_x']
            p['circle'].y = base_y + p['offset_y']
            
            # Update rainbow colors
            if isinstance(p['color_info'], RAINBOW):
                p['circle'].color = get_rainbow_color(p['color_info'].start_color, p['color_info'].speed, self.angle)

        # Collision logic
        for i in range(len(self.planet_circles) - 1, -1, -1):
            p1, c1 = self.planet_circles[i], self.planet_circles[i]['circle']
            
            # Sun collision (Destroy planet on hit)
            if math.hypot(c1.x - self.cx, c1.y - self.cy) < (c1.radius + self.sun.radius):
                c1.delete()
                self.planet_circles.pop(i)
                continue

            # Remove off-screen planets
            if c1.x < -100 or c1.x > self.width + 100 or c1.y < -100 or c1.y > self.height + 100:
                c1.delete()
                self.planet_circles.pop(i)
                continue

            # Planet-Planet collision
            for j in range(i - 1, -1, -1):
                p2, c2 = self.planet_circles[j], self.planet_circles[j]['circle']
                dx, dy = c2.x - c1.x, c2.y - c1.y
                dist = math.hypot(dx, dy)
                
                if dist < (c1.radius + c2.radius):
                    # Push apart+transfer momentum
                    nx, ny = dx / (dist or 0.1), dy / (dist or 0.1)
                    overlap = (c1.radius + c2.radius) - dist
                    p1['offset_x'] -= nx * overlap * 0.5
                    p1['offset_y'] -= ny * overlap * 0.5
                    p2['offset_x'] += nx * overlap * 0.5
                    p2['offset_y'] += ny * overlap * 0.5
                    
                    m1, m2 = c1.radius, c2.radius
                    p1['ovx'] -= nx * 50 * (m2 / m1)
                    p1['ovy'] -= ny * 50 * (m2 / m1)
                    p2['ovx'] += nx * 50 * (m1 / m2)
                    p2['ovy'] += ny * 50 * (m1 / m2)

        # Asteroid movement and collisions
        for a in self.asteroids[:]:
            a['shape'].x += a['vx'] * dt
            a['shape'].y += a['vy'] * dt
            ashp = a['shape']

            # Hit planet?
            for p in self.planet_circles:
                pc = p['circle']
                if math.hypot(ashp.x - pc.x, ashp.y - pc.y) < (ashp.radius + pc.radius):
                    p['ovx'] += a['vx'] * (ashp.radius / pc.radius) * 0.5
                    p['ovy'] += a['vy'] * (ashp.radius / pc.radius) * 0.5
                    ashp.delete()
                    self.asteroids.remove(a)
                    break
            else:
                # Remove if asteroid hits sun or off screen
                dist_sun = math.hypot(ashp.x - self.cx, ashp.y - self.cy)
                off = ashp.x < -50 or ashp.x > self.width+50 or ashp.y < -50 or ashp.y > self.height+50
                if dist_sun < (ashp.radius + self.sun.radius) or off:
                    ashp.delete()
                    self.asteroids.remove(a)

    def on_draw(self):
        self.clear()
        self.batch.draw()


game = SolarSystem()
clock.schedule_interval(game.update, 1 / 60)

run()
