from game_unit.brick import Brick


def get_bricks(settings, bricks, screen):
    for i in range(settings.brick_num):
        bricks.add(Brick(settings, screen, (62 + 124 * i, 50)))

    for i in range(settings.brick_num):
        bricks.add(Brick(settings, screen, (62 + 124 * i, 100)))
