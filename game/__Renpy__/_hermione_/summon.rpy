

label summon_hermione:

    call load_hermione_clothing_saves 

    call play_sound("door") #Sound of a door opening.

    ### RANDOM CLOTHING EVENTS ###
    call hermione_door_event 

    call update_her_uniform 

    call her_chibi("stand","mid","base") 

    if mad >= 1:

        if mad >=1 and mad < 3:
            call her_main("","normal","base",xpos="base",ypos="base") 
            ">Looks like Hermione is still a little upset with you..."
        elif mad >=3 and mad < 10:
            call her_main("","normal","base",xpos="base",ypos="base") 
            ">Hermione is upset with you."
        elif mad >=10 and mad < 20:
            call her_main("","annoyed","frown",xpos="base",ypos="base") 
            ">Hermione is very upset with you."
        elif mad >=20 and mad < 40:
            call her_main("","angry","angry",xpos="base",ypos="base") 
            ">Hermione is mad at you."
        elif mad >=40 and mad < 50:
            call her_main("","angry","angry",xpos="base",ypos="base") 
            ">Hermione is very mad at you."
        elif mad >=50 and mad < 60:
            call her_main("","angry","angry",xpos="base",ypos="base") 
            ">Hermione is furious at you."
        elif mad >=60:
            call her_main("","angry","angry",xpos="base",ypos="base") 
            ">Hermione hates your guts."

    else:
        if not hermione_door_event_happened:
            call her_main("Yes, [genie_name]?","base","base",xpos="base",ypos="base") 
        else:
            call her_main("...","base","base",xpos="base",ypos="base") 

    label day_time_requests:

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    $ wardrobe_active = False

    menu:
        "-Ask for a new student-" if hat_known and not luna_known:
            call luna_init 
            $ luna_known = True
            jump hat_intro_2
        "-Talk-":
            if not chitchated_with_her:
                jump hermione_talk_branches
                label hermione_talk_branches_return:
                if mad <= 7:
                    $ chitchated_with_her = True 
                    call chit_chat 
                    jump hermione_talk
                else:
                    her "I have nothing to say to you sir..."    
                    jump day_time_requests
            else:
                jump hermione_talk
        "-Tutoring-" if not daytime and v_tutoring < 14: #13 is last level.
            if mad >=1 and mad < 3:
                her "I'm sorry, maybe tomorrow..."
                jump day_time_requests
            elif mad >=3 and mad < 10:
                her "I am not in the mood today..."
                jump day_time_requests
            elif mad >= 10 and mad < 20:
                her "Absolutely not, [genie_name]"
                her "I {i}might{/i} consider it once you've said sorry"
                jump day_time_requests
                # Question: What to do between 9 and 20? Only "jump l_tutoring_check"?
            elif mad >=20:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump day_time_requests
            else:
                jump l_tutoring_check
                    
        "-Buy sexual favours-" if buying_favors_from_hermione_unlocked:
            if mad >=1 and mad < 3:
                her "I'm sorry, [genie_name], Maybe some other time..."
                jump day_time_requests
            elif mad >=  3 and mad < 10:
                her "I don't feel like it today..."
                her "Maybe in a couple of days..."
                jump day_time_requests
            elif mad >= 10 and mad < 20:
                her "No thank you...."
                jump day_time_requests
            elif mad >= 20 and mad < 30:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump day_time_requests
            elif mad >= 30 and mad < 40:
                her "You can't be serious!"
                jump day_time_requests
            elif mad >= 40:
                her "Is this some twisted joke to you, sir?!"
                her "After what you did I don't feel like doing this ever again!"
                jump day_time_requests
            else:
                jump silver_requests
                    
        "-Inventory-":
            $ active_girl = "hermione"

            call load_hermione_clothing_saves 

            call reset_wardrobe_vars 
            call update_wr_color_list 

            $ wardrobe_active = 1 #True
            call her_main("","","",xpos="wardrobe",ypos="base") 
            call screen wardrobe
                        
        #"-Ending \"Your whore\"-":
        #    $ public_whore_ending = False
        #    jump your_whore
                        
        #"-Ending \"Public whore\"-":
        #    $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
        #    jump your_whore
                    
        "-Dismiss her-":
            if daytime:
                if mad >=3 and mad < 7:
                    her "..............................."
                elif mad >=7:
                    her "*Humph!*..."
                else:
                    her "Oh, alright. I will go to classes then."
            else:
                if mad >=3 and mad < 7:
                    her "..............................."
                elif mad >=7:
                    her "Tch..."
                else:
                    her "Oh, alright. I will go to bed then."

            hide screen bld1
            hide screen blktone 

            hide screen hermione_main
            hide screen hermione_blink #Hermione stands still.

            hide screen ctc
            with d3

            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ menu_y = 0.5 #Menu position is back to default. (Center).
                        
            if daytime:
                $ hermione_takes_classes = True
                jump day_main_menu
            else:
                $ hermione_sleeping = True
                jump night_main_menu
                    
                    

