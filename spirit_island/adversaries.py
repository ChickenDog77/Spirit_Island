"""Adversary data for Spirit Island."""

ADVERSARIES = {
    "prussia": {
        "name": "Brandenburg-Prussia",
        "difficulty_range": "1-6",
        "flavor": "Efficient, military-focused colonizers with strong building.",
        "escalation": "After setup of a new invader card on the Explore space, on each board with 2+ towns, add 1 town to a land without town/city.",
        "levels": {
            0: {"difficulty": 1, "name": "No Adversary"},
            1: {"difficulty": 2, "rule": "Ravage cards also trigger a Build in the same lands after ravaging."},
            2: {"difficulty": 4, "rule": "The first time the invader deck is reshuffled, add an extra stage II card."},
            3: {"difficulty": 6, "rule": "Invader build actions add an extra town if there are already 2+ invaders."},
            4: {"difficulty": 7, "rule": "Invaders have +1 health."},
            5: {"difficulty": 9, "rule": "During setup, add 1 town to each land with a city."},
            6: {"difficulty": 10, "rule": "At terror level 2, the victory condition requires no cities or towns. At TL3, no cities."},
        },
    },
    "england": {
        "name": "England",
        "difficulty_range": "1-6",
        "flavor": "High immigration and coastal buildup.",
        "escalation": "After exploring, add 1 town to each coastal land that was not explored this turn.",
        "levels": {
            0: {"difficulty": 1, "name": "No Adversary"},
            1: {"difficulty": 3, "rule": "Buildings have +1 health."},
            2: {"difficulty": 4, "rule": "Explorers have +1 health (2 total)."},
            3: {"difficulty": 6, "rule": "During setup, add 1 city to each coastal land that already has a town."},
            4: {"difficulty": 7, "rule": "The first time you would earn a fear card, earn 1 fewer."},
            5: {"difficulty": 9, "rule": "During setup, add 1 town to each inland land adjacent to a coastal land with a city."},
            6: {"difficulty": 11, "rule": "Earning fear cards requires 5 fear per player instead of 4."},
        },
    },
    "sweden": {
        "name": "Sweden",
        "difficulty_range": "1-6",
        "flavor": "Heavy blight and environmental destruction.",
        "escalation": "After ravaging, add 1 blight to each land where invaders did damage but did not add blight.",
        "levels": {
            0: {"difficulty": 1, "name": "No Adversary"},
            1: {"difficulty": 2, "rule": "The blight card starts flipped (blighted island from the start)."},
            2: {"difficulty": 3, "rule": "During setup, add 1 extra blight to the blight card."},
            3: {"difficulty": 5, "rule": "Whenever blight is added to a land with your presence, you must destroy 1 of your presence there."},
            4: {"difficulty": 6, "rule": "Ravage does +1 extra damage to the land."},
            5: {"difficulty": 7, "rule": "After the blight card flips, add 2 blight to the card instead of the normal amount."},
            6: {"difficulty": 8, "rule": "At the start of each invader phase, add 1 blight to the land with the most invaders."},
        },
    },
}


def get_adversary(name_key):
    """Look up an adversary by key or name."""
    key = name_key.lower().strip()
    for k, adv in ADVERSARIES.items():
        if key in k or key in adv["name"].lower():
            return adv
    return None


def format_adversary(adv):
    """Format adversary details."""
    lines = [
        f"=== {adv['name']} ===",
        f"Difficulty Range: {adv['difficulty_range']}",
        f"Flavor: {adv['flavor']}",
        f"Escalation: {adv['escalation']}",
        "",
        "--- Levels ---",
    ]
    for lvl, info in adv["levels"].items():
        diff = info["difficulty"]
        rule = info.get("rule", "Base game rules.")
        lines.append(f"  Level {lvl} (Difficulty {diff}): {rule}")
    return "\n".join(lines)


def list_adversaries():
    """List all adversaries."""
    lines = []
    for adv in ADVERSARIES.values():
        lines.append(f"  {adv['name']} (Difficulty {adv['difficulty_range']}) - {adv['flavor']}")
    return "\n".join(lines)
