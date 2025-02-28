import random
from all_colors import *
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
background_color = (255, 255, 255)
screen.fill(background_color)

x = 0
y = 0
rect_size = 200

colors = [Black, White, DarkSlateGrey, SlateGrey, Red, Green, Blue, Orange, Yellow, Navy, Grey, GreenYellow,
          Brown, RosyBrown, SandyBrown, SaddleBrown, Lime, LimeGreen, Tan, Peru, Cyan, LightCyan, DarkCyan,
          Salmon, DarkSalmon, LightSalmon, Linen, Silver, DimGrey,LightGrey, DarkGrey, Ivory, Beige, Azure,
          Snow, Aqua, Teal, Olive, SeaGreen, Sienna, Chocolate, Maroon, Wheat, Purple, Indigo, Violet, Plum,
          Magenta, Pink, Gold, Coral, Tomato, Khaki, LightSlateGrey, Gainsboro, MistyRose, LavenderBlush]

rects = []
initial_colors = []

def create_rectangles():
    global rects, initial_colors
    for i in range(1, 18):
        rect = pygame.Rect(x, y, rect_size - 12 * i, rect_size - 12 * i)
        rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        rects.append(rect)
        initial_colors.append(random.choice(colors))

create_rectangles()

FPS = 60
clock = pygame.time.Clock()
running = True
color_change_interval = 10
last_color_update_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    if current_time - last_color_update_time >= color_change_interval:
        for i in range(len(rects)):
            initial_colors[i] = random.choice(colors)
        last_color_update_time = current_time

    screen.fill(background_color)

    for i, rect in enumerate(rects):
        pygame.draw.rect(screen, initial_colors[i], rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()