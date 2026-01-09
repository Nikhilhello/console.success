# import pygame
# import sys
# import random

# # --- CONFIGURATION ---
# WIDTH, HEIGHT = 1200, 800
# FPS = 60
# ROAD_WIDTH = 140
# LANE_WIDTH = ROAD_WIDTH // 2
# BUFFER_DIST = 30  # Safety distance between cars
# SPEED_LIMIT = 4

# # Colors
# BG_COLOR = (34, 139, 34)      # Forest Green
# ROAD_COLOR = (40, 40, 40)     # Dark Asphalt
# LINE_COLOR = (255, 255, 255)
# UI_BG_COLOR = (0, 0, 0, 200)  # Darker transparency for better read
# TEXT_WHITE = (255, 255, 255)
# TEXT_GRAY = (200, 200, 200)

# RED_LIGHT = (255, 50, 50)
# GREEN_LIGHT = (50, 255, 50)
# YELLOW_LIGHT = (255, 215, 0)
# CYAN_AI = (0, 255, 255)
# ORANGE_TRAD = (255, 165, 0)

# # Directions
# NORTH, SOUTH, EAST, WEST = 0, 1, 2, 3

# class Car:
#     def __init__(self, direction, lane_offset):
#         self.direction = direction
#         self.waiting = False
#         self.speed = 2 # Start speed
#         self.max_speed = random.uniform(3.0, 4.5) 
#         self.color = random.choice([(220, 60, 60), (60, 100, 220), (230, 230, 230), (220, 200, 50)])
        
#         # Dimensions
#         self.w, self.h = 22, 42 
        
#         # Spawn Positions
#         if direction == NORTH:
#             self.x = WIDTH // 2 + lane_offset - self.w//2
#             self.y = HEIGHT + 50
#         elif direction == SOUTH:
#             self.x = WIDTH // 2 - lane_offset - self.w//2
#             self.y = -50
#         elif direction == EAST:
#             self.x = -50
#             self.y = HEIGHT // 2 + lane_offset - self.w//2
#         elif direction == WEST:
#             self.x = WIDTH + 50
#             self.y = HEIGHT // 2 - lane_offset - self.w//2

#         self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
#         if direction in [EAST, WEST]:
#             self.rect.width, self.rect.height = self.h, self.w

#     def move(self, stop_line, light_state, cars_in_front):
#         should_stop = False
        
#         # 1. Traffic Light Logic
#         if light_state != "GREEN":
#             dist_to_line = 0
#             if self.direction == NORTH: dist_to_line = self.rect.top - stop_line
#             elif self.direction == SOUTH: dist_to_line = stop_line - self.rect.bottom
#             elif self.direction == EAST: dist_to_line = stop_line - self.rect.right
#             elif self.direction == WEST: dist_to_line = self.rect.left - stop_line
            
#             # If approaching line (within 60px) and hasn't crossed it
#             if 0 < dist_to_line < 60:
#                 should_stop = True

#         # 2. Collision Logic
#         for other in cars_in_front:
#             dist = 0
#             if self.direction == NORTH: dist = self.rect.top - other.rect.bottom
#             elif self.direction == SOUTH: dist = other.rect.top - self.rect.bottom
#             elif self.direction == EAST: dist = other.rect.left - self.rect.right
#             elif self.direction == WEST: dist = self.rect.left - other.rect.right
            
#             if 0 < dist < BUFFER_DIST:
#                 should_stop = True

#         # 3. Apply Movement
#         if should_stop:
#             self.waiting = True
#             self.speed = max(0, self.speed - 0.3) # Brake
#         else:
#             self.waiting = False
#             self.speed = min(self.max_speed, self.speed + 0.1) # Accelerate
        
#         if self.direction == NORTH: self.y -= self.speed
#         elif self.direction == SOUTH: self.y += self.speed
#         elif self.direction == EAST: self.x += self.speed
#         elif self.direction == WEST: self.x -= self.speed
        
#         self.rect.x = int(self.x)
#         self.rect.y = int(self.y)

#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, self.rect, border_radius=4)
#         # Headlights
#         h_col = (255, 255, 200)
#         if self.direction == NORTH: 
#             pygame.draw.circle(screen, h_col, (self.rect.left+4, self.rect.top), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.right-4, self.rect.top), 2)
#         elif self.direction == SOUTH:
#             pygame.draw.circle(screen, h_col, (self.rect.left+4, self.rect.bottom), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.right-4, self.rect.bottom), 2)
#         elif self.direction == EAST:
#             pygame.draw.circle(screen, h_col, (self.rect.right, self.rect.top+4), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.right, self.rect.bottom-4), 2)
#         elif self.direction == WEST:
#             pygame.draw.circle(screen, h_col, (self.rect.left, self.rect.top+4), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.left, self.rect.bottom-4), 2)

# class TrafficSim:
#     def __init__(self):
#         self.cars = []
#         self.mode = "TRADITIONAL (TIMER)"
        
#         # Stats
#         self.passed_count = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
#         self.total_wait_time = 0
#         self.total_cars_finished = 0
        
#         # Light State Machine
#         self.state = "NS_GREEN" 
#         self.timer = 0
        
#         # Stop Lines
#         self.stop_lines = {
#             NORTH: HEIGHT//2 + ROAD_WIDTH//2,
#             SOUTH: HEIGHT//2 - ROAD_WIDTH//2,
#             EAST: WIDTH//2 - ROAD_WIDTH//2,
#             WEST: WIDTH//2 + ROAD_WIDTH//2
#         }

#     def reset_stats(self):
#         """Resets all the counters to zero"""
#         self.passed_count = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
#         self.total_wait_time = 0
#         self.total_cars_finished = 0
#         print("Stats Reset!") # Console feedback

#     def update(self):
#         # 1. SPAWN LOGIC
#         if random.randint(0, 100) < 3: 
#             self.cars.append(Car(random.choice([NORTH, SOUTH, EAST, WEST]), LANE_WIDTH//2))

#         # 2. Logic Update
#         self.timer += 1
#         q_ns = sum(1 for c in self.cars if c.waiting and c.direction in [NORTH, SOUTH])
#         q_ew = sum(1 for c in self.cars if c.waiting and c.direction in [EAST, WEST])
        
#         # Accumulate Wait Time
#         for c in self.cars:
#             if c.waiting:
#                 self.total_wait_time += 1/60 
        
