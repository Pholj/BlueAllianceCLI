from api_commands import get_data_from_api
import argparse
from DLIV import get_554_history_events


def main():
    data = get_554_history_events()
    print(data)

if __name__ == "__main__":
    main()