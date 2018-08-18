label summon_snape:

    call play_sound("door")
    $ menu_x = 0.5
    $ menu_y = 0.5

    call sna_chibi("stand","mid","base")

    call sna_main("Yes, what is it?","snape_01",xpos="base",ypos="base")

    label snape_ready:
        pass

    menu:
        "-Get a potion-" if whoring > 10:
            hide screen snape_main
            with fade

            sna_[9] "I notice you're making a bit of progress on Miss Granger."
            sna_[21] "I've got some potions here that normally aren't available to students."
            sna_[21] "These might help speed up the process..."
            menu:
                "-Lactantium-" if potion_inv.has("p_milk_potion"):
                    ">You already have a Lactantium potion."
                    jump snape_ready
                "-Lactantium-" if not potion_inv.has("p_milk_potion"):
                    if potion_scene_11_progress < 1:
                        sna_[9] "Ah yes, a unique concoction of mine. I have a bottle on hand at all times."
                        sna_[13] "Just in case..."
                        sna_[18] "Here, take it!"
                        ">Snape quickly pushes the milky potion into your hands."
                        ">Milking potion received!"
                        $ potion_inv.add("p_milk_potion")
                    elif potion_scene_11_progress == 1:
                        sna_[9] "Good work on getting her to take it."
                        sna_[13] "Her breasts did look magnificently full in class."
                        sna_[13] "mmmm, and I think she was even leaking a little..."
                        sna_[20] "Get her to take another!"
                        sna_[18] "Here, I'll even give you a milker for the slut!"
                        ">Snape hands you an odd leather and metal harness."
                        m "What is-"
                        ">Snape quickly pushes another milky potion into your hands."
                        ">Milking potion received!"
                        sna_[12] "Don't worry about it, just get her to put it on. It's enchanted so it will handle the rest..."
                        sna_[6] "but I want it back before you leave!"
                        sna_[20] "I spent a fortune on the self cleaning model..."
                        $ potion_inv.add("p_milk_potion")
                    else:
                        sna_[13] "Mmmm, I wish I could be there to see you milk her..."
                        m "..."
                        m "(That's probably not a good idea...)"
                        sna_[12] "All that {b}delicious{/b} milk..."
                        m "(definitely not a good idea.)"
                        sna_[13] "..."
                        sna_[9] "Well anyway, I was wondering..."
                        sna_[9] "Want me to augment the potion?"
                        m "Augmented?"
                        m "I never asked for this..."
                        sna_[6] "I know... I'm offering it..."
                        m "Oh yeah, sorry. What sort of augmentation?"
                        sna_[10] "Well I can leave the potion as it is..."
                        sna_[12] "Or I can add an extra little something to it."
                        m "Such as?"
                        sna_[9] "Well..."
                        label snape_potion_choice:
                            pass
                        menu:
                            "-Normal potion-":
                                sna_[7] "Here you are Mr. Adventurous..."
                                $ potion_version = 1
                            "-futa potion-":
                                sna_[17] "What? Are you sure you want this one?"
                                sna_[18] "I mean I figured you were a bit of a pervert..."
                                sna_[19] "but I didn't think..."
                                sna_[18] "Oh well, if you want it, it's yours..."
                                menu:
                                    "-give it to me-":
                                        sna_[17] "really?"
                                        sna_[18] "you're more Adventurous than I thought!"
                                        sna_[20] "Here, I'll even give you an extra attachment for the milker!"
                                        ">Snape hands you a different cannister with a soft plastic opening in the bottom. It looks almost like an anus."
                                        sna_[19] "I also put an undetectable extension charm on the cannister... Promise to tell me what happens!"
                                    "-no-":
                                          sna_[7] "Too bad..."
                                          jump snape_potion_choice

                                $ potion_version = 2
                            "-Permanent breast expansion-":
                                sna_[18] "The milk production will still only last a day..."
                                sna_[9] "But her big boobs will be permanent..."
                                sna_[18] "Are you sure you want this?"
                                sna_[20] "She might not like it..."
                                menu:
                                    "-yes-":
                                        sna_[19] "Fantastic!!!"
                                    "-no-":
                                          sna_[7] "Too bad..."
                                          jump snape_potion_choice

                                $ potion_version = 3
                        ">Snape quickly pushes the milky potion into your hands."
                        ">Milking potion received!"
                        $ potion_inv.add("p_milk_potion")
                    jump snape_ready

                "-Veritaserum-" if potion_inv.has("p_veritaserum"):
                    ">You already have a Veritaserum potion."
                    jump snape_ready
                "-Veritaserum-" if not potion_inv.has("p_veritaserum"):
                    sna_[1] "Truth potion."
                    sna_[1] "This is dangerous stuff Genie..."
                    sna_[21] "Use it to make anyone tell the truth."
                    sna_[8] "Just not me!"
                    ">Snape hands you the tiny vial filled with a strange gold liquid."
                    ">Veritaserum received!"
                    $ potion_inv.add("p_veritaserum")
                    jump snape_ready

                "-Voluptatem-" if potion_inv.has("p_voluptatem"):
                    ">You already a bottle of Voluptatem."
                    jump snape_ready
                "-Voluptatem-" if not potion_inv.has("p_voluptatem"):
                    m "Volupwhatem?"
                    sna_[1] "This is actually an experimental potion of mine..."
                    sna_[7] "I'm not sure if this is ready for testing on humans yet."
                    ">Snape hands you the small bottle filled with a swirling pink and purple liquid."
                    ">Voluptatem received!"
                    $ potion_inv.add("p_voluptatem")
                    jump snape_ready

                "\"Never mind.\"":
                    jump snape_ready

        "-Talk-" if not chitchated_with_snape:
            $ chitchated_with_snape = True
            jump snape_talk

        "-Let's hang-" if not daytime and not sfmax: # Turns TRUE when friendship with Snape been maxed out.
            if one_of_ten == 10 and game_difficulty >= 2:  #Doesn't happen with easy difficulty.
                jump not_today #Snape says: "I am busy tonight."
