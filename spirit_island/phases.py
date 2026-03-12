"""Spirit Island game phases and turn structure."""

PHASE_ORDER = [
    "spirit",
    "fast_power",
    "invader",
    "slow_power",
    "time_passes",
]

PHASES = {
    "spirit": {
        "name": "Spirit Phase",
        "order": 1,
        "steps": [
            "1. Growth: Choose one growth option from your spirit panel.",
            "2. Gain Energy: Gain energy equal to your current energy track value.",
            "3. Pick Power Cards: You may pay energy to gain new power cards.",
        ],
        "tips": [
            "Growth is mandatory - you must pick exactly one growth option.",
            "Energy from growth options is gained in addition to your income.",
            "You can choose not to gain a new power card to save energy.",
            "Place presence from your tracks left-to-right to reveal higher values.",
        ],
        "next": "fast_power",
    },
    "fast_power": {
        "name": "Fast Powers Phase",
        "order": 2,
        "steps": [
            "1. Resolve any fast powers you played this turn (in any order).",
            "2. Also resolve any fast innate powers you qualify for.",
        ],
        "tips": [
            "Fast powers resolve BEFORE the invader phase.",
            "You can choose the order of your own fast powers.",
            "With multiple spirits, players decide together on resolution order.",
            "Check your innate power thresholds - you may qualify for free effects.",
        ],
        "next": "invader",
    },
    "invader": {
        "name": "Invader Phase",
        "order": 3,
        "steps": [
            "1. Blighted Island (if applicable): Check the blight card effect.",
            "2. Fear Cards: Resolve any earned fear cards (top to bottom).",
            "3. Ravage: Invaders deal damage in lands matching the Ravage card.",
            "4. Build: Invaders build in lands matching the Build card.",
            "5. Explore: Draw a new invader card and add explorers.",
            "6. Advance Invader Cards: Shift cards along the track.",
        ],
        "tips": [
            "Ravage, Build, Explore happen in that specific order - never skip steps.",
            "During Ravage: each town deals 2 damage, each city deals 3 damage to the land.",
            "If total invader damage >= 2, the land takes 1 blight (Dahan defend first).",
            "Dahan fight back AFTER taking damage - each surviving Dahan deals 2 damage to invaders.",
            "During Build: if a land has more towns than cities, add a city; otherwise add a town.",
            "During Explore: add 1 explorer to each land matching the card that is adjacent to a town/city OR the ocean.",
        ],
        "next": "slow_power",
    },
    "slow_power": {
        "name": "Slow Powers Phase",
        "order": 4,
        "steps": [
            "1. Resolve any slow powers you played this turn (in any order).",
            "2. Also resolve any slow innate powers you qualify for.",
        ],
        "tips": [
            "Slow powers resolve AFTER the invader phase.",
            "The land may look very different now than when you planned your cards!",
            "Slow powers are great for cleanup and repositioning for next turn.",
        ],
        "next": "time_passes",
    },
    "time_passes": {
        "name": "Time Passes",
        "order": 5,
        "steps": [
            "1. Discard all played power cards to your personal discard pile.",
            "2. Damage on spirits and Dahan heals (remove all damage tokens).",
            "3. Add power cards from your hand back to your available cards.",
        ],
        "tips": [
            "ALL damage heals - both from Dahan and spirits.",
            "Destroyed Dahan do NOT come back - healing only removes damage tokens.",
            "Your discard pile is face-up; you can reclaim cards via growth later.",
        ],
        "next": "spirit",
    },
}

INVADER_RAVAGE_RULES = """
=== RAVAGE STEP DETAILED RULES ===

1. Invaders deal damage to the LAND (and Dahan):
   - Each Explorer deals 1 damage
   - Each Town deals 2 damage
   - Each City deals 3 damage
   - Total this damage up

2. Apply damage to Dahan first (each Dahan has 2 health)

3. If invaders dealt 2+ total damage to the land, add 1 Blight
   - Blight cascades if the land already had blight
   - Each blight added removes 1 presence from any spirit there (spirit's choice)

4. Surviving Dahan fight back:
   - Each surviving Dahan deals 2 damage to invaders
   - Spirits choose how to distribute Dahan damage among invaders
   - Explorers have 1 health, Towns have 2, Cities have 3

5. Destroy any invaders/Dahan reduced to 0 health
"""

INVADER_BUILD_RULES = """
=== BUILD STEP DETAILED RULES ===

1. In each land matching the Build card that has at least 1 invader:
   - Count Towns vs Cities in that land
   - If Towns > Cities: add 1 City (town upgrades to city)
   - Otherwise: add 1 Town

2. If no invaders are present in a matching land, nothing is built there.
"""

INVADER_EXPLORE_RULES = """
=== EXPLORE STEP DETAILED RULES ===

1. Draw the top card of the invader deck.

2. Add 1 Explorer to EACH land of the matching terrain type that is:
   - Adjacent to a Town or City, OR
   - Adjacent to the Ocean

3. The new explore card goes on the Explore slot.
   The old Explore card shifts to Build.
   The old Build card shifts to Ravage.
   The old Ravage card is discarded.
"""


def get_phase_info(phase_key):
    """Get detailed information about a game phase."""
    return PHASES.get(phase_key)


def get_next_phase(current_phase):
    """Get the next phase after the current one."""
    phase = PHASES.get(current_phase)
    if phase:
        return phase["next"]
    return None


def get_phase_summary():
    """Get a one-line summary of all phases in order."""
    lines = []
    for key in PHASE_ORDER:
        p = PHASES[key]
        lines.append(f"  {p['order']}. {p['name']}")
    return "\n".join(lines)
