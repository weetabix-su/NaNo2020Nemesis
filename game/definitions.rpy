# Character Definitions

define think = Character(None, window_background=Image("gui/textbox_think.png", xalign=0.5, yalign=1.0))

define r = Character("Rumi", image = "rumi")

define mc = Character("David", image = "mc")

define pg = Character("Angela", image = "angela")

define weeb = Character("Rick", image = "weeb")

define m = Character("May")

define mike = Character("Mike")

define popgirl = Character("Anna")

define rfriend = Character("Some ass kissing bitch")

define teacher = Character("Teacher")


# Position Definitions
default pov_offset = 0


transform position:
    anchor (0.5, 1.0)
    yalign 1.0

transform one:
    position
    xalign 0.5
    yoffset pov_offset

transform two_left:
    position
    xalign 1.0/3.0
    yoffset pov_offset

transform two_right:
    position
    xalign 2.0/3.0
    yoffset pov_offset

transform three_left:
    position
    xalign 0.15
    yoffset pov_offset

transform three_right:
    position
    xalign 0.85
    yoffset pov_offset

# Sprite definitions

# MC sprites
image rumi cry = "images/sprites/rumi/mc_cry.png"
image rumi happy = "images/sprites/rumi/mc_happy.png"
image rumi laugh = "images/sprites/rumi/mc_laugh.png"
image rumi scared = "images/sprites/rumi/mc_scared.png"
image rumi think = "images/sprites/rumi/mc_thinking.png"

# Weeb sprites
image weeb cry = "images/sprites/weeb/weeb_crying.png"
image weeb happy = "images/sprites/weeb/weeb_happy.png"
image weeb laugh = "images/sprites/weeb/weeb_laugh.png"
image weeb scared = "images/sprites/weeb/weeb_scared.png"
image weeb think = "images/sprites/weeb/weeb_thinking.png"

# Rumi sprites normal
image mc cry = "images/sprites/mc/rumi_cry.png"
image mc happy = "images/sprites/mc/rumi_happy.png"
image mc laugh = "images/sprites/mc/rumi_laugh.png"
image mc scared = "images/sprites/mc/rumi_scared.png"
image mc think = "images/sprites/mc/rumi_thinking.png"
# With glasses and ponytail
image mc 2 cry = "images/sprites/mc/rumi2_cry.png"
image mc 2 happy = "images/sprites/mc/rumi2_happy.png"
image mc 2 laugh = "images/sprites/mc/rumi2_laugh.png"
image mc 2 scared = "images/sprites/mc/rumi2_scared.png"
image mc 2 think = "images/sprites/mc/rumi2_thinking.png"
# With only ponytail
image mc 3 cry = "images/sprites/mc/rumi3_cry.png"
image mc 3 happy = "images/sprites/mc/rumi3_happy.png"
image mc 3 laugh = "images/sprites/mc/rumi3_laugh.png"
image mc 3 scared = "images/sprites/mc/rumi3_scared.png"
image mc 3 think = "images/sprites/mc/rumi3_thinking.png"

# PG sprites
image pg cry= "images/sprites/loli_crying.png"
image pg happy= "images/sprites/loli_happy.png"
image pg laugh= "images/sprites/loli_laugh.png"
image pg scared= "images/sprites/loli_scared.png"
image pg think= "images/sprites/loli_thinking.png"

# BG Definitions

image bg afternoon = im.Scale("images/bg/afternoon01.jpg", 1280, 720)
image bg afternoon_2 = im.Scale("images/bg/afternoon02.jpg", 1280, 720)
image bg gate = im.Scale("images/bg/applegate school gate 3 entrance.jpg", 1280, 720)
image bg gate_2 = im.Scale("images/bg/generic_school_gate.jpg", 1280, 720)
image bg park = im.Scale("images/bg/beautiful_park_with_nice_volumetric_fog_to_immitate_that_bg_found_in_touma_a_panchu_a_girls_anime.jpg", 1280, 720)
image bg park_2 = im.Scale("images/bg/childrens_park_evening.jpg", 1280, 720)
image bg park_no_fence_day = im.Scale("images/bg/park_no_fence_day.jpg", 1280, 720)
image bg park_no_fence_night = im.Scale("images/bg/park_no_fence_night.jpg", 1280, 720)
image bg park_winter = im.Scale("images/bg/park_not_so_winter.jpg", 1280, 720)
image bg bus_stop_evening = im.Scale("images/bg/bus stop evening.jpg", 1280, 720)
image bg bus_stop_morning = im.Scale("images/bg/bus stop morning.jpg", 1280, 720)
image bg bus_stop_night = im.Scale("images/bg/bus stop night.jpg", 1280, 720)
image bg classroom = im.Scale("images/bg/Classroom_01_day.jpg", 1280, 720)
image bg classroom_2 = im.Scale("images/bg/Classroom_02_day.jpg", 1280, 720)
image bg evening = im.Scale("images/bg/evening02.jpg", 1280, 720)
image bg kitchen_day = im.Scale("images/bg/kitchen_day.jpg", 1280, 720)
image bg kitchen_night = im.Scale("images/bg/kitchen_night.jpg", 1280, 720)
image bg library = im.Scale("images/bg/library.png", 1280, 720)
image bg apartment_evening = im.Scale("images/bg/old_apartment_evening.jpg", 1280, 720)
image bg apartment_noon = im.Scale("images/bg/old_apartment_noon.jpg", 1280, 720)
image bg roadisde_dawn = im.Scale("images/bg/roadside_dawn.jpg", 1280, 720)
image bg roadisde_morning = im.Scale("images/bg/roadside_morning.jpg", 1280, 720)
image bg roadisde_night = im.Scale("images/bg/roadside_night_fullmoon.jpg", 1280, 720)
image bg room = im.Scale("images/bg/room.jpg", 1280, 720)
image bg room_dawn = im.Scale("images/bg/room_dawn_light_off.jpg", 1280, 720)
image bg room_dusk = im.Scale("images/bg/room_dusk_light_off.jpg", 1280, 720)
image bg room_dusk_light = im.Scale("images/bg/room_dusk_light_on.jpg", 1280, 720)
image bg room_evening = im.Scale("images/bg/room_evening_light_off.jpg", 1280, 720)
image bg room_noon = im.Scale("images/bg/room_noon_light_off.jpg", 1280, 720)
image bg corridor = im.Scale("image/bg/school_corridor_background.jpg", 1280, 720)
image bg corridor_2 = im.Scale("image/bg/uncle mugen school corridor morning.jpg", 1280, 720)
image bg seaside_road_evening = im.Scale("images/bg/seaside_road_evening.jpg", 1280, 720)
image bg seaside_road_morning = im.Scale("images/bg/seaside_road_morning.jpg", 1280, 720)
image bg seaside_road_sunset = im.Scale("images/bg/seaside_road_sunset.jpg", 1280, 720)
image bg mountain_road = im.Scale("images/bg/some_road_in_some_random_mountain.jpg", 1280, 720)
image bg street_usa = im.Scale("images/bg/someplace_usa.jpg", 1280, 720)
image bg street = im.Scale("images/bg/Street Background.jpg", 1280, 720)
image bg street_2 = im.Scale("images/bg/street_background_01.jpg", 1280, 720)
image bg street_3 = im.Scale("images/bg/street_background_04.jpg", 1280, 720)
image bg street_4 = im.Scale("images/bg/this_better_be_good_because_the_render_time_for_this_bg_is_horrendous_despite_having_a_render_farm.jpg", 1280, 720)



# CG Definitions