#            elif snape_friendship >= 39 and whoring <= 5: # Whoring level <= 2. Makes sure you don't proceed after Date #6 until reached Whoring lvl 3.
#                jump not_today #Snape says: "I am busy tonight."
            elif snape_friendship >= 88 and whoring <= 14: # Whoring level <= 5. Makes sure you don't proceed after Date #12 until reached Whoring lvl 6.
                jump not_today #Snape says: "I am busy tonight."
            else:
                $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                jump snape_dates
        
        "Push Snape about teaching you magic" if found_nettle_wine and not talked_snape_office:
            jump snape_nettle_wine

        "-Never mind-":
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)

            if daytime:
                sna "Alright, back to work then..."
            else:
                sna "Goodnight then."

            $ snape_busy = True
            hide screen snape_01 #Snape stands still.
            hide screen bld1
            hide screen snape_main
            with d3
            call play_sound("door")

            if daytime:
                call play_music("brittle_rille") #Day Theme
                jump day_main_menu
            else:
                call play_music("manatees") #Night Theme
                jump night_main_menu

label setup_snape_date:                
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    show screen blkfade
    $ fire_in_fireplace = True
    hide screen genie
    hide screen chair_right
    hide screen desk
    show screen desk
    show screen with_snape_animated
    show screen fireplace_fire

    hide screen snape_01 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3

    hide screen blkfade
    with fade
    return
    
