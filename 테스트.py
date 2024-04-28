import pygame
import random
import sys

# 게임 초기화
pygame.init()

# 화면 크기 설정 (너비, 높이)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meteor Protector")

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 화면을 4등분하여 구획을 생성하는 함수
def create_quadrants():
    quadrants = []
    quadrant_width = SCREEN_WIDTH // 2
    quadrant_height = SCREEN_HEIGHT // 2
    
    # 4등분을 위한 선을 그립니다.
    pygame.draw.line(screen, WHITE, (quadrant_width, 0), (quadrant_width, SCREEN_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, quadrant_height), (SCREEN_WIDTH, quadrant_height))

    # 정사각형의 좌표를 생성합니다.
    for x in range(2):
        for y in range(2):
            quadrant = pygame.Rect(x * quadrant_width, y * quadrant_height, quadrant_width, quadrant_height)
            quadrants.append(quadrant)
    return quadrants

# 각 구획의 중심 좌표
quadrant_centers = [(200, 200), (600, 200), (200, 600), (600, 600)]

# 각 구획에 빨간색 원을 그리는 함수
def draw_red_circle_at_quadrant_centers():
    for center in quadrant_centers:
        pygame.draw.circle(screen, RED, center, 10)  # 빨간색 원 그리기

# 각 구획의 중심을 계산하는 함수
def calculate_quadrant_center(quadrant):
    return (quadrant.left + quadrant.width // 2, quadrant.top + quadrant.height // 2)

# 각 구획에 원을 생성하는 함수
def create_circle(quadrant, circles):
    if calculate_quadrant_center(quadrant) not in quadrant_centers:
        return None  # 원이 생성되는 위치가 제한된 위치가 아니면 None 반환

    for circle in circles:
        if circle[0].colliderect(quadrant):
            return None  # 이미 구획에 원이 있는 경우 None 반환

    radius = random.randint(5, 20)  # 랜덤한 크기의 원 생성
    center_x, center_y = calculate_quadrant_center(quadrant)  # 각 구획의 중심을 계산합니다.
    x = random.randint(center_x - radius, center_x + radius)
    y = random.randint(center_y - radius, center_y + radius)
    circle_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
    return circle_rect, 1  # 반지름 정보를 함께 반환합니다.

# 게임 루프
def main():
    # 게임 종료 여부
    running = True

    # 구획 생성
    quadrants = create_quadrants()

    # 생성된 원들을 담을 리스트
    circles = []

    clock = pygame.time.Clock()  # 게임 속도 조절을 위한 clock 객체 생성
    time_since_last_growth = 0  # 마지막으로 원의 크기가 증가한 시간

    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 원 생성
        for quadrant in quadrants:
            if random.random() < 0.01:  # 원을 랜덤한 주기로 생성합니다.
                circle = create_circle(quadrant, circles)
                if circle:
                    circles.append(circle)

        # 원의 크기 증가 처리
        time_elapsed = clock.tick(30)  # 경과한 시간 (밀리초 단위)
        time_since_last_growth += time_elapsed
        if time_since_last_growth >= 10:  # 10ms마다 크기를 증가시킵니다.
            for i, circle in enumerate(circles):
                circle_rect, radius = circle
                if radius < 20:
                    radius += 1
                    circles[i] = (circle_rect, radius)  # 업데이트된 원 정보를 다시 저장합니다.
            time_since_last_growth = 0

        # 화면 업데이트
        screen.fill(BLACK)  # 배경을 검은색으로 설정합니다.
        for quadrant in quadrants:
            pygame.draw.rect(screen, WHITE, quadrant, 1)  # 사각형 그리기
        
        # 빨간색 원 그리기
        draw_red_circle_at_quadrant_centers()
        
        for circle in circles:
            pygame.draw.circle(screen, RED, circle[0].center, circle[1])  # 원 그리기

        pygame.display.flip()

    # 게임 종료
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