#         # --- STATE MACHINE ---
#         if self.state == "NS_GREEN":
#             should_switch = False
#             if self.mode.startswith("AI"):
#                 # AI switches if EW has traffic AND NS is empty OR EW has WAY more traffic
#                 if (q_ew > 0 and q_ns == 0) or (q_ew > q_ns + 4): 
#                     if self.timer > 60: should_switch = True
#             else:
#                 if self.timer > 300: should_switch = True
            
#             if should_switch:
#                 self.state = "NS_YELLOW"
#                 self.timer = 0
                
#         elif self.state == "NS_YELLOW":
#             if self.timer > 90: # Yellow duration
#                 self.state = "ALL_RED_TO_EW"
#                 self.timer = 0
                
#         elif self.state == "ALL_RED_TO_EW":
#             if self.timer > 40: # Clearance
#                 self.state = "EW_GREEN"
#                 self.timer = 0
                
#         elif self.state == "EW_GREEN":
#             should_switch = False
#             if self.mode.startswith("AI"):
#                 if (q_ns > 0 and q_ew == 0) or (q_ns > q_ew + 4):
#                      if self.timer > 60: should_switch = True
#             else:
#                 if self.timer > 300: should_switch = True
                
#             if should_switch:
#                 self.state = "EW_YELLOW"
#                 self.timer = 0
                
#         elif self.state == "EW_YELLOW":
#             if self.timer > 90:
#                 self.state = "ALL_RED_TO_NS"
#                 self.timer = 0
                
#         elif self.state == "ALL_RED_TO_NS":
#             if self.timer > 40:
#                 self.state = "NS_GREEN"
#                 self.timer = 0

#         # 3. Move Cars
#         for car in self.cars[:]:
#             # Determine Light Color for this car
#             light = "RED"
#             if car.direction in [NORTH, SOUTH]:
#                 if "NS_GREEN" in self.state: light = "GREEN"
#                 elif "NS_YELLOW" in self.state: light = "YELLOW"
#             else:
#                 if "EW_GREEN" in self.state: light = "GREEN"
#                 elif "EW_YELLOW" in self.state: light = "YELLOW"
            
#             same_lane = [c for c in self.cars if c.direction == car.direction and c != car]
#             car.move(self.stop_lines[car.direction], light, same_lane)
            
#             # Despawn
#             if not (-100 < car.rect.x < WIDTH + 100 and -100 < car.rect.y < HEIGHT + 100):
#                 self.cars.remove(car)
#                 self.passed_count[car.direction] += 1
#                 self.total_cars_finished += 1

#     def draw_dashboard(self, screen, font, font_bold):
#         # Panel
#         panel = pygame.Surface((320, 280), pygame.SRCALPHA) # Slightly taller for Reset text
#         panel.fill(UI_BG_COLOR)
#         screen.blit(panel, (20, 20))
        
#         # System Header
#         color = CYAN_AI if self.mode.startswith("AI") else ORANGE_TRAD
#         screen.blit(font_bold.render(f"SYSTEM: {self.mode.split(' ')[0]}", True, color), (35, 30))
        
#         # Queues & Passed
#         y = 70
#         q_ns = sum(1 for c in self.cars if c.waiting and c.direction in [NORTH, SOUTH])
#         q_ew = sum(1 for c in self.cars if c.waiting and c.direction in [EAST, WEST])
        
#         # Avg Wait Calculation
#         avg_wait = 0.0
#         if self.total_cars_finished > 0:
#             avg_wait = self.total_wait_time / self.total_cars_finished
        
#         # Rows
#         def draw_row(label, q_val, p_val, y_pos):
#             screen.blit(font.render(f"{label}", True, TEXT_GRAY), (35, y_pos))
#             screen.blit(font.render(f"Waiting: {q_val}", True, TEXT_WHITE), (110, y_pos))
#             screen.blit(font.render(f"Passed: {p_val}", True, GREEN_LIGHT), (220, y_pos))

#         draw_row("NORTH", sum(1 for c in self.cars if c.waiting and c.direction==NORTH), self.passed_count[NORTH], y); y+=25
#         draw_row("SOUTH", sum(1 for c in self.cars if c.waiting and c.direction==SOUTH), self.passed_count[SOUTH], y); y+=25
#         draw_row("EAST ", sum(1 for c in self.cars if c.waiting and c.direction==EAST), self.passed_count[EAST], y); y+=25
#         draw_row("WEST ", sum(1 for c in self.cars if c.waiting and c.direction==WEST), self.passed_count[WEST], y); y+=35

#         # Metrics
#         pygame.draw.line(screen, TEXT_GRAY, (35, y), (300, y), 1)
#         y += 10
#         screen.blit(font_bold.render(f"Avg Wait Time: {avg_wait:.1f} sec", True, TEXT_WHITE), (35, y))
#         y += 30
        
#         # Controls Text
#         screen.blit(font.render("[SPACE] Switch Mode", True, (150,150,150)), (35, y))
#         y += 20
#         screen.blit(font.render("[R] Reset Counts", True, (150,150,150)), (35, y))

#     def draw_scene(self, screen, font):
#         screen.fill(BG_COLOR)
        
#         # Road Layer
#         pygame.draw.rect(screen, ROAD_COLOR, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
#         pygame.draw.rect(screen, ROAD_COLOR, (0, HEIGHT//2 - ROAD_WIDTH//2, WIDTH, ROAD_WIDTH))
        
#         # Markings
#         for y in range(0, HEIGHT, 40): 
#             if not (HEIGHT//2 - ROAD_WIDTH//2 < y < HEIGHT//2 + ROAD_WIDTH//2):
#                 pygame.draw.line(screen, (200, 200, 0), (WIDTH//2, y), (WIDTH//2, y+20), 2)
#         for x in range(0, WIDTH, 40):
#             if not (WIDTH//2 - ROAD_WIDTH//2 < x < WIDTH//2 + ROAD_WIDTH//2):
#                 pygame.draw.line(screen, (200, 200, 0), (x, HEIGHT//2), (x+20, HEIGHT//2), 2)

#         # Stop Lines
#         stop_col = LINE_COLOR
#         pygame.draw.line(screen, stop_col, (WIDTH//2, self.stop_lines[NORTH]), (WIDTH//2+ROAD_WIDTH//2, self.stop_lines[NORTH]), 4)
#         pygame.draw.line(screen, stop_col, (WIDTH//2-ROAD_WIDTH//2, self.stop_lines[SOUTH]), (WIDTH//2, self.stop_lines[SOUTH]), 4)
#         pygame.draw.line(screen, stop_col, (self.stop_lines[EAST], HEIGHT//2), (self.stop_lines[EAST], HEIGHT//2+ROAD_WIDTH//2), 4)
#         pygame.draw.line(screen, stop_col, (self.stop_lines[WEST], HEIGHT//2-ROAD_WIDTH//2), (self.stop_lines[WEST], HEIGHT//2), 4)

