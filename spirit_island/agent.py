"""Interactive Spirit Island help agent."""

import sys

from spirit_island.game_state import GameState
from spirit_island.phases import (
    PHASES,
    PHASE_ORDER,
    INVADER_RAVAGE_RULES,
    INVADER_BUILD_RULES,
    INVADER_EXPLORE_RULES,
    get_phase_summary,
)
from spirit_island.spirits import (
    get_spirit,
    list_spirits,
    format_spirit_detail,
)
from spirit_island.power_cards import (
    search_power_cards,
    format_power_card,
    ELEMENTS,
    MINOR_POWERS,
    MAJOR_POWERS,
)
from spirit_island.fear import (
    format_fear_overview,
    LOSS_CONDITIONS,
    TERROR_LEVELS,
)
from spirit_island.adversaries import (
    get_adversary,
    format_adversary,
    list_adversaries,
)


HELP_TEXT = """
=== SPIRIT ISLAND HELP AGENT ===

Commands you can use during the game:

  GAME TRACKING
    status          - Show current game state
    next            - What's coming next? (phase steps and tips)
    advance         - Move to the next phase
    turn            - Show current turn number
    set spirit <n>  - Set which spirit you're playing
    set adversary <name> <level> - Set the adversary
    set players <n> - Set number of players
    set terror <n>  - Set terror level (1-3)
    invader <r> <b> <e> - Set invader cards (ravage/build/explore terrain)
    note <text>     - Add a game note

  RULES & REFERENCE
    phases          - Overview of all game phases
    phase <name>    - Details on a specific phase (spirit/fast/invader/slow/time)
    ravage          - Detailed ravage rules
    build           - Detailed build rules
    explore         - Detailed explore rules
    fear            - How the fear system works
    terror          - Terror level victory conditions
    win             - Victory and loss conditions

  SPIRITS
    spirits         - List all spirits
    spirit <name>   - Details on a specific spirit

  POWER CARDS
    card <name>     - Search for a power card by name
    search <query>  - Search cards by keyword (element, effect text, etc.)
    elements        - List all elements and what they're associated with
    minors          - List all minor power cards
    majors          - List all major power cards

  ADVERSARIES
    adversaries     - List all adversaries
    adversary <name> - Details on a specific adversary

  OTHER
    help            - Show this help text
    tips            - General gameplay tips
    quit / exit     - Exit the agent

Type a command or ask a question!
"""

GENERAL_TIPS = """
=== GENERAL GAMEPLAY TIPS ===

EARLY GAME (Turns 1-3):
  - Focus on growth - get presence on the board and unlock card plays/energy
  - Don't panic about a little blight - it's a resource
  - Prioritize lands that will Ravage this turn
  - Use Dahan defensively - they fight back after taking damage

MID GAME (Turns 4-6):
  - Start picking up major powers if your energy supports it
  - Work toward terror level 2 - it makes winning much easier
  - Coordinate with other spirits on which lands to protect
  - Keep an eye on the invader deck - you can predict upcoming terrains

LATE GAME (Turns 7+):
  - Push for the win - games that drag on tend to favor the invaders
  - Major powers should be your primary damage source
  - Fear generation becomes critical - each fear card can swing the game
  - Don't forget your innate powers - check thresholds every turn

COMMON MISTAKES:
  - Forgetting Dahan fight back during ravage (each does 2 damage!)
  - Not checking innate power thresholds
  - Skipping growth options that add presence
  - Placing presence from the wrong track
  - Forgetting that destroying towns/cities generates fear
  - Not advancing invader cards after explore
"""


