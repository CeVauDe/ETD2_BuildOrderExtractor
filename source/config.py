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

