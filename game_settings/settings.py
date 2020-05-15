class Settings:

    def __init__(self):
        self.screen_size = (1200, 1000)

        self.screen_color = (230, 230, 230)

        self.button_width = 150
        self.button_height = 40
        self.button_color = (0, 255, 0)
        self.button_selected_color = (0, 139, 0)
        self.button_text_color = (255, 255, 255)

        self.ball_moving_speed = float(0.9)
        self.ball_decrease_speed = float(0.0001)
        self.ball_num = 2

        self.brick_width = 80
        self.brick_height = 20
        self.brick_color = (205, 133, 63)
        self.brick_drop_speed = 0.01
        self.brick_increase_speed = 0.0
        self.brick_num = 8
        self.brick_rows = 7

        self.player_brick_width = 200
        self.player_brick_height = 20
        self.player_brick_color = (147, 112, 219)
        self.player_brick_speed = 1

        self.input_box_text_color = (0, 0, 0)
        self.input_box_text_width = 200

        self.vector_size = 80
        self.vector_wing_size = 10
