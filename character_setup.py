from knight import *
from enemy import *


abilities = {
    "normal_attack" : (Ability("normal_attack", 0, 15, 15, img_def_attack, 380, 80)),
    "multi_attack" : (Ability("multi_attack", 2, 15, 105, img_multi_attack, 380, 80)),
    "stun" : (Ability("stun", 4, 515, 15, img_stun_attack, 380, 80)),
    "heal" : (Ability("heal", 3, 15, 105, img_heal, 380, 80)),
    "multi_heal" : (Ability("multi_heal", 5, 515, 15, img_multi_heal, 380, 80)),
    "taunt" : (Ability("taunt", 3, 15, 105, img_taunt, 380, 80)),
    "dodge" : (Ability("dodge", 4, 515, 15, img_dodge, 380, 80)),
}

#here are the stats for all characters : first - HP, second - damage, third - abilities
stats_knights = {
    "king_arthur" : (50, 10,
                     {abilities["normal_attack"], abilities["multi_attack"], abilities["dodge"]}),
    "bedevere" : (50, 10,
                  {abilities["normal_attack"], abilities["taunt"], abilities["stun"]}),
    "lancelot" : (50, 10,
                  {abilities["normal_attack"], abilities["multi_attack"], abilities["stun"]}),
    "galahad" : (50, 10,
                 {abilities["normal_attack"], abilities["heal"], abilities["multi_heal"]}),
    "robin" : (50, 10,
               {abilities["normal_attack"], abilities["heal"], abilities["dodge"]}),
}

stats_enemies = {
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

def knights_setup(character_names : list):
    position = knights_posotion
    characters: list[Character] = []

    for name in character_names:
        characters.append(Knight(position, floor_line, name, stats_knights[name][0], stats_knights[name][1], stats_knights[name][2]))
        position += distance_between_characters + characters[-1].rect.width

    return characters

def enemies_setup(character_names : list):
    position = enemies_posotion
    characters: list[Character] = []

    for name in character_names:     
        characters.append(Character(position, floor_line, name, stats_enemies[name][0], stats_enemies[name][1]))
        position += distance_between_characters + characters[-1].rect.width

    return characters