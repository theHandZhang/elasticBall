class Account:
    def __init__(self, settings, account_name):

        if account_name == 'account':
            raise Exception("account name can not be 'account'!", account_name)
        self.account_name = account_name
        self.score = 0
        self.ball_num = settings.ball_num
        self.play_num = 0
        self.play_time = 0

    def store_info(self):
        file_path = 'account_information/' + self.account_name + '.txt'
        file = open(file_path, 'a')
        file.write()