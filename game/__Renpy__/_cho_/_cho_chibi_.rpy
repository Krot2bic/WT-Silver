

### Cho Chibi ###

label cho_chibi(action = "", xpos=cho_chibi_xpos, ypos=cho_chibi_ypos, flip=False, animation=False):
    $ cho_chibi_status = ""
    call update_cho_chibi_uniform

    if xpos != cho_chibi_xpos:
        if xpos == "mid":
            $ cho_chibi_xpos = 560
        elif xpos in ("wardrobe","center","base","default"): #Don't use these when there are other chibis around (like Hermione's). Use "mid" instead.
            $ cho_chibi_xpos = 530
        elif xpos == "desk":
            $ cho_chibi_xpos = 440
        elif xpos == "on_desk":
            $ cho_chibi_xpos = 350
        elif xpos == "door":
            $ cho_chibi_xpos = 750
        else:
            $ cho_chibi_xpos = int(xpos)

    if ypos != cho_chibi_ypos:
        if ypos in ("base","default"):
            $ cho_chibi_ypos = 250
        elif ypos == "on_desk":
            $ cho_chibi_ypos = 180
        else:
            $ cho_chibi_ypos = int(ypos)

    # Action command.
    if action == "hide":
        hide screen cho_stand
    elif action == "leave":
        call play_sound("door")
        hide screen cho_main
        hide screen bld1
        hide screen blktone
        with d3
        pause.5

    else:
        if action in ["fly"]:
            $ cho_chibi_animation = "fly"
            call update_cho_chibi_uniform
        if action in ["reset"]:
            $ cho_chibi_animation = None
            call update_cho_chibi_uniform

        if flip: #Same variable that the main sprite is using. #1 == Default
            $ cho_chibi_flip = -1
            show screen cho_stand
        else:
            $ cho_chibi_flip = 1
            show screen cho_stand

    if animation != False:
        $ cho_chibi_animation = animation

    return



### Cho Chibi Walk ###

label cho_walk(xpos=walk_xpos, ypos=walk_ypos, speed=cho_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    $ cho_chibi_status = "move"
    call update_cho_chibi_uniform

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ cho_chibi_xpos = 750
        $ cho_chibi_ypos = 250
        $ cho_chibi_flip = 1
    elif action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = cho_chibi_xpos
    $ walk_ypos = cho_chibi_ypos

    # Target location.
    if xpos == "mid":
        $ walk_xpos2 = 580 #540
    elif xpos == "desk":
        $ walk_xpos2 = 440
    elif xpos == "door":
        $ walk_xpos2 = 750
    else:
        $ walk_xpos2 = int(xpos)

    if ypos in ("base","default"):
        $ walk_ypos2 = 250
    else:
        $ walk_ypos2 = int(ypos)

    $ cho_speed = speed #Speed of walking animation. (lower = faster)

    # Walk right to left
    if walk_xpos >= walk_xpos2:
        $ cho_chibi_flip = 1
        show screen cho_walk
        $ tmp = cho_speed - redux_pause
        $ renpy.pause(tmp)
        $ cho_chibi_xpos = walk_xpos2
        $ cho_chibi_ypos = walk_ypos2
        hide screen cho_walk
        if loiter:
            $ cho_chibi_status = ""
            call update_cho_chibi_uniform
            show screen cho_stand

    # Walk left to right
    else:
        $ cho_chibi_flip = -1
        show screen cho_walk
        $ tmp = cho_speed - redux_pause
        $ renpy.pause(tmp)
        $ cho_chibi_xpos = walk_xpos2
        $ cho_chibi_ypos = walk_ypos2
        hide screen cho_walk
        if action == "leave":
            call play_sound("door")
            with d3
            pause.3
            $ cho_chibi_flip = 1
        else:
            if loiter:
                $ cho_chibi_status = ""
                call update_cho_chibi_uniform
                show screen cho_stand

    return

label cho_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen cho_stand
        with Dissolve((dissolveTime/10))
    else:
        hide screen cho_stand
    return



### CHO CHIBI SCREENS ###
screen cho_stand():
    tag cho_chibi
    zorder cho_chibi_zorder

    frame:
        style "empty"
        if cho_chibi_animation == "fly":
            at chibi_fly_idle
        add cho_chibi_stand    xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_shoes    xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_top      xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_bottom   xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_robe     xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        if cho_cloth_pile:
            add "characters/chibis/cloth_pile_r.png" xpos cho_pile_xpos ypos cho_pile_ypos

screen cho_walk():
    tag cho_chibi
    zorder cho_chibi_zorder

    frame:
        style "empty"
        if cho_chibi_animation == "fly":
            at chibi_fly(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2, speed=cho_speed)
        else:
            at cho_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2)
        add cho_chibi_walk         xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_shoes        xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_top          xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_bottom       xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_robe         xzoom cho_chibi_flip zoom (1.0/scaleratio)
        if cho_cloth_pile:
            add "characters/chibis/cloth_pile_r.png" xpos cho_pile_xpos ypos cho_pile_ypos


label flying_cho_chibi(flying=True):

    if flying == True:
        $ cho_chibi_stand  = "ch_hem fly_a" # Temporarily
        $ cho_chibi_walk   = "characters/hermione/chibis/broom/shime14.png" # Temporarily

        $ cho_chibi_top       = "characters/cho/chibis/blank.png"
        $ cho_chibi_bottom    = "characters/cho/chibis/blank.png"
        $ cho_chibi_robe      = "characters/cho/chibis/blank.png"

        $ cho_chibi_shoes         = "characters/cho/chibis/blank.png"
        $ cho_chibi_walk_shoes    = "characters/cho/chibis/blank.png"

    elif flying == False:
        call update_cho_chibi_uniform

    return

label update_cho_chibi_uniform:
    $ update_chibi_image("cho")
    return

init python:
    def update_chibi_image(name):
        if name == "cho":
            imagepath = "characters/cho/chibis/"
            animation = "_"+cho_chibi_animation if cho_chibi_animation else ""
            status = "_"+cho_chibi_status if cho_chibi_status else ""
            global cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk
            cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk, cho_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "ch_cho blink", "ch_cho walk", "ch_cho walk_shoes"

            if cho_chibi_animation == "fly":
                cho_chibi_stand = "ch_cho fly_idle"
                cho_chibi_walk = "ch_cho fly"

            if cho_class.get_worn("top"):
                cho_chibi_top = imagepath+"cc_top"+animation+status+".png" if animation else imagepath+"cc_top.png"

            if cho_class.get_worn("bottom"):
                cho_chibi_bottom = imagepath+"cc_bottom"+animation+status+".png" if animation else imagepath+"cc_bottom.png"

            if cho_class.get_worn("robe"):
                cho_chibi_robe = imagepath+"cc_robe"+animation+status+".png" if animation else imagepath+"cc_robe.png"

            if cho_class.get_worn("bottom") or cho_class.get_worn("stockings"):
                if not status == "_move":
                    cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
                else:
                    if animation:
                        cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
            else:
                cho_chibi_shoes = "blank"
        return