#         # Labels
#         lbl_col = (180, 180, 180)
#         # North label at Top
#         screen.blit(font.render("N", True, (0,0,0)), (WIDTH//2 - 5, 10))
#         screen.blit(font.render("S", True, (0,0,0)), (WIDTH//2 - 5, HEIGHT - 30))
#         screen.blit(font.render("W", True, (0,0,0)), (10, HEIGHT//2 - 10))
#         screen.blit(font.render("E", True, (0,0,0)), (WIDTH - 30, HEIGHT//2 - 10))
        
#         # Lane Arrows
#         screen.blit(font.render("↑", True, lbl_col), (WIDTH//2 + 20, HEIGHT - 100)) # Northbound lane
#         screen.blit(font.render("↓", True, lbl_col), (WIDTH//2 - 40, 100))        # Southbound lane
#         screen.blit(font.render("→", True, lbl_col), (100, HEIGHT//2 + 20))       # Eastbound lane
#         screen.blit(font.render("←", True, lbl_col), (WIDTH - 100, HEIGHT//2 - 40)) # Westbound lane

#     def draw_lights(self, screen):
#         # Draw traffic lights based on state
#         # NS Light
#         ns_color = RED_LIGHT
#         if "NS_GREEN" in self.state: ns_color = GREEN_LIGHT
#         elif "NS_YELLOW" in self.state: ns_color = YELLOW_LIGHT
        
#         # EW Light
#         ew_color = RED_LIGHT
#         if "EW_GREEN" in self.state: ew_color = GREEN_LIGHT
#         elif "EW_YELLOW" in self.state: ew_color = YELLOW_LIGHT
        
#         off = ROAD_WIDTH//2 + 20
#         # NS Lights
#         pygame.draw.circle(screen, ns_color, (WIDTH//2 + off, HEIGHT//2 + off), 12) 
#         pygame.draw.circle(screen, ns_color, (WIDTH//2 - off, HEIGHT//2 - off), 12) 
        
#         # EW Lights
#         pygame.draw.circle(screen, ew_color, (WIDTH//2 - off, HEIGHT//2 + off), 12) 
#         pygame.draw.circle(screen, ew_color, (WIDTH//2 + off, HEIGHT//2 - off), 12) 

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Professional Traffic AI Simulation")
#     clock = pygame.time.Clock()
    
#     font = pygame.font.SysFont("Verdana", 14)
#     font_bold = pygame.font.SysFont("Verdana", 18, bold=True)
    
#     sim = TrafficSim()
    
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     sim.mode = "AI OPTIMIZED" if sim.mode == "TRADITIONAL (TIMER)" else "TRADITIONAL (TIMER)"
#                 if event.key == pygame.K_r: # <-- RESET KEY LISTENER
#                     sim.reset_stats()

#         sim.update()
        
#         sim.draw_scene(screen, font_bold)
#         for car in sim.cars:
#             car.draw(screen)
#         sim.draw_lights(screen)
#         sim.draw_dashboard(screen, font, font_bold)
        
#         pygame.display.flip()
#         clock.tick(FPS)

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()

#----------------------============================-------------------------------------------------

# import pygame
# import sys
# import random

# # --- CONFIGURATION ---
# WIDTH, HEIGHT = 1200, 800
# FPS = 60
# ROAD_WIDTH = 140
# LANE_WIDTH = ROAD_WIDTH // 2
# BUFFER_DIST = 30  # Safety distance
# SPEED_LIMIT = 4

# # Colors
# BG_COLOR = (34, 139, 34)      # Forest Green
# ROAD_COLOR = (40, 40, 40)     # Dark Asphalt
# LINE_COLOR = (255, 255, 255)
# UI_BG_COLOR = (0, 0, 0, 200)  # Dark transparency
# TEXT_WHITE = (255, 255, 255)
# TEXT_GRAY = (200, 200, 200)
# TEXT_YELLOW = (255, 255, 50) # For waiting counts on road

# RED_LIGHT = (255, 50, 50)
# GREEN_LIGHT = (50, 255, 50)
# YELLOW_LIGHT = (255, 215, 0)
# CYAN_AI = (0, 255, 255)
# ORANGE_TRAD = (255, 165, 0)

# # Directions
# NORTH, SOUTH, EAST, WEST = 0, 1, 2, 3

# class Car:
#     def __init__(self, direction, lane_offset):
#         self.direction = direction
#         self.waiting = False
#         self.current_wait = 0 
        
#         self.speed = 2 
#         self.max_speed = random.uniform(3.0, 4.5) 
#         self.color = random.choice([(220, 60, 60), (60, 100, 220), (230, 230, 230), (220, 200, 50)])
        
#         # Dimensions
#         self.w, self.h = 22, 42 
        
#         # Spawn Positions
#         if direction == NORTH:
#             self.x = WIDTH // 2 + lane_offset - self.w//2
#             self.y = HEIGHT + 50
#         elif direction == SOUTH:
#             self.x = WIDTH // 2 - lane_offset - self.w//2
#             self.y = -50
#         elif direction == EAST:
#             self.x = -50
#             self.y = HEIGHT // 2 + lane_offset - self.w//2
#         elif direction == WEST:
#             self.x = WIDTH + 50
#             self.y = HEIGHT // 2 - lane_offset - self.w//2

#         self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
#         if direction in [EAST, WEST]:
#             self.rect.width, self.rect.height = self.h, self.w

#     def move(self, stop_line, light_state, cars_in_front):
#         should_stop = False
        
#         # 1. Traffic Light Logic
#         if light_state != "GREEN":
#             dist_to_line = 0
#             if self.direction == NORTH: dist_to_line = self.rect.top - stop_line
#             elif self.direction == SOUTH: dist_to_line = stop_line - self.rect.bottom
#             elif self.direction == EAST: dist_to_line = stop_line - self.rect.right
#             elif self.direction == WEST: dist_to_line = self.rect.left - stop_line
            
#             if 0 < dist_to_line < 60:
#                 should_stop = True

#         # 2. Collision Logic
#         for other in cars_in_front:
#             dist = 0
#             if self.direction == NORTH: dist = self.rect.top - other.rect.bottom
#             elif self.direction == SOUTH: dist = other.rect.top - self.rect.bottom
#             elif self.direction == EAST: dist = other.rect.left - self.rect.right
#             elif self.direction == WEST: dist = self.rect.left - other.rect.right
            
