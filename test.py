import requests

STEAM32_ID = 197033655

# def is_radiant(matches):
#     results = []
#     match_count = 1

#     for match in matches:
#         dict = {'match': match_count}
#         match_data = requests.get(
#             f"https://api.opendota.com/api/matches/{match['match_id']}").json()

#         for player in match_data['players']:
#             if player['account_id'] == STEAM32_ID:
#                 dict['is_radiant'] = player['player_slot'] < 128
#                 dict['won'] = (dict['is_radiant'] and match['radiant_win']) or (
#                     dict['is_radiant'] != True and match['radiant_win'] != True)

#         results.append(dict)
#         match_count += 1

#     return results


# def is_radiant(matches):
#     results = []
#     match_count = 1

#     for match in matches:
#         dict = {'match': match_count}
#         match_data = requests.get(
#             f"https://api.opendota.com/api/matches/{match['match_id']}").json()

#         user = [player for player in match_data['players'] if player['account_id'] == STEAM32_ID]

#         dict['is_radiant'] = user[0]['player_slot'] < 128

#         dict['won'] = dict['is_radiant'] and match['radiant_win']

#         results.append(dict)
#         match_count += 1

#     return results

def wins(matches):
    return [True if (match['player_slot'] < 128) ==  match['radiant_win'] else False for match in matches]


matches = requests.get(
    f"https://api.opendota.com/api/players/{STEAM32_ID}/matches?hero_id=80").json()[0:5]

# print(is_radiant(matches))
print(wins(matches))
