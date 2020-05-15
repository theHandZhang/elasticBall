from game_unit.brick import Brick


def get_bricks(settings, bricks, screen):

    for j in range(settings.brick_rows):

        for i in range(settings.brick_num):
            bricks.add(Brick(settings, screen, (62 + 124 * i, 50 + j * 50)))

