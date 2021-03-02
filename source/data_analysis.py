import pandas as pd
import source.config as cfg
import source.map_state as ms


def is_player_id_available(replay_data, player_id):
    if replay_data["playerCount"] <= player_id:
        print(f"Selected player not available in this replay.\nExit program.")
        return False
    return True


def get_df_from_replay_data(replay_data, df_te, player_id):
    items = []

    # get element selections and tower actions
    for item in replay_data["list"]:
        if item["playerID"] is not player_id:
            continue

        if item["type"] in cfg.type_idx.keys():
            item["upgrade_lvl_from"] = 1
            item["upgrade_lvl_to"] = 1
            item["upgrade_tower_from"] = ""
            item["upgrade_tower_to"] = ""
            if item["type"] is 1:
                item["tower_elements_list"] = df_te.loc[df_te["buildIdx"] == item["buildIdx"]]["tower_elements_list"].values[0]
            items.append(item)

    df_i = pd.DataFrame(items)

    df_i["elements"] = df_i.loc[df_i["type"] == 4]["summonIdx"].map(cfg.element_idx)
    df_i["action"] = df_i["type"].map(cfg.type_idx)
    df_i["towers"] = df_i.loc[df_i["type"] == 1]["buildIdx"].map(cfg.build_idx)

    df_i = df_i.explode("bpIdx", ignore_index=True)

    # get wave info
    wave_infos = []
    for wave_info in replay_data["snapShots"]:
        if wave_info["gameID"] == 0:
            wave_infos.append(wave_info)

    df_wi = pd.DataFrame(wave_infos)

    # merge items and wave info
    if not df_wi.empty:
        df = df_i.merge(
            right=df_wi,
            how='outer',
            on='frame',
            sort=True,
            indicator=True
        )
    else:
        df = df_i
        df["_merge"] = "left_only"
    return df


def resolve_tower_upgrades(df, df_te):
    map_state = ms.MapState(df_te=df_te)

    for index, row in df.iterrows():
        if row["_merge"] is "left_only":
            # build tower
            if row["action"] is cfg.build_tower_string:
                map_state.build_tower(
                    pos=row["bpIdx"],
                    elements_list=int(row["tower_elements_list"])
                )

            # upgrade tower
            elif row["action"] is cfg.upgrade_tower_string:
                tower_name, tower_lvl = map_state.upgrade_tower(
                    pos=row["bpIdx"],
                    new_element=int(row["upgradeEleIdx"])
                )
                df.at[index, "upgrade_tower_from"] = tower_name.old
                df.at[index, "upgrade_tower_to"] = tower_name.new
                df.at[index, "towers"] = tower_name.old
                df.at[index, "upgrade_lvl_from"] = tower_lvl.old
                df.at[index, "upgrade_lvl_to"] = tower_lvl.new

            # sell tower
            elif row["action"] is cfg.sell_tower_string:
                map_state.sell_tower(pos=row["bpIdx"])

            # cancel tower build
            elif row["action"] is cfg.cancel_build_string:
                map_state.cancel_tower_build(pos=row["bpIdx"])

    return df
