
label astoria_tonks_event: #send astoria to go see tonks

    $ spells_locked = False
    $ tonks_busy = True
    $ astoria_tonks_event_in_progress = False
    $ ton_astoria_date_counter += 1 #For Stats

    if ast_affection < 100:
        $ ast_affection += 1

    if ag_cs_imperio_sb.level == 0 and not astoria_tonks_intro_completed:
        jump astoria_tonks_0
    elif ag_cs_imperio_sb.level == 1 and not astoria_tonks_1_completed:
        jump astoria_tonks_1
    elif ag_cs_imperio_sb.level == 2 and not astoria_tonks_2_completed:
        jump astoria_tonks_2
    elif ag_cs_imperio_sb.level == 3 and not astoria_tonks_3_completed:
        jump astoria_tonks_3
    else: #Repeatable events.
        jump astoria_tonks_random


### TONKS EVENTS ###
label astoria_tonks_0: #First time astoria sent to tonks.
    call play_music("fun")
    call play_sound("door")
    call ast_main("","smile","base","base","mid",xpos="right",ypos="base")
    pause.5
    call nar(">Your door swings open as Astoria enters.")

    m "Oh, you're back!"
    call ast_main("Are you surprised, [ast_genie_name]?","smile","base","base","mid")
    m "A little... She does seem a bit weird."
    call ast_main("Then why would you send me there?!","open","base","worried","R")
    m "eh..."
    call ast_main("...","pout","narrow","narrow","mid")
    call ast_main("Well it wasn't too bad...","open","base","base","mid")
    call ast_main("She only wanted to ask a few questions.","upset","base","base","R")
    m "What sort of questions?"
    call ast_main("My favourite subjects, what I like, how old I am, stuff like that.","open","base","base","down")
    m "That's it? She didn't ask you to do anything weird?"
    call ast_main("Not really...","pout","base","base","R")
    call ast_main("Although she did have this look in her eyes... It was almost like she wanted to eat me...","open","narrow","worried","mid")
    call ast_main("She's not a werewolf is she, [ast_genie_name]?","open","wide","wide","wide")
    m "Holy shit! Are werewolves real here?"
    call ast_main("What do you mean here? Of course werewolves are real... We all learn that as children.","open","closed","base","mid")
    m "Just testing..."
    m "Oh, and I'm sure she's not a werewolf..."
    m "(I hope...)"
    call ast_main("She better not be, [ast_genie_name]!","disgust","base","worried","down")
    m "I'm sure you'll get used to her."
    call ast_main("Get used to her????","open","wide","wide","mid")
    call ast_main("I don't have to see her again do I?","disgust","base","worried","down")
    m "Well... If you want to keep learning new spells you might have to..."
    call ast_main("*hmph*-- you haven't even taught me any yet!","clench","angry","angry","mid")
    call ast_main("They're probably not even fun...","pout","angry","angry","R")

    if not snape_gave_spellbook:
        m "(Right. I still need that spellbook.)"
        m "Next time, [astoria_name]."
        m "I've got... uhm-... I've got stuff to take care of, yes."
        call ast_main("*I don't believe that one bit...","pout","angry","angry","R")
    else:
        m "Why don't you come over here then and we can start reading over the first one."
        call ast_main("alright...","grin","base","base","mid")

    $ astoria_tonks_intro_completed = True

    jump astoria_requests


