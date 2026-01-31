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
    help="FRC team number"
)