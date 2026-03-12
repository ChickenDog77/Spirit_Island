"""Minor and Major power card reference for Spirit Island."""

MINOR_POWERS = [
    {"name": "Call to Bloodshed", "cost": 0, "speed": "Slow", "elements": ["Sun", "Fire"],
     "effect": "Each Dahan in target land deals 1 damage to invaders."},
    {"name": "Call to Isolation", "cost": 0, "speed": "Fast", "elements": ["Sun", "Earth", "Animal"],
     "effect": "Push 1 Dahan and up to 2 explorers from target land."},
    {"name": "Call to Migrate", "cost": 0, "speed": "Slow", "elements": ["Fire", "Air", "Animal"],
     "effect": "Push up to 3 Dahan from target land."},
    {"name": "Call to Tend", "cost": 1, "speed": "Slow", "elements": ["Water", "Plant", "Animal"],
     "effect": "Remove 1 blight. Add 1 Dahan."},
    {"name": "Dark and Tangled Woods", "cost": 1, "speed": "Fast", "elements": ["Moon", "Earth", "Plant"],
     "effect": "2 Fear. Defend 3."},
    {"name": "Delusions of Danger", "cost": 1, "speed": "Fast", "elements": ["Sun", "Moon", "Air"],
     "effect": "2 Fear. Push up to 2 explorers from target land."},
    {"name": "Devouring Ants", "cost": 1, "speed": "Slow", "elements": ["Sun", "Earth", "Animal"],
     "effect": "1 Fear. 1 Damage."},
    {"name": "Dire Metamorphosis", "cost": 0, "speed": "Fast", "elements": ["Moon", "Animal"],
     "effect": "Replace 1 explorer with 1 Dahan."},
    {"name": "Drought", "cost": 1, "speed": "Slow", "elements": ["Sun", "Fire", "Earth"],
     "effect": "1 Damage to each town/city."},
    {"name": "Elemental Boon", "cost": 1, "speed": "Fast", "elements": ["Sun", "Moon", "Fire", "Water", "Earth", "Plant", "Air", "Animal"],
     "effect": "Target spirit gains 3 of any elements they choose (for their innate powers)."},
    {"name": "Encompassing Ward", "cost": 1, "speed": "Fast", "elements": ["Sun", "Water", "Earth"],
     "effect": "Defend 2 in every land where target spirit has presence."},
    {"name": "Enticing Splendor", "cost": 1, "speed": "Fast", "elements": ["Sun", "Air", "Plant"],
     "effect": "Gather up to 4 explorers. 1 Fear per 2 explorers gathered."},
    {"name": "Gnawing Rootbiters", "cost": 1, "speed": "Slow", "elements": ["Earth", "Animal"],
     "effect": "1 Damage. If target land has blight, +1 damage."},
    {"name": "Lure of the Unknown", "cost": 1, "speed": "Fast", "elements": ["Moon", "Fire", "Air", "Plant"],
     "effect": "Gather 1 explorer. 1 Fear."},
    {"name": "Raging Storm", "cost": 1, "speed": "Slow", "elements": ["Fire", "Air", "Water"],
     "effect": "1 Damage to each invader."},
    {"name": "Reaching Grasp", "cost": 0, "speed": "Slow", "elements": ["Sun", "Air"],
     "effect": "Add 1 presence to target land within range+1."},
    {"name": "Savage Mawbeasts", "cost": 2, "speed": "Slow", "elements": ["Moon", "Fire", "Animal"],
     "effect": "2 Damage. Push up to 2 explorers."},
    {"name": "Sap the Strength of Multitudes", "cost": 0, "speed": "Fast", "elements": ["Sun", "Water", "Animal"],
     "effect": "Defend 5. This turn only, invaders in target land have -1 health (min 1)."},
    {"name": "Song of Sanctity", "cost": 0, "speed": "Slow", "elements": ["Sun", "Plant", "Animal"],
     "effect": "Remove 1 blight."},
    {"name": "Uncanny Melting", "cost": 1, "speed": "Slow", "elements": ["Sun", "Moon", "Water"],
     "effect": "1 Fear. 1 Damage. If there are no Dahan, +1 damage."},
    {"name": "Veil the Night's Hunt", "cost": 1, "speed": "Fast", "elements": ["Moon", "Air", "Animal"],
     "effect": "1 Fear. Defend 3."},
    {"name": "Voice of Thunder", "cost": 1, "speed": "Slow", "elements": ["Sun", "Air"],
     "effect": "2 Fear. Push up to 2 Dahan."},
]

