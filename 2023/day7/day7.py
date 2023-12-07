from collections import defaultdict
lines = [line.rstrip().split() for line in open('mini.txt', 'r').readlines()]
suits = ['T', 'Q', 'K', 'A']
cards = ['*', 'J'] + list(str(_) for _ in range(2,10)) + suits
five_kind = 0
four_kind = 1
full_house = 2
three_kind = 3
two_pair = 4
one_pair = 5
high_card = 6

hands = {}
hand_bids = []

def type_of(hand):
    current_hand = defaultdict(int)
    for card in hand:
        current_hand[card] += 1
    type = None
    for card,freq in current_hand.items():
        if freq == 5:
            type = five_kind
            break
        elif freq == 4:
            type = four_kind
            break
        elif freq == 3:
            type = full_house if len(current_hand) == 2 else three_kind
            break
        elif freq == 2:
            type = two_pair if len(current_hand) == 3 else one_pair
            type = full_house if len(current_hand) == 2 else type
            break
        else: type = high_card
    assert type != None
    return type

for hand, bid in lines:
    group = []
    group.append((hand,bid))
    if 'J' in hand: 
        new_hand = hand.replace('J', '*')
        group.append((new_hand, bid))
    print(group)
    best_type = type_of(hand)
    best_entry = (hand,)
    if best_type in hands:
        hands[best_type].append(best_entry)
    else:
        hands[best_type] = [best_entry]

def custom_lex_order(char): 
    return cards.index(char)

def custom_sort(s):
    order_values = tuple(custom_lex_order(char) for char in s)
    return order_values

hands = sorted(list(hands.items()), reverse=True)
ans = 0
rank = 1

def heads(xs):
    return [x for x,_ in xs]
for k,v in hands:
    vs = sorted(v, key=lambda x: custom_sort(x[0]), reverse=False)
    for hand,bid in vs:
        ans += rank*bid
        rank += 1

# 6440
# pt2 5905
print(ans)

            

            
# too high pt2
251924230
251929880
251929880
251949996