label snape_nettle_wine:
    call setup_snape_date
    
    call sna_main("I've had the worst day ever today... Don't even talk to me.", "snape_06")
    m "..."
    m "Then why visit my office?"
    call sna_main("For the free drinks of course...", "snape_05")
    call sna_main("The company is fine too I suppose.", "snape_24")
    g9 "I can get behind that..."
    m "Something stronger today perhaps."
    call sna_main("Now you're speaking my language... where did you even find this?", "snape_23")
    m "I have my sources... and a seemingly endless cupboard."
    call sna_main("cheers.", "snape_23")
    call sna_main("...", "snape_22")
    m "So I'm assuming you're not teaching me any of your magic tonight."
    call sna_main("In due time, I'm dead tired after todays display.", "snape_12")
    m "..."
    m "Go on then..."
    call sna_main("It's that Longbottom kid.", "snape_18")
    m "Long...bottom?"
    call sna_main("His inabillity of grasping the most simple tasks is making a mockery of my subject.", "snape_18")
    m "Does this school not have some sort of program for that?"
    call sna_main("It's not like that... It's more his inability of memorizing the steps in brewing.", "snape_14")
    m "Is this where you want me to nod and pretend that I know what you're on about?"
    call sna_main("Potions are a very precise and noble profession you know.", "snape_12")
    m "..."
    call sna_main("But you'd probably only care about my more crude elixirs I've developed after hours.", "snape_13")
    m "..."
    m "\"Crude elixirs you say...\""
    call sna_main("I'm sorry... I'd rather be a Defence against the dark arts teacher, that's all.", "snape_12")
    m "No need to appologize, alcohol does that sometimes."
    m "Why are you still doing potions in that case... I mean, now when I'm here."
    call sna_main("You won't be here forever, I'm sure.", "snape_14")
    m "And?"
    call sna_main("And the man you're replacing would never put me in charge of that subject.", "snape_12")
    m "I see, so when he returns he'd know you were aware of me."
    call sna_main("Precisely...", "snape_12")
    call sna_main("...", "snape_12")
    call sna_main("Well, sorry for cutting it short. I'm going to retire for tonight.", "snape_01")
    m "There's always a new day tomorrow."
    call sna_main("That is true...", "snape_19")
    m "\"Maybe it's worth investigating a way to get in that office...\""

    $ talked_snape_office = True
    jump day_start
    
label snape_dates:  ### HANGING WITH SNAPE ###
    call setup_snape_date

    if snape_against_hermione: #Turns True after event_08 (Hermione shows up for the first time).
                               #Activates special event when hanging out with Snape next time.
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape

    if snape_against_hermione_02: #Activates after second visit from Hermione (event_09).
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape_02

    if hg_pf_DanceForMe_OBJ.points >= 2 and not snape_invated_to_watch: #After second dance where Snape entered room.
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape_03

    #ADD sQuest here "Pensieve Event"

    if wine >= 1 and not wine_not: # Using Dumbledor's wine for the first time.
        $ wine_not = True # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.
        call wine_first
    elif wine >= 1 and wine_not: # Using Dumbledor's wine not for the first time.
        call wine_not_first
    else:
        pass

    if snape_friendship >= 5 and snape_events == 0:
        call date_with_snape_01

    elif snape_friendship >= 12 and snape_events == 1: #LEVEL 02
        call date_with_snape_02

    elif snape_friendship >= 19 and snape_events == 2: #LEVEL 03
        call date_with_snape_03

    elif snape_friendship >= 27 and snape_events == 3: #LEVEL 04
        call date_with_snape_04

    elif snape_friendship >= 34 and snape_events == 4: #LEVEL 05
        call date_with_snape_05

    elif snape_friendship >= 41 and snape_events == 5: #LEVEL 06. Can't proceed after this until whoring >= Lv 3.
        call date_with_snape_06

    elif snape_friendship >= 48 and snape_events == 6: #LEVEL 07
        call date_with_snape_07

    elif snape_friendship >= 55 and snape_events == 7: #LEVEL 08
        call date_with_snape_08

    elif snape_friendship >= 62 and snape_events == 8: #LEVEL 09
        call date_with_snape_09

    elif snape_friendship >= 69 and snape_events == 9: #EVENT 10
        call date_with_snape_10

    elif snape_friendship >= 76 and snape_events == 10: #EVENT 10
        call date_with_snape_11

    elif snape_friendship >= 83 and snape_events == 11: #EVENT 11
        call date_with_snape_12

    elif snape_friendship >= 88 and snape_events == 12: #EVENT 12. If whoring level > 5.
        call date_with_snape_13

    elif snape_friendship >= 93 and snape_events == 13: #EVENT 13
        call date_with_snape_14

    elif snape_friendship >= 98 and snape_events == 14: #EVENT 14
        call date_with_snape_15

    else:
        show screen bld1
        with d3
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."
        hide screen bld1
        with d3

    $ snape_friendship +=1

    jump day_start


