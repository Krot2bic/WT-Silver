

label summon_luna:

    call play_sound("door")

    call lun_chibi("stand","mid","base")

    if luna_reverted:
        call lun_main("Hello, [lun_genie_name]!","normal","wink","base","mid",xpos="base",ypos="base")
    elif lun_dom >= lun_sub:
        if lun_dom >= 4:
            call lun_main("[lun_genie_name]...","normal","suspicious","angry","R",xpos="base",ypos="base")
        else:
            call lun_main("[lun_genie_name]...","upset","mad","mad","R",xpos="base",ypos="base")
    else:
        call lun_main("[lun_genie_name]...","normal","base","sad","mid",xpos="base",ypos="base")

    label luna_requests:

    $ hide_transitions = False
    $ luna_busy = True
    $ gave_luna_gift = True #Remove when adding gift texts!

    menu:

        # Talk
        #"-Chit Chat-":
        #    call luna_chitchat
        #    jump luna_requests


        # Personal Favors
        "-favours-" if not luna_reverted:
            if gold <= 0:
                m "I don't have any gold..."
                jump luna_requests
            jump luna_favor_menu

        "-Personal Favours-" if luna_reverted and ll_favor_list != []: # List is not empty.
            jump luna_favor_menu

        # Wardrobe
        "-Wardrobe-": # if luna_wardrobe_unlocked:
            $ active_girl = "luna"
            $ ll_quirky_muggle_ITEM.unlocked = True #Temporary unlock. Will be a random clothing event eventually.

            call load_luna_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            call lun_chibi("stand","wardrobe","base")

            $ hide_transitions = True
            call lun_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        #"{color=#858585}-Hidden-{/color}" if not luna_wardrobe_unlocked:
        #    call nar(">You haven't unlocked this feature yet.")
        #    jump luna_requests


        # Gifts
        "-Gifts-" if not gave_luna_gift:
            $ current_category = None
            jump luna_gift_menu

        "{color=#858585}-Gifts-{/color}" if gave_luna_gift:
            "Not yet added. WIP!"
            #m "I already gave her a gift today. Don't want to spoil her too much..."
            jump luna_requests


        # Dismiss
        "-Never mind-":

            if luna_reverted:
                call lun_main("Oh... alright then... Bye, [lun_genie_name]!","normal","wink","sad","down",xpos="base",ypos="base")

            jump end_luna_event


# Luna Favor Menu
label luna_favor_menu:

if not luna_reverted:
    menu:
        "-Talk to me-":
            jump luna_favour_1
        "-Sit on my lap-" if lun_whoring >= 3:
            jump luna_favour_2
        "-Strip for me-" if lun_whoring >= 5:
            jump luna_favour_3
        "-Touch me-" if lun_whoring >= 9:
            if lun_whoring == 9:
                jump luna_reversion_event
            jump luna_favour_4
        "-Touch me with Hermione-" if lun_whoring >= 11:
            jump luna_favour_5
        "-Suck it-" if lun_whoring >= 14:
            jump luna_favour_6
        "-Sex-" if lun_whoring >= 17:
            jump luna_favour_7

        "-Never mind-":
            jump luna_requests
else:
    call update_luna_favors

    python:
        menu_choices = []
        for i in ll_favor_list:
            if i in []: # Not in the game yet.
                menu_choices.append(("{color=#858585}-Not Available-{/color}","na"))
            #elif i.tier > lun_whoring:
            #    menu_choices.append(("{color=#858585}-Not ready-{/color}","vague"))
            else:
                menu_choices.append((i.getMenuText(),i.start_label))
        menu_choices.append(("-Never mind-", "nvm"))
        result = custom_menu(menu_choices)
    if result == "nvm":
        jump luna_requests
    elif result == "vague":
        call favor_not_ready
        jump luna_requests
    elif result == "na":
        call not_available
        jump luna_requests
    else:
        $ renpy.jump(result)

label update_luna_favors:
    python:
        for i in ll_favor_list:
            if i.tier != lun_tier and i.max_tiers >= lun_tier:
                i.tier = lun_tier

    return
