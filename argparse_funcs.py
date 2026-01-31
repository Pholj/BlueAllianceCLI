from api_commands import get_data_from_api

def team_history(args):
    endpoint = f"team/frc{args.team}/events"
    data = get_data_from_api(endpoint)
    event_list = []
    for events in data:
        event_list.append([events["name"],
                           events["start_date"]])
    return event_list


def match_results(args):
    endpoint = f"event/{args.event}/matches"