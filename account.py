class Account:
    def __init__(self, settings, account_name):
        self.account_name = account_name
        self.score = 0
        self.ball_num = settings.ball_num
        self.play_num = 0
        self.play_time = 0