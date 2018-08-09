import os
os.chdir('/Users/lezardvaleth/Documents/Python/AVG')

#notice the difference from directly import xxx
from Awaken_Room import Awaken_Room
room = Awaken_Room()
while True:
    play = getattr(room,'start')
    room = play()


