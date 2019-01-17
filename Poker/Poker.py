'''
This program emulate the texas poker game

problems to be solved:
1. how to decide the scores of each hand
2. how to get all the possible combination
3. 

'''

import random
from copy import deepcopy
from pymongo import MongoClient
import pymongo




#one hand for each player
class Hand(object):
    def __init__(self):
        self.cards = []

    def addCard(self,card):
        assert isinstance(card,tuple), 'card need to be a tuple such as ("Club", 13)'
        self.cards.append(card)

    def getHand(self):
        return self.cards

    def testHand(self):
        self.cards = [('Spade', 10), ('Spade', 11), ('Spade', 12), ('Spade', 13), ('Spade', 14)]

    #draw card
    def drawCard(self,deck):
        result = random.choice(deck)
        deck.remove(result)
        self.addCard(result)

    def clearHand(self):
        self.cards = []

    #for testing purpose
    def setHand(self,lst):
        self.cards = lst[:]



# assemble best hand  using nap sack to solve
class FinalHand(Hand):
    
    def getScore(self):
        '''
        return
        1. score
        2. first comparison
        3. second comparison if the first one is tied
        '''
        cards = self.getHand()
        #get all the numbers out
        card_num = []
        card_color = []
        for c in cards:
            card_num.append(c[1])
        card_num.sort()
        for color in cards:
            card_color.append(color[0])
        #royal Flush
        if ('Spade', 10) in cards and ('Spade', 11) in cards and ('Spade', 12) in cards and ('Spade', 13) in cards and ('Spade', 14) in cards:
            return 10,15,card_num[4] # 10 is the strong is hand, and 15 is for number comparing
        #straight flush
        elif card_num[0] + 4 == card_num[1] + 3 == card_num[2] + 2 == card_num[3] + 1 == card_num[4] and card_color[0] == card_color[1] == card_color[2] == card_color[3] == card_color[4]:
            return 9, card_num[4],card_num[4]
        #four of a kind
        elif card_num[0] == card_num[1] == card_num[2] == card_num[3] or card_num[1] == card_num[2] == card_num[3] == card_num[4]:
            return 8,card_num[3],card_num[4]
        #full house
        elif card_num[0] == card_num[1] == card_num[2] and card_num[3] == card_num[4]:
            return 7, card_num[2],card_num[4]
        elif card_num[0] == card_num[1] and card_num[2] == card_num[3] == card_num[4]:
            return 7,card_num[4],card_num[1]
        #flush
        elif card_color[0] == card_color[1] == card_color[2] == card_color[3] == card_color[4]:
            return 6,card_num[4],card_num[4]
        #straight
        elif card_num[0] + 4 == card_num[1] + 3 == card_num[2] + 2 == card_num[3] + 1 == card_num[4]:
            return 5,card_num[4],card_num[4]
        #three of a kind
        elif card_num[0] == card_num[1] == card_num[2]:
            return 4, card_num[2],card_num[4]
        elif card_num[1] == card_num[2] == card_num[3]:
            return 4, card_num[3],card_num[4]
        elif card_num[2] == card_num[3] == card_num[4]:
            return 4, card_num[4],card_num[1]
        #two pairs
        elif card_num[0] == card_num[1] and card_num[2] == card_num[3] or card_num[1] == card_num[2] and card_num[3] == card_num[4]:
            return 3, card_num[3],card_num[1]
        #pair
        elif card_num[0] == card_num[1]:
            return 2, card_num[1],card_num[4]
        elif card_num[1] == card_num[2]:
            return 2, card_num[2],card_num[4]
        elif card_num[2] == card_num[3]:
            return 2, card_num[3],card_num[4]
        elif card_num[3] == card_num[4]:
            return 2, card_num[4],card_num[2]
        #high card
        else:
            return 1, card_num[4],card_num[4]

#build a deck
def deckBuilder():
    shape = ['Spade', 'Heart', 'Diamond','Club']
    deck = []
    for s in shape:
        for num in range(13):
            card = (s,num+2)
            deck.append(card)
    return deck


# get new card
def drawCard(deck):
    result = random.choice(deck)
    deck.remove(result)
    return result, deck


#get public pool cards
def publicSet(deck):
    result = []
    for i in range(5):
        card,deck = drawCard(deck)
        result.append(card)
    return result,deck

