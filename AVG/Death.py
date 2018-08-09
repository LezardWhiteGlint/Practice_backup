class Death(object):
    def __init__(self):
        self.test = 1

    def start(self):
        print('You Died.')
        from sys import exit
        exit()