### SPECIAL DATE ###
label special_date_with_snape: #TAKES PLACE AFTER FIRST VISIT FROM HERMIONE.
    $ snape_against_hermione = False #Turns True after event_08. Activates special event (THIS EVENT) when hanging out with Snape next time.
    sna_[2] "..........................."
    m "...............................?"
    sna_[3] "I hate her so much..."
    menu:
        "\"Yeah! That bitch!\"":
            sna_[1] "Good to know that we are on the same page..."
            sna_[2] "That girl..."
        "\"You hate who?\"":
            sna_[1] "Why would you ask that?"
            sna_[1] "That Hermione girl of course!"
        "\"Is she that bad?\"":
            sna_[1] "She is the worst!"

    sna_[2] "A top student..."
    sna_[3] "Leads all sorts of extracurricular activities and clubs..."
    sna_[3] "the president of the school's Student Representative Body..."
    sna_[3] "Likely to become the head girl soon..."
    sna_[2] "................"
    sna_[3] "............"
    with hpunch
    sna_[5] "{size=+7}I hate that fucking witch!!!{/size}"
    g4 "{size=-4}(What the...?){/size}"
    sna_[2] ".............."
    sna_[2] "She used to be just an annoyance, but these days..."
    sna_[1] "She's become a full-fledged menace..."
    sna_[1] "That witch is officially my least favorite student in the entire school now..."
    m "What about that Potter boy?"
    sna_[6] "The Potter boy? Ha! Who's that!?"
    sna_[1] "No, I'm serious..."
    sna_[1] "I will go as far as to say that Potter and his wretched father combined..."
    sna_[1] "Have never caused me as much grief as this little witch does lately..."
    m "Now, now. We both know that's not true..."
    sna_[2] "Yeah... You're probably right..."
    sna_[7] "That bastard James Potter really did a number on me--"
    sna_[6] "Wait, how do you know this?"
    m "Well... I've read the books..."
    sna_[6] "What? What books?"
    m "Nah, never-mind. I'm a genie, remember? I know things..."
    sna_[9] "Hm... And yet you need me to teach you stuff..."
    m "Well, I told you. My magic is acting up in your world..."
    sna_[9] "Sure, sure..."
    m "......"
    m "She came by the other day..."
    sna_[10] "Who did?"
    m "The Hermione girl..."
    sna_[1] "What?!"
    sna_[2] "I thought we agreed on the \"no human contact\" rule."
    sna_[7] "(Even though lately I've been wondering whether or not she is human at all...)"
    m "I know... She kinda forced her way in..."
    sna_[1] "I imagine she did..."
    sna_[1] "What did she want?"

    if jerk_off_session:
        m "I'm not sure..."
        sna_[11] "??"
        m "I was jerking off the entire time she was talking..."
        sna_[2] "You've been..."
        sna_[2] "... doing what?"
        m "Hey, don't judge me!"
        m "You don't know what it's like to be cooped up in this tower like a prisoner!"
        sna_[2] "You... y-you...."
        sna_[12] "......"
        sna_[15] "Ha.... ha-ha... HA-HA-HA!!!"
        m "Wha..? What did I say?"
        sna_[14] "Ha-ha-ha! You are amazing!"
        sna_[9] "Are all genies so... wonderfully nihilistic?"
        m "Yeah... We immortals tend to not give a fuck."
        sna_[9] "Understandable..."
        sna_[10] "Unfortunately, us mere mortals cannot afford such a luxury..."

    else:
        m "Not sure... She was talking a lot..."
        m "Something about some \"greefeendo\" points... and..."
        m "Er... I wasn't paying attention to be honest..."
        sna_[1] "Nah... Probably another load of self-righteous crap..."
        sna_[7] "She is famous for that..."


    sna_[7] "I have a class early tomorrow, so let us call it a night."
    m "What about you teaching me magic and stuff?"
    sna_[10] "Yeah, absolutely..."
    sna_[10] "Next time..."
    m "Alright..."




    $ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)

    jump day_start

