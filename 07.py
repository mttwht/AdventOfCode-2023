with open("input-07.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """.splitlines()][1:]
# # Example answer  = 6440


card_strengths = "AKQJT98765432"


def get_hand_strength(hand: str):
    card_counts = {}
    for c in hand:
        if c not in card_counts:
            card_counts[c] = 1
        else:
            card_counts[c] += 1
    
    if 5 in card_counts.values():
        return 0
    elif 4 in card_counts.values():
        return 1
    elif 3 in card_counts.values() and 2 in card_counts.values():
        return 2
    elif 3 in card_counts.values():
        return 3
    elif 2 in card_counts.values() and len(card_counts) == 3:
        return 4
    elif 2 in card_counts.values():
        return 5
    else:
        return 6

def sort_hands(hands: list[str]):
    sorted_hands = {}
    for i in range(7):
        sorted_hands[i] = []

    for line in lines:
        hand, bid = line.split()
        hand_strength = get_hand_strength(hand)
        sorted_hands[hand_strength].append(line)

    for hand_strength in sorted_hands:
        sorted_hands[hand_strength].sort(key=lambda x: [card_strengths.index(c) for c in x[:5]])
        # sorted_hands[hand_strength].reverse()
    
    result = []
    for i in range(7):
        result += sorted_hands[i]

    return result


total_winnings = 0
sorted_hands = sort_hands(lines)
for hand in sorted_hands:
    index = sorted_hands.index(hand)
    rank = len(sorted_hands) - index
    h, bid = hand.split()
    winnings = int(bid) * rank
    total_winnings += winnings

print(total_winnings)
