# ETD2_BuildOrderExtractor
Python script, that can extract a build order from a local replay json from the game ElementTD 2

# install
1. clone repository 
2. create venv (I use pyCharm and created my venv there)
3. install requirements: `pip install -r requirements.txt`
4. run script as shown below

# usage
usage:  `main.py [-h] -n REPLAY_NAME [-p PLAYER_ID] [--replay_path REPLAY_PATH]`

optional arguments:

  `-h, --help            show this help message and exit`

  `-n REPLAY_NAME, --replay_name REPLAY_NAME
                        Filename of replay to extract from (*.json)`

  `-p PLAYER_ID, --player_ID PLAYER_ID
                        playerID (default: 0) of player whose build order to extract (1st player: playerID = 0, 2nd Player: playerID = 1,...)`

  `--replay_path REPLAY_PATH
                        Path to replay.json (default path goes to default replay directory)`