MAJOR_POWERS = [
    {"name": "Cleansing Floods", "cost": 5, "speed": "Slow", "elements": ["Sun", "Water"],
     "effect": "4 Damage. Remove 1 blight.", "threshold": "3 Water: +10 Damage."},
    {"name": "Dissolve the Bonds of Kinship", "cost": 4, "speed": "Slow", "elements": ["Fire", "Water", "Animal"],
     "effect": "1 Fear. Replace 1 city with 2 towns. Replace 1 town with 2 explorers.",
     "threshold": "2 Fire, 3 Animal: Repeat."},
    {"name": "Indomitable Claim", "cost": 4, "speed": "Fast", "elements": ["Sun", "Earth"],
     "effect": "Add 1 presence in target land. Defend 20.",
     "threshold": "3 Sun, 2 Earth: Invaders skip all actions in target land."},
    {"name": "Infinite Vitality", "cost": 4, "speed": "Fast", "elements": ["Earth", "Plant", "Animal"],
     "effect": "Dahan have +5 health. Defend 3.",
     "threshold": "2 Earth, 2 Plant, 2 Animal: Dahan in target land are not destroyed by damage."},
    {"name": "Insatiable Hunger of the Swarm", "cost": 3, "speed": "Slow", "elements": ["Fire", "Animal"],
     "effect": "Destroy all explorers and towns. Add 1 blight.",
     "threshold": "3 Fire, 2 Animal: Also destroy all cities."},
    {"name": "Pent-Up Calamity", "cost": 4, "speed": "Slow", "elements": ["Fire", "Earth"],
     "effect": "For each blight in target land: 2 fear, 3 damage.",
     "threshold": "3 Fire, 2 Earth: +2 damage per blight."},
    {"name": "Pillar of Living Flame", "cost": 4, "speed": "Fast", "elements": ["Sun", "Fire"],
     "effect": "3 Fear. 5 Damage.",
     "threshold": "3 Sun, 3 Fire: +4 Damage. +3 Fear."},
    {"name": "Powerstorm", "cost": 3, "speed": "Fast", "elements": ["Sun", "Fire", "Air"],
     "effect": "Target spirit gains 3 energy and may repeat 1 power card by paying its cost.",
     "threshold": "2 Sun, 2 Fire, 3 Air: Target spirit may instead repeat up to 2 power cards."},
    {"name": "Talons of Lightning", "cost": 4, "speed": "Fast", "elements": ["Fire", "Air"],
     "effect": "4 Damage.",
     "threshold": "3 Fire, 3 Air: +3 Damage. Destroy 1 town for each Dahan."},
    {"name": "Terrifying Chase", "cost": 4, "speed": "Slow", "elements": ["Air", "Plant", "Animal"],
     "effect": "3 Fear. Push up to 4 explorers/towns.",
     "threshold": "3 Air, 2 Animal: +4 Fear. Push all invaders."},
    {"name": "The Trees and Stones Speak of War", "cost": 4, "speed": "Fast", "elements": ["Sun", "Earth", "Plant"],
     "effect": "Defend 4. 2 Damage per Dahan.",
     "threshold": "2 Sun, 2 Earth, 3 Plant: +3 Damage per Dahan. You may push any Dahan."},
    {"name": "Tsunami", "cost": 6, "speed": "Slow", "elements": ["Water", "Earth"],
     "effect": "2 Fear. In each coastal land: 6 Damage.",
     "threshold": "3 Water, 2 Earth: In each coastal land, destroy all towns and cities."},
    {"name": "Vengeance of the Dead", "cost": 3, "speed": "Fast", "elements": ["Moon", "Fire"],
     "effect": "For each Dahan destroyed in target land this turn: 1 Fear, 1 Damage.",
     "threshold": "3 Moon, 2 Fire: Also for each blight added this turn."},
    {"name": "Wrap in Wings of Sunlight", "cost": 3, "speed": "Fast", "elements": ["Sun", "Air", "Animal"],
     "effect": "Move up to 5 Dahan between your lands. Defend 2 per Dahan in target land.",
     "threshold": "2 Sun, 2 Air, 2 Animal: Defend 4 per Dahan instead."},
]

ELEMENTS = {
    "Sun": "Common in defensive and support powers",
    "Moon": "Common in fear-generating and stealth powers",
    "Fire": "Common in offensive and destructive powers",
    "Air": "Common in movement and push powers",
    "Water": "Common in healing and flooding powers",
    "Earth": "Common in defense and growth powers",
    "Plant": "Common in growth and nature powers",
    "Animal": "Common in Dahan-related and beast powers",
}


def search_power_cards(query):
    """Search for power cards by name or keyword."""
    query = query.lower().strip()
    results = []
    for card in MINOR_POWERS + MAJOR_POWERS:
        if (query in card["name"].lower()
                or query in card["effect"].lower()
                or any(query in e.lower() for e in card["elements"])):
            results.append(card)
    return results


def format_power_card(card):
    """Format a power card for display."""
    is_major = card in MAJOR_POWERS
    card_type = "MAJOR" if is_major else "Minor"
    elems = ", ".join(card["elements"])
    lines = [
        f"[{card_type}] {card['name']}",
        f"  Cost: {card['cost']} | Speed: {card['speed']}",
        f"  Elements: {elems}",
        f"  Effect: {card['effect']}",
    ]
    if "threshold" in card:
        lines.append(f"  Threshold: {card['threshold']}")
    return "\n".join(lines)