class SpiritIslandAgent:
    """Interactive help agent for Spirit Island gameplay."""

    def __init__(self):
        self.game = GameState()

    def handle_command(self, raw_input):
        """Process a user command and return a response string."""
        text = raw_input.strip()
        if not text:
            return "Type 'help' for a list of commands."

        parts = text.split()
        cmd = parts[0].lower()
        args = parts[1:]

        # Game tracking commands
        if cmd == "status":
            return self.game.format_status()

        if cmd == "next":
            return self.game.get_whats_next()

        if cmd == "advance":
            phase = self.game.advance_phase()
            return f"Advanced to: {phase['name']} (Turn {self.game.turn})\n\n{self.game.get_whats_next()}"

        if cmd == "turn":
            return f"Current turn: {self.game.turn}"

        if cmd == "set":
            return self._handle_set(args)

        if cmd == "invader":
            return self._handle_invader(args)

        if cmd == "note":
            if args:
                note = " ".join(args)
                self.game.add_note(note)
                return f"Note added: {note}"
            return "Usage: note <text>"

        # Rules & reference
        if cmd == "phases":
            return f"=== GAME PHASES ===\n\n{get_phase_summary()}\n\nType 'phase <name>' for details on a specific phase."

        if cmd == "phase":
            return self._handle_phase(args)

        if cmd == "ravage":
            return INVADER_RAVAGE_RULES

        if cmd == "build":
            return INVADER_BUILD_RULES

        if cmd == "explore":
            return INVADER_EXPLORE_RULES

        if cmd == "fear":
            return format_fear_overview()

        if cmd in ("terror", "terrorlevel"):
            return self._handle_terror(args)

        if cmd == "win":
            return LOSS_CONDITIONS

        # Spirits
        if cmd == "spirits":
            return f"=== AVAILABLE SPIRITS ===\n\n{list_spirits()}\n\nType 'spirit <name>' for details."

        if cmd == "spirit":
            return self._handle_spirit(args)

        # Power cards
        if cmd == "card" or cmd == "search":
            return self._handle_card_search(args)

        if cmd == "elements":
            lines = ["=== ELEMENTS ===", ""]
            for elem, desc in ELEMENTS.items():
                lines.append(f"  {elem}: {desc}")
            return "\n".join(lines)

        if cmd == "minors":
            lines = ["=== MINOR POWER CARDS ===", ""]
            for card in MINOR_POWERS:
                lines.append(format_power_card(card))
                lines.append("")
            return "\n".join(lines)

        if cmd == "majors":
            lines = ["=== MAJOR POWER CARDS ===", ""]
            for card in MAJOR_POWERS:
                lines.append(format_power_card(card))
                lines.append("")
            return "\n".join(lines)

        # Adversaries
        if cmd == "adversaries":
            return f"=== ADVERSARIES ===\n\n{list_adversaries()}\n\nType 'adversary <name>' for details."

        if cmd == "adversary":
            return self._handle_adversary(args)

        # Other
        if cmd == "help":
            return HELP_TEXT

        if cmd == "tips":
            return GENERAL_TIPS

        if cmd in ("quit", "exit", "q"):
            return "__EXIT__"

        # Try to be helpful with unrecognized input
        return self._handle_freeform(text)

    def _handle_set(self, args):
        if not args:
            return "Usage: set spirit <name> | set adversary <name> <level> | set players <n> | set terror <n>"
        subcmd = args[0].lower()

        if subcmd == "spirit" and len(args) > 1:
            name = " ".join(args[1:])
            spirit = get_spirit(name)
            if spirit:
                self.game.spirit = spirit["name"]
                return f"Spirit set to: {spirit['name']}"
            return f"Spirit '{name}' not found. Type 'spirits' to see available spirits."

        if subcmd == "adversary" and len(args) > 1:
            name = args[1]
            level = int(args[2]) if len(args) > 2 else 0
            adv = get_adversary(name)
            if adv:
                self.game.adversary = adv["name"]
                self.game.adversary_level = level
                return f"Adversary set to: {adv['name']} Level {level}"
            return f"Adversary '{name}' not found. Type 'adversaries' to see available adversaries."

        if subcmd == "players" and len(args) > 1:
            try:
                n = int(args[1])
                if 1 <= n <= 4:
                    self.game.num_players = n
                    self.game.fear_per_card = 4
                    return f"Player count set to {n}. Fear cards require {4 * n} fear each."
                return "Player count must be 1-4."
            except ValueError:
                return "Usage: set players <number>"

        if subcmd == "terror" and len(args) > 1:
            try:
                level = int(args[1])
                self.game.set_terror_level(level)
                info = TERROR_LEVELS.get(level)
                if info:
                    return f"Terror Level set to {level}.\nVictory: {info['victory']}"
                return "Terror level must be 1-3."
            except ValueError:
                return "Usage: set terror <1-3>"

        return "Usage: set spirit <name> | set adversary <name> <level> | set players <n> | set terror <n>"

    def _handle_invader(self, args):
        if not args:
            return ("Usage: invader <ravage> <build> <explore>\n"
                    "Example: invader jungle wetland mountain\n"
                    "Use '-' for empty slots.")
        ravage = args[0] if len(args) > 0 and args[0] != "-" else None
        build = args[1] if len(args) > 1 and args[1] != "-" else None
        explore = args[2] if len(args) > 2 and args[2] != "-" else None
        self.game.set_invader_cards(explore=explore, build=build, ravage=ravage)
        return (f"Invader track updated:\n"
                f"  Ravage:  {self.game.invader_ravage or '(empty)'}\n"
                f"  Build:   {self.game.invader_build or '(empty)'}\n"
                f"  Explore: {self.game.invader_explore or '(empty)'}")

    def _handle_phase(self, args):
        if not args:
            return f"=== GAME PHASES ===\n\n{get_phase_summary()}\n\nType 'phase <name>' for details."

        name = args[0].lower()
        # Map friendly names to keys
        name_map = {
            "spirit": "spirit", "growth": "spirit",
            "fast": "fast_power", "fast_power": "fast_power", "fastpower": "fast_power",
            "invader": "invader", "invaders": "invader",
            "slow": "slow_power", "slow_power": "slow_power", "slowpower": "slow_power",
            "time": "time_passes", "time_passes": "time_passes", "timepasses": "time_passes",
            "cleanup": "time_passes",
        }
        key = name_map.get(name)
        if key and key in PHASES:
            phase = PHASES[key]
            lines = [f"=== {phase['name']} ===", ""]
            for step in phase["steps"]:
                lines.append(f"  {step}")
            lines.append("")
            lines.append("Tips:")
            for tip in phase["tips"]:
                lines.append(f"  * {tip}")
            return "\n".join(lines)
        return f"Unknown phase '{name}'. Available: spirit, fast, invader, slow, time"

    def _handle_terror(self, args):
        lines = ["=== TERROR LEVELS ===", ""]
        for level, info in TERROR_LEVELS.items():
            marker = " <<< CURRENT" if level == self.game.terror_level else ""
            lines.append(f"Terror Level {level}{marker}")
            lines.append(f"  {info['description']}")
            lines.append(f"  Victory: {info['victory']}")
            lines.append("")
        return "\n".join(lines)

    def _handle_spirit(self, args):
        if not args:
            return f"=== AVAILABLE SPIRITS ===\n\n{list_spirits()}\n\nType 'spirit <name>' for details."
        name = " ".join(args)
        spirit = get_spirit(name)
        if spirit:
            return format_spirit_detail(spirit)
        return f"Spirit '{name}' not found. Type 'spirits' to see available spirits."

    def _handle_card_search(self, args):
        if not args:
            return "Usage: card <name or keyword>\nExample: card flood | search fire"
        query = " ".join(args)
        results = search_power_cards(query)
        if not results:
            return f"No power cards found matching '{query}'."
        lines = [f"=== POWER CARDS MATCHING '{query}' ({len(results)} found) ===", ""]
        for card in results:
            lines.append(format_power_card(card))
            lines.append("")
        return "\n".join(lines)

    def _handle_adversary(self, args):
        if not args:
            return f"=== ADVERSARIES ===\n\n{list_adversaries()}\n\nType 'adversary <name>' for details."
        name = " ".join(args)
        adv = get_adversary(name)
        if adv:
            return format_adversary(adv)
        return f"Adversary '{name}' not found. Type 'adversaries' to see available adversaries."

    def _handle_freeform(self, text):
        """Try to match freeform questions to relevant info."""
        text_lower = text.lower()

        # Check for spirit names
        for key in ["lightning", "river", "earth", "shadows", "thunderspeaker",
                     "ocean", "bringer", "spread", "green"]:
            if key in text_lower:
                spirit = get_spirit(key)
                if spirit:
                    return format_spirit_detail(spirit)

        # Check for phase keywords
        if any(w in text_lower for w in ["ravage", "damage", "blight"]):
            return INVADER_RAVAGE_RULES
        if "build" in text_lower and "invader" in text_lower:
            return INVADER_BUILD_RULES
        if "explore" in text_lower:
            return INVADER_EXPLORE_RULES
        if "fear" in text_lower or "terror" in text_lower:
            return format_fear_overview()
        if any(w in text_lower for w in ["win", "lose", "victory", "defeat"]):
            return LOSS_CONDITIONS
        if "phase" in text_lower or "turn order" in text_lower:
            return f"=== GAME PHASES ===\n\n{get_phase_summary()}"

        # Check for card-related queries
        if any(w in text_lower for w in ["card", "power", "spell"]):
            # Try to extract a search term
            for skip in ["what", "does", "card", "power", "spell", "the", "do", "is", "mean", "?", "a"]:
                text_lower = text_lower.replace(skip, "")
            query = text_lower.strip()
            if query:
                results = search_power_cards(query)
                if results:
                    lines = [f"Found {len(results)} matching card(s):", ""]
                    for card in results:
                        lines.append(format_power_card(card))
                        lines.append("")
                    return "\n".join(lines)

        return (f"I'm not sure what you're asking about. Try:\n"
                f"  'help' - see all commands\n"
                f"  'spirit <name>' - look up a spirit\n"
                f"  'card <name>' - look up a power card\n"
                f"  'next' - see what's coming in the game\n"
                f"  'ravage' / 'build' / 'explore' - invader rules")


def main():
    """Run the interactive Spirit Island help agent."""
    agent = SpiritIslandAgent()

    print("=" * 55)
    print("   SPIRIT ISLAND HELP AGENT")
    print("   Your companion for navigating the game")
    print("=" * 55)
    print()
    print("Type 'help' for commands, or ask a question!")
    print("Type 'quit' to exit.")
    print()

    while True:
        try:
            user_input = input("\nSpirit Island > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! May the spirits protect the island!")
            break

        if not user_input:
            continue

        response = agent.handle_command(user_input)

        if response == "__EXIT__":
            print("\nGoodbye! May the spirits protect the island!")
            break

        print()
        print(response)


if __name__ == "__main__":
    main()
