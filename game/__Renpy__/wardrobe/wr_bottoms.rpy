#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_bottom:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_bottom
    #Luna
    if active_girl == "luna":
        jump equip_lun_bottom
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_bottom
    #Susan
    if active_girl == "susan":
        jump equip_sus_bottom


### Equip Bottom ###

label equip_her_bottom:    #useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

    if skirt_choice == h_skirt and bottom_color_choice == h_skirt_color:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    if hermione_action == "hands_behind" or hermione_action == "covering" or hermione_action == "fingering" or hermione_action == "covering_top" or hermione_action == "pinch" or hermione_action == "hands_cuffed" or hermione_action == "milk_breasts":

        $ wardrobe_active = 1
        hide screen hermione_main
        with d3
        ">Hermione is currently posing,... naked.\nWould you like her to get dressed?"
        menu:
            "-Make her get dressed-":
                call h_action("none") 
                hide screen hermione_main

            "-nvm-":
                show screen hermione_main
                with d3
                jump return_to_wardrobe

    if mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            ### Uniform Skirts ###

            #Uniform Skirt Very Long #Done
            if skirt_choice == "uni_skirt_1":
                m "Would you wear your school skirt for me? The very long one." 
                if whoring < 8:
                    call her_main("Of course, [genie_name].","soft","baseL") 
                    call her_main("Let me go and change real quick.","base","base") 
                elif whoring < 11:
                    call her_main("Alright... sure, why not.","base","down") 
                    call her_main("Let me go and change real quick.","base","base") 
                elif whoring < 20:
                    call her_main("Are you sure, [genie_name]?","disgust","down_raised") 
                    call her_main("That thing looks rather plain...","open","closed") 
                    call her_main("I would much rather wear one a bit shorter!","angry","wink") 
                    m "No, [hermione_name]. Wear the long one..."
                    call her_main("Ugh... Fine.","disgust","down_raised") 
                    call her_main("Let me just change it.","annoyed","annoyed") 
                else: #20+
                    call her_main("Are you serious?","angry","wink") 
                    call her_main("That thing is soooooo ugly!","annoyed","ahegao") 
                    call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!","disgust","narrow") 
                    m "No, [hermione_name]. Wear the long one..."
                    call her_main("Fine... Just let me change it...","disgust","glance") 
                    
            #Uniform Skirt Long #Done
            elif skirt_choice == "uni_skirt_2":
                m "Would you wear your school skirt for me? But make it a bit shorter would you." 
                if 5 <= whoring:
                    if whoring < 8:
                        call her_main("...","annoyed","annoyed") 
                        call her_main("Fine.","open","closed") 
                        call her_main("Let me go and change real quick.","base","base") 
                    elif whoring < 11:
                        call her_main("Sure, why not.","base","down") 
                        call her_main("Let me go and change real quick.","base","base") 
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") 
                        call her_main("Let me just change real quick.","base","glance") 
                    else: #20+
                        call her_main("...that old thing?","annoyed","angryL") 
                        m "Sure, is that a problem?"
                        call her_main("...","annoyed","ahegao") 
                        call her_main("I suppose not...","annoyed","down") 
                        call her_main("It's just so plain!","annoyed","angryL") 
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") 
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                    call her_main("I have to refuse, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Medium Length #Done
            elif skirt_choice == "uni_skirt_3":
                m "Would you wear your school skirt for me? But make it a bit shorter would you." 
                if 8 <= whoring:
                    if whoring < 11:
                        call her_main("Alright... sure, why not.","base","down") 
                        call her_main("Let me go and change real quick.","base","base") 
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") 
                        call her_main("Let me go and change real quick.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(At least it is short enough...)","annoyed","ahegao") 
                        call her_main("OK, [genie_name].","soft","baseL") 
                        call her_main("Let me just change real quick.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") 
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                        call her_main("I have to refuse, [genie_name].","normal","base") 
                    else:
                        call her_main("That's way too short, [genie_name]!","open","closed") 
                        call her_main("I have to refuse!","annoyed","suspicious") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Short #Done
            elif skirt_choice == "uni_skirt_4":
                m "Would you wear your school skirt for me? But make it a bit shorter would you."
                if 14 <= whoring:
                    if whoring < 20:
                        call her_main("Sure, why not.","soft","baseL") 
                        call her_main("Let me change it real quick.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(At least it is short enough...)","annoyed","ahegao") 
                        call her_main("OK, [genie_name].","soft","baseL") 
                        call her_main("Let me just change real quick.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") 
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                        call her_main("I have to refuse, [genie_name].","normal","base") 
                    else:
                        call her_main("That's way too short, [genie_name]!","open","closed") 
                        call her_main("I have to refuse!","annoyed","suspicious") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 14."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Shortest #Done
            elif skirt_choice == "uni_skirt_5":
                m "Would you wear your school skirt for me? The shortest one you have."  
                if 17 <= whoring:
                    if whoring < 23:
                        call her_main("Of course, [genie_name].","soft","baseL") 
                        call her_main("Let me just change real quick.","base","glance") 
                    else: #23+
                        call her_main("(That old thing?)","annoyed","down") 
                        call her_main("Can't I wear something a little shorter?","open","baseL",cheeks="blush") 
                        m "I don't think they make anything shorter."
                        call her_main("I guess This will just have to do then...","open","ahegao_raised",cheeks="blush") 
                        call her_main("Let me go change...","base","ahegao_raised",cheeks="blush") 
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") 
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                        call her_main("I have to refuse, [genie_name].","normal","base") 
                    else:
                        call her_main("How... How short?!","shock","wide") 
                        call her_main("Is that another one of your silly jokes, [genie_name]?","angry","worried") 
                        call her_main("No, please, don't tell me.","open","closed") 
                        call her_main("I don't even want to know...","annoyed","worriedL") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Gryffindor #Done
            elif skirt_choice == "uni_skirt_cheer_gryff":
                m "Could you wear your cheerleader skirt for me?"
                if 5 <= whoring:
                    if whoring < 11:
                        call her_main("Of course, [genie_name]!","soft","baseL",cheeks="blush") 
                        call her_main("Let me go change.","base","base") 
                    else:
                        call her_main("Alright, [genie_name]!","soft","base") 
                        call her_main("Let me just change it.","base","glance") 
                else:
                    call her_main("I don't know, [genie_name].","annoyed","down") 
                    call her_main("I'm not the cheerleader type!","angry","wink") 
                    call her_main("While I like the idea of supporting my house in Quidditch...","open","closed") 
                    call her_main("My priority is to secure this years house-cup instead!","open","baseL") 
                    call her_main("I have to refuse, [genie_name].","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Slytherin #Done
            elif skirt_choice == "uni_skirt_cheer" or skirt_choice == "uni_skirt_cheer_skimpy":
                if bottom_color_choice == "green" or bottom_color_choice == "blue" or bottom_color_choice == "yellow":
                    m "Would you wear this cheerleader skirt for me?" 
                    if 11 <= whoring:
                        if whoring < 14:
                            if bottom_color_choice == "green":
                                call her_main("But [genie_name], that's for Slytherins!","angry","wink") 
                            if bottom_color_choice == "blue":
                                call her_main("But [genie_name], that's for Ravenclaws!","angry","wink") 
                            if bottom_color_choice == "yellow":
                                call her_main("But [genie_name], that's for Hufflepuffs!","angry","wink") 
                            m "And?"
                            call her_main("I'm a Gryffindor!","annoyed","annoyed") 
                            if bottom_color_choice == "green":
                                call her_main("(A muggle-born on top of that.)","disgust","down_raised") 
                            call her_main("I can't wear this!","open","worriedCl") 
                            m "Why not?"
                            call her_main("I've already told you, I'm a Gryffindor!","annoyed","ahegao") 
                            m "(...)"
                            g9 "(I've got an idea!)"
                            g4 "[hermione_name], I completely forgot to mention!"
                            m "As the top student of Gryffingdoor, you were selected to switch places with a fellow student form another house!"
                            m "As a form of bonding method... To bring the four houses closer together!"
                            call her_main("But... the Hogwarts houses are supposed to compete with each other! Especially in a sport activity such as Quidditch!","disgust","glance") 
                            g4 "Nonsense! All it does is cause a hateful and unhealthy relationship between students!"
                            if bottom_color_choice == "green":
                                m "Especially Gryffindor and Slytherin!"
                                m "I mean, do you like being called a mudblood every day by them?"
                                call her_main("No, [genie_name].","angry","wink") 
                                m "Or when they call you a slut..."
                                g4 "Or a whore!"
                                g9 "Or bitch!"
                                g4 "Or... a whore!"
                                g4 "Or--"
                                call her_main("I get your point, [genie_name]!!!","scream","worriedCl",cheeks="blush") 
                            m "I'm giving you an opportunity to better your relationship with them!"
                            m "Now are you going to wear this for me or not?..."
                            call her_main("(...)","annoyed","angryL") 
                            call her_main("Fine, [genie_name]... Let me just put it on.","annoyed","annoyed") 
                        elif whoring < 20:
                            call her_main("Fine, [genie_name].","soft","ahegao") 
                            call her_main("(How humiliating to wear this as a Gryffindor...)","disgust","narrow") 
                            call her_main("Let me just change it.","soft","baseL") 
                        else: #20+
                            if bottom_color_choice == "green":
                                call her_main("Of course I will wear it!","smile","angry") 
                                call her_main("Gimme-Gimme--Gimme!!!","smile","happyCl") 
                                call her_main("(I'm definitely going to root for them on the next game!)","soft","baseL",cheeks="blush") 
                                call her_main("(If they are winning I won't have to wear this thing long anyway!)","base","glance") 
                                call her_main("Whoooo, go Slytherin!","smile","happyCl") 
                            else:
                                call her_main("If I really have to...","annoyed","annoyed") 
                                call her_main("Let me just change it.","soft","baseL") 
                    else:
                        if bottom_color_choice == "green":
                            call her_main("In green?","shock","wide") 
                        if bottom_color_choice == "blue":
                            call her_main("In blue?","shock","wide") 
                        if bottom_color_choice == "yellow":
                            call her_main("In yellow?","shock","wide") 
                        call her_main("Are you serious, [genie_name]?","angry","angry") 
                        call her_main("Are you sure you didn't just pick the wrong colour for me?","annoyed","suspicious") 
                        if bottom_color_choice == "green":
                            m "(Something tells me she doesn't want to wear green stuff.)"
                            m "(Is she allergic to grasshoppers or something?)"
                        else:
                            m "(Could have sworn I picked the right color for her...)"
                        m "Forget about it, girl."
                        call her_main("I will!","annoyed","annoyed") 
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe

                else: #Gryffindor #Base color and red color.
                    m "Could you wear your cheerleader skirt for me?"
                    if 5 <= whoring:
                        if whoring < 11:
                            call her_main("Of course, [genie_name]!","soft","baseL",cheeks="blush") 
                            call her_main("Let me go change.","base","base") 
                        else:
                            call her_main("Alright, [genie_name]!","soft","base") 
                            call her_main("Let me just change it.","base","glance") 
                    else:
                        call her_main("I don't know, [genie_name].","annoyed","down") 
                        call her_main("I'm not the cheerleader type!","angry","wink") 
                        call her_main("While I like the idea of supporting my house in Quidditch...","open","closed") 
                        call her_main("My priority is to secure this years house-cup instead!","open","baseL") 
                        call her_main("I have to refuse, [genie_name].","soft","base") 
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 5."
                        jump return_to_wardrobe
                    
                    
            ### Uniform Skirts Low ###

            #Uniform Skirt Low Very Long #Done
            elif skirt_choice == "uni_skirt_1_low":
                m "Would you wear your school skirt for me? The very long one. But pull it down a bit." 
                if 8 <= whoring:
                    if whoring < 11:
                        call her_main("Alright... sure, why not.","base","down") 
                        call her_main("Let me go and change real quick.","base","base") 
                    elif whoring < 20:
                        call her_main("Are you sure, [genie_name]?","disgust","down_raised") 
                        call her_main("That thing looks rather plain...","open","closed") 
                        call her_main("I would much rather wear one a bit shorter!","angry","wink") 
                        m "No, [hermione_name]. Wear the long one..."
                        call her_main("Ugh... Fine.","disgust","down_raised") 
                        call her_main("Let me just change it.","annoyed","annoyed") 
                    else: #20+
                        call her_main("Are you serious?","angry","wink") 
                        call her_main("That thing is soooooo ugly!","annoyed","ahegao") 
                        call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!","disgust","narrow") 
                        m "No, [hermione_name]. Wear the long one..."
                        call her_main("Fine... Just let me change it...","disgust","glance") 
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","shock","wide") 
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","angry","angry") 
                        call her_main("How can you even suggest such a thing!","angry","worriedCl") 
                        call her_main("(disgusting old fool...)","annoyed","annoyed") 
                    else:
                        call her_main("No, [genie_name].","open","closed") 
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","annoyed","annoyed") 
                        call her_main("My panties would be visible...","disgust","down_raised") 
                        m "That's kind of the point, [hermione_name]."
                        call her_main("I refuse!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Medium Length #Done
            elif skirt_choice == "uni_skirt_2_low":
                m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                if 11 <= whoring:
                    if whoring < 14:
                        call her_main("Alright... sure, why not.","base","down") 
                        call her_main("Let me go and change real quick.","base","base") 
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") 
                        call her_main("Let me go and change real quick.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(At least it is short enough...)","annoyed","ahegao") 
                        call her_main("OK, [genie_name].","soft","baseL") 
                        call her_main("Let me just change real quick.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","shock","wide") 
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","angry","angry") 
                        call her_main("How can you even suggest such a thing!","angry","worriedCl") 
                        call her_main("(disgusting old fool...)","annoyed","annoyed") 
                    else:
                        call her_main("No, [genie_name].","open","closed") 
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","annoyed","annoyed") 
                        call her_main("My panties would be visible...","disgust","down_raised") 
                        m "That's kind of the point, [hermione_name]."
                        call her_main("Besides, the length you suggested is way too short!","open","closed") 
                        call her_main("I refuse!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Short #Done
            elif skirt_choice == "uni_skirt_3_low":
                m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                if 17 <= whoring: 
                    if whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") 
                        call her_main("Let me go and change real quick.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(At least it is short enough...)","annoyed","ahegao") 
                        call her_main("OK, [genie_name].","soft","baseL") 
                        call her_main("Let me just change real quick.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","shock","wide") 
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","angry","angry") 
                        call her_main("How can you even suggest such a thing!","angry","worriedCl") 
                        call her_main("(disgusting old fool...)","annoyed","annoyed") 
                    else:
                        call her_main("No, [genie_name].","open","closed") 
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","annoyed","annoyed") 
                        call her_main("My panties would be visible...","disgust","down_raised") 
                        m "That's kind of the point, [hermione_name]."
                        call her_main("Besides, the length you suggested is way too short!","open","closed") 
                        call her_main("I refuse!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Shortest (Micro Skirt) #Not implemented.
            elif skirt_choice == "uni_skirt_4_low":
                m "Could you wear this school skirt for me?" 
                ">You hand her the micro skirt." 
                if 20 <= whoring:
                   call her_main("","base","base") 
                else:
                    call her_main("","base","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe


            ### Skirts ###
                    
            #Belted Mini Skirt #Done
            elif skirt_choice == "skirt_belted_mini":
                m "Could you wear this skirt I bought you?" 
                if 8 <= whoring: 
                    if whoring < 14:
                        call her_main("(It's so short!)","disgust","down_raised") 
                        call her_main("(...)","annoyed","angryL") 
                        call her_main("Ok, [genie_name]... I will wear it.","open","closed") 
                        m "Really?"
                        call her_main("Give me the skirt before I change my mind!","annoyed","annoyed") 
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","soft","baseL") 
                        call her_main("Let me just put it on.","base","glance") 
                    else: #23+
                        call her_main("Alright, [genie_name].","smile","happyCl") 
                        call her_main("Give it to me!","open_tongue","ahegao_raised",cheeks="blush") 
                        g4 "(!!!)"
                        call her_main("The skirt I mean.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") 
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                        call her_main("I have to refuse, [genie_name].","normal","base") 
                    else: 
                        call her_main("Absolutely not, [genie_name]!","scream","worriedCl") 
                        call her_main("I'm not going to wear a skirt that short!","angry","angry") 
                        call her_main("(What is he thinking?...)","angry","worried") 
                        call her_main("I refuse","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Belted Micro Skirt #Done
            elif skirt_choice == "skirt_belted_micro":
                m "Could you wear this skirt I bought you?"
                if 17 <= whoring: 
                    if whoring < 23: 
                        call her_main("(Oh wow, it's so short!)","disgust","down_raised") 
                        call her_main("(Everyone will be able to see my ass in this...)","soft","ahegao") 
                        call her_main("(...)","annoyed","angryL") 
                        call her_main("I will wear it!.","open","closed") 
                        m "Really?"
                        call her_main("Sure... It's short enough","soft","baseL") 
                        call her_main("Or would you say this is too inappropriate to wear in this school?","base","glance") 
                        g4 "Grrrrr--... You have my approval!"
                        call her_main("Thank you, [genie_name].","soft","baseL") 
                    else: #23+
                        call her_main("Alright, [genie_name].","smile","happyCl") 
                        call her_main("Give it to me!","open_tongue","ahegao_raised",cheeks="blush") 
                        g4 "(!!!)"
                        call her_main("The skirt I mean.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") 
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                        call her_main("I have to refuse, [genie_name].","normal","base") 
                    else: 
                        call her_main("Absolutely not, [genie_name]!","scream","worriedCl") 
                        call her_main("I'm not going to wear a skirt that short!","angry","angry") 
                        call her_main("(What is he thinking?...)","angry","worried") 
                        call her_main("I refuse","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe


            ### Pants ###
                    
            #Pants Jeans Long #Done
            elif skirt_choice == "pants_jeans_long":
                m "Could you wear these pants for me?" 
                if 2 <= whoring: 
                    if whoring < 5:
                        call her_main("[genie_name], those are jeans!","angry","wink") 
                        m "... yes?"
                        call her_main("Muggle pants!","disgust","down_raised",cheeks="blush") 
                        call her_main("Girls are supposed to wear skirts here at Hogwarts!","open","closed") 
                        call her_main("At all times! No exceptions!","annoyed","worriedL") 
                        m "That's a very sexist thing to say, don't you think?"
                        call her_main("I-- uhm...","angry","wink") 
                        call her_main("(Crap,... he is right...)","disgust","down_raised") 
                        call her_main("(Hmm... might as well wear them... They don't look too bad...)","clench","down_raised") 
                        m "(...)"
                        g4 "(How ridiculous!... How can she call those blankets around her hips skirts...)"
                        g9 "(At least I get a nice view of her ass in those pants!)"
                        call her_main("Fine, [genie_name].","annoyed","ahegao") 
                        call her_main("I will wear them.","soft","base") 
                    elif whoring < 8:
                        call her_main("Sure, [genie_name].","soft","baseL") 
                        call her_main("Let me go change.","base","base") 
                    else:
                        call her_main("But they are so long, [genie_name]!","annoyed","ahegao") 
                        call her_main("I can't even show off my legs in those!","annoyed","angry") 
                        call her_main("(They make my ass look amazing though...)","disgust","down_raised") 
                        call her_main("(Now that I think about it...)","annoyed","ahegao") 
                        call her_main("Fine, I will wear them.","base","glance") 
                else:
                    call her_main("I'm sorry, [genie_name].","soft","baseL") 
                    call her_main("But pants are not part of Hogwarts' school attire.","open","closed") 
                    call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") 
                    call her_main("I have to refuse!","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Pants Jeans Short #Done
            elif skirt_choice == "pants_jeans_short":
                m "Could you wear those pants for me?" 
                if 11 <= whoring:
                    if whoring < 20:
                        call her_main("Sure, [genie_name].","soft","baseL") 
                        call her_main("Let me go change.","base","base") 
                    else: #20+
                        call her_main("Alright, [genie_name].","soft","baseL") 
                        call her_main("(They are sooo tight,... I can barely even fit my ass into them...)","soft","ahegao") 
                        call her_main("Let me put them on for you.","base","glance") 
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") 
                        call her_main("But pants are not part of Hogwarts' school attire.","open","closed") 
                        call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") 
                        call her_main("I have to refuse!","normal","base") 
                    elif whoring < 5: 
                        call her_main("... What are these?","annoyed","suspicious") 
                        m "Pants..?"
                        call her_main("...","annoyed","annoyed") 
                        call her_main("These aren't pants!","angry","worriedCl") 
                        m "What are they then?"
                        call her_main("Underwear!","shock","wide") 
                        m "So you're not going to wear them?"
                        call her_main("NO!","scream","worriedCl") 
                        call her_main("...","angry","angry") 
                    else: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") 
                        call her_main("But I don't think I should wear pants like those on school grounds...","open","closed") 
                        call her_main("(They look really nice though...)","base","down") 
                        call her_main("(Maybe next time...)","base","baseL") 
                        call her_main("I have to refuse.","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Pants Retro Shorts #Done
            elif skirt_choice == "pants_retro_shorts":
                m "I want you to wear these pants for me." 
                if 17 <= whoring: 
                    if whoring < 20:
                        call her_main("(These pants look so short...)","disgust","down_raised") 
                        call her_main("(My ass is gonna be on display the whole time in those...)","open_tongue","ahegao_raised",cheeks="blush") 
                        call her_main("Alright, [genie_name].","smile","happyCl") 
                        call her_main("Let me just change it.","base","glance") 
                    else: #20+
                        call her_main("Alright, [genie_name].","soft","baseL") 
                        call her_main("I bet you love how my ass looks in those.","smile","glance") 
                        g9 "You bet I do!"
                        call her_main("Glad to hear that, [genie_name].","base","glance") 
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") 
                        call her_main("But pants are not part of Hogwarts' school attire.","open","closed") 
                        call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") 
                        call her_main("I have to refuse!","normal","base") 
                    elif whoring < 11: 
                        call her_main("No, [genie_name].","open","worriedCl") 
                        call her_main("I will not wear pants that short here in school!","angry","worried") 
                        call her_main("(What is he thinking?!...)","annoyed","angryL") 
                    else: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") 
                        call her_main("But I don't think I should wear pants like those on school grounds...","open","closed") 
                        call her_main("(They look really nice though...)","base","down") 
                        call her_main("(Maybe next time...)","base","baseL") 
                        call her_main("I have to refuse.","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Pants Rocker Shorts #Done
            elif skirt_choice == "pants_rocker":
                m "I want you to wear these pants for me." 
                if 20 <= whoring: 
                    if whoring < 23:
                        call her_main("(These pants are so short...)","disgust","down_raised") 
                        call her_main("(I'm such a pervert!)","open_tongue","ahegao_raised",cheeks="blush") 
                        call her_main("Alright, [genie_name].","smile","happyCl") 
                        call her_main("Let me just change it.","base","glance") 
                    else:
                        call her_main("Alright, [genie_name].","soft","baseL") 
                        call her_main("I bet you love how my ass looks in those.","smile","glance") 
                        g9 "You bet I do!"
                        call her_main("Glad to hear that, [genie_name].","base","glance") 
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") 
                        call her_main("But pants are not part of Hogwarts' school attire.","open","closed") 
                        call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") 
                        call her_main("I have to refuse!","normal","base") 
                    elif whoring < 5: 
                        call her_main("What?!...","angry","angry") 
                        call her_main("What?!... What is this?","angry","angry",emote="01") 
                        m "I just said those are--"
                        call her_main("[genie_name]!","shock","wide") 
                        call her_main("You can't just hand underwear to your students!","angry","worried") 
                        m "Underwear?"
                        call her_main("Yes, underwear! Panties!","open","worriedCl") 
                        call her_main("What else can you possibly call this?","annoyed","annoyed") 
                        m "That's a perfectly fine pair of jeans!"
                        m "No need to make such a fuss about them!... Just put them on!"
                        call her_main("No I will not!","scream","worriedCl") 
                        call her_main("(Not in a million years...)","angry","angry") 
                    elif whoring < 11: 
                        call her_main("I'm sorry, [genie_name].","open","worriedCl") 
                        call her_main("But I will not wear pants that short on school grounds!","angry","worried") 
                        call her_main("(What is he thinking?!...)","annoyed","angryL") 
                    else: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") 
                        call her_main("But I don't think I should wear pants like those on school grounds...","open","closed") 
                        call her_main("(They look really nice though...)","base","down") 
                        call her_main("(Maybe next time...)","base","baseL") 
                        call her_main("I have to refuse.","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
            else:
                pass

            hide screen hermione_main
            with d3

            pause.5

            call set_h_bottom(skirt_choice,bottom_color_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if skirt_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">She won't wear that skirt just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if skirt_choice == "uni_skirt_2" and whoring < 5: #no vest
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3" and whoring < 8: #no tie
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_4" and whoring < 14: #cleavage
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 14."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_5" and whoring < 17: #crop top
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe

            if skirt_choice == "uni_top_cheer" and whoring < 5:
                if (bottom_color_choice == "green" or bottom_color_choice == "dark_green" or bottom_color_choice == "blue" or bottom_color_choice == "dark_blue" or bottom_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that skirt just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    ">She won't wear that skirt just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe

            if skirt_choice == "uni_top_cheer_skimpy" and whoring < 8:
                if (bottom_color_choice == "green" or bottom_color_choice == "dark_green" or bottom_color_choice == "blue" or bottom_color_choice == "dark_blue" or bottom_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that skirt just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    ">She won't wear that skirt just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe


            #Uniform Low
            if skirt_choice == "uni_skirt_1_low" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_2_low" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3_low" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            #if skirt_choice == "uni_skirt_4_low" and whoring < 20:
            #    ">She won't wear that top just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Try again at whoring level 20."
            #    jump return_to_wardrobe

            #Skirts
            if skirt_choice == "skirt_belted_mini" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "skirt_belted_micro" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe

            #Pants
            if skirt_choice == "pants_jeans_long" and whoring < 2:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if skirt_choice == "pants_jeans_short" and whoring < 11:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "pants_retro_shorts" and whoring < 17:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if skirt_choice == "pants_rocker" and whoring < 20:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe



            else:
                pass

            $ wardrobe_active = 1
            call set_h_bottom(skirt_choice,bottom_color_choice) 
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe



### Equip Astoria's Bottom ###
label equip_ast_bottom: 
    call set_ast_bottom(skirt_choice) 
        
    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Bottom ###
label equip_sus_bottom:
    call set_sus_bottom(skirt_choice) 

    hide screen wardrobe
    call screen wardrobe

