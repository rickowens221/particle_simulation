import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Параметры экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle Simulation with Slower Attraction")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметры частицы
num_particles = 100
particles = []
friction = 0.97  # Коэффициент трения для замедления частиц
chaos_intensity = 0.5  # Интенсивность случайного движения

for _ in range(num_particles):
    x = random.randint(0, width)
    y = random.randint(0, height)
    dx = random.uniform(-1, 1)  # Начальная скорость уменьшена
    dy = random.uniform(-1, 1)
    particles.append([x, y, dx, dy])

# Главный цикл
running = True
while running:
    screen.fill(BLACK)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        # Притягивание частиц к курсору при нажатии
        if mouse_pressed:
            dir_x = mouse_x - particle[0]
            dir_y = mouse_y - particle[1]
            distance = math.sqrt(dir_x ** 2 + dir_y ** 2)
            force = min(1.5, distance / 50)  # Уменьшена максимальная сила притягивания
            particle[2] += (dir_x / distance) * force if distance != 0 else 0
            particle[3] += (dir_y / distance) * force if distance != 0 else 0
        else:
            # Добавляем хаотичное движение при отсутствии нажатия
            particle[2] += random.uniform(-chaos_intensity, chaos_intensity)
            particle[3] += random.uniform(-chaos_intensity, chaos_intensity)

        # Обновление позиции частицы с учетом трения
        particle[0] += particle[2]
        particle[1] += particle[3]

        # Применение трения для замедления
        particle[2] *= friction
        particle[3] *= friction

        # Отражение от стен
        if particle[0] <= 0 or particle[0] >= width:
            particle[2] *= -1
        if particle[1] <= 0 or particle[1] >= height:
            particle[3] *= -1

        # Рисуем частицу
        pygame.draw.circle(screen, WHITE, (int(particle[0]), int(particle[1])), 3)

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()