label astoria_tonks_1:
    call play_music("fun")
    call play_sound("door")
    call ast_main("","clench","angry","angry","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Astoria enters your office, a sullen look painted over her face.")
    m "How was your--"
    call ast_main("Awful!","open","closed","angry","mid")
    call ast_main("That Tonks is a real creep, [ast_genie_name]!","pout","base","worried","down")
    m "Really? What'd she do?"
    call ast_main("She called my uniform conservative!","disgust","narrow","base","down")
    call ast_main("How can a uniform even have political beliefs?","pout","base","base","R")
    call ast_main("Let alone conservative!","open","base","worried","down")
    call ast_main("She's probably one of those loonies who complains on the--","pout","angry","angry","L")
    m "That's not what conservative means."
    call ast_main("Yes it is! I read it--","scream","closed","base","mid")
    m "It means she thinks your uniform hides too much skin..."
    call ast_main("Oh...","clench","narrow","narrow","down")
    call ast_main("Really?","disgust","base","base","mid")
    call ast_main("I guess that would explain the measuring tape...","open","base","base","L")
    m "Why don't you tell me what happened from the start?"
    call ast_main("Alright...","upset","narrow","narrow","mid")
    call ast_main("Well first we got to her office.","open","base","base","mid")
    call ast_main("We were just chatting a bit.","open","base","base","R")
    call ast_main("About Candy, pets, school stuff, and if there are any boys I liked...","worried","base","base","mid")
    call ast_main("She even showed me a secret passage from here to to the kitchens I didn't even know of!","grin","angry","angry","mid")
    call ast_main("Anyways, when we got there, Ginny Weasley suddenly spurted out of her office!","upset","base","worried","down")
    m "(Ginny Weasley? Haven't I heard that name before?)"
    m "(Is that the Granger girl's Lesbo friend? I can't remember...)"
    call ast_main("Her face was all red and she didn't want to look at me...","worried","base","base","down")
    call ast_main("I figured that she was probably getting in trouble for something so I didn't say anything...","open","base","base","R")
    call ast_main("Once we were inside, she asked what spell I'd cast this time...","upset","base","base","down")
    call ast_main("And who I cast it on...","open","base","base","R")
    call ast_main("But I don't think she was very interested...","smile","base","base","down")
    call ast_main("She was more excited about my uniform.","upset","base","base","mid")
    call ast_main("She said she'd just found out that as a teacher, she was allowed to choose uniforms for her students.","pout","angry","angry","R")
    m "(We can do that?... Did that Granger lie to me?!?)"
    call ast_main("And that she wanted to make some changes to my uniform because it was too conservative!","upset","ahegao","ahegao","ahegao")
    call ast_main("I told her I don't associate with any political party and ran out of there!","scream","angry","angry","R")
    call ast_main("But if she just meant my vest was too thick I guess that's not too bad...","disgust","narrow","narrow","down")
    m "(I'm sure that's what she meant...)"
    call ast_main("Do I have to go back there sir?","upset","base","worried","mid")
    m "Only if you want to keep casting new spells..."
    call ast_main("Ugh...","disgust","ahegao","ahegao","ahegao")
    call ast_main("Fine...","pout","angry","angry","L")
    call ast_main("Just make sure she keeps politics out of it!","pout","angry","angry","mid")
    m "Will do..."
    call ast_main("Good! Now about those new spells...","pout","base","base","R")
    m "We can start reading one now if you want."
    call ast_main("Yay!","grin","happyCl","base","mid")

    $ astoria_tonks_1_completed = True

    jump astoria_requests


label astoria_tonks_2:
    call play_music("fun")
    call play_sound("door")
    call ast_main("","smile","base","base","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Astoria happily walks into your office, humming a tune as she closes the door.")
    call ast_main("Hey, [ast_genie_name]!","grin","happyCl","base","mid")
    m "Hello, [astoria_name]... You seem chipper today."
    call ast_main("Guess what?","grin","angry","angry","mid")
    m "What's that?"
    call ast_main("Tonks wants me to be a model!","smile","angry","angry","down",cheeks="blush")
    m "A model?"
    call ast_main("Uh huh! Did you know she's actually a costume designer in her spare time?","open","base","base","mid")
    m "I did not..."
    call ast_main("Well she is! And she thinks I've got what it takes to be a model!","grin","angry","angry","mid")
    m "Really..."
    call ast_main("Yep! She even spent all day taking my measurements so she could start working on some special outfits for me!","grin","happyCl","base","mid")
    call ast_main("Plus she even said she'd start working on a new, cooler version of my uniform!","smile","base","base","mid")
    m "Huh..."
    call ast_main("Isn't that great sir?","grin","happyCl","base","mid")
    m "Sure is."
    call ast_main("And to think I thought she'd do something nasty...","open","base","base","R")
    m "I wouldn't put that past her just yet..."
    call ast_main("Pfft, you're one to talk old man!","pout","angry","angry","mid")
    call ast_main("I bet you spent all day thinking about what we're going to do to Susan next didn't you?","grin","angry","angry","mid")
    m "The thought might have crossed my mind..."
    call ast_main("Well if you wanna get to that we have to learn the new spell first, [ast_genie_name]!","open","base","base","L")
    call ast_main("Speaking of which...","worried","base","base","R")

    $ astoria_tonks_2_completed = True

    jump astoria_requests


