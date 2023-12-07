from collections import defaultdict
from ordered_enum import OrderedEnum
lines = [line.rstrip().split() for line in open('mini.txt', 'r').readlines()]
suits = ['T', 'Q', 'K', 'A']
cards = ['J'] + list(str(_) for _ in range(2,10)) + suits

def freq(hand):
    freq = defaultdict(int)
    for card in hand:
        freq[card] += 1
    return freq

class HandType(OrderedEnum):
    HighCard = 0,
    OnePair = 1,
    TwoPair = 2,
    ThreeKind = 3,
    FullHouse = 4,
    FourKind  = 5,
    FiveKind = 6

def get_type(hand) -> HandType:
    dist = freq(hand)
    n = len(dist)
    if n == len(hand):
        return HandType.HighCard
    if n == 1:
        return HandType.FiveKind
    freqs = set(dist.values())
    if n == 2:
        if 3 in freqs: return HandType.FullHouse
        if 4 in freqs: return HandType.FourKind
    if n == 3:
        if 3 in freqs: return HandType.ThreeKind
        return HandType.TwoPair
    return HandType.OnePair

def custom_lex_order(char): 
    return cards.index(char)

def custom_sort(tup):
    _, original_hand = tup
    order_values = tuple(custom_lex_order(char) for char in original_hand)
    return order_values

def get_variations(hand):
    res = [(hand,hand)]
    for suit in cards:
        if suit == 'J': continue
        new_hand = hand.replace('J', suit)
        res.append((new_hand, hand))
    return res

hands = defaultdict(list)
for original_hand, bet in lines:
    best_type = HandType.HighCard
    best_hand = original_hand
    new_hands = get_variations(original_hand)
    for hand in new_hands:
        type = get_type(hand)
        if type > best_type:
            best_type = type
            best_hand = hand
    hands[best_type].append(((best_hand, original_hand), int(bet)))

hands = sorted(hands.items(), key=lambda tup: tup[0])
print(hands)
rank = 1
ans = 0
for type, hands in hands:
    print(type, hands)
    new_hands = sorted(hands, key=lambda x: custom_sort(x[0]), reverse=False)
    for hand, bet in new_hands:
        ans += rank * bet
        rank += 1
print(ans)
