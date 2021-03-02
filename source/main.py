import pandas as pd
import os
import source.project_io as project_io
import source.data_analysis as da

cwd = os.getcwd()
path_root = os.path.join(os.getenv('APPDATA'), "..\\LocalLow\\Element Studios\\Element TD 2")
fn_replay = "ETD2_Replay_Player0_21-01-07_05-26.json"
player_ID = 0
pfn_replay = os.path.join(path_root, fn_replay)
pfn_tower_elements = os.path.join(cwd, "..\\data\\tower_elements.csv")

data = project_io.read_replay_data(pfn_replay)

if not da.is_player_id_available(data, player_ID):
    exit(-1)

df_te = project_io.read_tower_elements(pfn_tower_elements)

df = da.get_df_from_replay_data(data, df_te, player_ID)

df = da.resolve_tower_upgrades(df, df_te)

project_io.print_build_order(df=df)
