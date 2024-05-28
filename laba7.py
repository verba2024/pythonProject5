import math
from random import choice, randint as rnd

import pygame
from datetime import datetime

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 100)
BLACK = (0, 0, 29)
COLORS = [RED, BLUE, GRAY, WHITE, GREEN, MAGENTA, CYAN, BLACK]


class GameSettings:
    """
    Класс с настройками игры
    Позволяет быстро изменять любые настройки
    SCREEN_SIZE - размер окна
    GRAVITY_X - гравитация по x
    GRAVITY_Y - гравитация по y
    """

    SCREEN_SIZE = (800, 600)
    GRAVITY_X = 0
    GRAVITY_Y = 9.8
    FPS = 30
    HARD = 1

timepiece = 0
# timepiece - разница времени между текущим и предыдущим кадром[c]


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Класс мяча
        Args:
        x и y - начальное положение мяча по горизонтали и по вертикали
        self.vx и self.vy - скорость мяча по x и y соответственно
        self.live - время существования мяча
        self.crash - количество возможных отскоков
        """

        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(COLORS)
        self.live = 15
        self.crash = 4

    def move(self):
        """Перемещение мяча
        Args:
        self.x и self.y - перемещение мяча по x и y соответственно
        self.vx и self.vy - скорость мяча по x и y соответственно
        GRAVITY_X и GRAVITY_Y - сила гравитации, действующая на мяч по x и y соответственно
        timepiece - разница времени между текущим и предыдущим кадром(в секундах)
        """

        # значение timepiece умноженное на 10
        Timepiece = timepiece * 10
        # обращаемся к классу настроек игры
        self.vx += GameSettings.GRAVITY_X * Timepiece
        self.vy -= GameSettings.GRAVITY_Y * Timepiece

        # проверяем столкновение со стенками по y
        if self.y + self.r >= GameSettings.SCREEN_SIZE[1]:
            if self.crash <= 0:
                # если исчерпал кол-во возможных столкновений со стеной, то мяч исчезает
                return False
            self.crash -= 1
            self.vy /= -math.sqrt(2)
        if self.y - self.r <= 0:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vy /= -math.sqrt(2)

        # проверяем столкновение со стенками по x
        if self.x + self.r >= GameSettings.SCREEN_SIZE[0]:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vx /= -math.sqrt(2)
        if self.x - self.r <= 0:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vx /= -math.sqrt(2)

        # self.x + self.vx * Timepiece - перемещение по x, которое совершил мяч за один кадр
        self.x = max(
            0, min(GameSettings.SCREEN_SIZE[0], self.x + self.vx * Timepiece))
        self.y = max(
            0, min(GameSettings.SCREEN_SIZE[1], self.y - self.vy * Timepiece))

        return True

    def draw(self):  # функция отрисовки мяча
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """
        Функция проверяет, сталкивалкивается ли мяч с целью,
        описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
            distance - расстояние между центрами сталкивающихся объектов
        Returns:
            Возвращает True в случае столкновения мяча и цели.
            В противном случае возвращает False.
        """

        if self.live <= 0:
            return False
        # считаем как гипотенузу прямоугольного треугольника, где катеты - разница координат
        distance = math.sqrt((obj.x - self.x)**2 + (obj.y - self.y)**2)
        # Проверка на возможность столкновения объектов
        if distance <= self.r + obj.r:
            return True
        return False


class JumpingBall(Ball):
    """
  Прыгающий мяч
    """
    def __init__(self, screen, x=40, y=450):
        # super() позволяет вызывать методы, реализованные в базовом классе
        super().__init__(screen, x, y)
        self.crash = 15

    def move(self):
        """Перемещение прыгающего мяча
            Args:
            self.x и self.y - перемещение мяча по x и y соответственно
            self.vx и self.vy - скорость мяча по x и y соответственно
            GRAVITY_X и GRAVITY_Y - сила гравитации, действующая на мяч по x и y соответственно
            timepiece - разница времени между текущим и предыдущим кадром(в секундах)
        """
        Timepiece = timepiece * 10

        self.vx += GameSettings.GRAVITY_X * Timepiece
        self.vy -= GameSettings.GRAVITY_Y * Timepiece

        if self.y + self.r >= GameSettings.SCREEN_SIZE[1]:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vy /= -math.sqrt(1.25)
        if self.y - self.r <= 0:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vy /= -math.sqrt(1.25)

        if self.x + self.r >= GameSettings.SCREEN_SIZE[0]:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vx /= -math.sqrt(1.25)
        if self.x - self.r <= 0:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vx /= -math.sqrt(1.25)

        self.x = max(
            0, min(GameSettings.SCREEN_SIZE[0], self.x + self.vx * Timepiece))
        self.y = max(
            0, min(GameSettings.SCREEN_SIZE[1], self.y - self.vy * Timepiece))

        return True


class FlyingBall(Ball):
    def __init__(self, screen, x=40, y=450):
        super().__init__(screen, x, y)
        self.color = choice(COLORS)

    def move(self):
        Timepiece = timepiece * 10

        if self.y + self.r >= GameSettings.SCREEN_SIZE[1]:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vy /= -math.sqrt(1.25)
        if self.y - self.r <= 0:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vy /= -math.sqrt(1.25)

        if self.x + self.r >= GameSettings.SCREEN_SIZE[0]:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vx /= -math.sqrt(1.25)
        if self.x - self.r <= 0:
            if self.crash <= 0:
                return False
            self.crash -= 1
            self.vx /= -math.sqrt(1.25)

        self.x = max(
            0, min(GameSettings.SCREEN_SIZE[0], self.x + self.vx * Timepiece))
        self.y = max(
            0, min(GameSettings.SCREEN_SIZE[1], self.y - self.vy * Timepiece))

        return True


AVAILABLE_BALL_TYPES = [
    Ball,
    JumpingBall,
    FlyingBall
]


class BallHandler:
    """
    Выделенный в отдельный класс список шаров, запущенных пушкой
    Содержит функции для работы с шарами
    """
    def __init__(self):
        self.__balls = list()
        self.__balls_will = list()
        self.shot_count = 0

    def add_ball(self, ball):
        """
        Добавляет шар в список
        Args:
            ball - Шар, который нужно добавить в список
        """
        self.__balls.append(ball)

    def remove_ball(self, ball):
        """
        Удаляет шар из списка
        Args:
            ball - Шар, который нужно удалить из списка
        """
        self.__balls.remove(ball)

    def move(self):
        """
        Двигает все шары по игровому полю
        Если шар "умирает", удаляет его из списка
        """
        for ball in self.__balls:
            if not ball.move():
                self.remove_ball(ball)

    def get_next_ball(self):
        """
        Получает следующий шар из списка
        """
        # т.к мы получаем шар только при выстреле, мы можем считать их
        # количество здесь
        self.shot_count += 1

        if len(self.__balls_will) <= 0:
            self.refill()
        ball = self.__balls_will.pop(0)
        return ball

    def get_queue(self):
        """
        Возвращает список шаров, которые будут запущены следующими
        """
        return self.__balls_will

    def refill(self):
        """
        Восполняет список шаров, которые будут запущены
        """
        for i in range(15):
            self.__balls_will.append(
                choice(AVAILABLE_BALL_TYPES)
            )

    def hittest(self, obj):
        """
        Проверяет каждый шар на столкновения с объектов
        Args:
            obj - объект, с которым проверяется столкновение шаров
        Return:
            Возвращает шар, который столкнулся с объектом первым
            Если ни один шар не столкнулся, возвращает None
        """
        for ball in self.__balls:
            if ball.hittest(obj):
                return ball
        return None

    def draw(self):
        """
        Отвечает за отрисовку всех шаров
        """
        for ball in self.__balls:
            ball.draw()


class Gun:
    """
        класс пушки
        Args:
            COLORS[2] - серый
            self.angle - угол, под которым ищ пушки вылетает мяч
            self.active - флаг, показывающий, сидит ли за текущей пушкой игрок
    """
    def __init__(self, screen, balls):
        self.screen = screen

        self.f2_power = 20
        self.f2_on = 0

        self.angle = 1
        self.color = COLORS[4]
        self.balls = balls
        self.shots_done = 0
        self.active = False
        self.r = 10

        self.x = 20
        self.y = 450

    def fire2_start(self, event):
        if not self.active:
            return
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от
        положения мыши.
        """
        if not self.active or not self.f2_on:
            return

        new_ball = self.balls.get_next_ball()(
            self.screen,
            self.x,
            self.y)

        self.angle = math.atan2(
            (event.pos[1]-new_ball.y),
            (event.pos[0]-new_ball.x)
        )

        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = -self.f2_power * math.sin(self.angle)
        self.balls.add_ball(new_ball)
        self.f2_on = 0
        self.f2_power = 20

    def update_position(self, x, y):
        """
        Изменяет позицию пушки, с которой игрок стреляет
        """
        self.x = x
        self.y = y

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if not self.active:
            return
        if event:
            self.angle = math.atan2(
                (event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = COLORS[0]
        else:
            self.color = COLORS[2]

    # Для исключения ошибок, сделаем пустую функцию move()
    def move(self):
        """
        Двигает пушку согласно заданным правилам
        """
        pass

    def draw(self):  # отрисовка пушек
        pygame.draw.circle(
            self.screen,
            self.color if self.active else COLORS[2],
            (
                self.x,
                self.y
            ),
            10
        )
        if not self.active:
            return
        direction = (
            math.cos(self.angle),
            math.sin(self.angle)
        )
        direction = [x * self.f2_power for x in direction]
        pygame.draw.line(  # положение бомбардировщика
            self.screen,
            self.color,
            (self.x, self.y),
            (self.x + direction[0], self.y + direction[1]),
            5
        )

    def power_up(self):
        if self.active and self.f2_on:
            if self.f2_power < 100:
                self.f2_power += timepiece * 100
            self.color = COLORS[0]
        else:
            self.color = COLORS[2]


class MovingGun(Gun):
    """
    Пушка, двигающаяся в заданном направлении
    """
    def __init__(self, screen, balls):
        super().__init__(screen, balls)
        self.from_x = self.x
        self.from_y = self.y
        self.to_x = self.from_x + rnd(-40, 40)
        self.to_y = self.from_y + rnd(-40, 40)

    def update_position(self, x, y):
        """
        Обновляет корневую позицию с учётом цели перемещения
        """
        # Вычисляем расстояние между пушками
        diff_x = x - self.x
        diff_y = y - self.y

        # Обновляем цель перемещения
        self.to_x += diff_x
        self.to_y += diff_y

        # Обновляем положения пушки
        super().update_position(x, y)
        self.from_x = self.x
        self.from_y = self.y

    def move(self):
        """
        Двигает пушку
        """
        def swap_positions(from_x, to_x, from_y, to_y):
            """
            Меняет позиции местами
            """
            tmp_x = to_x
            tmp_y = to_y
            self.to_x = from_x
            self.from_x = tmp_x
            self.to_y = from_y
            self.from_y = tmp_y
        Timepiece = timepiece
        self.x = self.x + (self.to_x - self.x) * Timepiece
        self.y = self.y + (self.to_y - self.y) * Timepiece
        distance = math.sqrt((self.to_x - self.x)**2 + (self.to_y - self.y)**2)
        if distance <= 1:
            swap_positions(self.from_x, self.to_x, self.from_y, self.to_y)


GUN_TYPES = [
    Gun,
    MovingGun
]


class Target:
    def __init__(self, screen, hard):
        """
        Инициализирует цель
        """
        self.screen = screen

        self.x = rnd(600, 780)
        self.y = rnd(300, 550)

        self.origin_x = self.x
        self.origin_y = self.y

        self.r = rnd(*hard.targets_size_range)
        self.color = COLORS[0]

    def move(self):
        """
        Двигает цель по заданному правилу
        """
        pass  # стандартная цель неподвижна, поэтому мы ничего не делаем

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (
                self.x,
                self.y
            ),
            self.r
        )

class MovingTarget(Target):
    """
    Цель, движущаяся туда-орбатно
    """
    def __init__(self, screen, hard):
        super().__init__(screen, hard)
        self.from_x = self.origin_x
        self.from_y = self.origin_y

        self.to_x = self.from_x + rnd(-40, 40)
        self.to_y = self.from_y + rnd(-40, 40)

    def move(self):
        def swap_positions(from_x, to_x, from_y, to_y):
            tmp_x = to_x
            tmp_y = to_y
            self.to_x = from_x
            self.from_x = tmp_x
            self.to_y = from_y
            self.from_y = tmp_y
        Timepiece = timepiece * 0.5
        self.x = self.x + (self.to_x - self.x) * Timepiece
        self.y = self.y + (self.to_y - self.y) * Timepiece
        distance = math.sqrt((self.to_x - self.x)**2 + (self.to_y - self.y)**2)
        if distance <= 1:
            swap_positions(self.from_x, self.to_x, self.from_y, self.to_y)


class FallingTarget(Target):
    """
        Цель, падающая вниз
    """
    def __init__(self, screen, hard):
        super().__init__(screen, hard)
        self.r = 40
        self.vy = 9.8

    def move(self):
        Timepiece = timepiece * 10
        self.vy -= GameSettings.GRAVITY_Y * Timepiece
        self.y -= self.vy * Timepiece

        # Чтобы не удалять цель, помещаем её вверх экрана
        if self.y > GameSettings.SCREEN_SIZE[1] + 40:
            self.y = -40
            self.vy = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (
                self.x,
                self.y
            ),
            self.r
        )


