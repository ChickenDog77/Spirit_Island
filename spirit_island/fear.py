"""Fear and victory condition tracking for Spirit Island."""

TERROR_LEVELS = {
    1: {
        "name": "Terror Level 1",
        "victory": "Destroy all invaders on the island (no explorers, towns, or cities remain).",
        "description": "The invaders are confident and fully committed to colonization.",
    },
    2: {
        "name": "Terror Level 2",
        "victory": "Destroy all towns and cities (explorers may remain).",
        "description": "The invaders are nervous. Explorers alone will flee if the towns and cities fall.",
    },
    3: {
        "name": "Terror Level 3",
        "victory": "Destroy all cities (towns and explorers may remain).",
        "description": "The invaders are terrified. Only the cities hold them to the island.",
    },
}

FEAR_CARDS_BASE = [
    {"name": "Dahan Raid", "level1": "Each player may push 1 explorer from a land with Dahan.",
     "level2": "In each land with Dahan, destroy 1 explorer.", "level3": "In each land with Dahan, destroy all explorers."},
    {"name": "Flee the Pestilent Land", "level1": "Each player pushes 1 explorer.",
     "level2": "Each player pushes up to 3 explorers.", "level3": "Push all explorers from each blighted land."},
    {"name": "Seek Safety", "level1": "Explorers do not participate in ravage this turn.",
     "level2": "Each player removes 1 explorer.", "level3": "Remove all explorers from lands without towns/cities."},
    {"name": "Dahan Enheartened", "level1": "In each land with Dahan, defend 1.",
     "level2": "In each land with Dahan, defend 3.", "level3": "Each Dahan has +1 health this turn and deals +1 damage."},
    {"name": "Belief Takes Root", "level1": "Each player may gather 1 Dahan into a land with your presence.",
     "level2": "Add 1 Dahan to a land with your presence.", "level3": "Add 2 Dahan. Each Dahan deals +1 damage this turn."},
    {"name": "Overseas Trade Disrupted", "level1": "Skip the next build step in coastal lands.",
     "level2": "Each player destroys 1 town in a coastal land.", "level3": "Destroy all towns in coastal lands."},
    {"name": "Tall Tales of Savagery", "level1": "Each player generates 2 fear.",
     "level2": "Generate 4 fear. Push 1 explorer from each land.", "level3": "Generate 6 fear. Each player destroys 1 town."},
    {"name": "Retreat", "level1": "Push 1 explorer from each land with Dahan.",
     "level2": "Push all explorers from lands with Dahan.", "level3": "Push all explorers. Destroy 1 town per 3 Dahan."},
    {"name": "Wary of the Interior", "level1": "Invaders do not explore inland this turn.",
     "level2": "Invaders do not explore or build inland.", "level3": "Destroy all inland towns."},
]


LOSS_CONDITIONS = """
=== LOSS CONDITIONS ===

You LOSE the game if any of these happen:
  1. Any spirit is destroyed (all presence removed from the board)
  2. The blight card flips and its "blighted" side effect triggers removal
     of all blight from the card (island is fully overrun)
  3. You need to draw an invader card but the deck is empty
     (the invaders have fully committed)

You WIN if:
  - At the current terror level, the victory condition is met
  - OR you play a card/effect that grants an alternate victory
  - Terror Level Victory is the easiest path:
    TL1: No invaders remain at all
    TL2: No towns or cities remain
    TL3: No cities remain
"""


def get_terror_level_info(level):
    """Get information about a specific terror level."""
    return TERROR_LEVELS.get(level)


def format_fear_overview():
    """Return a formatted overview of the fear system."""
    lines = [
        "=== FEAR SYSTEM ===",
        "",
        "Generating Fear:",
        "  - Destroying a Town generates 1 Fear",
        "  - Destroying a City generates 2 Fear",
        "  - Some power cards generate additional Fear",
        "",
        "Fear Cards:",
        "  - Each fear card requires 4 fear per player to earn",
        "  - Earned fear cards are resolved at the start of the Invader Phase",
        "  - The effect used depends on the current Terror Level",
        "",
        "Terror Levels:",
    ]
    for level, info in TERROR_LEVELS.items():
        lines.append(f"  Terror Level {level}: {info['description']}")
        lines.append(f"    Victory: {info['victory']}")
        lines.append("")

    return "\n".join(lines)
