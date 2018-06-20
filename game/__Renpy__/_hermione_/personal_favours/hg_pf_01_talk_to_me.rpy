

### HERMIONE PERSONAL FAVOUR 1 ###

### TALK TO ME ###

label hg_pf_TalkToMe:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"
    
    # First time event
    if hg_pf_TalkToMe_OBJ.points == 0:

        menu:
            "\"(Yes, let's do that.)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    # Choose outfit if avalable
    if hg_maid_OBJ.purchased or hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased or hg_msMarvel_OBJ.purchased or hg_heartDancer_OBJ.purchased or hg_powerGirl_OBJ.purchased or hg_harleyQuinn_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL") 
                menu:
                    "-A maid-" if hg_maid_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_maid_OBJ) 
                        pass
                    "-A Cheerleader-" if hg_gryffCheer_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_gryffCheer_OBJ) 
                        pass
                    "-A Slytherin Cheerleader-" if hg_slythCheer_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_slythCheer_OBJ) 
                        pass
                    "-Ms Marvel-" if hg_msMarvel_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_msMarvel_OBJ) 
                        pass
                    "-A heart dancer-" if hg_heartDancer_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_heartDancer_OBJ) 
                        pass
                    "-power girl-" if hg_powerGirl_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_powerGirl_OBJ) 
                        pass  
                    "-Harley Quinn-" if hg_harleyQuinn_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_harleyQuinn_OBJ) 
                        pass
            "\"(Not right now.)\"":
                pass

    call play_music("chipper_doodle") 

    m "Alright then..."
    m "Just tell me some news about you."
    call her_main("","open","suspicious")

    # First time this event taking place.
    if hg_pf_TalkToMe_OBJ.points == 0: 
        her "Ehm... Alright..."
        her "I just stand here and talk then...? Like this?"
    else:
        her "Here in the middle, right? I remember..."
    
    call her_main("","base","base",xpos="mid",ypos="base",trans="fade") 
    call ctc 
    
    m "Well?"

    # First time event
    if hg_pf_TalkToMe_OBJ.points == 0 and whoring <=5:
        $ hg_pf_TalkToMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

        call her_main("Em... very well...","open","worried") 
        call nar(">Hermione is feeling confused...") 
        call her_main("...................","annoyed","angryL") 

    #Event 1 and 2
    if whoring >= 0 and  whoring <= 5:
        if whoring >= 3 and whoring <= 5:
            $ hg_pf_TalkToMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

        call her_main("My life has been quite uneventful lately, to be honest...","annoyed","angryL") 
        her "Apart from the day when I failed that test..."
        her "I still can't believe it happened..."

        menu: 
            "-Jerk off while she is talking-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                call nar(">You reach under the desk and grab your cock...") 
                
                hide screen genie
                show screen genie_jerking_off
                hide screen bld1
                with d3
                
                call ctc 
                
                call her_main("[genie_name], what are you doing?","open","base",xpos="mid") 
                m "What? Oh, it's nothing. Just scratching my leg."
                m "You were saying?"
                call her_main("Yes... Well, that test I failed...","open","base") 
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Yes, what a tragedy that was..."
                her "Exactly! I'm glad you understand, [genie_name]."
                #pass

        her "Come to think of it, I don't feel like talking about it anymore..."
        m "Alright, what else has happened lately?"
        her "Em... Well, I'm doing pretty well at herbology..."
        her "I mean, I always score the top marks, but I have been studying really hard anyway..."
        her "And now I sort of feel like sometimes I know more than professor Sprout herself..."

        if d_flag_01:
            m "{size=-4}(Yes... ah...){/size}"
        else:
            m "(Professor Sprout... He-he, what a ridiculous name...)"
        
        call her_main("Did you say something, [genie_name]?","normal","frown") 
        m "It's nothing, keep going..."
        call her_main("Well, some students are making fun of professor Quirell behind his back...","open","base") 

        her "I disapprove of such behavior, of course."
        if d_flag_01:
            m "{size=-4}(Come on! Say something naughty!){/size}"
        else:
            m ".................."

        her "Oh, and my \"Men's Rights Movement\" group is gaining popularity..."
        her "I'm very happy about that..."
        call her_main("I think, given time, we will be able to make a real difference...","open","closed") 
        call her_main("It is so invigorating to know that you are doing the right thing!","base","base") 
        her "Wouldn't you agree, professor?"

        if d_flag_01:
            m "{size=-4}(Dammit. Now she's killed the mood completely...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
        else:
            m "Zzzz........"
            
        call her_main("[genie_name]?","angry","angry") 
        m "Yes, yes, I'm totally listening..."
        m "This is all very self-righteous, er..."
        m "I mean, very invigorating and stuff..."
        call her_main("..........................","normal","frown") 

    #Event 3
    elif whoring >= 6:
        $ hg_pf_TalkToMe_OBJ.hearts_level = 3 #Event hearts level (0-3)

        call her_main("My life has been quite uneventful lately, to be honest...","annoyed","angryL") 
        her "Hm..."
        her "There is a fierce competition going on between the \"Slytherin\" and the \"Gryffindor\" house."
        her "To be honest, [genie_name], there should be none..."
        her "\"Gryffindor\" would have been in the lead if not for those \"Slytherin\" harlots..."
        her "The things I hear those girls do simply to get a few extra points..."
        call her_main("How despicable!","open","angryCl") 
        m "What does this make you then, [hermione_name]?"
        call her_main("Exactly!","normal","base") 
        m "Huh?"
        call her_main("I have to work even harder to compensate for the damage those nasty girls are doing...","open","angryCl") 
        call her_main("Thank you for helping me out, [genie_name].","normal","base") 

        menu: 
            "-Start jerking off-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                call nar(">You reach under the desk and grab your cock...") 
                hide screen genie
                show screen genie_jerking_off
                with d3
                
                call ctc 
                
                call her_main("[genie_name], what are you doing?","open","base",xpos="mid") 
                her "You are not.....?"
                call her_main("Are you...?","annoyed","worriedL") 
                m "What? Oh, it's nothing. Keep going."
                call her_main("Hm...","normal","frown") 
                m "{size=-4}(Is she onto me? Nah...){/size}"
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Don't mention it."
                
        call her_main("Well, like I was saying...","open","closed",xpos="mid") 
        her "I heard that this one girl sold one of the professors some naughty pictures of herself for ten house points..."

        if d_flag_01:
            m "{size=-4}(What a slut... ah... Yes...){/size}"
        else:
            m "Ten points, huh?"

        her "Yes..."

        if d_flag_01:
            call her_main("And these two other girls...","annoyed","worriedL") 
            her "There is a rumor that they are actually sleeping with professor snape..."
            m "{size=-4}(Yes... Those nasty \"slytherin\" sluts!){/size}"
            call her_main("Also, there was this one girl who gave a teacher a handjob, right during class...","base","base") 
            m "{size=-4}(Yes... This is good stuff, go on!){/size}"
            call her_main("And this other girl, she sucked off a teacher!","annoyed","worriedL") 
            m "{size=-4}(Yes! Yes!){/size}"
            call her_main("And another girl let a teacher cum in her mouth...","smile","baseL") 
            her "And she swallowed it all and loved it!"
            m "{size=-4}(Wait... Is she making this up?){/size}"
            call her_main("I'm a nasty girl too, you know...","smile","glance") 
            g4 "What?!"
            call her_main("I just want to suck a cock...","open_tongue","glance") 
            her "I want men to cum on my face like in those videos I saw!"
            g4 "{size=-4}(You little slut! That did it!) *Argh!*{/size}"

            hide screen hermione_main
            with d3

            call cum_block 

            g4 "Argh! YES!"
            hide screen bld1
            with d1
            show screen genie_jerking_sperm
            with d3
            call ctc 

            if whoring <= 10:
                $ mad = +7
                call her_main("I knew it! You were touching yourself, [genie_name]!","angry","angry") 
                #show screen genie_jerking_sperm_02
                #with d3
                g4 "What? No, I was just... ah, shit, this feels good..."
                show screen genie
                with d3
                call her_main("This is disgusting! How could you!?","scream","worriedCl") 
                her "[genie_name], you are the headmaster! You are supposed to set a good example!"
                m "Hey, little missy, are you going to judge me or do you want your points?"
                call her_main("My points please, I believe I earned those.","angry","worriedCl",emote="05") 
                m "Yes, you did."
                call her_main("Ew... I feel so dirty now...","angry","angry") 
                hide screen genie_jerking_sperm_02
                with d3
            else:
                call her_main("I knew it! You were touching yourself, [genie_name]!","smile","glance") 
                #show screen genie_jerking_sperm_02
                #with d3
                g4 "What? No, I was just... ah, shit, this feels good..."
                show screen genie
                with d3
                call her_main("How could you [genie_name]? In front of a young innocent student!","scream","angryCl") 
                m "Hey, little missy, what you were saying wasn't exactly innocent"
                call her_main("I don't know what you're talking about...","smile","baseL") 
                m "I'm sure. Do you want your points or not?"
                call her_main("{size=-4}he sure did cum a lot{image=textheart}{/size}","base","base") 
                hide screen genie_jerking_sperm_02
                with d3

        else:
            her "We need to put an end to this behavior, [genie_name]!"
            m "Yeah, sure..."
            her "So you agree with me then?"
            her "I think we need to implement a new penalty system to punish girls who are known to sell favours..."
            m "(All I heard was \"punish girls\"...)"
            her "This will also help the boys in our school to feel less discriminated against!"
            m "The boys?"
            m "Oh, right... Nobody wants to buy sexual favours from them... Poor bastards."
            her "I'm so glad that you understand my concerns, [genie_name]."
            m "Yes, yes, sure..."
            
    stop music fadeout 2.0
    
    if whoring >= 11:
        m "Five points to \"Gryffindor\", [hermione_name]. Well done." 
        her "Oh, don't worry about the points, [genie_name]. We were just having a nice talk."
        m "Really? What about \"Gryffindor\" winning the cup?"
        call her_main("It's only 5 points...","soft","baseL") 
        m "If you say so."
        call her_main("Will this be all then?","base","base") 
        m "Yes, you can go now."
    else:
        $ gryffindor +=5
        m "Five points to \"Gryffindor\" [hermione_name]. Well done." 
        show screen hermione_main
        hide screen hermione_stand_f #Hermione stands still.
        with d3
        her "Will this be all then?"
        if whoring >= 0 and whoring <= 2: #LEVEL 01
            her "*sigh of relief*"
        m "Yes, you can go now."

    if hg_pf_TalkToMe_OBJ.points == 0:
        call her_main("Another 5 points... The Guys will be so happy.","base","base") 
        her "Thank you, [genie_name]."
    
    if whoring < 3: #Adds points till 3.
        $ whoring +=1
    
    $ hg_pf_TalkToMe_OBJ.points += 1
    
    jump end_hg_pf












