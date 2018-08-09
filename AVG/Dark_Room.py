class Dark_Room(object):
    def __init__(self):
        self.test = 1

    def start(self):
        print('You are teleported to a room.')
        print('It is total darkness around you')
        print('You notice that you have a flashlight and a lighter.')
        print('Which one are you going to use?')
        option = input('>>>')
        if option == 'flashlight':
            print('There is a strange circle in front you.')
            print('You step inside it, and blue light surrounds you.')
            from Death import Death
            room = Death()
            return room
        elif option == 'lighter':
            print('The whole room turns into a gigantice fireball.')
            from Death import Death
            room = Death()
            return room
