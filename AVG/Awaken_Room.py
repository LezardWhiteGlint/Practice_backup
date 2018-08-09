class Awaken_Room(object):
    def __init__(self):
        self.test = 1

    def start(self):
        print('You wake up in a room.')
        print('You do not remember who you are.')
        print('There is a panel in front of you.')
        print('There are 5 buttons on the panel')
        print('There are flashing digitals 1,2,3,4,5 on those buttons.')
        print('What do you do?(push_1/push_2/push_3/push_4/push_5)')
        option = input('>>>')
        if option == 'push_1':
            from Dark_Room import Dark_Room
            room = Dark_Room()
            return room
        elif option == 'push_2':
            from Dark_Room import Dark_Room
            room = Dark_Room()
            return room
        elif option == 'push_3':
            from Dark_Room import Dark_Room
            room = Dark_Room()
            return room
        elif option == 'push_4':
            from Dark_Room import Dark_Room
            room = Dark_Room()
            return room
        elif option == 'push_5':
            from Dark_Room import Dark_Room
            room = Dark_Room()
            return room
        elif option == 'push_all':
            from End import End
            room = End()
            return room
        else:
            print('You stand there, do nothing.')
            print('Everything is fading away.')
            room = Awaken_Room()
            return room

        