class Bombs:
    """
    Падающие цели
    """
    def __init__(self, screen, x, y, state):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = COLORS[7]
        self.state = state

    def drop(self):
        """
        Цель, падающая вниз
        """
        # Создадим объект цели
        target = FallingTarget(self.screen, self.state.hard)
        target.x = self.x + 20
        target.y = self.y + 35
        # Добавим цель к остальным
        self.state.targets.append(
            target
        )

    def draw(self):
        """
        Отрисовываем "бомбу"
        """
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x, self.y, 40, 15)
        )


class GameHard:
    """
    Класс, содержащий значения, зависящие от сложности
    """
    def __init__(
                 self, targets=4,
                 targets_size_range=(30, 50), allowed_targets=[Target]):
        self.targets = targets
        self.targets_size_range = targets_size_range
        self.allowed_targets = allowed_targets


Hards = [
    GameHard(1, (40, 50), [Target]),
    GameHard(2, (30, 40), [Target, MovingTarget])
]


class GameState:
    """
    Класс, содержащий информацию о текущей игре
    Очки, очередь шаров, цели
    """
    def __init__(self, screen, hard):
        """
        Инициализирует объект класса, содержащий данные о состоянии игры
        Args:
            screen - экран
            difficulty - сложность
        """
        self.points = 0
        self.targets = list()
        self.balls = BallHandler()

        self.bomb = Bombs(screen, GameSettings.SCREEN_SIZE[0] - 400, 10, self)

        self.active_gun = choice(GUN_TYPES)(screen, self.balls)
        self.guns = [choice(GUN_TYPES)(screen, self.balls) for i in range(2)]
        for i in self.guns:
            x = rnd(
                0,
                GameSettings.SCREEN_SIZE[0] // 2)
            y = rnd(
                GameSettings.SCREEN_SIZE[1]//2,
                GameSettings.SCREEN_SIZE[1] - 15)
            i.update_position(x, y)

        self.guns += [self.active_gun]

        self.screen = screen
        self.hard = hard

    def hit_target(self, target):
        """
        Вызывается при попадании по цели
        """
        self.points += 1
        self.balls.shot_count = 0
        self.targets.remove(target)

    def new_round(self):
        """
        Начинает новый раунд
        """
        self.balls.shot_count = 0
        self.targets = [
            choice(self.hard.allowed_targets)(
                self.screen, self.hard) for i in range(
                    self.hard.targets)
        ]


pygame.init()
screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE)
#  Текст на экране
font = pygame.font.Font(pygame.font.get_default_font(), 14)

