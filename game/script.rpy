# splashscreen is displayed on game launch before main menu
label splashscreen:
    play sound "gui/boot.ogg"
    return

# this is the new game's start point
label start:
    # Day 1 dialogue
    jump Day1_MC1
    jump Day1_Rumi
    jump Day1_MC2
    # Day 2 dialogue
    jump Day2_Rumi
    jump Day2_MC
    jump Day2_Rumi2
    # Day 3 dialogue
    jump Day3_MC
    jump Day3_Rumi
    # Day 4 dialogue
    jump Day4_MC1
    jump Day4_Rumi
    jump Day4_MC2
    jump Day4_May
    jump Day4_MC3
    jump Day4_Rumi2
    # Day 5 dialogue
    jump Day5_Rumi
    # Day 6 dialogue
    jump Day6_Rumi
    jump Day6_MC
    # Day 7 dialogue
    jump Day7_MC
    # Day 16 dialogue
    jump Day16_PGWeeb
    # Day 17 dialogue
    jump Day17_MC
    # Day 18 dialogue
    jump Day18_MC
    # Day 18 dialogue
    jump Day19_MC
    # Day 29 dialogue
    jump Day29_MC
    # Day 139 dialogue
    jump Day139
    # Year 9 dialogue
    jump Year9_Day1_MC
    jump Year9_Day2_MC
    jump Day2_Unknown
