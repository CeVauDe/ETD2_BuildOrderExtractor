version_string = "0.2.0"
build_tower_string = "Build"
upgrade_tower_string = "Upgrade"
sell_tower_string = "Sell"
select_element_string = "Select element"
cancel_build_string = "Cancel"

actions_to_print = [build_tower_string,
                    upgrade_tower_string,
                    # sell_tower_string,
                    select_element_string,
                    cancel_build_string]

actions_build = [build_tower_string,
                 upgrade_tower_string,
                 sell_tower_string,
                 cancel_build_string]

towers_not_to_print = ["Arrow", "Cannon"]

element_scalator = {
    4: 100000,
    5: 10000,
    0: 1000,
    1: 100,
    2: 10,
    3: 1
}

type_idx = {1: build_tower_string,
            2: upgrade_tower_string,
            3: sell_tower_string,
            4: select_element_string,
            7: "tbd",
            10: cancel_build_string}

element_idx = {0: "Water",
               1: "Fire",
               2: "Nature",
               3: "Earth",
               4: "Light",
               5: "Darkness",
               6: "Income",
               7: "Essence"}

build_idx = {0: "Arrow",
             1: "Cannon",
             6: "Light",
             7: "Darkness",
             2: "Water",
             3: "Fire",
             4: "Nature",
             5: "Earth",
             43: "Periodic",
             20: "Atom",
             15: "Lightning",
             12: "Poison",
             19: "Disease",
             8: "Vapor",
             11: "Ice",
             13: "Solar",
             16: "Infernal",
             17: "Mushroom",
             18: "Life",
             21: "Howitzer",
             10: "Geyser",
             22: "Trickery",
             9: "Well",
             14: "Blacksmith",
             32: "Astral",
             42: "Laser",
             38: "Runic",
             41: "Ethereal",
             29: "Flooding",
             28: "Wisp",
             37: "Flamethrower",
             24: "Haste",
             23: "Impulse",
             27: "Golem",
             33: "Quake",
             36: "Money",
             34: "Nova",
             35: "Jinx",
             25: "Windstorm",
             30: "Polar",
             26: "Corrosion",
             40: "Root",
             39: "Incarnation",
             31: "Muck"
             }

tower_elements = {'buildIdx': {0: 0, 1: 1, 2: 6, 3: 7, 4: 2, 5: 3, 6: 4, 7: 5, 8: 43, 9: 20, 10: 15, 11: 12, 12: 19, 13: 8, 14: 11, 15: 13, 16: 16, 17: 17, 18: 18, 19: 21, 20: 10, 21: 22, 22: 9, 23: 14, 24: 32, 25: 42, 26: 38, 27: 41, 28: 29, 29: 28, 30: 37, 31: 24, 32: 23, 33: 27, 34: 33, 35: 36, 36: 34, 37: 35, 38: 25, 39: 30, 40: 26, 41: 40, 42: 39, 43: 31}, 'tower_name': {0: 'Arrow', 1: 'Cannon', 2: 'Light', 3: 'Darkness', 4: 'Water', 5: 'Fire', 6: 'Nature', 7: 'Earth', 8: 'Periodic', 9: 'Atom', 10: 'Lightning', 11: 'Poison', 12: 'Disease', 13: 'Vapor', 14: 'Ice', 15: 'Solar', 16: 'Infernal', 17: 'Mushroom', 18: 'Life', 19: 'Howitzer', 20: 'Geyser', 21: 'Trickery', 22: 'Well', 23: 'Blacksmith', 24: 'Astral', 25: 'Laser', 26: 'Runic', 27: 'Ethereal', 28: 'Flooding', 29: 'Wisp', 30: 'Flamethrower', 31: 'Haste', 32: 'Impulse', 33: 'Golem', 34: 'Quake', 35: 'Money', 36: 'Nova', 37: 'Jinx', 38: 'Windstorm', 39: 'Polar', 40: 'Corrosion', 41: 'Root', 42: 'Incarnation', 43: 'Muck'}, 'tower_elements_list': {0: 0, 1: 0, 2: 100000, 3: 10000, 4: 1000, 5: 100, 6: 10, 7: 1, 8: 111111, 9: 100001, 10: 100100, 11: 11000, 12: 10010, 13: 1100, 14: 101000, 15: 110, 16: 10100, 17: 11, 18: 100010, 19: 10001, 20: 1001, 21: 110000, 22: 1010, 23: 101, 24: 111000, 25: 110001, 26: 110100, 27: 110010, 28: 11010, 29: 101010, 30: 10101, 31: 1101, 32: 1110, 33: 1011, 34: 111, 35: 100101, 36: 100110, 37: 10110, 38: 101100, 39: 101001, 40: 11100, 41: 10011, 42: 100011, 43: 11001}}