# Создадим объект класса GameState, содержащий информацию о текущей игре
state = GameState(screen, Hards[GameSettings.HARD])

# Переменная-счётчик для сброса целей с бомбы
dropping_time = 0

clock = pygame.time.Clock()
finished = False

while not finished:
    # Счёт в игре
    screen.fill(COLORS[3])
    text = font.render(
        f"Your score: {state.points}",
        True,
        COLORS[7])
    screen.blit(text, (10, 10))

    # Пока в игре существуют цели
    if len(state.targets) > 0:
        # Выключаем и рисуем все пушки
        for gun in state.guns:
            gun.active = False
            gun.draw()

        # Включаем начальную пушку
        gun = state.active_gun
        gun.active = True

        # Количество оставшихся целей
        text = font.render(
            f" Remaining goals: {len(state.targets)}",
            True,
            COLORS[7])
        screen.blit(text, (6, 22))

        # Количество использованных шаров
        text = font.render(
            f"Spent balls on target: {state.balls.shot_count}",
            True,
            COLORS[7]
        )
        screen.blit(text, (10, 36))

        # Список следующих шаров
        count_ball = 0
        for i in state.balls.get_queue():
            text = font.render(
                f"{str(i).split('.')[-1][:-2]}", True, COLORS[7])
            screen.blit(text, (10, 60 + (count_ball * 13)))
            count_ball += 1

        # Рисуем цели
        for target in state.targets:
            target.draw()
        # Рисуем шары
        state.balls.draw()
        # Рисуем бомбы
        state.bomb.draw()

        pygame.display.update()

        # Используем timestep для вычисления передвижения,
        # чтобы не привязывать скорость шара к количеству FPS
        # clock.tick() возвращает количество миллисекунд,
        # прошедших с последнего кадра
        timepiece = clock.tick(GameSettings.FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                gun.fire2_end(event)
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)

        # Двигаем шары
        state.balls.move()

        # Отсчитываем время для сброса целей с бомбы
        if dropping_time >= 5:
            dropping_time = 0
            state.bomb.drop()
        else:
            dropping_time += timepiece

        # Для переключения между пушками проверяем, попал ли шарик в пушку
        for gun_test in state.guns:
            gun_test.move()
            if gun_test == state.active_gun:
                continue
            htest = state.balls.hittest(gun_test)
            if htest is not None:
                state.balls.remove_ball(htest)
                state.balls.get_queue().insert(0, type(htest))
                state.active_gun = gun_test

        # Для уничтожения целей проверяем, попал ли какой-либо шарик в цель
        for target in state.targets:
            target.move()
            htest = state.balls.hittest(target)
            if htest is not None:
                state.hit_target(target)
                state.balls.remove_ball(htest)

        # Увеличение силы выстрела в конце
        gun.power_up()
    else:
        # Начинаем новый раунд
        state.new_round()

pygame.quit()
