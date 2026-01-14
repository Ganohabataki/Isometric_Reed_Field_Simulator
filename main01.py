# %pip install windows-curses

import curses
import time
import math

### Configuation ###
MAP_SIZE = 80
SPEED = 0.4
FPS = 90

### Reeds String ###
REED_CHARS = ".:!|/({)}[]<>iI"  # From low wind to high wind

def get_wind_force(x, y, t): 
    """
    Calculate wind force by position and time
    Use trigonometric functions instead of noise library to wind
    Make irregular patterns of wind force with different 3 waves with different frequencies and directions
    """
    wave1_integer = 1
    wave2_integer = 0.5
    wave3_integer = 0.3
    
    # Wave 1 : Diagonal, big
    wave1 = math.sin(x * 0.1 + y * 0.1 + t * 0.5) * wave1_integer
    
    # Wave 2 : X, fast ripples
    wave2 = math.cos(x * 0.2 + t * 1.2) * wave2_integer
    
    # Wave 3 : Y, slow (add complexity)
    wave3 = math.sin(y * 0.3 - t * 0.8) * wave3_integer
    
    # Combine waves 
    total_wave = wave1 + wave2 + wave3
    
    # Normalize to -1 to 1
    return total_wave 

def draw_isometric(stdscr, grid_size, t):
    max_y, max_x = stdscr.getmaxyx()
    center_x = max_x // 2
    center_y = max_y // 3
    
    for y in range(grid_size):
        for x in range(grid_size):
            
            # 1. Calculate wind force
            wind_val = get_wind_force(x,y,t)
            
            # Convert wind value to reed character index
            idx = int((wind_val +1) / 2 * len(REED_CHARS))
            idx = max(0, min(idx, len(REED_CHARS) - 1))
            char = REED_CHARS[idx]
            
            # 2. Convert grid to isometric coordinates
            iso_x = center_x + (x - y) * 4       
            iso_y = center_y + int((x + y) * 0.6) 
            
            # 3. Draw
            if 0 <= iso_x < max_x and 0 <= iso_y < max_y:
                # Coloring : Stronger wind = brighter color
                color_pair = 1 if idx < 3 else 2 
                try : 
                    stdscr.addch(iso_y, iso_x, char, curses.color_pair(color_pair))
                except curses.error:
                    pass
# stdscr is the main window object provided by curses

def main(stdscr):
    """ Repeat drawing"""
    curses.curs_set(0) # Hide cursor
    stdscr.nodelay(True) 
    stdscr.timeout(0)
    
    curses.start_color()
    # Color 1 : Dim green (shadow)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    # Color 2 : Bright yellow (winded reeds, highlight)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    t = 0.0 # Time variable for wind animation
    
    try:
        while True:
            start_time = time.time()
            stdscr.erase()
            
            draw_isometric(stdscr, MAP_SIZE, t)
            
            stdscr.refresh()
            
            t += 0.05 * SPEED
            
            key = stdscr.getch()
            if key == ord('q') or key == 27:
                break
            
            elapsed = time.time() - start_time
            sleep_time = max(0, (1 / FPS) - elapsed)
            time.sleep(sleep_time)
            
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except ImportError:
        print("This program requires the 'curses' module, which is not available on this platform.")
        print("On Windows, you can install it via 'pip install windows-curses'.")