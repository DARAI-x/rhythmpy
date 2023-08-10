import pygame
import math

pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Continuous Object Rotation and Text Display")

# 이미지 로드
character = pygame.image.load("C:/Users/손종후/OneDrive/바탕 화면/temp/12in-Vinyl-LP-Record-Angle.jpg")

# 캐릭터 초기 위치 설정
character_width = 100
character_height = 100
character_x_pos = -80 - character_width // 2
character_y_pos = size[1] - character_height

original_width = character.get_width()
original_height = character.get_height()
new_width = 100
new_height = 100
character_resized = pygame.transform.scale(character, (new_width, new_height))

initial_speed = 5
speed_decrement = 0.02
delay = 10

rotation_angle = 0

# 글꼴 설정
font = pygame.font.Font(None, 36)
text = "bgm-() by()     "
text_surface = font.render(text, True, (255, 255, 255))
text_width = text_surface.get_width()
text_height = text_surface.get_height()
#스코어보드
scoreboardbrightness = 255

font = pygame.font.Font(None, 36)
main = "bgm-() by()     "
main_surface = font.render(main, True, (255, 255, 255))
main_width = text_surface.get_width()
main_height = text_surface.get_height()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 캐릭터 위치 업데이트
    character_x_pos += initial_speed
    if character_x_pos > size[0]:
        character_x_pos = -new_width
        initial_speed = 5

    initial_speed -= speed_decrement

    rotation_angle += 2.5
    if rotation_angle > 360:
        rotation_angle = 0

    # 회전한 이미지 생성
    rotated_character = pygame.transform.rotate(character_resized, rotation_angle)

    screen.fill((0, 0, 0))

    # 글씨 위치 계산
    text_x = character_x_pos - text_width - 10  # 캐릭터 왼쪽에 위치
    text_y = character_y_pos + new_height // 2 - text_height // 2

    # 왼쪽에 글씨 그리기
    screen.blit(text_surface, (text_x, text_y))

    # 스코어보드 그리기
    pygame.draw.rect(screen, (30, 30, scoreboardbrightness), (screen_width/2-250, screen_height/2 - 150, 500, 300),1)  # 전광판 위치와 크기 설정
    rotated_rect = rotated_character.get_rect(center=(character_x_pos + new_width // 2, character_y_pos + new_height // 2))
    screen.blit(rotated_character, rotated_rect)

    pygame.display.flip()
    pygame.time.delay(delay)

pygame.quit()
