levels = [0, 100, 375, 775, 1250, 1950, 2750, 4000, 5500, 7500]
# add images = "" in future
def position(player_index):
    if player_index == 0:
        x = -100
        y = 0
    elif player_index == 1:
        x = 0
        y = -100
    elif player_index == 2:
        x = 100
        y = 0
    elif player_index == 3:
        x = 0
        y = 100
    return x, y

def attributes(index):
    # s
    if index == 0:
        strength = 10
        agility = 20
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_9\Idle\i00.png'
        name = "Orc"
    elif index == 1:
        strength = 11
        agility = 20
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_6\Idle\i00.png'
        name = "Tiny"
    elif index == 2:
        strength = 12
        agility = 20
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_12\Idle\i00.png'
        name = "Vasilisk"
    elif index == 3:
        strength = 13
        agility = 20
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_4\Idle\i00.png'
        name = "Magma Golem"
    # a
    elif index == 4:
        strength = 5
        agility = 30
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_1\Idle\i00.png'
        name = "Killmonger"
    elif index == 5:
        strength = 6
        agility = 30
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_7\Idle\i00.png'
        name = "Goblin"
    elif index == 6:
        strength = 7
        agility = 30
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_2\Idle\i00.png'
        name = "Phantom Assassin"
    elif index == 7:
        strength = 8
        agility = 30
        intelligence = 10
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_8\Idle\i00.png'
        name = "Ogre"
    # i
    elif index == 8:
        strength = 20
        agility = 20
        intelligence = 15
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_5\Idle\i00.png'
        name = "Ice Golem"
    elif index == 9:
        strength = 21
        agility = 20
        intelligence = 15
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_10\Idle\i00.png'
        name = "Enchantress"
    elif index == 10:
        strength = 22
        agility = 20
        intelligence = 15
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_3\Idle\i00.png'
        name = "Shadow King"
    elif index == 11:
        strength = 23
        agility = 20
        intelligence = 15
        hp = 0
        speed = 0
        damage = 0
        regen = 0
        evasion = 0
        attack_speed = 0
        strength_level = 10
        agility_level = 20
        intelligence_level = 10
        image = 'sprite\hero_11\Idle\i00.png'
        name = "Karl"
    return strength, agility, intelligence, hp, speed, damage, regen, evasion, attack_speed, strength_level, agility_level, intelligence_level, image, name
