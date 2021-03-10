import json
import pandas as pd
import config as cfg
import map_state as ms


class Replay:
    def __init__(self, ):
        self.pfn_replay = ""
        self.replay_data = {}
        self.df_te = pd.DataFrame(cfg.tower_elements)
        self.df = pd.DataFrame()
        self.display_string_lines = []

    def load_replay_data(self, pfn_replay):
        self.pfn_replay = pfn_replay
        with open(self.pfn_replay, "r") as replay_file:
            self.replay_data = json.load(fp=replay_file)

    def get_available_players(self):
        return self.replay_data["playerName"]

    def get_build_order(self, player_id):
        self._make_df_from_replay_data(player_id=player_id)
        self._resolve_tower_upgrades()
        self._print_build_order()
        return "".join(self.display_string_lines)

    def _make_df_from_replay_data(self, player_id):
        items = []

        # get element selections and tower actions
        for item in self.replay_data["list"]:
            if item["playerID"] is not player_id:
                continue

            if item["type"] in cfg.type_idx.keys():
                item["upgrade_lvl_from"] = 1
                item["upgrade_lvl_to"] = 1
                item["upgrade_tower_from"] = ""
                item["upgrade_tower_to"] = ""
                if item["type"] == 1:
                    item["tower_elements_list"] = self.df_te.loc[self.df_te["buildIdx"] == item["buildIdx"]]["tower_elements_list"].values[0]
                items.append(item)

        df_i = pd.DataFrame(items)

        df_i["elements"] = df_i.loc[df_i["type"] == 4]["summonIdx"].map(cfg.element_idx)
        df_i["action"] = df_i["type"].map(cfg.type_idx)
        df_i["towers"] = df_i.loc[df_i["type"] == 1]["buildIdx"].map(cfg.build_idx)

        df_i = df_i.explode("bpIdx", ignore_index=True)

        # get wave info
        wave_infos = []
        for wave_info in self.replay_data["snapShots"]:
            if wave_info["gameID"] == 0:
                wave_infos.append(wave_info)

        df_wi = pd.DataFrame(wave_infos)

        # merge items and wave info
        if not df_wi.empty:
            self.df = df_i.merge(
                right=df_wi,
                how='outer',
                on='frame',
                sort=True,
                indicator=True
            )
        else:
            self.df = df_i
            self.df["_merge"] = "left_only"
        pass

    def _resolve_tower_upgrades(self):
        map_state = ms.MapState(df_te=self.df_te)

        for index, row in self.df.iterrows():
            if row["_merge"] == "left_only":
                # build tower
                if row["action"] == cfg.build_tower_string:
                    map_state.build_tower(
                        pos=row["bpIdx"],
                        elements_list=int(row["tower_elements_list"])
                    )

                # upgrade tower
                elif row["action"] == cfg.upgrade_tower_string:
                    tower_name, tower_lvl = map_state.upgrade_tower(
                        pos=row["bpIdx"],
                        new_element=int(row["upgradeEleIdx"])
                    )
                    self.df.at[index, "upgrade_tower_from"] = tower_name.old
                    self.df.at[index, "upgrade_tower_to"] = tower_name.new
                    self.df.at[index, "towers"] = tower_name.old
                    self.df.at[index, "upgrade_lvl_from"] = tower_lvl.old
                    self.df.at[index, "upgrade_lvl_to"] = tower_lvl.new

                # sell tower
                elif row["action"] == cfg.sell_tower_string:
                    map_state.sell_tower(pos=row["bpIdx"])

                # cancel tower build
                elif row["action"] == cfg.cancel_build_string:
                    map_state.cancel_tower_build(pos=row["bpIdx"])
        pass

    def _print_header(self):
        self.display_string_lines.append(f"+--------+----------+-----------------+-------------------+------------+\n")
        self.display_string_lines.append(f"|  Wave  |  Action  |      Tower      |    Upgrade to     |  Position  |\n")
        self.display_string_lines.append(f"+--------+----------+-----------------+-------------------+------------+\n")

    def _print_line(self, row, current_wave):
        if row["action"] not in cfg.actions_to_print or row['towers'] in cfg.towers_not_to_print:
            return

        # select element
        if int(row["type"]) == 4:
            self.display_string_lines.append(f"+********+**********+*****************+*******************+************+\n")
            self.display_string_lines.append(f"|  {current_wave:3}   |   {row['action']}:     {row['elements']:37} |\n")
            self.display_string_lines.append(f"+********+**********+*****************+*******************+************+\n")
            return

        upgrade = ""
        if int(row["type"]) == 2:
            upgrade = f"{row['upgrade_tower_to']:15} {row['upgrade_lvl_to']:1.0f}"

        # print(f"+--------+----------+-----------------+-------------------+------------+")
        self.display_string_lines.append(f"|  {current_wave:3}   | {row['action']:8} | {row['towers']:15} | {upgrade:17} |     {row['bpIdx']:3}    |\n")

    def _print_tail(self):
        self.display_string_lines.append(f"+--------+----------+-----------------+-------------------+------------+\n")

    def _print_build_order(self):

        current_wave = "Pre"
        self._print_header()

        for index, row in self.df.iterrows():
            if row["_merge"] == "left_only":
                self._print_line(row=row, current_wave=current_wave)
            else:
                current_wave = f"{int(row['wave'] + 2):3}"

        self._print_tail()
