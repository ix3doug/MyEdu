# Define the character's attributes
character_name = "Hero"
character_class = "Knight"
character_home_region = "Forgotten Isles"
character_special_ability = "Shield of Resilience"

# Initialize the character's statistics
level = 25
experience_points = 456
health_points = 100
quests = 4

# Initialize float character statistics
attack_power = 1.3
defense_rating = 2.4
crit_chance = 0.5

# Create a dictionary to hold all character attributes
character_info = {
    "Overview": {
        "Name": character_name,
        "Level": level,
    },
    "Identity": {
        "Class": character_class,
        "Home Region": character_home_region,
        "Special Ability": character_special_ability,
    },
    "Progress": {
        "Experience Points": experience_points,
        "Health Points": health_points,
        "Quests": quests,
    },
    "Stats": {
        "Attack Scale": attack_power,
        "Defense Rating": defense_rating,
        "Critical Chance": crit_chance,
    },
}

# Print each attribute on its own line
for section_name, attributes in character_info.items():
    for attribute, value in attributes.items():
        print(f"{attribute}: {value}")
    print("-" * 30)


# DEBUG: Remove Before Prod
print("character_info is",type(character_info))
print("character_name is",type(character_name))
print("attack_power is",type(attack_power))