import os
import random
import sys
import time

def clear_screen():
  
    os.system('cls' if os.name == 'nt' else 'clear')

def firework_simulation():
    clear_screen()
    
   
    colors = [
        "\033[91m", 
        "\033[92m", 
        "\033[93m",  
        "\033[94m", 
        "\033[95m",  
        "\033[96m",  
    ]
    reset_color = "\033[0m"
    particles = ["*", "+", "o", "•", "✦", "★", "·"]

    width = 50
    height = 20

    print("Countdown to launch starting...\n")
    time.sleep(1)

    for rocket in range(5):
        
        for y in range(height, height // 2, -1):
            clear_screen()
            print("\n" * y + " " * (width // 2) + "🚀 |")
            time.sleep(0.06)

      
        chosen_color = random.choice(colors)
        for radius in range(1, 6):
            clear_screen()
            canvas = [[" " for _ in range(width)] for _ in range(height)]
            center_x = width // 2
            center_y = height // 2

            for _ in range(radius * 12):
                dx = random.randint(-radius * 2, radius * 2)
                dy = random.randint(-radius, radius)
                nx, ny = center_x + dx, center_y + dy

                if 0 <= nx < width and 0 <= ny < height:
                    canvas[ny][nx] = random.choice(particles)

           
            lines = ["".join(row) for row in canvas]
            sys.stdout.write(chosen_color + "\n".join(lines) + reset_color + "\n")
            sys.stdout.flush()
            time.sleep(0.08)

        time.sleep(0.3)

    clear_screen()
    print(f"\n{random.choice(colors)}✨ Surprise Assignment Successfully Completed! ✨{reset_color}\n")

if __name__ == "__main__":
    firework_simulation()
