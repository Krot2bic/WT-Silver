

####NIGHT STARTS HERE###<<<<<<<<<<<-----------------------------------------------------------------------------------------------------###
###=====================================================================================================================================###
label night_start:
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
#    $ renpy.set_style_preference("dialog", "Night")


###RESET STUFF

call reset_hermione_main

$ only_upper = False #When true, legs are not displayed in the hermione_main screen.
$ no_blinking = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm = False #Shows cum stains on Hermione's uniform.
$ uni_sperm = False
$ textColor = "#1e1008"

call luna_night_flags
$ daytime = False
$ interface_color = "gray"
$ snape_busy = False
$ hermione_takes_classes = False
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.


stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

scene black

hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen done_reading #Hiding genie sitting with closed book in his hands.
hide screen done_reading_near_fire #Done reading by the fire
hide screen new_window #Hiding clear sky bg.

hide screen bld1
hide screen blktone
hide screen blkfade

### WEATHER ###
$ show_weather()





if package_is_here:
    hide screen package


hide screen main_room

hide screen genie
hide screen owl
hide screen owl_02


show screen main_room
show screen candlefire

show screen genie
if package_is_here:
    show screen package

#hide screen statistics
#show screen statistics

hide screen points
show screen points

if got_mail or mail_from_her or letters >= 1:
    show screen owl
with fade







call points_changes #Makes changes in the Slytherin house points.
call points_changes_gryffindor #Makes changes in the Gryffindor (And the rest of the houses) house points. (07_points_gry.rpy)
# call snape_bonus # Not in use anymore.

### NIGHT REQUESTS ###
jump Night_Request_Block


label night_resume:

### NIGHT EVENTS ###
if day == 1:
    call event_02 #Returns
if day == 2:
    jump event_03 #No return. Jumps next day.
if day == 4:
    jump event_05 #Before Duel #No return.
if day == 5:
    jump event_07 #No return.
if days_without_an_event == 1 and hermione_is_waiting_02 and not event11_happened:
    call event_11 #Returns
if days_without_an_event == 1 and event11_happened and not event12_happened:
    jump event_12 #No return.
if days_without_an_event == 1 and event12_happened and not event13_happened:
    jump event_13 #No return.
if day >= 15 and day <=20 and not event15_happened:
    call event_15 #Returns
    
if whoring == 11 and not touched_by_boy:
    call nar("!!! Attention !!!","start")
    ">Increasing Hermione's whoring level any further without doing more public requests will lock your game to a specific ending."
    ">This message will repeat until you increase her whoring level, or do a certain number of public requests!"
    call nar(">You should also save your game here.","end")
    menu:
        "-Understood-":
            pass
        "-Don't tell me what to do!-":
            pass

if gave_the_dress and days_without_an_event >= 2: #$ gave_the_dress = True #Turns True when Hermione has the dress.
    jump good_bye_snape


if luna_known and not luna_unlocked:
    call hat_intro_3 #Returns

if luna_corruption == 11 and luna_reverted:
    jump luna_reverted_greeting_2 #No return.

if milking == -1:
    call potion_scene_11_1_2 #Returns
if milking == -3:
    call potion_scene_11_3_2

### Guide ###
#Random Number for Tip/Fact of the Day
$ daily_rndm_tip_or_fact = renpy.random.randint(0, 18)
call update_quests
call update_hints





label night_main_menu:

### MENU PLACEMENT ###
$ menu_x = 0.5
$ menu_y = 0.5

if phoenix_is_feed:
    show screen phoenix_food

hide screen bld1
hide screen blktone
with d1

show screen animation_feather
call screen main_room_menu
