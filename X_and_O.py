import sys

import pygame

pygame.init()
size_block = 100
margin = 15
length = height = size_block * 3 + margin * 4
window_size = (length, height)
arr = [[0] * 3 for i in range(3)]
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
counter = 0
game_over = False


def check_win(array, token):
    zeroes = 0
    for row in array:
        zeroes += row.count(0)
        if row.count(token) == 3:
            return 'Победил '+ token
    for col in range(3):
        if array[0][col] == token and array[1][col] == token and array[2][col] == token:
            return 'Победил '+ token
    if array[0][0] == token and array[1][1] == token and array[2][2] == token:
        return 'Победил '+ token
    if array[2][0] == token and array[1][1] == token and array[0][2] == token:
        return 'Победил '+ token
    if zeroes == 0:
        return 'Ничья'
    return False


screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Крестики нолики')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            i = x_mouse // (margin + size_block)
            j = y_mouse // (margin + size_block)
            if arr[j][i] == 0:
                if counter % 2 == 0:
                    arr[j][i] = 'X'
                else:
                    arr[j][i] = 'O'
                counter += 1
            print((arr))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            arr = [[0] * 3 for i in range(3)]
            counter = 0
            screen.fill(black)
    if not game_over:
        for j in range(3):
            for i in range(3):
                if arr[j][i] == 'X':
                    color = red
                elif arr[j][i] == 'O':
                    color = green
                else:
                    color = white
                x = i * size_block + margin * (i + 1)
                y = j * size_block + margin * (j + 1)
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block / 2, y + size_block / 2), size_block / 2 - 5, 3)
    if (counter - 1) % 2 == 0:
        game_over = check_win(arr, 'X')
    else:
        game_over = check_win(arr, 'O')
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('stxinqkai', 80)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()
