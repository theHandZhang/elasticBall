from datetime import datetime


class Account:
    def __init__(self, settings, account_name):

        if account_name == 'account':
            raise Exception("account name can not be 'account'!", account_name)
        self.account_name = account_name
        self.score = 0
        self.ball_num = settings.ball_num
        self.play_time = 0
        self.current_time = 0

    def time_start(self):
        self.current_time = datetime.now()
        print(self.current_time)

    def time_end(self):
        self.play_time = datetime.now() - self.current_time
        print(self.play_time)

    def store_info(self):
        file_path = 'account_information/' + self.account_name + '.txt'
        file = open(file_path, 'a')
        file.write(str(self.play_time) + '##' + str(self.score) + '\n')
        file.close()