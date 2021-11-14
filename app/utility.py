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

    result = [True if (match['player_slot'] < 128) == match['radiant_win']
              else False for match in matches]

    return match_map(result)


def match_map(data):
    """Transforms a list of boolean values to integers.

    For each win/loss, a counter is increased/decreased and indexed in 
    place of the boolean.

    Args:
        data -- a list of results in the form [True, True, False, True, ...]

    Returns:
        a list of values resulting in the net wins/losses for a user on a hero
    """
    x = 0
    result = []

    for value in data:
        x = (x + 1) if value is True else (x - 1)
        result.append(x)

    return result
