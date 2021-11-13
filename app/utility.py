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
        f"https://api.opendota.com/api/players/{steam32_id}/matches?hero_id={hero_id}").json()[0:num_results]

    return [True if (match['player_slot'] < 128) == match['radiant_win'] else False for match in matches]
