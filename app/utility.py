STEAM32_ID = 197033655

def wins_list(matches):
    """Determine whether a user won a match in a list of matches. 

    :return: list of boolean values corresponding to a win, i.e. True -> win
    """
    return [True if (match['player_slot'] < 128) ==  match['radiant_win'] else False for match in matches]