import requests
STEAM32_ID = 197033655
BASE_URL = "https://api.opendota.com/api"


def match_results(steam32_id, hero_id, num_results=20):
    """Determine whether a user won a match from a list of matches. 

    Args:
        steam32_id -- id relating to user's Steam ID
        hero_id -- id relating to a specific hero

    Returns:
        list of boolean values corresponding to a win, i.e. True -> win
    """
    matches = requests.get(
        f"https: // api.opendota.com/api/players/{steam32_id} + \
             matches?hero_id={hero_id}"). json()[0:num_results]

    return [True if (match['player_slot'] < 128) == match['radiant_win'] 
                else False for match in matches]


def match_map(data):
    """Transforms a list of T/F values to integers

    For each win, a counter is increased and indexed in place of the boolean; 
    the opposite occurs for a loss.

    Args:
        data -- a list of results in the form [True, True, False, True, ...]

    Results:
        a list of values resulting in the net wins/losses for a user on a hero
    """
    x = 0
    result = []

    for value in data:
        x = (x + 1) if value is True else (x - 1)
        result.append(x)
    
    return result