#######################################################################################################################
label special_date_with_snape_02: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen bld1
    with d5
    #$ snape_against_hermione = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    m "......................."
    m "Hermione Granger came by again..."
    sna_[1] "Don't mention the witch's name when I'm off duty..."
    sna_[2] "..............."
    sna_[3] "Dammit! I am a grown man, Albus!"
    m "My name is not--"
    sna_[3] "An esteemed wizard..."
    m "Well, alright, let it out..."
    sna_[2] "How come one tiny....cunt, is able to cause me so much grief?!"
    sna_[4] "I thought with you as my ally I will have a chance to--"
    m "To unclench?"
    sna_[2] "Yeah, that could be the word..."
    sna_[16] "But all I did was give her more leverage to harass me with..."
    sna_[16] "She's even turning the teachers against me now..."
    sna_[3] "................."
    sna_[7] "She must go..."
    m "What do you mean?"
    with hpunch
    sna_[5] "{size=+6}I will have to kill her!{/size}"
    g4 "Like, literally kill her?"
    sna_[6] "Do I have any other choice?"
    m "You're joking, right?"
    sna_[6] "Am i?!"
    sna_[11] "Can you do this for me?"
    m "Em..."
    m "As much I would \"enjoy\" murdering a teenage girl..."
    m "Genies can't kill..."
    sna_[7] "Rats!"
    m "And we frown upon murderers..."
    if jerk_off_session:
        sna_[17] "Really? I thought you didn't give a fuck..."
        m "to a certain degree..."
        sna_[7] "............."
    sna_[2] "Well... don't mind me then..."
    sna_[2] "I'm all talk..."
    sna_[2] "I would never actually harm a student..."
    sna_[3] "(...permanently that is.)"
    m "Listen, if she bugs you so much, why not just find a less radical way to deal with her?"
    sna_[7] "Nah... Flogging has been outlawed for years now..."
    m "That's not what I mean..."
    sna_[1] "Huh?"
    m "She is a top student, right?"
    sna_[2] "Yes, damn her. The girl is a hard worker, I will give her that."
    m "She also has a reputation for being self-righteous."
    sna_[6] "Oh, yes!"
    m "And she thinks that she is better than everyone else..."
    sna_[17] "Where are you going with this?"
    m "Well, it seems like all of her power comes from her reputation..."
    sna_[11] "......................?"
    m "What if we take that away from her?"
    sna_[10] "That would shut her up I suppose..."
    sna_[2] "But how? She's practically a saint."
    sna_[7] "Even students who hate her secretly admire her."
    sna_[2] "She hasn't failed a single test in her entire time here..."
    sna_[2] "She is always ahead of the schedule..."
    sna_[3] "Damn, how I hate it when she corrects me during my classes..."
    sna_[6] "And thanks to her the \"Gryffindor\" house is way ahead of everybody else now..."
    sna_[7] "Even \"Slytherin\" is no match for them this year..."
    sna_[16] "........................"
    sna_[6] "Dammit... I need more wine..."
    m "The wine can wait. Hear me out!"
    sna_[1] "Huh...?"
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label fuck_off:
    m "Hm... Let us..."
    menu:
        m "..."
        "{size=-3}\"Make sure she is not a top student any longer!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            sna_[1] "What? You mean grade her unfairly?"
            sna_[2] "Nah... Dumbledore would never allow--"
            sna_[9] "Wait a second!"
            m "Exactly!"
            sna_[18] "You're right! I can grade her tests unfairly! I could even persuade other teachers to do the same!"
            sna_[18] "I could say that the order comes from you..."
            sna_[19] "And when the real Dumbledore shows up I will pretend that I had no idea that he was away..."
            m "Works for me."
            sna_[10] "Er..."
            sna_[10] "This is still you, genie, right?"
            m "Yeah, yeah, still here..."
            sna_[18] "OK, good."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off
        "{size=-3}\"Make sure \"Gryffindor\" loses the cup this year!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            sna_[1] "You mean to just start subtracting points from them for no good reason?"
            sna_[18] "Oh, I like that!"
            sna_[20] "There are a couple of \"Slytherin\" girls who are long overdue for receiving some extra house points as well."
            sna_[19] "Oh, this will work out magnificently!"
            sna_[18] "You are a Genius!"
            m "Yes, I am a genius genie. What are the odds of that..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Ruin her reputation!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            sna_[1] "Tarnish her reputation?"
            sna_[1] "But the girl is incorruptible..."
            m "Nonsense!"
            m "All we need to do is convince her that she needs to make some sacrifices \"for the greater good\"."
            sna_[9] "Oh, but of course..."
            sna_[21] "She would gladly \"Get her hands dirty\" to save the honour of her precious \"Gryffindor\" house!"
            sna_[9] "And when she does, we will have the leverage we need..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    sna_[9] "This could actually work!"
    m "I think so too."
    sna_[19] "Oh, I feel so alive tonight!"
    sna_[15] "Pour me another goblet!"
    sna_[19] "The \"Defence Against the Dark Arts\" class will start late tomorrow!"
    m "....."
    m "Don't you think this is a bit too brutal though?"
    m "I mean, she's just a girl..."
    sna_[8] "Just a girl?"
    sna_[8] "Oh no, no, no..."
    sna_[4] "She is the embodiment of pure evil!"
    sna_[2] "If we don't do this now..."
    sna_[3] "One of those days I may just snap and \"Avada Kedavra\" her!"
    m "You'll do what?"
    sna_[4] "Murder her for real!"
    m "Alright, alright... got it."
    m "Let's choose the lesser of two evils then."
    sna_[7] "Yes..."
    sna_[6] "Now, pour me some more wine."

    ">You spend rest of the evening in Snape's company drinking your worries away."

    $ snape_against_hermione_02 = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    $ hermione_is_waiting_02 = True #Triggers another visit from Hermione. (Event_11)


    #$ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    hide screen bld1
    with d3
    $ days_without_an_event = 0 #Making sure next even will not start right away.
    jump day_start


