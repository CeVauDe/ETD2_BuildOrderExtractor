import json
import pandas as pd
import config as cfg


def read_replay_data(pfn_replay):

    with open(pfn_replay, "r") as replay_file:
        replay_data = json.load(fp=replay_file)

    return replay_data


def read_tower_elements(pfn_tower_elements):
    df = pd.read_csv(pfn_tower_elements, sep=';')
    return df


def print_header():
    print(f"+--------+----------+-----------------+-------------------+------------+")
    print(f"|  Wave  |  Action  |      Tower      |    Upgrade to     |  Position  |")
    print(f"+--------+----------+-----------------+-------------------+------------+")


def print_line(row, current_wave):
    if row["action"] not in cfg.actions_to_print or row['towers'] in cfg.towers_not_to_print:
        return

    # select element
    if int(row["type"]) == 4:
        print(f"+********+**********+*****************+*******************+************+")
        print(f"|  {current_wave:3}   |   {row['action']}:     {row['elements']:37} |")
        print(f"+********+**********+*****************+*******************+************+")
        return

    upgrade = ""
    if int(row["type"]) == 2:
        upgrade = f"{row['upgrade_tower_to']:15} {row['upgrade_lvl_to']:1.0f}"

    # print(f"+--------+----------+-----------------+-------------------+------------+")
    print(f"|  {current_wave:3}   | {row['action']:8} | {row['towers']:15} | {upgrade:17} |     {row['bpIdx']:3}    |")


def print_tail():
    print(f"+--------+----------+-----------------+-------------------+------------+")


def print_build_order(df):

    current_wave = "Pre"
    print_header()

    for index, row in df.iterrows():
        if row["_merge"] == "left_only":
            print_line(row=row, current_wave=current_wave)
        else:
            current_wave = f"{int(row['wave'] + 2):3}"

    print_tail()
