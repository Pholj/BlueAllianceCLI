
def team_avg_points(args):
    #Gets average points for a team
    endpoint - f"/team/frc{args.team}/"


#new parser, default

team_info_parser = team_subparsers.add_parser(
    "info",
    help="Show basic team information"
)

team_info_parser.add_argument(
    "team_num,
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
    "event_key",
    type=str,
    nargs="?",
    default="2026ohmv"
)
