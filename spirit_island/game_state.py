"""Game state tracker for Spirit Island sessions."""

from spirit_island.phases import PHASE_ORDER, PHASES


class GameState:
    """Tracks the current state of a Spirit Island game session."""

    def __init__(self):
        self.turn = 1
        self.phase_index = 0
        self.terror_level = 1
        self.fear_generated = 0
        self.fear_per_card = 4  # default for 1 player
        self.num_players = 1
        self.spirit = None
        self.adversary = None
        self.adversary_level = 0
        self.invader_explore = None
        self.invader_build = None
        self.invader_ravage = None
        self.notes = []

    @property
    def current_phase_key(self):
        return PHASE_ORDER[self.phase_index]

    @property
    def current_phase(self):
        return PHASES[self.current_phase_key]

    def advance_phase(self):
        """Move to the next phase. Returns the new phase info."""
        self.phase_index = (self.phase_index + 1) % len(PHASE_ORDER)
        if self.phase_index == 0:
            self.turn += 1
        return self.current_phase

    def set_terror_level(self, level):
        if 1 <= level <= 3:
            self.terror_level = level

    def add_fear(self, amount):
        self.fear_generated += amount
        cards_earned = self.fear_generated // (self.fear_per_card * self.num_players)
        return cards_earned

    def set_invader_cards(self, explore=None, build=None, ravage=None):
        if explore is not None:
            self.invader_explore = explore
        if build is not None:
            self.invader_build = build
        if ravage is not None:
            self.invader_ravage = ravage

    def add_note(self, note):
        self.notes.append(f"Turn {self.turn}: {note}")

    def format_status(self):
        lines = [
            f"=== GAME STATUS ===",
            f"Turn: {self.turn}",
            f"Current Phase: {self.current_phase['name']}",
            f"Terror Level: {self.terror_level}",
        ]
        if self.spirit:
            lines.append(f"Spirit: {self.spirit}")
        if self.adversary:
            lines.append(f"Adversary: {self.adversary} (Level {self.adversary_level})")
        lines.append("")
        lines.append("Invader Track:")
        lines.append(f"  Ravage:  {self.invader_ravage or '(empty)'}")
        lines.append(f"  Build:   {self.invader_build or '(empty)'}")
        lines.append(f"  Explore: {self.invader_explore or '(empty)'}")

        if self.notes:
            lines.append("")
            lines.append("Recent Notes:")
            for note in self.notes[-5:]:
                lines.append(f"  - {note}")

        return "\n".join(lines)

    def get_whats_next(self):
        """Explain what's coming up next in the game."""
        phase = self.current_phase
        lines = [
            f"--- WHAT'S NEXT: {phase['name']} ---",
            "",
        ]
        for step in phase["steps"]:
            lines.append(f"  {step}")
        lines.append("")
        lines.append("Tips:")
        for tip in phase["tips"]:
            lines.append(f"  * {tip}")

        # Add invader-specific context
        if self.current_phase_key == "invader":
            lines.append("")
            if self.invader_ravage:
                lines.append(f"  >> RAVAGE will hit: {self.invader_ravage} lands")
            if self.invader_build:
                lines.append(f"  >> BUILD will happen in: {self.invader_build} lands")
            lines.append(f"  >> EXPLORE will reveal a new card from the invader deck")

        return "\n".join(lines)
