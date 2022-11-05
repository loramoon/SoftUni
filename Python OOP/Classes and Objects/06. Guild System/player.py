class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}"
        result += f"\nGuild: {self.guild}"
        result += f"\nHP: {self.hp}"
        result += f"\nMP: {self.mp}"
        for k, v in self.skills.items():
            result += f"\n==={k} - {v}"
        return result
