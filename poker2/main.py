# -*- coding: UTF-8 -*-
import random
from machine.std_mach import create_deck,\
    shuffled_deck,\
    record_deck
from dealer.mike import deal_to_a_player,deal_to_multi_players
# 场景1:
# 拿出一幅新牌,记录，洗牌，在记录
first_deck = []
create_deck(first_deck)
record_deck(first_deck,"deck_001.txt")

shuffled_deck(first_deck)
record_deck(first_deck,"deck_002.txt")
'''
#场景二
Lisa_deck = []
deal_to_a_player(first_deck,5,Lisa_deck)
record_deck(Lisa_deck,"Lisa_deck.txt")

Jimmy_deck = []
deal_to_a_player(first_deck,15,Jimmy_deck)
record_deck(Jimmy_deck,"Jimmy_deck.txt")


Nina_deck = []
deal_to_a_player(first_deck,13,Nina_deck)
record_deck(Nina_deck,"Nina_deck.txt")

Cindy_deck = []
deal_to_a_player(first_deck,7,Cindy_deck)
record_deck(Cindy_deck,"Cindy_deck.txt")

'''
#场景三
Lisa_deck = []
Jimmy_deck = []
Nina_deck = []
Cindy_deck = []
deal_to_multi_players(first_deck,Lisa_deck,Jimmy_deck,Nina_deck,Cindy_deck)
record_deck(Lisa_deck,"Lisa_deck.txt")
record_deck(Jimmy_deck,"Jimmy_deck.txt")
record_deck(Nina_deck,"Nina_deck.txt")
record_deck(Cindy_deck,"Cindy_deck.txt")
