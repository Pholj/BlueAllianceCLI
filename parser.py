import argparse


#Parser structure: main.py category(team) action action-related-info
parser = argparse.ArgumentParser(
        description="FRC Blue Alliance data fetcher"
)

sub_parser = parser.add_subparsers(
        dest="category",
        required=True
)
#This sub_parser is the first positional argument after main.py ___ ___
team_parser = sub_parser.add_parser("team")

#Apart of the team-category, move this into a team file later?
team_subparsers = team_parser.add_subparsers(
    dest="action", 
    required=True)

team_info_parser = team_subparsers.add_parser(
    "info",
    help="Show basic team information"
)

team_info_parser.add_argument(
    "team",
    type=int,
    nargs="?",
    default=554,
    help="FRC team number (Defaults to 554)"
)

team_avgscore_parser = team_parser.add_parser(
    "avg",
    help="Gives you average shooting and score info"
)

team_info_parser.add_argument(
    "event",
    type=str,
    nargs="?",
    default="2026ohmv"
)
