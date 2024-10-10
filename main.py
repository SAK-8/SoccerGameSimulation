import random

# Define player attributes

team_a_info = {'courtois': [13, 'gk', 0],
               'ivanovic': [2, 'rb', 0], 'cahill': [24, 'cb1', 0],'terry':[26, 'cb2', 0], 'azpilicueta':[28, 'lb', 0],
               'hazard':[10, 'lm', 0], 'fabregas':[4, 'cdm1', 0], 'matic':[21, 'cdm2', 0], 'willian':[22, 'rm', 0],
               'oscar': [8, 'ss1', 0], 'costa': [19, 'st1', 0]}

team_b_info = {'lloris': [25, 'gk', 85],
                'assou-ekkoto': [2, 'lb', 78], 'vertonghen': [5, 'cb1', 82], 'dawson': [20, 'cb2', 79], 'walker': [28, 'rb', 79],
                'sigurdsson': [22, 'lm', 76], 'dembele':[19, 'cm1', 81], 'sandro': [30, 'cm2', 80],
                'lennon': [7, 'rm', 80], 'bale': [11, 'st1', 86], 'adebayor': [10, 'st2', 80]}

def calculate_team(team):
    width = 0
    defense = 0
    offense = 0

    if 'cdm1' in team:
        defense += 1
    else:
        defense = -1
    if 'cdm2' in team:
        defense += 1
    if 'lm' in team:
        width += 1
    else:
        width = -1
    if 'cam1' in team:
        offense += 1
    else:
        offense = -1
    if 'cam2' in team:
        offense += 1
    if 'cam3' in team:
        offense += 1

    midfield_positions = ['cdm', 'cdm2', 'lm', 'cm1', 'cm2', 'cm3', 'cam1', 'cam2', 'cam3', 'rm']

    # Initialize total overall rating
    total_overall_mid = 0
    amount = 0

    # Iterate over midfield positions and sum their overall ratings
    for position in midfield_positions:
        for player_info in team.values():
            if position in player_info[1]:
                total_overall_mid += player_info[2]
                amount = amount + 1

    total_overall_mid = total_overall_mid/amount + width + defense + offense

    width = 0
    offense = 0

    if 'st1' in team:
        offense += 1
    else:
        offense = -1
    if 'lw' in team:
        width += 1
    else:
        width = -1
    if 'rw' in team:
        width += 1

    attack_positions = ['st1', 'st2', 'lw', 'rw', 'ss1', 'ss2']

    # Initialize total overall rating
    total_overall_att = 0
    amount = 0

    # Iterate over midfield positions and sum their overall ratings
    for position in attack_positions:
        for player_info in team.values():
            if position in player_info[1]:
                total_overall_att += player_info[2]
                amount = amount + 1

    total_overall_att = total_overall_att/amount + width + offense

    width = 0
    defense = 0

    if 'lb' in team:
        width += 1
        defense += 1
    else:
        width = -1
    if 'lwb' in team:
        defense = defense - 1
        width += 1
    if 'cb1' in team:
        defense += 1
    if 'cb2' in team:
        defense += 1
    if 'cb3' in team:
        defense += 1
    if 'rb' in team:
        width += 1
        defense += 1
    if 'rwb' in team:
        defense = defense - 1
        width += 1

    defender_positions = ['lb', 'lwb', 'cb1', 'cb2', 'cb3', 'rb', 'rwb']

    # Initialize total overall rating
    total_overall_def = 0
    amount = 0

    # Iterate over midfield positions and sum their overall ratings
    for position in defender_positions:
        for player_info in team.values():
            if position in player_info[1]:
                total_overall_def += player_info[2]
                amount = amount + 1

    total_overall_def = total_overall_def/amount + width + defense
    return total_overall_def, total_overall_mid, total_overall_att


team_a_ratings = calculate_team(team_a_info)

total_def_a, total_mid_a, total_att_a = team_a_ratings

team_b_ratings = calculate_team(team_b_info)

total_def_b, total_mid_b, total_att_b = team_b_ratings
team_a = {'name': 'Chelsea',
          'attack': total_att_a,
          'midfield': total_mid_a,
          'defense': total_def_a,
          'goalkeeper': 86}
team_b = {'name': 'Tottenham',
          'attack': total_att_b,
          'midfield': total_mid_b,
          'defense': total_def_b,
          'goalkeeper': 85}


def simulate_match(team_aa, team_bb):
    # Generate random factors using Gaussian distribution
    attack_factor_a = random.gauss(team_aa['attack']/15, 1)
    defense_factor_a = random.gauss(team_aa['defense']/15, 1)
    midfield_factor_a = random.gauss(team_aa['midfield']/15, 1)
    attack_factor_b = random.gauss(team_bb['attack']/15, 1)
    midfield_factor_b = random.gauss(team_bb['midfield']/15, 1)
    defense_factor_b = random.gauss(team_bb['defense']/15, 1)

    # Calculate scores based on team attributes and random factors
    chance_a = attack_factor_a + midfield_factor_a
    chance_b = attack_factor_b + midfield_factor_b
    # Adjust for goalkeepers
    goalkeeper_factor_a = random.gauss(team_aa['goalkeeper']/12,.25)
    goalkeeper_factor_b = random.gauss(team_bb['goalkeeper']/12,.25)

    # Ensure scores are within a realistic range
    score_a = int(random.gauss(chance_a/2, 1) - defense_factor_b/4 - goalkeeper_factor_b/3)
    score_b = int(random.gauss(chance_b/2, 1) - defense_factor_a/4 - goalkeeper_factor_a/3)

    if score_b < 0:
        score_b = 0
    if score_a < 0:
        score_a = 0

    return score_a, score_b
#Simulate and print multiple match results to observe score distribution
for _ in range(5):
    result = simulate_match(team_a, team_b)
    print(f"Match Result: {team_a['name']} {result[0]} - {result[1]} {team_b['name']}")