label astoria_tonks_3:
    #call play_music("fun")
    call play_sound("door")
    call ast_main("","upset","closed","base","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Astoria walks into your office, snobbishly wrinkling her nose.")

    m "Welcome back, [astoria_name]. How was--"
    call ast_main("Cut the chit-chat, [ast_genie_name]! I don't have time for it!","clench","closed","base","mid")
    call ast_main("Tonks said you could help me with my model job!","open","base","base","mid")
    m "She did? How am I supposed to help?"
    call ast_main("She made me some cool, new outfits she wants me to wear.","open","base","base","down")
    call ast_main("I haven't tried them on yet so I don't know if they'll even fit.... They look really small...","disgust","closed","worried","down")
    call ast_main("It's simple, I'll try them on and see how they suit me...","open","base","base","down")
    call ast_main("All you need to do is sit on your bum and tell me how great I look!","open","closed","base","mid")
    call ast_main("Do you think you can manage that, [ast_genie_name]?","upset","narrow","narrow","mid")
    m "I will try..."
    call ast_main("Great! Now lets get started!","grin","angry","angry","mid")

    call popup("You can now access Susan & Astoria's wardrobe and change their appearance!", "Congratulations!", "interface/icons/head/head_astoria_2.png")

    "Developer note:" ">We have made both Susan's and Astoria's wardrobe available.\nAll available clothing has also been unlocked."
    "Developer note:" ">Susan's wardrobe as well as Astoria's clothings will unlock with future events instead in later patches."

    "Developer note:" ">This marks the end of the current Astoria and Susan content! We hope you liked it!"

    $ astoria_tonks_3_completed = True

    $ astoria_wardrobe_unlocked = True
    $ susan_wardrobe_unlocked = True

    $ active_girl = "astoria"

    #call load_astoria_clothing_saves

    call reset_wardrobe_vars
    call update_wr_color_list

    $ hide_transitions = True
    call ast_main(xpos="wardrobe",ypos="base")
    call screen wardrobe

#Tonks gives Astoria a shorter skirt
label astoria_tonks_4:
    #call play_music("fun")
    call play_sound("door")
    call ast_main("","upset","closed","base","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Astoria walks into your office in a new skirt, her eyes nervously looking to the side.")

    m "Welcome back, [astoria_name]. I like--"
    ast "Shut up!"
    m "..."
    ast "I don't want to talk about it, OK?"
    g4 "Talk about what?"
    ast "..."
    m "Have a fun time with Tonks?"
    ast "Do I look like I'm having fun?"
    m "Mmmm, you look like a lot of fun from where I'm sitting..."
    ast "Gross Dumby!"
    m "So, will you going to be wearing that skirt from now on?"
    ast "I have to, don't I?"
    m "Or else what?"
    ast "Or else Tonks will dob us in to the ministry! At least try to keep up, Dumby."
    m "Mmmm, well things certainly have gotten interesting..."
    ast "Stop looking at me like that! You've got the same look in your eye as she did!"
    m "Ready for your next lesson then?"
    ast "..."
    ast "Do I have to sit on your lap again?"
    m "I don't know how else you expect to read the book..."
    ast "..."
    ast "You're almost as sick as she is..."



#Tonks spanks Astoria for sending Susan home covered in cum
label astoria_tonks_5:
    call play_sound("door")
    call ast_main("","upset","closed","base","mid",xpos="right",ypos="base")
    pause.5

    call nar(">Astoria walks into your office in a new skirt, her face a mess from crying...")

    ast "I want you to fire Tonks!"
    m "What-"
    ast "FIRE HER!!!"
    m "I'm not sure I can do that... don't forget about Azkaban."
    ast "She's the one that deserves to be locked away! She's an evil, old witch!"
    m "At least tell me what's going on."
    ast "She spanked me! Like I'm some sort of child!"
    m "..."
    ast "It's not fair! She's crazy!"
    m "She spanked you?"
    ast "Really hard!"
    ast "I was even crying and telling her to stop but she kept going!"
    ast "It was horrible! No one can do that to me!"
    m "Why did she spank you?"
    ast "For nothing! She just said that I deserved it! AS IF!"
    m "It didn't have anything to do with Susan?"
    ast "..."
    m "Astoria..."
    ast "She might have mentioned it... But that still doesn't make it OK!"
    ast "All I did was tell Susan to walk home!"
    ast "Why is it my fault if she walked through the great hall covered in {b}your{/b} cum?"
    ast "I never told her to do that!"
    m "..."
    ast "Besides, it's not like there was anyone who didn't think she was a slut anyways..."
    m "..."
    ast "Well... Say something! When are you going to fire that old hag?"
    m "Unless you think Azkaban is better than a spanking, I think we should keep miss Tonks around."
    ast "*Pffft* I knew you'd be useless!"
    m "We could slow down with the spells until she cools off, if you think that would help."
    ast "And just let her get away with this?"
    ast "No... I'm just going to have to get back at her through Susan!"
    m "Susan?"
    ast "Of course! If she wasn't such a cow none of this would have happened."
    ">With that, Astoria hops up onto your lap in her tiny skirt, giving you a dangerous look at the witches' thighs."
    ast "Now, hurry up, Dumby! I'll never get my revenge at your reading pace!"