#######################################################################################################################
label special_date_with_snape_03: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen bld1
    with d5

    sna_[2] "So..."
    sna_[7] "You got the girl to strip for you..."
    sna_[3] "And you didn't even invite me?!"
    m "Well..."
    m "I don't think the girl would be willing to--"
    sna_[12] "Those naked, perfectly shaped breasts..."
    sna_[13] "Those magnificent long legs..."
    sna_[12] "Her ample and tender behind..."
    sna_[13] "I've seen everything..."
    sna_[20] "I've seen it all!"
    m "(...)"
    sna_[16] "As much of a nuisance I think the girl is..."
    sna_[5] "{size=+7}I could stare at those tits all day!!!{/size}"
    m "..."
    sna_[7] "You've got to invite me next time, my friend!"
    sna_[8] "My life depends on it!"

    menu:
        m "..."
        "-Sure, why the hell not-":
            pass
        "-Uhh-":
            pass

    sna_[19] "Splendid!"
    sna_[9] "I can hardly wait I tell you!"
    sna_[21] "Do you think she will let me touch them...?"

    ">You spend rest of the evening in Snape's company talking about Hermione's naked breasts."

    $ snape_invated_to_watch = True

    hide screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes

    $ days_without_an_event = 0 #Making sure next even will not start right away.
    jump day_start




####Snape bonus###
#label snape_bonus:
#    if snape_events == 1:
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=3
#            "Slytherin got +3 points as a Snape-Bonus."

#    if snape_events == 2:#WEEK No.2
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=7
#            "Slytherin got +7 points as a Snape-Bonus."

#    if snape_events == 3:#WEEK No.3
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=10
#            "Slytherin got +10 points as a Snape-Bonus."

#    if snape_events == 4:#WEEK No.4
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=12
#            "Slytherin got +12 points as a Snape-Bonus."

