from pathlib import Path

# This will have to be changed if this file is moved
anipy_cli_folder = Path(Path(__file__).parent)

# These are the paths used by anipy-cli to store data
# They are all pathlib.Path objects

# In order to specify a relative path, use the / operator
# Ex. ~/Downloads/anipy would be Path.home() / 'Downloads' / 'anipy'
# You could also just use a regular path string and turn it into a Path object
# Ex. ~/Downloads/anipy would be Path('~/Downloads/anipy')

download_folder_path = anipy_cli_folder / "download"
seasonals_dl_path = download_folder_path / "seasonals"
user_files_path = anipy_cli_folder / "user_files"
history_file_path = user_files_path / "history.json"
seasonal_file_path = user_files_path /"seasonals.txt"

gogoanime_url = "https://gogoanime.film/"


mpv_path = "mpv"

# Specify additional mpv options 
# you will need to leave a comma (,) between
# each command and every command should 
# be wrappedd in quotes (").
# Example: ["--fs", "--cache"]
# Look here for various commands: https://github.com/mpv-player/mpv/blob/master/DOCS/man/options.rst
mpv_commandline_options = []


