import argparse

parser = argparse.ArgumentParser(
        description="FRC Blue Alliance data fetcher"
)

parser.add_argument(
        "--command",
        choices=["team_history", "match_results", "head_to_head"],
        type=str,
        help='''I'll probably include this in the README so its not so bad...
        
        command to execute:\n
                "team_history" - Get event history for a team\n
                "match_results" - Get match results for an event\n
                "head_to_head" - Compare two teams at an event'''
)

parser.add_argument(
        "--team",
        type=int,
        help="your FRC team number"
)

parser.add_argument(
        "--opp",
        type=int,
        help="enemy FRC team number"
)

parser.add_argument(
        "--event",
        type=str,
        help="FRC event code"
)

parser.add_argument(
        "--year",
        type=int,
        help="FRC season year"
)

parser.add_argument(
        "--match",
        type=str,
        help="FRC match code"
)