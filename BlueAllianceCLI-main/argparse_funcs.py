from api_commands import get_data_from_api

def team_info(args):
    #getting basic info
    endpoint = f"/team/frc{args.team}"
    data = get_data_from_api(endpoint)
    print(data["nickname"] , ":", data["team_number"])
    print(data["school_name"], ":", data["city"])
    print(data["rookie_year"])

def team_avg_points(args):
    #Gets average points for a team
    endpoint - f"/team/frc{args.team}/"