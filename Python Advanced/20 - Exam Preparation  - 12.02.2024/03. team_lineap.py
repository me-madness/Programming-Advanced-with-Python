# First task is from the lecture


def team_lineup(*args):
    country_player = {}
    for player_name, country in args:
        if country not in country_player:
            country_player[country] = []
        country_player[country].append(player_name)
        
    result = ""
    
    sorted_players = sorted(country_player.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for country, players in sorted_players:
        result += f"{country}:\n"
        for player_name in players:
            result += f"  -{player_name}\n"
    return result                



print(team_lineup(
    *args: ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))


# Second task is from me