#             if 0 < dist < BUFFER_DIST:
#                 should_stop = True

#         # 3. Apply Movement
#         if should_stop:
#             self.waiting = True
#             self.current_wait += 1/60 # Add frame time
#             self.speed = max(0, self.speed - 0.3) 
#         else:
#             self.waiting = False
#             self.speed = min(self.max_speed, self.speed + 0.1) 
        
#         if self.direction == NORTH: self.y -= self.speed
#         elif self.direction == SOUTH: self.y += self.speed
#         elif self.direction == EAST: self.x += self.speed
#         elif self.direction == WEST: self.x -= self.speed
        
#         self.rect.x = int(self.x)
#         self.rect.y = int(self.y)

#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, self.rect, border_radius=4)
#         # Headlights
#         h_col = (255, 255, 200)
#         if self.direction == NORTH: 
#             pygame.draw.circle(screen, h_col, (self.rect.left+4, self.rect.top), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.right-4, self.rect.top), 2)
#         elif self.direction == SOUTH:
#             pygame.draw.circle(screen, h_col, (self.rect.left+4, self.rect.bottom), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.right-4, self.rect.bottom), 2)
#         elif self.direction == EAST:
#             pygame.draw.circle(screen, h_col, (self.rect.right, self.rect.top+4), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.right, self.rect.bottom-4), 2)
#         elif self.direction == WEST:
#             pygame.draw.circle(screen, h_col, (self.rect.left, self.rect.top+4), 2)
#             pygame.draw.circle(screen, h_col, (self.rect.left, self.rect.bottom-4), 2)

# class TrafficSim:
#     def __init__(self):
#         self.cars = []
#         self.mode = "TRADITIONAL (TIMER)"
        
#         # Stats
#         self.passed_count = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
#         self.total_wait_time = 0
#         self.total_cars_finished = 0
#         self.max_current_wait = 0.0
        
#         self.state = "NS_GREEN" 
#         self.timer = 0
        
#         self.stop_lines = {
#             NORTH: HEIGHT//2 + ROAD_WIDTH//2,
#             SOUTH: HEIGHT//2 - ROAD_WIDTH//2,
#             EAST: WIDTH//2 - ROAD_WIDTH//2,
#             WEST: WIDTH//2 + ROAD_WIDTH//2
#         }

#     def reset_stats(self):
#         self.passed_count = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
#         self.total_wait_time = 0
#         self.total_cars_finished = 0
#         self.max_current_wait = 0.0
#         for c in self.cars: c.current_wait = 0
#         print("Stats Reset!")

#     def update(self):
#         # 1. Spawn Rate (Slightly increased to ensure traffic builds up for AI to solve)
#         if random.randint(0, 100) < 4: 
#             self.cars.append(Car(random.choice([NORTH, SOUTH, EAST, WEST]), LANE_WIDTH//2))

#         # 2. Logic
#         self.timer += 1
#         q_ns = sum(1 for c in self.cars if c.waiting and c.direction in [NORTH, SOUTH])
#         q_ew = sum(1 for c in self.cars if c.waiting and c.direction in [EAST, WEST])
        
#         # Calculate Stats
#         current_max = 0
#         for c in self.cars:
#             if c.waiting:
#                 self.total_wait_time += 1/60
#                 if c.current_wait > current_max:
#                     current_max = c.current_wait
#         self.max_current_wait = current_max

#         # --- SMART vs DUMB LOGIC ---
        
#         # TRADITIONAL: Dumb Timer
#         # I increased the timer to 400 frames (approx 6.5 seconds).
#         # This forces cars to sit at red lights even if the road is empty,
#         # ensuring the "Before AI" mode looks inefficient.
#         TRADITIONAL_CYCLE = 400 

#         # AI: Smart Logic
#         # It checks if the current green lane is empty. If it is, switch immediately.
#         # It also switches if the other side is piling up dangerously.
        
#         if self.state == "NS_GREEN":
#             should_switch = False
            
#             if self.mode.startswith("AI"):
#                 # AI RULE 1: If North/South is empty, switch immediately (don't wait!)
#                 if q_ns == 0 and q_ew > 0 and self.timer > 30: # Min green 0.5s
#                     should_switch = True
#                 # AI RULE 2: If East/West is piling up huge, force switch
#                 elif q_ew > 5 and self.timer > 60:
#                     should_switch = True
#             else:
#                 # Traditional: Wait for fixed timer
#                 if self.timer > TRADITIONAL_CYCLE: should_switch = True
            
#             if should_switch:
#                 self.state = "NS_YELLOW"
#                 self.timer = 0
                
#         elif self.state == "NS_YELLOW":
#             if self.timer > 90: self.state = "ALL_RED_TO_EW"; self.timer = 0
            
#         elif self.state == "ALL_RED_TO_EW":
#             if self.timer > 40: self.state = "EW_GREEN"; self.timer = 0
            
#         elif self.state == "EW_GREEN":
#             should_switch = False
            
#             if self.mode.startswith("AI"):
#                 # AI RULE 1: If East/West is empty, switch immediately
#                 if q_ew == 0 and q_ns > 0 and self.timer > 30:
#                     should_switch = True
#                 # AI RULE 2: If North/South is piling up
#                 elif q_ns > 5 and self.timer > 60:
#                     should_switch = True
#             else:
#                 # Traditional: Wait for fixed timer
#                 if self.timer > TRADITIONAL_CYCLE: should_switch = True
                
#             if should_switch:
#                 self.state = "EW_YELLOW"; self.timer = 0
                
#         elif self.state == "EW_YELLOW":
#             if self.timer > 90: self.state = "ALL_RED_TO_NS"; self.timer = 0
            
#         elif self.state == "ALL_RED_TO_NS":
#             if self.timer > 40: self.state = "NS_GREEN"; self.timer = 0

#         # 3. Move Cars
#         for car in self.cars[:]:
#             light = "RED"
#             if car.direction in [NORTH, SOUTH]:
#                 if "NS_GREEN" in self.state: light = "GREEN"
#                 elif "NS_YELLOW" in self.state: light = "YELLOW"
#             else:
#                 if "EW_GREEN" in self.state: light = "GREEN"
#                 elif "EW_YELLOW" in self.state: light = "YELLOW"
            
#             same_lane = [c for c in self.cars if c.direction == car.direction and c != car]
#             car.move(self.stop_lines[car.direction], light, same_lane)
            
