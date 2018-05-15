label fireplace:

    if fireplace_examined and not day == 1 and not fire_in_fireplace:
        #$ renpy.play('sounds/fire01.ogg')  
        #play bg_sounds "sounds/fire01.ogg" fadeout 1.0 fadein 1.0 #LOUD!
        #play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        $ fire_in_fireplace = True
        show screen fireplace_fire
        jump day_main_menu
    if fireplace_examined and fire_in_fireplace and not day == 1:
        $ fire_in_fireplace = False
        stop bg_sounds #Stops playing the fire SFX.
        hide screen fireplace_fire
        jump day_main_menu
    else:
        menu:
            "-Examine the fireplace-" if not fireplace_examined:
                $ fireplace_examined = True
                hide screen genie
                call gen_chibi("stand","mid","base")
                show screen chair_02 #Empty chair near the desk.
                show screen desk
                with Dissolve(0.5)
                m "Hm... Looks like an ordinary fireplace..."
                show screen genie
                hide screen genie_stands
                hide screen chair_02 #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu

            "-Never mind-":
                jump day_main_menu
