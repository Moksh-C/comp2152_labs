import random

def load_game():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            return lines[-1].strip() if lines else "No previous game data found."
    except FileNotFoundError:
        return "No previous game data found."

def adjust_combat_strength(combat_strength, m_combat_strength):
    print(f"Hero's combat strength: {combat_strength}")
    print(f"Monster's combat strength: {m_combat_strength}")

def collect_loot(loot_options, belt):
    item = random.choice(loot_options)
    belt.append(item)
    loot_options.remove(item)
    print(f"You got: {item}")
    return loot_options, belt

def use_loot(belt, health_points):
    for item in belt:
        if item == "Health Potion":
            health_points += 5
            print("Used Health Potion! +5 HP")
        elif item == "Poison Potion":
            health_points -= 3
            print("Used Poison Potion! -3 HP")
    return belt, health_points

def inception_dream(num_dream_lvls):
    if num_dream_lvls == 0:
        return 0
    return 2 + inception_dream(num_dream_lvls - 1)

def hero_attacks(combat_strength, m_health_points):
    damage = random.randint(1, combat_strength)
    m_health_points = max(0, m_health_points - damage)
    print(f"Hero attacks! Monster loses {damage} HP. Remaining HP: {m_health_points}")
    return m_health_points

def monster_attacks(m_combat_strength, health_points):
    damage = random.randint(1, m_combat_strength)
    health_points = max(0, health_points - damage)
    print(f"Monster attacks! Hero loses {damage} HP. Remaining HP: {health_points}")
    return health_points

def save_game(winner, hero_name, num_stars):
    with open("save.txt", "a") as file:
        file.write(f"Hero {hero_name} has {('defeated' if winner == 'Hero' else 'lost to')} the monster and gained {num_stars} stars.\n")
    print("Game saved successfully!")