#             if not (-100 < car.rect.x < WIDTH + 100 and -100 < car.rect.y < HEIGHT + 100):
#                 self.cars.remove(car)
#                 self.passed_count[car.direction] += 1
#                 self.total_cars_finished += 1

#     def draw_dashboard(self, screen, font, font_bold):
#         # Panel (Shortened since we removed "Waiting")
#         panel = pygame.Surface((280, 240), pygame.SRCALPHA)
#         panel.fill(UI_BG_COLOR)
#         screen.blit(panel, (20, 20))
        
#         # System Header
#         color = CYAN_AI if self.mode.startswith("AI") else ORANGE_TRAD
#         screen.blit(font_bold.render(f"SYSTEM: {self.mode.split(' ')[0]}", True, color), (35, 30))
        
#         y = 70
        
#         # Passed Counts Only
#         def draw_pass_row(label, p_val, y_pos):
#             screen.blit(font.render(f"{label}", True, TEXT_GRAY), (35, y_pos))
#             screen.blit(font.render(f"Passed: {p_val}", True, GREEN_LIGHT), (160, y_pos))

#         draw_pass_row("NORTH", self.passed_count[NORTH], y); y+=25
#         draw_pass_row("SOUTH", self.passed_count[SOUTH], y); y+=25
#         draw_pass_row("EAST ", self.passed_count[EAST], y); y+=25
#         draw_pass_row("WEST ", self.passed_count[WEST], y); y+=35

#         # Metrics
#         pygame.draw.line(screen, TEXT_GRAY, (35, y), (260, y), 1)
#         y += 10
        
#         avg_wait = self.total_wait_time / self.total_cars_finished if self.total_cars_finished > 0 else 0.0
#         screen.blit(font_bold.render(f"Avg Wait: {avg_wait:.1f} sec", True, TEXT_WHITE), (35, y)); y+=30
        
#         # Controls
#         screen.blit(font.render("[SPACE] Switch Mode", True, (150,150,150)), (35, y))
#         y += 20
#         screen.blit(font.render("[R] Reset Stats", True, (150,150,150)), (35, y))

#     def draw_on_road_stats(self, screen, font):
#         # Calculate counts
#         q_n = sum(1 for c in self.cars if c.waiting and c.direction == NORTH)
#         q_s = sum(1 for c in self.cars if c.waiting and c.direction == SOUTH)
#         q_e = sum(1 for c in self.cars if c.waiting and c.direction == EAST)
#         q_w = sum(1 for c in self.cars if c.waiting and c.direction == WEST)
        
#         # Draw waiting counts directly ON the road near the stop lines
#         # Locations are tweaked to be next to the traffic lights
        
#         # North Lane (Waiting at Bottom, text goes right of lane)
#         if q_n > 0:
#             screen.blit(font.render(f"Waiting: {q_n}", True, TEXT_YELLOW), (WIDTH//2 + 80, HEIGHT//2 + 80))
            
#         # South Lane (Waiting at Top, text goes left of lane)
#         if q_s > 0:
#             screen.blit(font.render(f"Waiting: {q_s}", True, TEXT_YELLOW), (WIDTH//2 - 180, HEIGHT//2 - 100))
            
#         # East Lane (Waiting at Left, text goes above lane)
#         if q_e > 0:
#             screen.blit(font.render(f"Waiting: {q_e}", True, TEXT_YELLOW), (WIDTH//2 - 120, HEIGHT//2 + 80))
            
#         # West Lane (Waiting at Right, text goes below lane)
#         if q_w > 0:
#             screen.blit(font.render(f"Waiting: {q_w}", True, TEXT_YELLOW), (WIDTH//2 + 80, HEIGHT//2 - 100))

#     def draw_scene(self, screen, font):
#         screen.fill(BG_COLOR)
#         # Roads
#         pygame.draw.rect(screen, ROAD_COLOR, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
#         pygame.draw.rect(screen, ROAD_COLOR, (0, HEIGHT//2 - ROAD_WIDTH//2, WIDTH, ROAD_WIDTH))
        
#         # Markings
#         for y in range(0, HEIGHT, 40): 
#             if not (HEIGHT//2 - ROAD_WIDTH//2 < y < HEIGHT//2 + ROAD_WIDTH//2):
#                 pygame.draw.line(screen, (200, 200, 0), (WIDTH//2, y), (WIDTH//2, y+20), 2)
#         for x in range(0, WIDTH, 40):
#             if not (WIDTH//2 - ROAD_WIDTH//2 < x < WIDTH//2 + ROAD_WIDTH//2):
#                 pygame.draw.line(screen, (200, 200, 0), (x, HEIGHT//2), (x+20, HEIGHT//2), 2)

#         # Stop Lines
#         stop_col = LINE_COLOR
#         pygame.draw.line(screen, stop_col, (WIDTH//2, self.stop_lines[NORTH]), (WIDTH//2+ROAD_WIDTH//2, self.stop_lines[NORTH]), 4)
#         pygame.draw.line(screen, stop_col, (WIDTH//2-ROAD_WIDTH//2, self.stop_lines[SOUTH]), (WIDTH//2, self.stop_lines[SOUTH]), 4)
#         pygame.draw.line(screen, stop_col, (self.stop_lines[EAST], HEIGHT//2), (self.stop_lines[EAST], HEIGHT//2+ROAD_WIDTH//2), 4)
#         pygame.draw.line(screen, stop_col, (self.stop_lines[WEST], HEIGHT//2-ROAD_WIDTH//2), (self.stop_lines[WEST], HEIGHT//2), 4)

#         # Labels
#         lbl_col = (180, 180, 180)
#         screen.blit(font.render("N", True, (0,0,0)), (WIDTH//2 - 5, 10))
#         screen.blit(font.render("S", True, (0,0,0)), (WIDTH//2 - 5, HEIGHT - 30))
#         screen.blit(font.render("W", True, (0,0,0)), (10, HEIGHT//2 - 10))
#         screen.blit(font.render("E", True, (0,0,0)), (WIDTH - 30, HEIGHT//2 - 10))

#     def draw_lights(self, screen):
#         ns_color = RED_LIGHT
#         if "NS_GREEN" in self.state: ns_color = GREEN_LIGHT
#         elif "NS_YELLOW" in self.state: ns_color = YELLOW_LIGHT
        
#         ew_color = RED_LIGHT
#         if "EW_GREEN" in self.state: ew_color = GREEN_LIGHT
#         elif "EW_YELLOW" in self.state: ew_color = YELLOW_LIGHT
        