#    if snape_events == 5:#WEEK No.5
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=16
#            "Slytherin got +16 points as a Snape-Bonus."

#    if snape_events == 6:#WEEK No.6
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=22
#            "Slytherin got +22 points as a Snape-Bonus."

#    if snape_events == 7:#WEEK No.7
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=26
#            "Slytherin got +26 points as a Snape-Bonus."

#    if snape_events == 8:#WEEK No.8
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=32
#            "Slytherin got +32 points as a Snape-Bonus."

#    if snape_events == 9:#WEEK No.9
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=36
#            "Slytherin got +36 points as a Snape-Bonus."

#    if snape_events == 10:#WEEK No.10
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=43
#            "Slytherin got +43 points as a Snape-Bonus."

#    if snape_events == 11:#WEEK No.11
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=46
#            "Slytherin got +46 points as a Snape-Bonus."

#    if snape_events == 12:#WEEK No.12
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=50
#            "Slytherin got +50 points as a Snape-Bonus."

#    if snape_events == 13:#WEEK No.13
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=56
#            "Slytherin got +56 points as a Snape-Bonus."

#    if snape_events == 14:#WEEK No.14
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=61
#            "Slytherin got +61 points as a Snape-Bonus."

#    if snape_events == 15:#WEEK No.15
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=66
#            "Slytherin got +66 points as a Snape-Bonus."

#return




####################################
label wine_first:
    m "Look what I've got!"
    call sna_head("Hm..?","snape_05")
    call sna_head("Let me see...")
    pause.1
    $ the_gift = "images/store/27.png" # WINE.
    show screen gift
    with d3
    ">You hand over the bottle you found in the cupboard to professor Snape..."
    hide screen gift
    with d3
    $ wine -= 1


    call sna_head("This one has got to be from Albus' personal stash!","snape_24")
    call sna_head("Some pricey and incredibly rare stuff.","snape_06")
    m "Shall we then?"
    call sna_head("We most certainly shall!","snape_02")
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Your relationship with Professor Snape has improved."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    return


label wine_not_first:
    m "Look what I've got!"
    hide screen s_head2
    pause.1
    $ the_gift = "images/store/27.png" # WINE.
    show screen gift
    with d3
    ">You hand over the bottle you fond in the cupboard to professor Snape..."
    hide screen gift
    with d3
    $ wine -= 1

    call sna_head("Another one?","snape_05")
    if one_of_ten == 1:
        call sna_head("Splendid!","snape_02")
    elif one_of_ten == 2:
        call sna_head("Alright!","snape_02")
    elif one_of_ten == 3:
        call sna_head("Awesome!","snape_02")
    elif one_of_ten == 4:
        call sna_head("Well done, my friend!","snape_02")
    elif one_of_ten == 5:
        call sna_head("Did you find Albus' secret stash or was it his personal wine cellar?","snape_05")
    elif one_of_ten == 6:
        call sna_head("lately I am having hard time drinking anything but this!","snape_02")
    elif one_of_ten == 7:
        call sna_head("Great! I feel less stressed out already!","snape_02")
    elif one_of_ten == 8:
        call sna_head("This just keeps getting better and better!","snape_02")
    elif one_of_ten == 9:
        call sna_head("Seriously, how big is that stash?","snape_05")
    elif one_of_ten == 2:
        call sna_head("It's sure good to be us! let's uncork that bastard!","snape_02")

    call bld
    call give_reward(">Your relationship with Professor Snape has improved.","images/store/01.png")
    #">Your relationship with Professor Snape has improved."

    if game_difficulty < 2:      #Easy difficulty
        $ snape_friendship +=3
    else:                        #Normal and hard difficulty
        $ snape_friendship +=2

    return


  ########
label not_today:
    if one_out_of_three == 1:
        sna "Sorry, I can't tonight..."
    elif one_out_of_three == 2:
        sna "Sorry, I have other business to attend to tonight..."
    elif one_out_of_three == 3:
        sna "Sorry, I have other plans. Maybe some other time?"

    jump snape_ready
