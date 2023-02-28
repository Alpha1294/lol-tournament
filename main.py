from league import Player, Team
import random


# Create 16 Team objects
teams = [
    Team("G2"), Team("Fnatic"), Team("MAD Lions"), Team("Astralis"),
    Team("Evil Geniuses"), Team("Giants"), Team("Misfits"), Team("Vitality"),
    Team("100 Thieves"), Team("Schalke 04 Esports"), Team(
        "T1"), Team("Cloud 9"),
    Team("Splyce"), Team("TSM"), Team("Movistar Riders"), Team("Team Liquid")
]

# Shuffle the list of teams for seeding
random.shuffle(teams)

# Create the first round of matches

matches = [(teams[i], teams[i+1]) for i in range(0, len(teams), 2)]

# Simulate the first round of matches

winners = []

for match in matches:
    print("Match:", match[0].name, "vs", match[1].name)
    winner = random.choice(match)
    print("Winner:", winner.name)
    winners.append(winner)

# Create subsequent round of matches
while len(winners) > 1:
    matches = [(winners[i], winners[i+1]) for i in range(0, len(winners), 2)]
    winners = []
    for match in matches:
        print("Match: ", match[0].name, "vs", match[1].name)
        winner = random.choice(match)
        print("Winner:", winner.name)
        winners.append(winner)

print("Tournament winner:", winners[0].name)
