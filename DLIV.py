from api_commands import get_data_from_api

def get_554_history_events():
    endpoint = "team/frc554/events"
    data = get_data_from_api(endpoint)
    event_list = []
    for events in data:
        event_list.append(events["name"])
    return event_list


