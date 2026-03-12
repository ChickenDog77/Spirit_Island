"""Spirit Island spirit data and abilities."""

SPIRITS = {
    "lightning": {
        "name": "Lightning's Swift Strike",
        "complexity": "Low",
        "play_style": "Aggressive offense - destroy invaders before they can act.",
        "summary": (
            "A high-offense spirit that excels at killing invaders quickly. "
            "Most powers are fast, letting you strike before the invader phase. "
            "Low defense and poor at handling blight."
        ),
        "special_rules": [
            "Swiftness of Lightning: All of your slow powers become fast powers."
        ],
        "innate_powers": [
            {
                "name": "Thundering Destruction",
                "speed": "Fast",
                "thresholds": [
                    {"elements": "1 Fire, 1 Air", "effect": "1 Damage in target land."},
                    {"elements": "2 Fire, 2 Air", "effect": "Repeat in the same or a different land."},
                    {"elements": "3 Fire, 3 Air, 1 Water", "effect": "Repeat again in the same or a different land."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Energy",
            "B: +1 Presence (range 1), +1 Presence (range 1)",
            "C: +3 Energy",
        ],
        "unique_powers": [
            {"name": "Harbingers of the Lightning", "cost": 0, "speed": "Fast",
             "elements": ["Fire", "Air"],
             "effect": "Push up to 1 Dahan. 1 Damage if target land has Dahan."},
            {"name": "Lightning's Boon", "cost": 1, "speed": "Fast",
             "elements": ["Fire", "Air"],
             "effect": "Target spirit may use 1 slow power as fast."},
            {"name": "Shatter Homesteads", "cost": 3, "speed": "Slow",
             "elements": ["Fire", "Air"],
             "effect": "Destroy 1 Town."},
            {"name": "Raging Storm", "cost": 3, "speed": "Slow",
             "elements": ["Fire", "Water", "Air"],
             "effect": "3 Damage."},
        ],
    },
    "river": {
        "name": "River Surges in Sunlight",
        "complexity": "Low",
        "play_style": "Flexible support - push invaders away and rally Dahan.",
        "summary": (
            "A versatile spirit good at pushing invaders out of dangerous lands "
            "and moving Dahan to where they're needed. Has solid energy income "
            "and decent card plays."
        ),
        "special_rules": [
            "Massive Flooding: Slow powers may be used as fast if the target land is adjacent to the ocean."
        ],
        "innate_powers": [
            {
                "name": "Massive Flooding",
                "speed": "Slow",
                "thresholds": [
                    {"elements": "1 Sun, 1 Water", "effect": "Push 1 Explorer."},
                    {"elements": "2 Sun, 2 Water", "effect": "Instead, 2 Damage."},
                    {"elements": "3 Sun, 3 Water, 1 Earth", "effect": "Instead, 3 Damage and push up to 3 invaders."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Presence (range 1)",
            "B: +1 Presence (range 1), +1 Power Card",
            "C: +1 Presence (range 2), +3 Energy",
        ],
        "unique_powers": [
            {"name": "Boon of Vigor", "cost": 0, "speed": "Fast",
             "elements": ["Sun", "Water"],
             "effect": "Target spirit gains 1 energy."},
            {"name": "Flash Floods", "cost": 2, "speed": "Fast",
             "elements": ["Sun", "Water"],
             "effect": "2 Damage."},
            {"name": "Wash Away", "cost": 1, "speed": "Slow",
             "elements": ["Water", "Earth"],
             "effect": "Push up to 3 explorers/towns."},
            {"name": "River's Bounty", "cost": 0, "speed": "Slow",
             "elements": ["Sun", "Water", "Animal"],
             "effect": "Gather up to 2 Dahan. If there are now 2+ Dahan, add 1 Dahan and gain 1 energy."},
        ],
    },
    "earth": {
        "name": "Vital Strength of the Earth",
        "complexity": "Low",
        "play_style": "Defensive wall - protect the land with raw toughness.",
        "summary": (
            "An incredibly tough defensive spirit. Generates lots of defend power "
            "and is nearly impossible to destroy. Slow to start but becomes "
            "an immovable force."
        ),
        "special_rules": [
            "Rituals of Destruction: Your slow powers can destroy towns during the slow phase."
        ],
        "innate_powers": [
            {
                "name": "Guard the Healing Land",
                "speed": "Fast",
                "thresholds": [
                    {"elements": "1 Earth, 1 Plant", "effect": "Defend 3."},
                    {"elements": "2 Earth, 2 Plant", "effect": "Instead, Defend 6."},
                    {"elements": "3 Earth, 3 Plant, 1 Water", "effect": "Instead, Defend 9 and remove 1 blight."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Energy",
            "B: +1 Presence (range 1), +1 Power Card",
            "C: +2 Presence (range 1)",
        ],
        "unique_powers": [
            {"name": "Draw of the Fruitful Earth", "cost": 1, "speed": "Slow",
             "elements": ["Earth", "Plant", "Animal"],
             "effect": "Gather up to 2 explorers and up to 2 Dahan."},
            {"name": "A Year of Perfect Stillness", "cost": 3, "speed": "Fast",
             "elements": ["Sun", "Earth"],
             "effect": "Invaders skip all actions in target land this turn."},
            {"name": "Rituals of Destruction", "cost": 3, "speed": "Slow",
             "elements": ["Sun", "Moon", "Earth", "Plant"],
             "effect": "Destroy 1 town. Push up to 3 Dahan."},
            {"name": "Guard the Healing Land", "cost": 3, "speed": "Fast",
             "elements": ["Earth", "Plant", "Water"],
             "effect": "Defend 4. Remove 1 blight."},
        ],
    },
    "shadows": {
        "name": "Shadows Flicker Like Flame",
        "complexity": "Low",
        "play_style": "Fear generation and strategic invader removal.",
        "summary": (
            "Excels at generating fear to trigger fear cards and picking off "
            "individual invaders. Not great at large-scale defense but can "
            "whittle down invader presence over time."
        ),
        "special_rules": [
            "Shadows do not cause Defend to prevent damage to Dahan."
        ],
        "innate_powers": [
            {
                "name": "Darkness Swallows the Unwary",
                "speed": "Slow",
                "thresholds": [
                    {"elements": "1 Moon, 1 Fire", "effect": "1 Fear."},
                    {"elements": "2 Moon, 2 Fire, 1 Air", "effect": "1 Fear and 1 Damage."},
                    {"elements": "3 Moon, 3 Fire, 2 Air", "effect": "1 Fear and destroy 1 explorer."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Presence (range 1)",
            "B: +1 Presence (range 1), +1 Power Card",
            "C: +1 Presence (range 0), +3 Energy",
        ],
        "unique_powers": [
            {"name": "Concealing Shadows", "cost": 0, "speed": "Fast",
             "elements": ["Moon", "Air"],
             "effect": "1 Fear. Dahan take no damage from invaders this turn."},
            {"name": "Favors Called Due", "cost": 1, "speed": "Fast",
             "elements": ["Moon", "Air", "Animal"],
             "effect": "Gather up to 4 Dahan. 1 Fear if you gather any Dahan."},
            {"name": "Mantle of Dread", "cost": 1, "speed": "Slow",
             "elements": ["Moon", "Fire"],
             "effect": "2 Fear."},
            {"name": "Crops Wither and Fade", "cost": 1, "speed": "Slow",
             "elements": ["Moon", "Fire", "Earth"],
             "effect": "1 Damage. If target land has no blight, 1 Fear."},
        ],
    },
    "thunderspeaker": {
        "name": "Thunderspeaker",
        "complexity": "Moderate",
        "play_style": "Dahan commander - use Dahan as your primary weapon.",
        "summary": (
            "A spirit that turns the Dahan into a powerful fighting force. "
            "Dahan under Thunderspeaker's guidance hit harder and move where needed. "
            "Requires careful Dahan positioning."
        ),
        "special_rules": [
            "Thunderspeaker's presence counts as Dahan for targeting purposes.",
            "When Dahan in one of Thunderspeaker's lands would be destroyed, you may destroy your presence instead.",
        ],
        "innate_powers": [
            {
                "name": "Lead the Furious Assault",
                "speed": "Slow",
                "thresholds": [
                    {"elements": "1 Sun, 1 Air", "effect": "Each Dahan in target land deals damage equal to their health."},
                    {"elements": "2 Sun, 2 Fire, 2 Air", "effect": "You may push any number of Dahan. Then, each Dahan deals 3 damage."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Presence (range 1)",
            "B: +1 Presence (range 1), +1 Power Card",
            "C: +1 Presence (range 2), +2 Energy",
        ],
        "unique_powers": [
            {"name": "Voice of Thunder", "cost": 0, "speed": "Slow",
             "elements": ["Sun", "Air"],
             "effect": "Push up to 4 Dahan. 2 Fear if target land has town/city."},
            {"name": "Sudden Ambush", "cost": 2, "speed": "Fast",
             "elements": ["Sun", "Fire", "Air"],
             "effect": "Each Dahan deals 1 damage."},
            {"name": "Words of Warning", "cost": 1, "speed": "Fast",
             "elements": ["Sun", "Air"],
             "effect": "Defend 2. Gather up to 3 Dahan."},
            {"name": "Manifestation of Power and Glory", "cost": 3, "speed": "Slow",
             "elements": ["Sun", "Fire", "Air"],
             "effect": "2 Fear. Push up to 2 explorers/towns. Add 1 Dahan."},
        ],
    },
    "ocean": {
        "name": "Ocean's Hungry Grasp",
        "complexity": "Moderate",
        "play_style": "Coastal control - drown invaders in the sea.",
        "summary": (
            "A unique spirit that can only place presence in the ocean but reaches "
            "into coastal lands to drown invaders. Gains energy from drowning things. "
            "Limited reach but devastating in coastal areas."
        ),
        "special_rules": [
            "Presence may only be placed in the ocean.",
            "Whenever invaders or Dahan are pushed into the ocean, they are destroyed.",
            "When invaders are destroyed by being pushed into the ocean, gain 1 energy per invader.",
        ],
        "innate_powers": [
            {
                "name": "Pound Ships to Splinters",
                "speed": "Slow",
                "thresholds": [
                    {"elements": "1 Water, 1 Earth", "effect": "Defend 4 in target coastal land."},
                    {"elements": "2 Water, 2 Earth, 1 Moon", "effect": "Also, 2 Damage in target coastal land."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Presence (ocean)",
            "B: +1 Presence (ocean), +1 Power Card",
            "C: +2 Presence (ocean)",
        ],
        "unique_powers": [
            {"name": "Call of the Deeps", "cost": 0, "speed": "Slow",
             "elements": ["Water", "Earth"],
             "effect": "Gather 1 explorer to the ocean (drowning it). 1 Fear."},
            {"name": "Swallow the Land-Dwellers", "cost": 3, "speed": "Slow",
             "elements": ["Water", "Earth"],
             "effect": "Push up to 3 explorers/towns into the ocean (drowning them)."},
            {"name": "Grasping Tide", "cost": 1, "speed": "Fast",
             "elements": ["Water", "Moon"],
             "effect": "Defend 4."},
            {"name": "Tidal Boon", "cost": 0, "speed": "Fast",
             "elements": ["Water", "Moon", "Earth"],
             "effect": "Target spirit gains 2 energy. If you target yourself, gain 1 energy instead."},
        ],
    },
    "bringer": {
        "name": "Bringer of Dreams and Nightmares",
        "complexity": "High",
        "play_style": "Pure fear engine - win through terror without direct damage.",
        "summary": (
            "A spirit that cannot deal damage directly but generates enormous amounts "
            "of fear. Wins by reaching terror level victory conditions. Unique and "
            "challenging playstyle requiring creative problem-solving."
        ),
        "special_rules": [
            "To the Dreaming: Your powers never deal damage to invaders. "
            "Whenever you use a power that would deal damage, instead generate that much fear.",
        ],
        "innate_powers": [
            {
                "name": "Night Terrors",
                "speed": "Fast",
                "thresholds": [
                    {"elements": "2 Moon", "effect": "2 Fear."},
                    {"elements": "3 Moon, 1 Air", "effect": "Instead, 3 Fear. Push 1 explorer."},
                    {"elements": "4 Moon, 2 Air", "effect": "Instead, 4 Fear. Push 1 town."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Presence (range 0)",
            "B: +1 Presence (range 1), +1 Power Card",
            "C: +1 Presence (range 0), +2 Energy",
        ],
        "unique_powers": [
            {"name": "Call on Midnight's Dream", "cost": 0, "speed": "Fast",
             "elements": ["Moon"],
             "effect": "1 Fear. You may push 1 explorer."},
            {"name": "Dreams of the Dahan", "cost": 0, "speed": "Fast",
             "elements": ["Moon", "Animal"],
             "effect": "Gather up to 2 Dahan. Dahan have +1 health this turn."},
            {"name": "Predatory Nightmares", "cost": 2, "speed": "Slow",
             "elements": ["Moon", "Fire", "Animal"],
             "effect": "2 Fear. 2 Damage (converts to fear via special rule)."},
            {"name": "Dread Apparitions", "cost": 2, "speed": "Fast",
             "elements": ["Moon", "Air"],
             "effect": "3 Fear. Defend 2."},
        ],
    },
    "spread": {
        "name": "A Spread of Rampant Green",
        "complexity": "Moderate",
        "play_style": "Growth and presence flooding - overwhelm the board.",
        "summary": (
            "A spirit focused on rapid presence placement and choking out invaders "
            "by covering the board. Excellent at preventing builds and explores "
            "by keeping sacred sites everywhere."
        ),
        "special_rules": [
            "Steady Regeneration: During time passes, if you have 3+ presence in a land, remove 1 blight from it."
        ],
        "innate_powers": [
            {
                "name": "Creepers Tear into Mortar",
                "speed": "Slow",
                "thresholds": [
                    {"elements": "2 Plant", "effect": "1 Damage to 1 town/city."},
                    {"elements": "3 Plant, 1 Water", "effect": "Instead, 2 Damage to 1 town/city."},
                    {"elements": "4 Plant, 2 Water, 1 Earth", "effect": "Instead, destroy 1 town/city."},
                ],
            }
        ],
        "growth_options": [
            "A: Reclaim all cards, +1 Presence (range 1)",
            "B: +2 Presence (range 1)",
            "C: +1 Presence (range 2), +1 Power Card",
        ],
        "unique_powers": [
            {"name": "Gift of Proliferation", "cost": 1, "speed": "Fast",
             "elements": ["Sun", "Plant"],
             "effect": "Target spirit adds 1 presence to a land with their presence."},
            {"name": "Stem the Flow of Fresh Water", "cost": 0, "speed": "Slow",
             "elements": ["Plant", "Water"],
             "effect": "1 Damage. Remove 1 blight."},
            {"name": "Overgrow in a Night", "cost": 1, "speed": "Fast",
             "elements": ["Moon", "Plant"],
             "effect": "Add 1 presence in target land. Push all explorers from target land."},
            {"name": "Fields Choked with Growth", "cost": 2, "speed": "Slow",
             "elements": ["Earth", "Plant"],
             "effect": "Defend 3. Remove 1 blight if there are 2+ presence in target land."},
        ],
    },
}


def get_spirit(name_key):
    """Look up a spirit by key or partial name match."""
    key = name_key.lower().strip()
    # Direct key match
    if key in SPIRITS:
        return SPIRITS[key]
    # Partial name match
    for k, spirit in SPIRITS.items():
        if key in spirit["name"].lower() or key in k:
            return spirit
    return None


def list_spirits():
    """Return a formatted list of all spirits."""
    lines = []
    for spirit in SPIRITS.values():
        lines.append(f"  [{spirit['complexity']}] {spirit['name']} - {spirit['play_style']}")
    return "\n".join(lines)


def format_spirit_detail(spirit):
    """Format a full spirit detail view."""
    lines = [
        f"=== {spirit['name']} ===",
        f"Complexity: {spirit['complexity']}",
        f"Play Style: {spirit['play_style']}",
        "",
        spirit["summary"],
        "",
        "--- Special Rules ---",
    ]
    for rule in spirit["special_rules"]:
        lines.append(f"  * {rule}")

    lines.append("")
    lines.append("--- Growth Options ---")
    for opt in spirit["growth_options"]:
        lines.append(f"  {opt}")

    lines.append("")
    lines.append("--- Innate Powers ---")
    for innate in spirit["innate_powers"]:
        lines.append(f"  {innate['name']} (Speed: {innate['speed']})")
        for thresh in innate["thresholds"]:
            lines.append(f"    [{thresh['elements']}] -> {thresh['effect']}")

    lines.append("")
    lines.append("--- Unique Power Cards ---")
    for card in spirit["unique_powers"]:
        elems = ", ".join(card["elements"])
        lines.append(f"  {card['name']} (Cost: {card['cost']}, Speed: {card['speed']})")
        lines.append(f"    Elements: {elems}")
        lines.append(f"    Effect: {card['effect']}")

    return "\n".join(lines)
