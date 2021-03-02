import os
import argparse
import project_io as project_io
import data_analysis as da
import sys
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--replay_name",
                        help="Filename of replay to extract from (*.json)",
                        required=True)
    parser.add_argument("-p", "--player_ID",
                        help="playerID (default: 0) of player whose build order to extract (1st player: playerID = 0, 2nd Player: playerID = 1,...)",
                        type=int,
                        default=0,
                        required=False)
    parser.add_argument("--replay_path",
                        help="Path to replay.json (default path goes to default replay directory)",
                        default=os.path.join(os.getenv('APPDATA'), "..\\LocalLow\\Element Studios\\Element TD 2"),
                        required=False)
    args = parser.parse_args()

    # load replay data
    fn_replay = args.replay_name
    player_ID = args.player_ID
    path_root = args.replay_path
    pfn_replay = os.path.join(path_root, fn_replay)

    data = project_io.read_replay_data(pfn_replay)

    if not da.is_player_id_available(data, player_ID):
        exit(-1)

    # load tower data
    exec_file = Path(sys.argv[0])
    p_root = exec_file.parent.parent
    pfn_tower_elements = os.path.join(p_root, "data\\tower_elements.csv")
    df_te = project_io.read_tower_elements(pfn_tower_elements)

    # process replay
    df = da.get_df_from_replay_data(data, df_te, player_ID)

    df = da.resolve_tower_upgrades(df, df_te)

    # print result to console
    project_io.print_build_order(df=df)



