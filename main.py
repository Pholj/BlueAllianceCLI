from DLIV import get_554_history_events
from parser import parser

def main():
    args = parser.parse_args()
    data = get_554_history_events()

if __name__ == "__main__":
    main()