label hermione_talk: 
    menu:           
        "-Working-":
            label working_menu:
            menu:
                "-Work as a maid-" if daytime and hg_outfits.purchased('hg_maid'):
                    jump job_1

                "-Work as a maid-" if daytime and not hg_outfits.purchased('hg_maid'):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu
                                        
                "{color=#858585}-Work as a maid-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu
                                    
                "-Work as a cheerleader for Gryffindor-" if daytime and hg_outfits.purchased('hg_gryffCheer'):
                     jump job_3

                "-Work as a cheerleader for Gryffindor-" if daytime and not hg_outfits.purchased('hg_gryffCheer'):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu
                                    
                "{color=#858585}-Work as a cheerleader for Gryffindor-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu
                                    
                "-Work as a cheerleader for Slytherin-" if daytime and hg_outfits.purchased('hg_slythCheer'):
                    jump job_4

                "-Work as a cheerleader for Slytherin-" if daytime and not hg_outfits.purchased('hg_slythCheer'):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu
                                    
                "{color=#858585}-Work as a cheerleader for Slytherin-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu
                                          
                "-Never mind-":
                    jump hermione_talk     
                            
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ genie_name = "Sir"
                    jump genie_change
                "-Dumbledore-":
                    $ genie_name = "Dumbledore"
                    jump genie_change
                "-Professor-":
                    $ genie_name = "Professor"
                    jump genie_change
                "-Old man-":
                    $ genie_name = "Old man"
                    jump genie_change
                "-Genie-":
                    if whoring >=5:
                        $ genie_name = "Genie"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-My Lord-":
                    if whoring >=7:
                        $ genie_name = "My Lord"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Darling-":
                    if whoring >=10:
                        $ genie_name = "Darling"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Lord Voldemort-":
                    if whoring >=15:
                        $ genie_name = "Lord Voldemort"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Daddy-":
                    if whoring >=20:
                        $ genie_name = "Daddy"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Master-":
                    if whoring >=20:
                        $ genie_name = "Master"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ genie_name = "Sir"
                        jump genie_change
                    if whoring >=20:
                        $ genie_name = temp_name
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Never mind-":
                    jump hermione_talk
                            
        "-From now on I will refer to you as-":
            menu:
                "-Miss Granger-":
                    $ hermione_name = "Miss Granger"
                    jump hermione_change
                "-Girl-":
                    $ hermione_name = "Girl"
                    jump hermione_change
                "-Good Girl-":
                    if whoring >=5:
                        $ hermione_name = "Good Girl"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slave-":
                    if whoring >=10:
                        $ hermione_name = "Slave"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Princess-":
                    if whoring >=10:
                        $ hermione_name = "Princess"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Whore-":
                    if whoring >=15:
                        $ hermione_name = "Whore"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Little Girl-":
                    if whoring >=15:
                        $ hermione_name = "Little Girl"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slytherin Slut-":
                    if whoring >=18:
                        $ hermione_name = "Slytherin Slut"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Mudblood-":
                    if whoring >=20:
                        $ hermione_name = "Mudblood"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if hermione_name == "":
                        $ hermione_name = "Miss granger"
                    if whoring >=20:
                        $ hermione_name = temp_name
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Never mind-":
                    jump hermione_talk
                            
        "-Never mind":
            jump day_time_requests
                    
                    
label genie_change:
    call her_main("Ok, from now on I'll call you [genie_name].","base","base") 
    jump hermione_talk
    
label genie_change_fail:
    call her_main("I'm not calling you that!","scream","angryCl") 
    jump hermione_talk
    
label hermione_change:
    if whoring >= 20:
        call her_main("You can call me whatever you want, [genie_name]!","base","glance") 
    else:
        call her_main("Sure, [genie_name]. I like that name.","base","base") 
    jump hermione_talk
    
label hermione_change_fail:
    call her_main("I'm not letting you call me that!","scream","angryCl") 
    jump hermione_talk
    