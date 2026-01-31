from DLIV import get_554_history_events
from parser import parser
from argparse_funcs import team_info

def main():
    args = parser.parse_args()
    if args.category == "team":
        if args.action == "info":
            team_info(args)
    print(args)

if __name__ == "__main__":
    main()