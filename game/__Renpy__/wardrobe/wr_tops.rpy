#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_top:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_top
    #Luna
    if active_girl == "luna":
        jump equip_lun_top
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_top
    #Susan
    if active_girl == "susan":
        jump equip_sus_top


### Equip Hermione's Top ###

label equip_her_top:    

    if top_choice == h_top and top_color_choice == h_top_color:
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

            ### Uniform ###

            #Uniform Top Vest and Tie #Done
            if top_choice == "uni_top_1":
                m "Would you wear your uniform top for me? All of it, vest and tie!" 
                if whoring < 8:
                    call her_main("Of course, [genie_name].","soft","baseL") 
                    call her_main("Let me go and change real quick.","base","base") 
                elif whoring < 14:
                    call her_main("Alright, [genie_name].","smile","happyCl") 
                    call her_main("Let me go and change real quick.","base","glance") 
                elif whoring < 20:
                    call her_main("Are you sure, [genie_name]?","angry","wink") 
                    call her_main("My old school top?","angry","base") 
                    call her_main("You don't even want me to remove my tie or show off my cleavage??","disgust","glance") 
                    m "No, [hermione_name]. No cleavage today."
                    call her_main("(Is he up to something?)","annoyed","suspicious") 
                    call her_main("(Maybe this is a test of some sort...)","disgust","down_raised") 
                    call her_main("OK, let me change it real quick","annoyed","annoyed") 
                else: #20+
                    call her_main("That old thing?","angry","wide") 
                    call her_main("Is this some silly joke, [genie_name]?","angry","angry") 
                    m "..."
                    m "(I don't know. Is it?)"
                    call her_main("This is unacceptable!","scream","worriedCl") 
                    call her_main("It doesn't even show any skin!","angry","down_raised") 
                    m "(...)"
                    call her_main("You are insulting my tits, [genie_name]!!!","soft","base",tears="soft") 
                    g4 "*Gasps* {w=0.9}I would never do that, [hermione_name]!"
                    if one_of_ten == 1:
                        g4 "Your tits are marvelous!"
                    if one_of_ten == 2:
                        g4 "Your tits are magnificent!"
                    if one_of_ten == 3:
                        g4 "Your tits are breathtaking!"
                    if one_of_ten == 4:
                        g4 "Your tits are wonderful!"
                    if one_of_ten == 5:
                        g4 "Your tits are spectacular!"
                    if one_of_ten == 6:
                        g4 "Your tits are sensational!"
                    if one_of_ten == 7:
                        g4 "Your tits are glorious!"
                    if one_of_ten == 8:
                        g4 "Your tits are beautiful!"
                    if one_of_ten == 9:
                        g4 "Your tits are lovely!"
                    if one_of_ten == 10:
                        g4 "Your tits are bananas!"
                    call her_main("And yet you want me to wear those... rags!","annoyed","annoyed") 
                    m "You going to wear it or not?"
                    call her_main("Ugh--Fine, let me change it real quick.","annoyed","baseL") 
                    
            #Uniform Top Tie only #Done
            elif top_choice == "uni_top_2":
                m "Would you wear your uniform top for me? But leave the vest off." 
                if 2 <= whoring:
                    if whoring < 5:
                        call her_main("OK, [genie_name].","base","glance") 
                        call her_main("While I find it inappropriate for a Hogwarts student to not wear their proper school attire at all times,...","open","closed") 
                        call her_main("(And of course half of house Slytherin doesn't even bother to tie their shoes...)","annoyed","angryL") 
                        call her_main("You are the headmaster, after all. You make the rules.","open","closed") 
                        call her_main("Let me just go and change, [genie_name].","base","base") 
                    elif whoring < 11:
                        call her_main("Alright, [genie_name].","soft","baseL") 
                        call her_main("Let me go and change it real quick.","base","base") 
                    elif whoring < 17:
                        call her_main("Sure, [genie_name].","grin","baseL") 
                        call her_main("I will just change it right here if you don't mind.","base","glance") 
                        #g4 "(Baby I don't mind at all!)"
                        #g9 "(Show me those titties!)"
                        # $ wardrobe_strip = True 
                    else: #17+
                        call her_main("Just my school shirt and my tie?","soft","base") 
                        m "Yes, [hermione_name]."
                        call her_main("Do you want me to tie the shirt around my breasts?","open","baseL") 
                        m "No, put it on properly."
                        call her_main("Properly, [genie_name]?","angry","wink") 
                        m "You know, buttons and everything."
                        call her_main("(I completely forgot this shirt even had buttons...)","annoyed","down") 
                        call her_main("Can't I leave these buttons open, [genie_name]?","soft","baseL") 
                        m "I'm afraid not, [hermione_name]."
                        call her_main("(I'm gonna get laughed at for wearing my shirt like this.)","annoyed","ahegao") 
                        call her_main("Fine, let me just change it real quick.","base","baseL") 
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") 
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                    call her_main("I have to refuse, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Uniform Top No Tie #Done
            elif top_choice == "uni_top_3":
                m "Would you wear your uniform top for me? But remove the tie and the vest." 
                if 5 <= whoring: #Gets removed at level 11.
                    call her_main("You better appreciate this, [genie_name].","annoyed","annoyed") 
                    call her_main("Can't believe I'm willing to remove my precious Grffindor tie for you...","angry","angry") 
                    m "It's only a tie, girl!"
                    call her_main("No it is not...","scream","worriedCl") 
                    call her_main("...","annoyed","worriedL") 
                    call her_main("Just let me go and change...","annoyed","base") 
                else:
                    call her_main("No thank you, [genie_name].","open","worriedL") 
                    call her_main("No amount of points will ever convince me to remove my precious Gryffindor tie!","open","closed") 
                    call her_main("It's the single most valuable piece of clothing I possess!","soft","baseL") 
                    m "(Maybe for you girl...)"
                    g9 "(But for me it's your panties!)"
                    call her_main("My tie represents my affiliation and commitment to the house Gryffindor, after all...","soft","base") 
                    m "..."
                    call her_main("Every Gryffindor student knows that--","open","down") 
                    m "(There she goes again, rambling on about her school-house...)"
                    call her_main("...when Godric Gryffindor, the greatest of the four founders of Hogwarts, choose the colours red and gold for his house he...","open","closed") 
                    m "(I don't understand a word she's is saying,... {w=0.9}but she has a lovely accent!)"
                    call her_main("...the golden mane of a lion, which is also our houses emblematic animal,...","smile","happyCl") 
                    m "(Should I just jerk off again while she's talking?)"
                    m "(Probably too late now... {w=0.9}Please tell me she's almost done...)"
                    call her_main("...as can be read about in \"Hogwarts: A History\", which you [genie_name], of course have read a great many times...","open","closed") 
                    m "(...)"
                    call her_main("...it is also important for a student of Hogwarts to--","soft","baseL") 
                    g4 "Enough, girl!"
                    m "Leave your tie on."
                    g4 "(And stop talking!)"
                    call her_main("Very well, [genie_name].","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Top Cleavage #Done
            elif top_choice == "uni_top_4":
                m "Would you wear your uniform top for me? Just the shirt..." 
                g9 "And unbutton some of those buttons! I want you to show some cleavage!" 
                if 8 <= whoring:
                    if whoring < 11:
                        call her_main("(Lets just hope nobody stares at them too much.)","annoyed","down") 
                        call her_main("Fine, [genie_name]. {w=0.9}Let me go change.","open","suspicious") 
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") 
                        call her_main("I will just change it here.","base","glance") 
                        m "Yes, do that, [hermione_name]."
                        g4 "(And show me those tits!)"
                    else: #20+
                        call her_main("(Buttons?...)","base","suspicious") 
                        call her_main("(Oh, he means those.)","base","down") 
                        call her_main("Can't I just tie the shirt around my breasts so I can remove it more easily?","open","closed") 
                        m "Is that really a concern of yours, [hermione_name]"
                        call her_main("Well, yes.","soft","baseL") 
                        call her_main("I like showing them to people!","grin","wink",cheeks="blush") 
                        g4 "You hopeless slut!"
                        call her_main("...","base","glance") 
                        m "Wear your shirt properly, for now."
                        m "If you are in luck, and I change my mind, I will let you know."
                        call her_main("Yes, [genie_name]. {w=0.9}Let me just change it!","soft","baseL") 
                else:
                    if whoring >=2:
                        call her_main("Show some...","open","suspicious") 
                        call her_main("Cleavage?","angry","angry") 
                        call her_main("[genie_name], with all due respect,...","open","closed") 
                        call her_main("I'm not going to walk around school looking like some... {w=0.9}harlot!","angry","angry",emote="01") 
                        call her_main("(What does he think I am? A Slytherin?)","annoyed","angryL") 
                        m "It can greatly boost a women's self-confidence if she's willing to show some--"
                        call her_main("I feel very self-confident just the way am, [genie_name].","open","closed") 
                        call her_main("I definitely refuse.","annoyed","suspicious") 
                    else:
                        call her_main("Whoops.","angry","down_raised") 
                        call her_main("I dropped my wand.","open","down") 
                        call her_main("I'm sorry, [genie_name]. {w=0.9}Let me just pick it up real quick.","open","baseL",cheeks="blush") 
                        hide screen hermione_main
                        with d3
                        ">You are walking on very thin ice here!"
                        call her_main("What was it you wanted from me, [genie_name]?","soft","baseL") 
                        m "(Maybe it's not a good idea to ask her that now.)"
                        m "Never mind, girl."
                        call her_main("OK, [genie_name].","base","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Crop-Top #Done
            elif top_choice == "uni_top_5":
                m "I want you to pull up the two ends of your school top and tie them together around your chest." 
                if 11 <= whoring:
                    if whoring < 14:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","open","closed") 
                        call her_main("Everybody is going to look at my breasts...","annoyed","down") 
                        g9 "I would be concerned if they didn't!"
                        call her_main("Ugh--Fine. {w=0.9}Let me just change it real quick.","soft","angry") 
                    elif whoring < 20:
                        call her_main("Tie my shirt around my breasts?.","open","suspicious") 
                        m "Yes, if you could do that."
                        call her_main("Of course, [genie_name].","grin","angry",cheeks="blush") 
                        call her_main("I will just change right here, if you don't mind.","base","glance") 
                        #m "{w=0.5}.{w=0.5}.{w=0.5}.{w=1.0}!"
                        # $ wardrobe_strip = True 
                    else: #20+
                        call her_main("Of course, [genie_name].","soft","baseL") #soft, baseL
                        call her_main("I love wearing my top like this! It's so handy!","smile","happyCl",emote="06") 
                        call her_main("I can just untie it whenever a Slytherin boy walks past me!","soft","ahegao") 
                        call her_main("Or a Slytherin girl of course! I'm not saying that I'm leaving them out!","smile","happyCl") 
                        m "And what about students of other houses?"
                        call her_main("They too of course!","open","baseL",cheeks="blush") 
                        call her_main("(But not as much, now that I think about it.)","annoyed","ahegao") 
                        call her_main("Let me change my top for you real quick!","grin","baseL") 
                        # $ wardrobe_strip = True 
                else:
                    call her_main("This is just ridiculous!","angry","angry") 
                    call her_main("I'm not walking around school wearing my shirt like that!","annoyed","suspicious") 
                    call her_main("I refuse!","open","worriedL") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Top Vest with Cleavage #Done
            elif top_choice == "uni_top_6":
                m "Would you wear your vest for me? Just the vest. Maybe your shirt beneath it. But don't think about closing any of those buttons!"
                if 8 <= whoring:
                    if whoring < 11:
                        call her_main("Sure, why not.","soft","baseL") 
                        call her_main("Let me just change it.","base","base") 
                    elif whoring < 20:
                        call her_main("Just my vest?","annoyed","down") 
                        call her_main("(At least I get to show off my cleavage.)","annoyed","ahegao") 
                        call her_main("Alright, [genie_name]. I will change it.","base","glance") 
                    else: #20+
                        call her_main("My vest, [genie_name]?","angry","wink") 
                        call her_main("Don't you have anything more fashionable?","annoyed","ahegao") 
                        call her_main("Besides, red and yellow doesn't really suit me.","open","closed") 
                        m "Wear it, or I will have you cover up your tits too!"
                        call her_main("(That would be horrible!)","shock","wide") 
                        call her_main("Yes, [genie_name]. Let me change it for you.","soft","baseL") 
                else:
                    if whoring < 5:
                        call her_main("Just my vest?","base","base") 
                        call her_main("Without my Gryffindor tie?!","shock","wide") 
                        call her_main("Why would I want to do that? I refuse, [genie_name]!","angry","base") 
                    else:
                        call her_main("I'm sorry, [genie_name].","open","closed") 
                        call her_main("But there is no way I will walk around school with...","angry","angry") 
                        call her_main("I will not show off my cleavage, [genie_name]!","open","closed") 
                        call her_main("I have to refuse!","annoyed","baseL") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                   
                    
            #Uniform Top Cheer #Done
            elif top_choice == "uni_top_cheer" or top_choice == "uni_top_cheer_skimpy":
                if top_color_choice == "green" or top_color_choice == "blue" or top_color_choice == "yellow":
                    m "Would you wear this cheerleader skirt for me?" 
                    if 11 <= whoring:
                        if whoring < 14:
                            if top_color_choice == "green":
                                call her_main("But [genie_name], that's for Slytherins!","angry","wink") 
                            if top_color_choice == "blue":
                                call her_main("But [genie_name], that's for Ravenclaws!","angry","wink") 
                            if top_color_choice == "yellow":
                                call her_main("But [genie_name], that's for Hufflepuffs!","angry","wink") 
                            m "And?"
                            call her_main("I'm a Gryffindor!","annoyed","annoyed") 
                            if top_color_choice == "green":
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
                            if top_color_choice == "green":
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
                            if top_color_choice == "green":
                                call her_main("Of course I will wear it!","smile","angry") 
                                call her_main("Gimme-Gimme--Gimme!!!","smile","happyCl") 
                                call her_main("(I'm definitely going to root for them on the next game!)","soft","baseL",cheeks="blush") 
                                call her_main("(If they are winning I won't have to wear this thing long anyway!)","base","glance") 
                                call her_main("Whoooo, go Slytherin!","smile","happyCl") 
                            else:
                                call her_main("If I really have to...","annoyed","annoyed") 
                                call her_main("Let me just change it.","soft","baseL") 
                    else:
                        if top_color_choice == "green":
                            call her_main("In green?","shock","wide") 
                        if top_color_choice == "blue":
                            call her_main("In blue?","shock","wide") 
                        if top_color_choice == "yellow":
                            call her_main("In yellow?","shock","wide") 
                        call her_main("Are you serious, [genie_name]?","angry","angry") 
                        call her_main("Are you sure you didn't just pick the wrong colour for me?","annoyed","suspicious") 
                        if top_color_choice == "green":
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
                    if top_choice == "uni_top_cheer":

                        m "Could you wear your cheerleader attire for me? Just the top."
                        if 5 <= whoring:
                            if whoring < 11:
                                call her_main("Of course, [genie_name]!","soft","baseL",cheeks="blush") 
                                call her_main("Let me go change.","base","base") 
                            elif whoring < 20:
                                call her_main("Alright, [genie_name]!","soft","base") 
                                call her_main("Let me just change it.","base","glance") 
                            else: #20+
                                call her_main("What is this? Is this for boys?","angry","wide") 
                                call her_main("Did you steal this from the Gryffindor mascot, [genie_name]?","angry","angry") 
                                call her_main("Want me to put on that giant lion-head too?","open","worriedL") 
                                m "(A lion-head? Do they have stuff like that here?)"
                                call her_main("You can't be serious, [genie_name]!","open","worriedCl") 
                                m "Wear it, or I will have you go naked!"
                                call her_main("...","shock","wide") 
                                call her_main("(Does he really think of making me do that?)","angry","wink") 
                                call her_main("{size=-5}(How exciting!){/size}","smile","happyCl") 
                                call her_main("I will wear it if I absolutely have to,...","open","closed") 
                                call her_main("{size=-5}Do I?{/size}","angry","wink") 
                                m "Yes."
                                call her_main("Tzzz--Your loss...","angry","angry") 
                        else:
                            call her_main("I don't know, [genie_name].","annoyed","down") 
                            call her_main("I'm not the cheerleader type!","angry","wink") 
                            call her_main("While I like the idea of supporting my house in Quidditch...","open","closed") 
                            call her_main("My priority is to secure this years house-cup instead!","open","baseL") 
                            call her_main("I have to refuse, [genie_name].","soft","base") 
                            if cheats_active or game_difficulty <= 2:
                                ">Try again at whoring level 5."
                            jump return_to_wardrobe

                    if top_choice == "uni_top_cheer_skimpy":
                        m "Could you wear the top from your cheerleader attire for me?"
                        if 8 <= whoring: 
                            g9 "The skimpy one!" 
                            if whoring < 14:
                                call her_main("Sure, [genie_name]!","soft","baseL",cheeks="blush") 
                                call her_main("Let me go change.","base","base") 
                            elif whoring < 23:
                                call her_main("Alright, [genie_name]!","soft","base") 
                                call her_main("Let me just change it.","base","glance") 
                            else: #23+
                                call her_main("The Gryffindor one?","annoyed","suspicious") 
                                call her_main("But Gryffindor isn't even the winning team!","angry","wink") 
                                call her_main("Gryffindor isn't even trying to win!","open","worriedL") 
                                call her_main("(They are so embarrassing...)","annoyed","ahegao") 
                                call her_main("Do I really have to?","angry","wink") 
                                m "Yes, [hermione_name]. Wear the Gryffindor one!"
                                call her_main("Fine, if I have to... Let me just change it.","annoyed","annoyed") 
                        else:
                            if whoring < 3: 
                                g9 "The skimp--" 
                                m "Girl? What are you doing?" 
                                ">You see Hermione eying the piece of cloth." 
                                call her_main("(Thats the schools Quidditch uniform alright, but...)","annoyed","down") 
                                call her_main("(There are so many holes in it...)","disgust","down_raised") 
                                call her_main("(Could it be...!)","soft","wide") 
                                call her_main("[genie_name], do you have a rat problem?","open","closed") 
                                m "A rat problem?"
                                call her_main("Yes, rats! They are everywhere in Hogwarts.","open","worried") 
                                call her_main("And I'm not talking about pet-rats.","disgust","glance") 
                                m "(People here keep rats as their pet?)"
                                call her_main("You should talk with Mr. Filch. He will surely know what to do about it!","open","closed") 
                                call her_main("And throw this away while you're at it. It has holes everywhere!","annoyed","annoyed") 
                            else: 
                                g9 "The skimpy one!" 
                                call her_main("The skimpy one?","shock","wide") 
                                call her_main("Are you out of your mind, [genie_name]?","scream","worriedCl") 
                                call her_main("I'm not going to walk around looking like those... Slytherins!","angry","worried") 
                                m "But it's a Gryffindor uniform!"
                                call her_main("That has nothing to do with it!","angry","angry") 
                                call her_main("(stupid sluts... always distracting our team with their breasts...)","annoyed","annoyed") 
                                call her_main("(Always flashed their tits at our players...)","annoyed","angryL") 
                                call her_main("(I hate those skunks! I will never fall that low.)","angry","angry") 
                                call her_main("I'm not going to wear that, [genie_name]!","annoyed","annoyed") 
                            if cheats_active or game_difficulty <= 2:
                                ">Try again at whoring level 8."
                            jump return_to_wardrobe

        
            ### Muggle ###

            #Muggle Pullover #Done
            elif top_choice == "normal_pullover":
                m "Could you wear this top I bought you?" 
                if 0 <= whoring:
                    if whoring < 5:
                        call her_main("[genie_name], that's a pullover!","angry","wink") 
                        m "... So what?"
                        call her_main("Muggle clothing!","disgust","down_raised",cheeks="blush") 
                        call her_main("Muggle clothes are against the Hogwarts rules for--","open","closed") 
                        m "Proper school attire... Yeah yeah, heard that one a hundred times already..."
                        call her_main("(...)","annoyed","annoyed") #very upset, annoyed
                        m "I'm telling you to wear it. I'm the headmaster, after all."
                        g9 "(I can do shit like that!)"
                        call her_main("Fine... Let me go and put it on...","annoyed","angryL") 
                    elif whoring < 11:
                        call her_main("Alright, [genie_name].","soft","baseL") 
                        call her_main("(I really like the colour...)","base","down") 
                        call her_main("(I probably look really cute in it!)","base","happyCl") 
                        call her_main("Let me put it on, [genie_name].","base","base") 
                    else: #11+
                        call her_main("Sure, [genie_name].","smile","glance") 
                        call her_main("Let me put it on real quick.","base","glance") 
                else:
                    pass

            #Muggle Pullover #Done
            elif top_choice == "normal_pullover_sexy":
                m "Could you wear this pullover I bought you?" 
                if 2 <= whoring:
                    if whoring < 11:
                        call her_main("Very well, [genie_name]. Just let me---","soft","baseL") 
                        m "One second,... I'm almost done..."
                        call her_main("Done, [genie_name]? What are you doing with the--","open","suspicious") 
                        m "Shhh! Be quiet, girl... I have to read the manual."
                        g4 "(Right,... I just have to push here, and pull on this...)"
                        ">A heart shaped hole magically appeared in the fabric!"
                        g9 "(Ah, there is is!)"
                        m "Ok girl, now put it on."
                        call her_main("(What did he just do to that pullover?)","annoyed","suspicious") 
                        call her_main("(Doesn't look any different to me...)","annoyed","down") 
                        call her_main("OK, [genie_name]. Let me put it on.","soft","baseL") 
                    elif whoring < 20:
                        call her_main("You never mentioned that there's a hole in it.","open","down") 
                        call her_main("(Right over my enormous cleavage...)","disgust","down_raised") 
                        m "It's not my fault you never noticed..."
                        call her_main("I can really feel that it's brimming with magic!","base","glance") 
                        call her_main("Maybe to see it you need a certain degree of... sexual awareness, for it to appear...","soft","baseL",cheeks="blush") 
                        m "Oh yes! I think something like that was mentioned in the manual!"
                        call her_main("(...)","disgust","glance") 
                        call her_main("Fine... Let me just put it on.","soft","ahegao") 
                    else: #20+
                        call her_main("Alright, [genie_name].","smile","happyCl") 
                        call her_main("Let me put it on real quick.","base","glance") 
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") 
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                    call her_main("I have to refuse, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe

            #Muggle Sweater #Done
            elif top_choice == "normal_sweater":
                m "Could you wear this top I bought you?" 
                if 2 <= whoring:
                    if whoring < 5:
                        call her_main("[genie_name], that's a sweater!","angry","wink") 
                        m "... So what?"
                        call her_main("Muggle clothing!","disgust","down_raised",cheeks="blush") 
                        call her_main("Muggle clothes are against the Hogwarts rules for--","open","closed") 
                        m "Proper school attire... Yeah yeah, heard that one a hundred times already..."
                        call her_main("(...)","annoyed","annoyed") 
                        m "I'm telling you to wear it. I'm the headmaster, after all."
                        g9 "(I can do shit like that!)"
                        call her_main("Fine... Let me go and put it on...","annoyed","angryL") 
                    elif whoring < 20:
                        call her_main("OK, [genie_name].","soft","baseL") 
                        call her_main("(It does look a lot like one of my old sweaters...)","annoyed","down") 
                        call her_main("Let me put it on.","base","base") 
                    else: #20+
                        call her_main("Sure, [genie_name].","smile","glance") 
                        call her_main("Let me put it on real quick.","base","glance") 
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") 
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                    call her_main("I have to refuse, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe

            #Muggle Waitress Top #Kinda done
            elif top_choice == "normal_waitress_top":
                m "Would you wear this top I bought you." 
                if 8 <= whoring:
                    if whoring < 11:
                        call her_main("Fine, [genie_name].","open","closed") 
                        call her_main("Let me put it on before I change my mind...","annoyed","annoyed") 
                    else: #11+
                        call her_main("Alright, [genie_name].","soft","ahegao") 
                        call her_main("Let me just change it.","base","glance") 
                else:
                    if whoring < 2:
                        call her_main("I'm sorry, [genie_name].","base","base") 
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") 
                        call her_main("I have to refuse, [genie_name].","normal","base") 
                    else: #2-7
                        call her_main("I'm sorry, [genie_name].","open","closed") 
                        call her_main("But don't even think I would wear a top like this in school!","angry","angry") 
                        call her_main("No thanks.","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    

            ### Wicked ###

            #Leather Jacket #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves" or top_choice == "wicked_leather_jacket_sleeveless" or top_choice == "wicked_leather_jacket_sleeves":
                m "Could you wear this leather Jacket for me?"

                if 17 <= whoring: 
                    if whoring < 20:
                        call her_main("You should know, [genie_name].","open","closed") 
                        call her_main("I don't mind wearing this in your office.","open","worriedL") 
                        call her_main("(Or wearing nothing at all most of the time.)","annoyed","annoyed") 
                        call her_main("But wearing something like this in class...","angry","angry") 
                        call her_main("You better appreciate this, [genie_name]!","annoyed","angry") 
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","open","closed") 
                        call her_main("It is a really nice looking jacked, after all...","annoyed","down") 
                        call her_main("Let me just change it.","base","base") 
                    else: #23+
                        call her_main("Of course, [genie_name]!","smile","happyCl") 
                        call her_main("I really love this jacket!","smile","glance") 
                        call her_main("(Maybe I will wear it open a couple of times...)","soft","ahegao") 
                        call her_main("(I want to show the boys my new bra...)","grin","baseL") 
                        call her_main("Let me just put it on real quick.","base","glance") 
                else:
                    if whoring < 5: 
                        call her_main("[genie_name]?!","shock","wide") 
                        call her_main("How can you even suggest something like that to one of your student!","angry","wink") 
                        call her_main("What kind of silly joke is this?","shock","worriedCl") 
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","annoyed","suspicious") 
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif whoring < 11: 
                        call her_main("I can't believe you are asking me this, [genie_name]","angry","angry") 
                        call her_main("A leather jacket?... On me?","angry","worried") 
                        call her_main("Not even a Slytherin would wear something like that!","open","closed") 
                        call her_main("I definitely refuse!","annoyed","annoyed") 
                    else:
                        call her_main("No, [genie_name].","open","closed") 
                        call her_main("Even with all the favours I'm willing to do for you...","open","worriedL") 
                        call her_main("I am not going to wear a jacket like this on school grounds.","annoyed","annoyed") 
                        call her_main("I refuse!","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            #Leather Jacket Open #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves_open" or top_choice == "wicked_leather_jacket_sleeveless_open" or top_choice == "wicked_leather_jacket_sleeves_open": 
                m "Could you wear this leather Jacket for me?"
                g9 "But leave the front open!"
                if 11 <= whoring: 
                    g9 "Those puppies need to breath!"

                if 17 <= whoring: 
                    if whoring < 20:
                        call her_main("You should know, [genie_name].","open","closed") 
                        call her_main("I don't mind wearing this in your office.","open","worriedL") 
                        call her_main("(Or wearing nothing at all most of the time.)","annoyed","annoyed") 
                        call her_main("But wearing something like this in class...","angry","angry") 
                        call her_main("(no way in hell am I going to leave it open once I step out of his office...)","annoyed","ahegao") 
                        call her_main("You better appreciate this, [genie_name]!","angry","angry") 
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","open","closed") 
                        call her_main("It is a really nice looking jacked, after all...","annoyed","down") 
                        call her_main("Just... do you expect me to leave it open the whole time?","angry","wink") 
                        m "Naturally, [hermione_name]."
                        call her_main("With just my bra beneath it?","disgust","narrow") 
                        g9 "You betcha!"
                        call her_main("(Can't believe I'm agreeing to this...)","angry","angry") 
                        call her_main("Fine, [genie_name]. I will wear it open.","annoyed","annoyed") 
                    else: #23+
                        call her_main("Of course, [genie_name].","soft","baseL") 
                        call her_main("Should I wear a bra beneath it, or would you like me to really show them off!?","smile","glance") 
                        m "Uhm..."
                        call her_main("I'm kidding!","smile","happyCl") 
                        call her_main("The other teachers wouldn't allow that sadly.","annoyed","down") 
                        call her_main("(Except for maybe Professor Snape...)","annoyed","ahegao") 
                        call her_main("Let me just put it on real quick.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("[genie_name]?!","shock","wide") 
                        call her_main("How can you even suggest something like that to one of your student!","angry","wink") 
                        call her_main("What kind of silly joke is this?","shock","worriedCl") 
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","annoyed","suspicious") 
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif whoring < 11: 
                        call her_main("I can't believe you are asking me this, [genie_name]","angry","angry") 
                        call her_main("A leather jacket?... On me?","angry","worried") 
                        call her_main("Not even a Slytherin would wear something like that!","open","closed") 
                        call her_main("I definitely refuse!","annoyed","annoyed") 
                    else:
                        call her_main("No, [genie_name].","open","closed") 
                        call her_main("Even with all the favours I'm willing to do for you...","open","worriedL") 
                        call her_main("I am not going to wear a jacket like this on school grounds.","annoyed","annoyed") 
                        call her_main("I refuse!","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            #Rocker Top #Done
            elif top_choice == "wicked_rocker_top":
                if whoring < 5: 
                    m "Could you wear this top--"
                else: 
                    m "Could you wear this top for me?"

                if 20 <= whoring: 
                    if whoring < 23: 
                        call her_main("Sure, why not.","open","closed") 
                        m "really?"
                        call her_main("Yes,... It's just a normal top after all...","soft","baseL") 
                        m "(...)"
                        m "(Am I going crazy?)"
                        call her_main("Just let me change it real quick.","base","glance") 
                    else: #23+
                        call her_main("Of course, [genie_name].","soft","ahegao") 
                        call her_main("I like how much it emphasizes my breasts!","smile","glance") 
                        call her_main("I really do love it!","smile","happyCl") 
                        call her_main("Let me just put it on real quick.","base","glance") 
                else:
                    if whoring < 5: 
                        call her_main("A--...","shock","worriedCl") #Add screen shake and sneeze sound.
                        call her_main("A--Achou!!","angry","worriedCl",cheeks="blush",emote="05") #Add screen shake and sneeze sound.
                        ">Hermione sneezed."
                        call her_main("Ahh,...","silly","ahegao") 
                        call her_main("I'm terribly sorry [genie_name]...","angry","wink") 
                        call her_main("Thank you...","base","happyCl") 
                        ">Hermione grabs the tissue."
                        g4 "(Wait! what tissue?! Not my...)"
                        ">Hermione sneezes into the top."
                        m "(Oh that's just perfect...)"
                        call her_main("I'm sorry sir. What was it you asked me?","soft","baseL") 
                        m "Nothing, girl..."
                    elif whoring < 11: 
                        call her_main("What?... What is this?!","shock","wide") 
                        call her_main("Wizard... Sex?!","scream","angry",emote="01") 
                        call her_main("What is this even supposed to mean?","angry","angry") 
                        m "It's just something the kids say nowadays!"
                        call her_main("It most certainly is not!","annoyed","annoyed") 
                        m "If you say so..."
                        call her_main("Keep this offensive... thing for yourself, [genie_name].","scream","angryCl") 
                        call her_main("I'm not going to wear it!","angry","worried") 
                    else: #11-19
                        call her_main("No, [genie_name]!","open","closed") 
                        call her_main("I'm not going to wear a shirt like this on school grounds!","open","worriedL") 
                        call her_main("What are you even thinking!","angry","angry") 
                        call her_main("I refuse!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe
                    
            
            #Misc #Doesn't have texts yet.
            elif top_choice == "top_banner" and top_color_choice != "green" and top_color_choice != "dark_green":
                if 11 <= whoring:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_ripped_tie_striped":
                if 11 <= whoring:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_tie_striped":
                if 11 <= whoring:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_banner" and (top_color_choice == "green" or top_color_choice == "dark_green"):
                if 17 <= whoring:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
            elif top_choice == "top_fishnets":
                if 20 <= whoring:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_top(top_choice,top_color_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if top_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">She won't wear that top just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if top_choice == "uni_top_2" and whoring < 2: #no vest
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "uni_top_3" and whoring < 5: #no tie
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if top_choice == "uni_top_4" and whoring < 8: #cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "uni_top_5" and whoring < 11: #crop top
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "uni_top_6" and whoring < 8: #vest w/cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe

            if top_choice == "uni_top_cheer":
                if (top_color_choice == "green" or top_color_choice == "dark_green" or top_color_choice == "blue" or top_color_choice == "dark_blue" or top_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    if whoring < 5:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 5."
                        jump return_to_wardrobe

            if top_choice == "uni_top_cheer_skimpy":
                if (top_color_choice == "green" or top_color_choice == "dark_green" or top_color_choice == "blue" or top_color_choice == "dark_blue" or top_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    if whoring < 8:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 8."
                        jump return_to_wardrobe

            #Muggle
            if top_choice == "normal_pullover" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_pullover_sexy" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_sweater" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_waitress_top" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "normal_waitress_top" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Wicked
            if top_choice == "wicked_leather_jacket_short_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_short_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_rocker_top" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe

            #Misc
            if top_choice == "top_banner" and top_color_choice != "green" and top_color_choice != "dark_green" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_ripped_tie_striped" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_tie_striped" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_banner" and (top_color_choice == "green" or top_color_choice == "dark_green") and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "top_fishnets" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe
            else:
                pass

            $ wardrobe_active = 1
            call set_h_top(top_choice,top_color_choice) 
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe

            


### Equip Astoria's Top ###
label equip_ast_top: 
    call set_ast_top(top_choice) 
        
    hide screen wardrobe
    call screen wardrobe
        
### Equip Susan's Top ###
label equip_sus_top:
    call set_sus_top(top_choice) 

    hide screen wardrobe
    call screen wardrobe
        
        



