from DLIV import get_554_history_events
from parser import parser
from argparse_funcs import team_history

def main():
    args = parser.parse_args()
    if args.command == "team_history": #Gets you all their past events + dates
        print(team_history(args))
    elif args.command == "match_results":
        pass
    elif args.command == "head_to_head":
        pass
    print(args)

if __name__ == "__main__":
    main()