#         off = ROAD_WIDTH//2 + 20
#         pygame.draw.circle(screen, ns_color, (WIDTH//2 + off, HEIGHT//2 + off), 12) 
#         pygame.draw.circle(screen, ns_color, (WIDTH//2 - off, HEIGHT//2 - off), 12) 
#         pygame.draw.circle(screen, ew_color, (WIDTH//2 - off, HEIGHT//2 + off), 12) 
#         pygame.draw.circle(screen, ew_color, (WIDTH//2 + off, HEIGHT//2 - off), 12) 

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Professional Traffic AI Simulation")
#     clock = pygame.time.Clock()
    
#     font = pygame.font.SysFont("Verdana", 14)
#     font_bold = pygame.font.SysFont("Verdana", 18, bold=True)
    
#     sim = TrafficSim()
    
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     sim.mode = "AI OPTIMIZED" if sim.mode == "TRADITIONAL (TIMER)" else "TRADITIONAL (TIMER)"
#                 if event.key == pygame.K_r:
#                     sim.reset_stats()

#         sim.update()
#         sim.draw_scene(screen, font_bold)
#         sim.draw_on_road_stats(screen, font_bold)
#         for car in sim.cars:
#             car.draw(screen)
#         sim.draw_lights(screen)
#         sim.draw_dashboard(screen, font, font_bold)
        
#         pygame.display.flip()
#         clock.tick(FPS)

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()

# ---------------------------------------------
# ==========added Ambulance===================================
# =============================================================
import pygame
import sys
import random

# --- CONFIGURATION ---
WIDTH, HEIGHT = 1200, 800
FPS = 60
ROAD_WIDTH = 140
LANE_WIDTH = ROAD_WIDTH // 2
BUFFER_DIST = 30  # Safety distance
SPEED_LIMIT = 4

# Colors
BG_COLOR = (34, 139, 34)      # Forest Green
ROAD_COLOR = (40, 40, 40)     # Dark Asphalt
LINE_COLOR = (255, 255, 255)
UI_BG_COLOR = (0, 0, 0, 200)  # Dark transparency
TEXT_WHITE = (255, 255, 255)
TEXT_GRAY = (200, 200, 200)
TEXT_YELLOW = (255, 255, 50) 

RED_LIGHT = (255, 50, 50)
GREEN_LIGHT = (50, 255, 50)
YELLOW_LIGHT = (255, 215, 0)
CYAN_AI = (0, 255, 255)
ORANGE_TRAD = (255, 165, 0)

# Directions
NORTH, SOUTH, EAST, WEST = 0, 1, 2, 3

class Car:
    def __init__(self, direction, lane_offset, is_ambulance=False):
        self.direction = direction
        self.waiting = False
        self.current_wait = 0 
        self.is_ambulance = is_ambulance
        
        self.speed = 2 
        
        if self.is_ambulance:
            self.max_speed = 7.0 # Ambulance moves VERY fast
            self.color = (255, 255, 255) # White body
        else:
            self.max_speed = random.uniform(3.0, 4.5) 
            self.color = random.choice([(220, 60, 60), (60, 100, 220), (230, 230, 230), (220, 200, 50)])
        
        # Dimensions
        self.w, self.h = 22, 42 
        
        # Spawn Positions
        if direction == NORTH:
            self.x = WIDTH // 2 + lane_offset - self.w//2
            self.y = HEIGHT + 50
        elif direction == SOUTH:
            self.x = WIDTH // 2 - lane_offset - self.w//2
            self.y = -50
        elif direction == EAST:
            self.x = -50
            self.y = HEIGHT // 2 + lane_offset - self.w//2
        elif direction == WEST:
            self.x = WIDTH + 50
            self.y = HEIGHT // 2 - lane_offset - self.w//2

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if direction in [EAST, WEST]:
            self.rect.width, self.rect.height = self.h, self.w

    def move(self, stop_line, light_state, cars_in_front):
        should_stop = False
        
        # 1. Traffic Light Logic
        # If light is RED or YELLOW, check if we need to stop
        if light_state != "GREEN":
            dist_to_line = 0
            if self.direction == NORTH: dist_to_line = self.rect.top - stop_line
            elif self.direction == SOUTH: dist_to_line = stop_line - self.rect.bottom
            elif self.direction == EAST: dist_to_line = stop_line - self.rect.right
            elif self.direction == WEST: dist_to_line = self.rect.left - stop_line
            
            # Stop if approaching the line (and haven't crossed it)
            if 0 < dist_to_line < 60:
                should_stop = True

        # 2. Collision Logic
        for other in cars_in_front:
            dist = 0
            if self.direction == NORTH: dist = self.rect.top - other.rect.bottom
            elif self.direction == SOUTH: dist = other.rect.top - self.rect.bottom
            elif self.direction == EAST: dist = other.rect.left - self.rect.right
            elif self.direction == WEST: dist = self.rect.left - other.rect.right
            
            if 0 < dist < BUFFER_DIST:
                should_stop = True

        # 3. Apply Movement
        if should_stop:
            self.waiting = True
            self.current_wait += 1/60 
            self.speed = max(0, self.speed - 0.3) 
        else:
            self.waiting = False
            self.speed = min(self.max_speed, self.speed + 0.1) 
        
        if self.direction == NORTH: self.y -= self.speed
        elif self.direction == SOUTH: self.y += self.speed
        elif self.direction == EAST: self.x += self.speed
        elif self.direction == WEST: self.x -= self.speed
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=4)
        
        # Draw Red Cross for Ambulance
        if self.is_ambulance:
            cross_color = (255, 0, 0)
            if self.direction in [NORTH, SOUTH]:
                pygame.draw.rect(screen, cross_color, (self.rect.centerx - 3, self.rect.centery - 8, 6, 16))
                pygame.draw.rect(screen, cross_color, (self.rect.centerx - 8, self.rect.centery - 3, 16, 6))
            else:
                pygame.draw.rect(screen, cross_color, (self.rect.centerx - 8, self.rect.centery - 3, 16, 6))
                pygame.draw.rect(screen, cross_color, (self.rect.centerx - 3, self.rect.centery - 8, 6, 16))

        # Headlights
        h_col = (255, 255, 200)
        if self.direction == NORTH: 
            pygame.draw.circle(screen, h_col, (self.rect.left+4, self.rect.top), 2)
            pygame.draw.circle(screen, h_col, (self.rect.right-4, self.rect.top), 2)
        elif self.direction == SOUTH:
            pygame.draw.circle(screen, h_col, (self.rect.left+4, self.rect.bottom), 2)
            pygame.draw.circle(screen, h_col, (self.rect.right-4, self.rect.bottom), 2)
        elif self.direction == EAST:
            pygame.draw.circle(screen, h_col, (self.rect.right, self.rect.top+4), 2)
            pygame.draw.circle(screen, h_col, (self.rect.right, self.rect.bottom-4), 2)
        elif self.direction == WEST:
            pygame.draw.circle(screen, h_col, (self.rect.left, self.rect.top+4), 2)
            pygame.draw.circle(screen, h_col, (self.rect.left, self.rect.bottom-4), 2)

