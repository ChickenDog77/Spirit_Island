# Spirit Island Help Agent

An interactive companion tool for the board game **Spirit Island**. Run it alongside your game to track phases, look up rules, understand cards, and get tips on what's coming next.

## Quick Start

```bash
python -m spirit_island
```

No dependencies required - runs on Python 3.6+.

## What It Does

- **Phase Tracking** - Tracks which phase you're in and tells you exactly what to do next
- **Game State** - Remembers your spirit, adversary, terror level, and invader cards
- **Spirit Reference** - Detailed info on 8 base game spirits including unique powers and innate abilities
- **Power Card Lookup** - Search minor and major power cards by name, element, or keyword
- **Rules Reference** - Detailed breakdowns of ravage, build, explore, and fear mechanics
- **Adversary Info** - Rules for Brandenburg-Prussia, England, and Sweden at all levels
- **Gameplay Tips** - Strategic advice for early, mid, and late game

## Example Session

```
Spirit Island > set spirit lightning
Spirit set to: Lightning's Swift Strike

Spirit Island > next
--- WHAT'S NEXT: Spirit Phase ---
  1. Growth: Choose one growth option from your spirit panel.
  2. Gain Energy: Gain energy equal to your current energy track value.
  3. Pick Power Cards: You may pay energy to gain new power cards.

Spirit Island > advance
Advanced to: Fast Powers Phase (Turn 1)

Spirit Island > card flood
=== POWER CARDS MATCHING 'flood' (2 found) ===
[Minor] Flash Floods
  Cost: 2 | Speed: Fast
  Elements: Sun, Water
  Effect: 2 Damage.

[MAJOR] Cleansing Floods
  Cost: 5 | Speed: Slow
  Elements: Sun, Water
  Effect: 4 Damage. Remove 1 blight.
  Threshold: 3 Water: +10 Damage.

Spirit Island > ravage
=== RAVAGE STEP DETAILED RULES ===
1. Invaders deal damage to the LAND (and Dahan)...
```

## Commands

| Category | Command | Description |
|----------|---------|-------------|
| **Tracking** | `status` | Show current game state |
| | `next` | What's coming next (steps + tips) |
| | `advance` | Move to the next phase |
| | `set spirit <name>` | Set your spirit |
| | `set adversary <name> <level>` | Set the adversary |
| | `set terror <1-3>` | Set terror level |
| | `invader <ravage> <build> <explore>` | Set invader track terrains |
| | `note <text>` | Add a game note |
| **Rules** | `phases` | Overview of all phases |
| | `phase <name>` | Detail on a specific phase |
| | `ravage` / `build` / `explore` | Detailed invader rules |
| | `fear` | Fear system overview |
| | `win` | Victory and loss conditions |
| **Spirits** | `spirits` | List all spirits |
| | `spirit <name>` | Spirit details and powers |
| **Cards** | `card <name>` | Search power cards |
| | `elements` | Element reference |
| | `minors` / `majors` | List all minor/major powers |
| **Adversaries** | `adversaries` | List adversaries |
| | `adversary <name>` | Adversary details |
| **Other** | `help` | Show all commands |
| | `tips` | General gameplay tips |

## Spirits Included

- Lightning's Swift Strike (Low complexity)
- River Surges in Sunlight (Low)
- Vital Strength of the Earth (Low)
- Shadows Flicker Like Flame (Low)
- Thunderspeaker (Moderate)
- Ocean's Hungry Grasp (Moderate)
- Bringer of Dreams and Nightmares (High)
- A Spread of Rampant Green (Moderate)
