import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    # Open and parse the players data
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, data in players_data.items():
        # 1. Handle the Race (get existing or create a new one)
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # 2. Handle the Skills associated with this race
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race  # Link it to the race instance we just got/created
                }
            )

        # 3. Handle the Guild (Guild can be null/absent for some players)
        guild = None
        guild_data = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        # 4. Handle the Player
        # Using get_or_create here as well to prevent duplicate players if the script runs twice
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
