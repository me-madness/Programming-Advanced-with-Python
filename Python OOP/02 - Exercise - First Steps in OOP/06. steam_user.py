class SteamUser:
    def __init__(self, username: str, games: str, played_hours: int) -> None:
        pass
    
    
    def buy_game(self):
        pass
    
    
    def status(self):
        pass
    
    
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())    