from character import *

#here are the stats for all characters : first - HP, second - damage
stats = {
    "king_arthur" : (50, 10),
    "bedevere" : (50, 10),
    "lancelot" : (50, 10),
    "galahad" : (50, 10),
    "robin" : (50, 10),

    "french" : (25, 6),
    "ni_knight_small" : (20, 10),
    "ni_knight_big" : (50, 10),
    "three_headed_knight" : (200, 10),
    "killer_rabbit" : (25, 10),
    "tim_enchanter" : (30, 10),
    "black_knight" : (60, 10),
    "black_beast" : (200, 10),
}

# x and y used to position the characters
floor_line = 460
knights_posotion = 40
enemies_posotion = 520
distance_between_characters = 20

def characters_setup(character_names : list, are_knights : bool):
    position = knights_posotion if are_knights else enemies_posotion
    characters = []

    for name in character_names:
        characters.append(Character(position, floor_line, name, stats[name][0], stats[name][1]))
        position += distance_between_characters + characters[-1].rect.width

    return characters