#get best hand by combine initial hand with 3 public card

def getBestHand(hand,hand_and_publicSet):
    '''
    hand: input with 2 cards
    pulicSet: input with 5 cards
    card_count : need 5 to be evaluated
    using brutal force algorithem
    '''
    result = (0,0,0)
    try:
        if len(hand.getHand()) == 5:
            result = hand.getScore()
        else:
            nextCard = hand_and_publicSet[0]
            #print(publicSet)
            other_hand = deepcopy(hand)
            hand.addCard(nextCard)
            with_score, with_first_c, with_second_c = getBestHand(hand,hand_and_publicSet[1:])
            without_score, without_first_c, without_second_c = getBestHand(other_hand,hand_and_publicSet[1:])
            if with_score > without_score or with_score == without_score and with_first_c > without_first_c or with_score == without_score and with_first_c == without_first_c and with_second_c > without_second_c:
                result = (with_score, with_first_c, with_second_c)
                #print('go left')
            else:
                result = (without_score, without_first_c, without_second_c)
                #print('go right')
    except IndexError:
        pass
    return result

        
        

#compare the hand decide which one is the wining hand
def handsCompare(result_a,result_b):
    if result_a[0] > result_b[0] or result_a[0] == result_b[0] and result_a[1] > result_b[1] or result_a[0] == result_b[0] and result_a[1] == result_b[1] and result_a[2] > result_b[2]:
        return result_a
    else:
        return result_b

def run(player_num = 2):
    deck = deckBuilder()
    #set player list
    players = []
    initial_hand = []
    results = {}
    for i in range(player_num):
        players.append(FinalHand())
    #print(players)
    #player draw cards
    for i in range(2):
        for p in players:
            p.drawCard(deck)
    #remember initial hand for statics
    for p in players:
        temp = p.getHand()
        temp.sort()
        initial_hand.append(temp[:])
        #print(initial_hand)
    #print(initial_hand)
    #public set
    pool,deck = publicSet(deck)
    #each player get their best hand
    for m in range(len(players)):
        hand_and_publicSet = players[m].getHand() + pool
        #print(hand_and_publicSet)
        players[m].clearHand()
        #print(players[m].getHand())
        r = getBestHand(players[m],hand_and_publicSet)
        #print(r)
        results[str(initial_hand[m])] = r
    #print(results)
    #compare and output
    temp_a = results[list(results.keys())[0]]
    for n in range(len(results)-1):
        temp_b = results[list(results.keys())[n+1]]
        temp_a = handsCompare(temp_a,temp_b)
    #look for winner key
    for k in results:
        if results[k] == temp_a:
            return k,temp_a,initial_hand


def main(player_num=2,runtimes=1):
    client = MongoClient()
    DB = client.Poker
    Collection = DB['player_num_'+str(player_num)]
    for i in range(runtimes):
        result,score,initial_hands = run(player_num)
        post1 = {'tag' : 'winner',
            'initial_hand' : result,
                'score' : score}
        Collection.insert_one(post1)
        for e in initial_hands:
            post2 = {'tag' : 'all',
                'initial_hand' : e,
                    'score' : (0,0,0)}
            Collection.insert_one(post2)
        #print(post)
        


##def unit_test():
##    deck = deckBuilder()
##    player_a = FinalHand()
##    player_b = FinalHand()
##    for i in range(5):
##        player.drawCard(deck)
##    score, first_c, second_c = player.getScore()
##    return score, first_c, second_c
##
####def multi_test(session=10):
####    result ={}
####    for i in range(session):
####        score, first_c, second_c = unit_test()
####        try:
####            result[score] += 1
####        except KeyError:
####            result[score] = 1
####    return result
#####result = multi_test()
##
####deck = deckBuilder()
##
####for i in range(2):
####    player.drawCard(deck)
####pool,deck = publicSet(deck)
##player = FinalHand()
##pool = [('Heart', 7), ('Club', 9), ('Diamond', 10), ('Diamond', 10), ('Spade', 13)]
##player.setHand([('Heart', 2), ('Club', 3)])
##result = getBestHand(player,pool)

for i in range(1000000):
    main(7,1)
    if (i+1) % 1000 == 0:
        print(i+1)
        

