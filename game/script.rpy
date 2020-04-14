# splashscreen is displayed on game launch before main menu
label splashscreen:
    play sound "gui/boot.ogg"
    return

# this is the new game's start point
label start:
    # Day 1 dialogue
    call Day1_MC1 from _call_Day1_MC1
    call Day1_Rumi from _call_Day1_Rumi
    call Day1_MC2 from _call_Day1_MC2
    # Day 2 dialogue
    call Day2_Rumi from _call_Day2_Rumi
    call Day2_MC from _call_Day2_MC
    call Day2_Rumi2 from _call_Day2_Rumi2
    # Day 3 dialogue
    call Day3_MC from _call_Day3_MC
    call Day3_Rumi from _call_Day3_Rumi
    # Day 4 dialogue
    call Day4_MC1 from _call_Day4_MC1
    call Day4_Rumi from _call_Day4_Rumi
    call Day4_MC2 from _call_Day4_MC2
    call Day4_May from _call_Day4_May
    call Day4_MC3 from _call_Day4_MC3
    call Day4_Rumi2 from _call_Day4_Rumi2
    # Day 5 dialogue
    call Day5_Rumi from _call_Day5_Rumi
    # Day 6 dialogue
    call Day6_Rumi from _call_Day6_Rumi
    call Day6_MC from _call_Day6_MC
    # Day 7 dialogue
    call Day7_MC from _call_Day7_MC
    # Day 16 dialogue
    call Day16_PGWeeb from _call_Day16_PGWeeb
    # Day 17 dialogue
    call Day17_MC from _call_Day17_MC
    # Day 18 dialogue
    call Day18_MC from _call_Day18_MC
    # Day 19 dialogue
    call Day19_MC from _call_Day19_MC
    # Day 20 dialogue
    call Day20_MC from _call_Day20_MC
    call Day20_Rumi from _call_Day20_Rumi
    call Day20_MC2 from _call_Day20_MC2
    # Day 29 dialogue
    call Day29_MC from _call_Day29_MC
    # Day 139 dialogue
    call Day139 from _call_Day139
    # Year 9 dialogue
    call Year9_Day1_MC from _call_Year9_Day1_MC
    call Year9_Day2_MC from _call_Year9_Day2_MC
    call Day2_Unknown from _call_Day2_Unknown
