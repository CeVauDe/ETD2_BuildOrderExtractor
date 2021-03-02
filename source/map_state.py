import pandas as pd
import config as cfg
from dataclasses import dataclass


@dataclass
class TowerName:
    old: str = "notSet"
    new: str = "notSet"


@dataclass
class TowerLvl:
    old: int = -1
    new: int = -1


class MapState:
    def __init__(self, df_te):
        self.tower_table = pd.DataFrame(columns=["position",
                                                 "tower_elements_list",
                                                 "tower_name",
                                                 "tower_lvl",
                                                 "prev_tower_elements_list",
                                                 "prev_tower_name",
                                                 "prev_tower_lvl"])
        self.df_te = df_te

    def build_tower(self, pos, elements_list):
        self.tower_table = self.tower_table.append({
            "position": int(pos),
            "tower_elements_list": elements_list,
            "tower_name": self.df_te.loc[self.df_te["tower_elements_list"] == elements_list]["tower_name"].values[0],
            "tower_lvl": 1,
            "prev_tower_elements_list": elements_list,
            "prev_tower_name": self.df_te.loc[self.df_te["tower_elements_list"] == elements_list]["tower_name"].values[0],
            "prev_tower_lvl": 1
        }, ignore_index=True)

    def upgrade_tower(self, pos, new_element):
        tower_lvl = TowerLvl()
        tower_name = TowerName()
        tower_lvl.old = self.tower_table.loc[self.tower_table["position"] == pos, "tower_lvl"].values[0]
        tower_name.old = self.tower_table.loc[self.tower_table["position"] == pos, "tower_name"].values[0]

        self.tower_table.loc[self.tower_table["position"] == pos, "prev_tower_elements_list"] = \
            self.tower_table.loc[self.tower_table["position"] == pos, "tower_elements_list"]
        self.tower_table.loc[self.tower_table["position"] == pos, "prev_tower_name"] = \
            self.tower_table.loc[self.tower_table["position"] == pos, "tower_name"]
        self.tower_table.loc[self.tower_table["position"] == pos, "prev_tower_lvl"] = \
            self.tower_table.loc[self.tower_table["position"] == pos, "tower_lvl"]

        if new_element < 0:
            tower_lvl.new = tower_lvl.old + 1
            self.tower_table.loc[self.tower_table["position"] == pos, "tower_lvl"] = tower_lvl.new
        else:
            tower_lvl.new = 1
            old_element_list = self.tower_table.loc[self.tower_table["position"] == pos, "tower_elements_list"].values
            new_element_list = old_element_list + cfg.element_scalator[new_element]
            self.tower_table.loc[self.tower_table["position"] == pos, "tower_elements_list"] = new_element_list

            tower_name.new = self.df_te.loc[self.df_te["tower_elements_list"] == new_element_list[0]]["tower_name"].values[0]
            self.tower_table.loc[self.tower_table["position"] == pos, "tower_name"] = tower_name.new

        return tower_name, tower_lvl

    def sell_tower(self, pos):
        idx = self.tower_table.loc[self.tower_table["position"] == pos].index
        self.tower_table.drop(index=idx)

    def cancel_tower_build(self, pos):
        self.tower_table.loc[self.tower_table["position"] == pos, "tower_elements_list"] = \
            self.tower_table.loc[self.tower_table["position"] == pos, "prev_tower_elements_list"]
        self.tower_table.loc[self.tower_table["position"] == pos, "tower_name"] = \
            self.tower_table.loc[self.tower_table["position"] == pos, "prev_tower_name"]
        self.tower_table.loc[self.tower_table["position"] == pos, "tower_lvl"] = \
            self.tower_table.loc[self.tower_table["position"] == pos, "prev_tower_lvl"]