class TrafficSim:
    def __init__(self):
        self.cars = []
        self.mode = "TRADITIONAL (TIMER)"
        
        # Stats
        self.passed_count = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
        self.total_wait_time = 0
        self.total_cars_finished = 0
        self.max_current_wait = 0.0
        
        self.state = "NS_GREEN" 
        self.timer = 0
        
        self.stop_lines = {
            NORTH: HEIGHT//2 + ROAD_WIDTH//2,
            SOUTH: HEIGHT//2 - ROAD_WIDTH//2,
            EAST: WIDTH//2 - ROAD_WIDTH//2,
            WEST: WIDTH//2 + ROAD_WIDTH//2
        }

    def reset_stats(self):
        self.passed_count = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
        self.total_wait_time = 0
        self.total_cars_finished = 0
        self.max_current_wait = 0.0
        for c in self.cars: c.current_wait = 0
        print("Stats Reset!")

    def spawn_ambulance(self):
        """Force spawn an ambulance in a random direction"""
        d = random.choice([NORTH, SOUTH, EAST, WEST])
        amb = Car(d, LANE_WIDTH//2, is_ambulance=True)
        self.cars.append(amb)
        print(f"🚑 Ambulance dispatched from {['NORTH','SOUTH','EAST','WEST'][d]}!")

    def update(self):
        # 1. Spawn Normal Traffic
        if random.randint(0, 100) < 3: 
            self.cars.append(Car(random.choice([NORTH, SOUTH, EAST, WEST]), LANE_WIDTH//2))

        # 2. Update Stats
        self.timer += 1
        q_ns = sum(1 for c in self.cars if c.waiting and c.direction in [NORTH, SOUTH])
        q_ew = sum(1 for c in self.cars if c.waiting and c.direction in [EAST, WEST])
        
        current_max = 0
        for c in self.cars:
            if c.waiting:
                self.total_wait_time += 1/60
                if c.current_wait > current_max: current_max = c.current_wait
        self.max_current_wait = current_max

        # 3. Detect Ambulance
        amb_detected = False
        amb_needed_state = None
        
        # We loop through cars to find if an ambulance exists in the simulation
        for c in self.cars:
            if c.is_ambulance:
                amb_detected = True
                if c.direction in [NORTH, SOUTH]:
                    amb_needed_state = "NS"
                else:
                    amb_needed_state = "EW"
                break # Prioritize the first ambulance found

        # --- DECISION LOGIC ---
        should_switch = False
        TRADITIONAL_CYCLE = 300 

        # === AMBULANCE OVERRIDE LOGIC ===
        if amb_detected:
            # If Ambulance needs NS Green
            if amb_needed_state == "NS":
                if "EW_GREEN" in self.state:
                    should_switch = True # Must switch immediately
                elif "NS_GREEN" in self.state:
                    self.timer = 0 # RESET Timer to keep it green indefinitely
                    should_switch = False 
            
            # If Ambulance needs EW Green
            elif amb_needed_state == "EW":
                if "NS_GREEN" in self.state:
                    should_switch = True # Must switch immediately
                elif "EW_GREEN" in self.state:
                    self.timer = 0 # RESET Timer to keep it green indefinitely
                    should_switch = False

        else:
            # === NORMAL LOGIC (Only runs if no ambulance) ===
            if self.mode.startswith("AI"):
                if "NS_GREEN" in self.state:
                    if (q_ew > 0 and q_ns == 0) or (q_ew > q_ns + 4): 
                        if self.timer > 60: should_switch = True
                elif "EW_GREEN" in self.state:
                    if (q_ns > 0 and q_ew == 0) or (q_ns > q_ew + 4):
                        if self.timer > 60: should_switch = True
            else:
                # Timer Logic
                if self.timer > TRADITIONAL_CYCLE: should_switch = True

        # --- STATE EXECUTION (Transitions) ---
        # This part ensures we cycle correctly (Green -> Yellow -> Red -> Green)
        
        if self.state == "NS_GREEN":
            if should_switch:
                self.state = "NS_YELLOW"
                self.timer = 0
                
        elif self.state == "NS_YELLOW":
            # Yellow must finish its cycle
            if self.timer > 90: 
                self.state = "ALL_RED_TO_EW"
                self.timer = 0
                
        elif self.state == "ALL_RED_TO_EW":
            # Safety Red must finish
            if self.timer > 40: 
                self.state = "EW_GREEN"
                self.timer = 0
                
        elif self.state == "EW_GREEN":
            if should_switch:
                self.state = "EW_YELLOW"
                self.timer = 0
                
        elif self.state == "EW_YELLOW":
            if self.timer > 90: 
                self.state = "ALL_RED_TO_NS"
                self.timer = 0
                
        elif self.state == "ALL_RED_TO_NS":
            if self.timer > 40: 
                self.state = "NS_GREEN"
                self.timer = 0

        # 4. Move Cars
        for car in self.cars[:]:
            light = "RED"
            # Determine if this car sees Green based on Direction
            if car.direction in [NORTH, SOUTH]:
                if "NS_GREEN" in self.state: light = "GREEN"
            else:
                if "EW_GREEN" in self.state: light = "GREEN"
            
            same_lane = [c for c in self.cars if c.direction == car.direction and c != car]
            car.move(self.stop_lines[car.direction], light, same_lane)
            
            # Despawn Logic
            if not (-100 < car.rect.x < WIDTH + 100 and -100 < car.rect.y < HEIGHT + 100):
                self.cars.remove(car)
                self.passed_count[car.direction] += 1
                self.total_cars_finished += 1

    def draw_dashboard(self, screen, font, font_bold):
        panel = pygame.Surface((280, 260), pygame.SRCALPHA)
        panel.fill(UI_BG_COLOR)
        screen.blit(panel, (20, 20))
        
        color = CYAN_AI if self.mode.startswith("AI") else ORANGE_TRAD
        screen.blit(font_bold.render(f"SYSTEM: {self.mode.split(' ')[0]}", True, color), (35, 30))
        
        y = 70
        def draw_pass_row(label, p_val, y_pos):
            screen.blit(font.render(f"{label}", True, TEXT_GRAY), (35, y_pos))
            screen.blit(font.render(f"Passed: {p_val}", True, GREEN_LIGHT), (160, y_pos))

        draw_pass_row("NORTH", self.passed_count[NORTH], y); y+=25
        draw_pass_row("SOUTH", self.passed_count[SOUTH], y); y+=25
        draw_pass_row("EAST ", self.passed_count[EAST], y); y+=25
        draw_pass_row("WEST ", self.passed_count[WEST], y); y+=35

        pygame.draw.line(screen, TEXT_GRAY, (35, y), (260, y), 1)
        y += 10
        avg_wait = self.total_wait_time / self.total_cars_finished if self.total_cars_finished > 0 else 0.0
        screen.blit(font_bold.render(f"Avg Wait: {avg_wait:.1f} sec", True, TEXT_WHITE), (35, y)); y+=30
        
        screen.blit(font.render("[SPACE] Switch Mode", True, (150,150,150)), (35, y)); y+=20
        screen.blit(font.render("[R] Reset Stats", True, (150,150,150)), (35, y)); y+=20
        screen.blit(font.render("[A] Spawn Ambulance", True, (255, 100, 100)), (35, y))

    def draw_on_road_stats(self, screen, font):
        q_n = sum(1 for c in self.cars if c.waiting and c.direction == NORTH)
        q_s = sum(1 for c in self.cars if c.waiting and c.direction == SOUTH)
        q_e = sum(1 for c in self.cars if c.waiting and c.direction == EAST)
        q_w = sum(1 for c in self.cars if c.waiting and c.direction == WEST)
        
        if q_n > 0: screen.blit(font.render(f"Waiting: {q_n}", True, TEXT_YELLOW), (WIDTH//2 + 80, HEIGHT//2 + 80))
        if q_s > 0: screen.blit(font.render(f"Waiting: {q_s}", True, TEXT_YELLOW), (WIDTH//2 - 180, HEIGHT//2 - 100))
        if q_e > 0: screen.blit(font.render(f"Waiting: {q_e}", True, TEXT_YELLOW), (WIDTH//2 - 120, HEIGHT//2 + 80))
        if q_w > 0: screen.blit(font.render(f"Waiting: {q_w}", True, TEXT_YELLOW), (WIDTH//2 + 80, HEIGHT//2 - 100))

    def draw_scene(self, screen, font):
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, ROAD_COLOR, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
        pygame.draw.rect(screen, ROAD_COLOR, (0, HEIGHT//2 - ROAD_WIDTH//2, WIDTH, ROAD_WIDTH))
        
        for y in range(0, HEIGHT, 40): 
            if not (HEIGHT//2 - ROAD_WIDTH//2 < y < HEIGHT//2 + ROAD_WIDTH//2):
                pygame.draw.line(screen, (200, 200, 0), (WIDTH//2, y), (WIDTH//2, y+20), 2)
        for x in range(0, WIDTH, 40):
            if not (WIDTH//2 - ROAD_WIDTH//2 < x < WIDTH//2 + ROAD_WIDTH//2):
                pygame.draw.line(screen, (200, 200, 0), (x, HEIGHT//2), (x+20, HEIGHT//2), 2)

        stop_col = LINE_COLOR
        pygame.draw.line(screen, stop_col, (WIDTH//2, self.stop_lines[NORTH]), (WIDTH//2+ROAD_WIDTH//2, self.stop_lines[NORTH]), 4)
        pygame.draw.line(screen, stop_col, (WIDTH//2-ROAD_WIDTH//2, self.stop_lines[SOUTH]), (WIDTH//2, self.stop_lines[SOUTH]), 4)
        pygame.draw.line(screen, stop_col, (self.stop_lines[EAST], HEIGHT//2), (self.stop_lines[EAST], HEIGHT//2+ROAD_WIDTH//2), 4)
        pygame.draw.line(screen, stop_col, (self.stop_lines[WEST], HEIGHT//2-ROAD_WIDTH//2), (self.stop_lines[WEST], HEIGHT//2), 4)

        screen.blit(font.render("N", True, (0,0,0)), (WIDTH//2 - 5, 10))
        screen.blit(font.render("S", True, (0,0,0)), (WIDTH//2 - 5, HEIGHT - 30))
        screen.blit(font.render("W", True, (0,0,0)), (10, HEIGHT//2 - 10))
        screen.blit(font.render("E", True, (0,0,0)), (WIDTH - 30, HEIGHT//2 - 10))

    def draw_lights(self, screen):
        ns_color = RED_LIGHT
        if "NS_GREEN" in self.state: ns_color = GREEN_LIGHT
        elif "NS_YELLOW" in self.state: ns_color = YELLOW_LIGHT
        
        ew_color = RED_LIGHT
        if "EW_GREEN" in self.state: ew_color = GREEN_LIGHT
        elif "EW_YELLOW" in self.state: ew_color = YELLOW_LIGHT
        
        off = ROAD_WIDTH//2 + 20
        pygame.draw.circle(screen, ns_color, (WIDTH//2 + off, HEIGHT//2 + off), 12) 
        pygame.draw.circle(screen, ns_color, (WIDTH//2 - off, HEIGHT//2 - off), 12) 
        pygame.draw.circle(screen, ew_color, (WIDTH//2 - off, HEIGHT//2 + off), 12) 
        pygame.draw.circle(screen, ew_color, (WIDTH//2 + off, HEIGHT//2 - off), 12) 

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Professional Traffic AI Simulation")
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Verdana", 14)
    font_bold = pygame.font.SysFont("Verdana", 18, bold=True)
    
    sim = TrafficSim()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sim.mode = "AI OPTIMIZED" if sim.mode == "TRADITIONAL (TIMER)" else "TRADITIONAL (TIMER)"
                if event.key == pygame.K_r:
                    sim.reset_stats()
                if event.key == pygame.K_a: # Spawn Ambulance
                    sim.spawn_ambulance()

        sim.update()
        sim.draw_scene(screen, font_bold)
        sim.draw_on_road_stats(screen, font_bold)
        for car in sim.cars:
            car.draw(screen)
        sim.draw_lights(screen)
        sim.draw_dashboard(screen, font, font_bold)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()