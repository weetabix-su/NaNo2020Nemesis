# Character Definitions

define think = Character(None, window_background=Image("gui/textbox_think.png", xalign=0.5, yalign=1.0))

define r = Character("Rumi", image = "rumi")

define mc = Character("David", image = "mc")

define pg = Character("Angela", image = "pg")

define weeb = Character("Rick", image = "weeb")

define m = Character("May")

define mcmom = Character("David's Mom")

define rdad = Character("Rumi's Dad")

define mike = Character("Mike")

define popgirl = Character("Anna")

define rfriend = Character("{size=-11}Some ass-kissing bitch{/size}")

define tea = Character("Teacher")

define eric = Character("Eric")

define audrey = Character("Audrey")

define dominic = Character("Dominic")

define mel = Character("Mel")

define maria = Character("Maria")

define marty = Character("Marty")

define tori = Character("Victoria")

define kat = Character("Katrina")

define caren = Character("Caren")

define sandra = Character("Sandra")

define yui = Character("Yui")

define leona = Character("Leona")

define waitress = Character("Waitress")

define waitressJ = Character("Josephine")

define unknownA = Character("??? #1")

define unknownB = Character("??? #2")


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
    xalign 0.275
    yoffset pov_offset

transform two_right:
    position
    xalign 0.725
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
# With pink hair
image rumi 2 cry = "images/sprites/rumi/mc2_cry.png"
image rumi 2 happy = "images/sprites/rumi/mc2_happy.png"
image rumi 2 laugh = "images/sprites/rumi/mc2_laugh.png"
image rumi 2 scared = "images/sprites/rumi/mc2_scared.png"
image rumi 2 think = "images/sprites/rumi/mc2_thinking.png"

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
image mc 3 cry = "images/sprites/mc/rumi3_crying.png"
image mc 3 happy = "images/sprites/mc/rumi3_happy.png"
image mc 3 laugh = "images/sprites/mc/rumi3_laughing.png"
image mc 3 scared = "images/sprites/mc/rumi3_scared.png"
image mc 3 think = "images/sprites/mc/rumi3_thinking.png"
# Silhouetted
image mc silhouette_b = im.MatrixColor(Image("images/sprites/mc/rumi_scared.png"), im.matrix((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,)))
image mc silhouette_w = im.MatrixColor(Image("images/sprites/mc/rumi_scared.png"), im.matrix((0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,)))

# PG sprites
image pg cry = "images/sprites/pg/loli_crying.png"
image pg happy = "images/sprites/pg/loli_happy.png"
image pg laugh = "images/sprites/pg/loli_laugh.png"
image pg scared = "images/sprites/pg/loli_scared.png"
image pg think = "images/sprites/pg/loli_thinking.png"

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
image bg rooftop = im.Scale("images/bg/uncle_mugen_school_building_rooftop_day.jpg", 1280, 941)
image bg gym = im.Scale("images/bg/basketball court.png", 1280, 908)
image bg gym_showers = im.Scale("images/bg/toilet_04.jpg", 1280, 720)
image bg evening = im.Scale("images/bg/evening02.jpg", 1280, 720)
image bg kitchen_day = im.Scale("images/bg/kitchen_day.jpg", 1280, 720)
image bg kitchen_night = im.Scale("images/bg/kitchen_night.jpg", 1280, 720)
image bg bathroom = im.Scale("images/bg/bathroom_post_processed.jpg", 1280, 843)
image bg library = im.Scale("images/bg/library.png", 1280, 720)
image bg apartment_evening = im.Scale("images/bg/old_apartment_evening.jpg", 1280, 720)
image bg apartment_noon = im.Scale("images/bg/old_apartment_noon.jpg", 1280, 720)
image bg roadside_dawn = im.Scale("images/bg/roadside_dawn.jpg", 1280, 720)
image bg roadside_morning = im.Scale("images/bg/roadside_morning.jpg", 1280, 720)
image bg roadside_night = im.Scale("images/bg/roadside_night_fullmoon.jpg", 1280, 720)
image bg beach_night = im.Scale("images/bg/beach_night_no_moon.jpg", 1280, 720)
image bg room = im.Scale("images/bg/room.jpg", 1280, 876)
image bg room_dawn = im.Scale("images/bg/room_dawn_light_off.jpg", 1280, 720)
image bg room_dusk = im.Scale("images/bg/room_dusk_light_off.jpg", 1280, 720)
image bg room_dusk_light = im.Scale("images/bg/room_dusk_light_on.jpg", 1280, 720)
image bg room_evening = im.Scale("images/bg/room_evening_light_off.jpg", 1280, 720)
image bg room_noon = im.Scale("images/bg/room_noon_light_off.jpg", 1280, 720)
image bg corridor = im.Scale("images/bg/school_corridor_background.jpg", 1280, 720)
image bg corridor_2 = im.Scale("images/bg/uncle mugen school corridor morning.jpg", 1280, 720)
image bg seaside_road_evening = im.Scale("images/bg/seaside_road_evening.jpg", 1280, 720)
image bg seaside_road_morning = im.Scale("images/bg/seaside_road_morning.jpg", 1280, 720)
image bg seaside_road_sunset = im.Scale("images/bg/seaside_road_sunset.jpg", 1280, 720)
image bg mountain_road = im.Scale("images/bg/some_road_in_some_random_mountain.jpg", 1280, 720)
image bg street_usa = im.Scale("images/bg/someplace_usa.jpg", 1280, 720)
image bg street = im.Scale("images/bg/Street Background.jpg", 1280, 720)
image bg street_2 = im.Scale("images/bg/street_background_01.jpg", 1280, 720)
image bg street_3 = im.Scale("images/bg/street_background_04.jpg", 1280, 720)
image bg street_4 = im.Scale("images/bg/this_better_be_good_because_the_render_time_for_this_bg_is_horrendous_despite_having_a_render_farm.jpg", 1280, 720)
image bg street_5 = im.Scale("images/bg/street_background_00.jpg", 1280, 720)

image bg bighouse = im.Scale("images/bg/the_jp_mansion_night.jpg", 1280, 844)

# The following BGs are from Guttari Nyanko (guttari8.sakura.ne.jp)
image bg bighouse_lobby = im.Scale("images/bg/bijyutukan00.jpg", 1280, 960)
image bg bighouse_dining = im.Scale("images/bg/rissyoku00a.jpg", 1280, 960)
image bg bighouse_table = im.Scale("images/bg/syokudou00.jpg", 1280, 960)
image bg bighouse_lib = im.Scale("images/bg/tosyo00.jpg", 1280, 960)

image white = "#ffffff"

# Text Generators
image txt cen = renpy.ParameterizedText(ypos=0.5, xpos=0.5, xalign=0.5, yalign=0.5, text_align=0.5)