#Tonks spends the whole time rubbing Astoria's butt
label astoria_tonks_6:





### REPEATABLE RANDOM EVENTS ###
label astoria_tonks_random:
    $ random_number = renpy.random.randint(1, 3)

    #Tonks is into beast stuff?!
    if random_number == 1:
        #call play_music("fun")
        call play_sound("door")
        call ast_main("","pout","base","base","R",xpos="right",ypos="base")
        pause.5

        call nar(">Astoria casually walks into your office, mindlessly looking around.")
        m "Well, how was it?"
        call ast_main("Nothing special, [ast_genie_name].","pout","base","base","L")
        call ast_main("We were mostly just drinking tea and talking...","pout","base","base","R")
        call ast_main("There was a book on her shelf that caught my eye and I wanted to ready it...","open","base","base","mid")
        call ast_main("I think it was named Bestiary or Bestiality or something...","open","narrow","narrow","R")
        call ast_main("She wouldn't let me read it though... I wonder why...","pout","base","base","down")
        m "(...)"
        m "Want to cast some spells, [astoria_name]?"
        call ast_main("Of course, [ast_genie_name]!","grin","base","base","down")

    #Tonks is the best!
    if random_number == 2:
        call play_music("fun")
        call play_sound("door")
        call ast_main("","grin","base","base","mid",xpos="right",ypos="base")
        pause.5

        call nar(">Astoria merrily walks into your office, humming a tune as she closes the door.")
        m "So... how was your day?"
        call ast_main("It was amazing, [ast_genie_name]!!!","scream","wide","wide","wide")
        call ast_main("Tonks showed me her creature book! All the magical creatures she's encountered over her years as an Auror!","open","base","base","mid")
        call ast_main("A giant, a werewolf, even a vampire!","grin","angry","angry","mid")
        call ast_main("She's sooooo cool, [ast_genie_name]! The best teacher we've ever had here at this lame school!","grin","happyCl","base","mid")
        m "I'm glad to hear that."
        m "Want to cast some spells?"
        call ast_main("Hihihi-- of couse!","grin","base","base","mid")

    #Tonks sucks!
    if random_number == 3:
        #call play_music("fun")
        call play_sound("door")
        call ast_main("","pout","angry","angry","R",xpos="right",ypos="base")
        pause.8

        call ast_main("I hate her, [ast_genie_name]!","scream","closed","angry","mid")
        m "Tonks? Last time you said you liked her..."
        call ast_main("That was before she wanted me to clean up her whole staff-room!","scream","angry","angry","mid")
        call ast_main("Not to mention the horrible outfit she made me wear.","clench","angry","angry","R")
        m "Wait, what outfit?"
        call ast_main("I think she called it a maiden outfit, or something.","pout","angry","angry","L")
        call ast_main("I looked so stupid in it...","pout","angry","angry","down")
        if astoria_tonks_3_completed:
            call ast_main("She said if I really wanted to be a model, I'll need to wear whatever I'm told to wear.","open","closed","base","mid")
            call ast_main("Even if it meant wearing nothing at all, [ast_genie_name]! Can you believe that?!","scream","wide","wide","wide")
        m "Hmm..."
        g9 "I would love to see you in that outfit too!"
        call ast_main("Not a chance!","clench","angry","angry","mid")
        call ast_main("Good night, [ast_genie_name]!","open","closed","base","mid")
        m "Wait, don't you want to--"
        hide screen astoria_main
        with d3
        pause.5

        call nar("Astoria quickly stomps out of your room.")

        $ astoria_busy = True

        call play_music("night_theme")
        jump night_main_menu

    #ADD more random Tonks events.

    jump astoria_requests
