

### Talk with Cho ###

label cc_pf_talk:

    # Tier 1
    if main_matches_won == 0:

        if cc_pf_talk_OBJ.level == 0:    # 0 Hearts.
            # Talk about her boyfriends.
            call cc_pf_talk_T1_E1

        elif cc_pf_talk_OBJ.level == 1:  # 1 Heart.
            # Talk about her Quidditch team.
            # Unlocks public requests favours.
            $ cho_requests_unlocked = True
            call cc_pf_talk_T1_E2

        else:                            # 2+ Hearts.
            # Talk about Cedric some more.
            call cc_pf_talk_T1_E3

    # Tier 2
    elif main_matches_won == 1:

        if cc_pf_talk_OBJ.level == 0:    # 0 Hearts.
            # Talk about Malfoy.
            call cc_pf_talk_T2_E1
        elif cc_pf_talk_OBJ.level == 1:  # 1 Heart.
            # Talk about Hermione.
            call cc_pf_talk_T2_E2
        else:                            # 2+ Hearts.
            # Cho gets bullied by the Slytherin Quidditch team.
            call cc_pf_talk_T2_E3

    # End event jump
    # (only used when the event isn't called.)
    label end_cho_talk_event:

        if main_matches_won == 0:
            if cho_whoring < 3: # Points til 3
                $ cho_whoring += 1

        elif main_matches_won == 1:
            if cho_whoring < 8: # Points til 8
                $ cho_whoring += 1

        if cc_pf_talk_OBJ.level < 3:
            $ cc_pf_talk_OBJ.level += 1

    # Stats
    $ cc_pf_talk_OBJ.points += 1

    jump end_cho_event



### Tier 1 ###

label cc_pf_talk_T1_E1: # Complete.
    m "Let’s have a little chat shall we."
    g9 "Just to get to know each other a little bit better."
    call cho_main("Of course, Sir.","smile","base","base","mid")
    m "First, I'd like you to come a bit closer."
    call cho_main("Very well, [cho_genie_name]...","soft","base","base","R")

    call cho_walk("desk", "base", speed=1.6)

    call play_music("chipper_doodle")
    call cho_main(face="happy",xpos="mid",ypos="base",trans="fade")
    call ctc

    call cho_main("What would you like to talk about?","soft","base","base","mid")
    m "Do you have a boyfriend, Miss Chang?"
    call cho_main("Excuse me?","open","wide","base","mid",trans="hpunch") # Shocked
    m "I asked if you have boyfriend. Anybody you fool around with?"
    call cho_main("Me? Professor? He-{w=0.8} hav-{w=0.5} a boyfrind?","open","wide","base","R") # Reluctant, Embarassed
    g9 "Or a girlfriend! That would be even better, now that I think about it!"
    call cho_main("Sir that's-{w} that's not something a headmaster should be concerned about.","open","base","sad","L")
    call cho_main("And I don’t see how this information would be of importance for my training.","open","wide","raised","downR")
    call cho_main("Why would it matter if- {w}Even if I did I'd-","soft","wide","base","down")
    g9 "So you don't have one?"
    call cho_main("You're making me nervous, [cho_genie_name]. {image=textheart}","horny","narrow","sad","R")
    m "(So cute.{w=0.5} Perhaps this is something I could push her further on...)"

    call cho_main("Sir, I do not have a boyfriend at the moment.{w} I hope that answers your question.","soft","closed","angry","mid")
    g9 "So, a girlfriend then?"
    call cho_main("!!!","angry","wide","raised","mid",trans="hpunch")
    call cho_main("No!","scream","closed","angry","mid",trans="hpunch")
    call cho_main("","annoyed","narrow","angry","mid")
    m "(She doesn’t seem that keen on the subject, perhaps I could tell her...)"

    label get_cho_to_talk:

    menu:
        "\"It's important to open up to your headmaster.\"":
            m "Emphasis on \"opening up\"..."
            call cho_main("I don't think that will be necessary, [cho_genie_name].","annoyed","narrow","angry","mid")
            m "There's a lot more to gather from discussing previous life choices than you might think."
            m "You get to learn a lot about the way someone has matured by previous experiences..."
            m "Like a first kiss, who it was with, and so on..."
            call cho_main("You think I'm mature?","soft","base","base","mid")
            g4 "(That's what she's focusing on?)"
            m "*Ahem*, yes.{w=0.5} Of course you are, don't you think so?"
            call cho_main("Well, my previous boyfriend didn't seem to think so...","open","base","raised","R")
            m "So you did have one?"
            call cho_main("*Ugh*{w=0.8} Fine...{w=0.8} I'll tell you about him...","soft","narrow","base","down")

            pass

        "\"It's okay if you like girls...\"":
            m "Swinging the other way, you know..."
            call cho_main("What?","angry","wide","base","mid")
            m "Some people like flicking the bean rather than rubbing a wand..."
            call cho_main("*Uhmm*, I never said I minded either way...","quiver","narrow","sad","R")
            m "So you have had a girlfriend?"
            call cho_main("I'd rather not talk about it right now...","soft","narrow","sad","mid")
            m "(Damn, maybe that's not the way to go about this, maybe instead I could tell her...)"

            jump get_cho_to_talk

        "\"Let me tell you something about my own previous relationships...\"":
            call cho_main("Sir, I'd rather not hear a boring old tale about any of your old flames...","open","narrow","base","R")
            g9 "Oh they weren't boring at all!"
            call cho_main("Hmm?","annoyed","narrow","base","mid")
            g9 "They were very intimate..."
            call cho_main("???","annoyed","base","raised","mid")
            g4 "Very sexual!"
            call cho_main("!!!","annoyed","wide","base","mid")
            g9 "Lots of acrobatic stuff!"
            call cho_main("NO Sir, please!{w=0.5} I don't want to know any of that!","scream","closed","angry","mid",trans="hpunch")
            call cho_main("(Gross!{w=0.5} Keep it to yourself...)","angry","narrow","sad","R")
            m "I just wanted to expand my backstory a little bit...{w=0.5} What's so wrong with that..."

            jump get_cho_to_talk

    # Cedric Diggory
    call cho_main("Cedric was my boyfriend during the time Hogwarts was hosting the \"triwizards tournament\".","soft","base","base","R")
    m "(They host tournaments here? Interesting...)"
    call cho_main("That year was the most fun I've ever had!","smile","base","base","mid")
    m "Was he that good?"
    call cho_main("What?{w=0.5} No, Sir, not because of him!{w} The tourney, [cho_genie_name]!","soft","narrow","base","mid")
    m "Sure..."
    call cho_main("We should have it every year if you were to ask me!","open","closed","base","mid")
    g9 "(A cosplay tournament is what this school needs...)"
    call cho_main("Sir that would be great!","smile","narrow","base","mid")
    g4 "(Wait, wait!{w=0.8} A \"nude\" cosplay tournament!{w=0.6} Even better!)"
    call cho_main("And with new contesters every month! You've got to do this, Sir!","smile","base","base","mid")
    m "I'll think about it..."

    m "Now tell me, how come you two ended up together?"
    call cho_main("Oh. Well...","soft","base","base","down")
    call cho_main("I have this thing for...{w=0.5} athletes.","horny","base","base","down")
    call cho_main("Cedric was the representative champion of our school, so of course I had to date him.","horny","base","sad","down")
    m "Of course..."
    m "(She's into athletes, so so...)"
    g4 "(You should see me, girl. I'm shredded!)"
    m "(Too bad you can only see the body of that wrinkly old geezer...)"
    m "(Maybe there's like a steroid spell...)"
    g4 "{size=-4}Plexus maximus!{/size}"
    call cho_main("Did you say something?","soft","base","raised","mid")
    m "Oh, it was nothing... go on."

    call cho_main("Anyway, Cedric even put his life at risk during the whole thing.","open","base","base","R")
    m "Oh you poor, poor thing..."
    m "I can see why you didn't want to mention him before then..."
    call cho_main("Why?","soft","narrow","raised","mid")
    m "He surely will be missed."
    call cho_main("Sir?","angry","narrow","base","mid")
    m "Died just the way he lived,...{w} as a plot device."
    call cho_main("Sir, Cedric isn't dead.","open","angry","angry","mid")
    m "Oh...{w} he's not?"
    call cho_main("No!","annoyed","narrow","angry","mid")
    m "I could've sworn I read that somewhere..."
    m "Are you sure he's still around?{w} What if he \"did\" die, but then he returned from the dead?"
    g4 "For all you know he could be a vampire!"
    call cho_main("Sir, you're talking nonsense...","annoyed","angry","angry","R")
    call cho_main("Please don't joke about your student like that. It's so unlike you...","open","closed","base","mid")
    call cho_main("He's one of your bests! The best student \"Hufflepuff\" has ever seen!","open","base","base","mid")
    m "A \"Hufflepuff\"? Well, that explains everything..."
    m "If he's such an exceptionally great student, then why aren't you two still together?"
    call cho_main("Things didn't work out, naturally...","open","base","raised","R")
    call cho_main("The tourney ended, and he didn't win, so...","soft","base","raised","down")
    m "So you two broke up?... Because he didn't win?"
    call cho_main("That was one of the reasons...","soft","base","base","downR")
    call cho_main("There is also the fact that he's on the \"Hufflepuff Quidditch team\", as their Seeker.","open","base","base","mid")
    call cho_main("It's our last shot at winning the Quidditch house cup, for the both of us.","angry","base","base","down")
    call cho_main("We'd constantly be at each other's throats.","soft","narrow","angry","mid")
    g4 "Intriguing!"
    m "You are missing out, girl..." # Small text
    g9 "{size=-4}Hatesex is the best!{/size}" # Small text
    call cho_main("I didn't quite hear that, Sir.","base","base","base","mid")
    m "Who else did you do it with?"
    call cho_main("Do it with?","soft","narrow","raised","mid") # Shocked
    m "Smooshing, kissing, snogging,...{w} whatever you call it nowadays..."
    call cho_main("With all due respect, Professor, it's very odd that you'd ask me about those sort of things...","open","closed","base","mid")
    call cho_main("But,... you \"are\" helping me.{w} So I guess I owe you that much...","annoyed","base","base","R")
    g9 "That's what I wanted to hear."

    # Fleur
    call cho_main("Well, Cedric wasn't the only one I was with during the year of the tourney...","open","base","raised","down")
    g9 "Is that so...{w} feel free to elaborate!"
    call cho_main("I was sort of dating somebody else....","quiver","base","sad","downR")
    call cho_main("At the same time.","horny","base","sad","R") # Embarrassed
    m "No{w} way!"
    g4 "You were cheating on that Hufflepuffer?"
    call cho_main("I wouldn't call it cheating, Professor. It wasn't even that serious with Cedric to begin with.","annoyed","narrow","base","mid")
    call cho_main("I had a unique opportunity that's all...","soft","base","base","R")
    call cho_main("One of those \"no strings attached\" kind of things... Trying out new stuff...","smile","base","base","L")
    m "Like what?"
    call cho_main("Dating a girl, for example.","base","narrow","base","mid")
    g9 "(Finally this gets interesting!)"
    call cho_main("She was one of the students from Beauxbaton.","soft","base","base","downR")
    m "(...)"
    call cho_main("A French girl.","soft","base","base","down")
    g9 "And I hope you also frenched that french girl!"
    call cho_main("Among other things...","angry","closed","sad","mid") # Super embarrassed
    call cho_main("(Why am I telling him this?)","horny","narrow","sad","R")
    g9 "And who was it?"
    call cho_main("Fleur Delacour.{w} She was also a champion at the tourney.","soft","base","sad","mid")
    g4 "I'm in shock!"

    # Viktor
    call cho_main("Then there also was Viktor Crum who-","open","base","base","R")
    with hpunch
    g4 "Slow down, girl! I'm still not over the fact that you made out with a girl!"
    call cho_main("","annoyed","narrow","base","mid")

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_chang
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call bld

        "-Participate in the conversation-":
            $ masturbating = False

    g9 "I want to hear everything!"

    call cho_main("I'm sorry, Sir. It's just that...","open","closed","raised","mid")

    if daytime:
        call cho_main("I'm really late for classes. May we postpone this talk to some other time?","soft","narrow","sad","R")
    else:
        call cho_main("It's getting really late. May we postpone this talk to some other time?","soft","narrow","sad","R")

    if masturbating:
        g4 "What? Please don't go now. I've only just started!"
        call cho_main("Started with what, [cho_genie_name]?","annoyed","narrow","angry","mid")
        g4 "I'll give you 10 house points if you stay!{w=0.8} Just a tiny bit longer!"
        call cho_main("And what makes you believe that I'd agree to such a thing? Getting rewardred with points for doing nothing?","open","closed","base","mid")
        call cho_main("Earning house points in such a way is despicable, and it would be unfair towards the other school houses, as well as my fellow students...","open","narrow","base","mid")
        call cho_main("","annoyed","narrow","angry","mid")
        g4 "Fifty points?"
        call cho_main("I have to go now, Sir.","soft","closed","raised","mid")
        m "(Fuck me...)"

        call gen_chibi("sit_behind_desk")
        with d3
        pause.8

        call cho_main("Until next time!","base","narrow","base","mid")

    else:
        m "Okay, girl. You may leave..."
        call cho_main("Thank you, Sir.","base","base","base","down")
        call cho_main("See you next time.","smile","base","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    call bld
    m "(...)"
    if masturbating:
        m "Well, I got blue-balled..."
        m "Feel like I've deserved it..."

    return



# Second Event
label cc_pf_talk_T1_E2: # Complete.
    g9 "Get closer, [cho_name]..."
    call cho_main("...","annoyed","base","base","down")

    call cho_chibi("stand","desk","base")

    call play_music("chipper_doodle")
    call cho_main("","annoyed","narrow","angry","mid",xpos="mid",ypos="base",trans="fade")
    call ctc

    call cho_main("Another talk, Professor?","soft","narrow","angry","mid")
    call cho_main("Are we going to discuss my previous relationships again?","open","narrow","base","R")
    g9 "I don't know.{w} Would you like to?"
    call cho_main("I'd rather not.","soft","narrow","angry","mid")
    m "Tell me about yourself then."
    call cho_main("Of course, [cho_genie_name].","smile","base","base","mid")
    call cho_main("We did a couple more Quidditch session yesterday.{w} To get ready for our big game against \"Hufflepuff\".","open","narrow","base","mid")
    call cho_main("Our team really believes that we have a chance to win this time!{w} They got a great boost in confidance after I've told'em that the great \"Albus Dumbledore\" would be training us himself!","smile","base","base","mid")
    m "Are you getting along with your team well?"
    call cho_main("I'd say so.{w} But there has been a time when...","soft","base","base","mid")
    call cho_main("Let's just say that it has been difficult for me at first. After all Quidditch is largely dominated by men...","open","narrow","sad","down")
    call cho_main("Getting accepted into our Quidditch team was a challenge. I really had to prove I was worth it.","angry","narrow","sad","mid")
    g9 "And how exactly did you manage that? Mind spilling the beans?"
    call cho_main("Through diligance, expertice, and determination!","open","closed","base","mid")
    m "(...)"
    m "I was sort of expecting something else entirely but,... you do you..."
    call cho_main("And as you can see it did work out in my favour, Sir.","open","base","base","mid")
    call cho_main("Very few teams have allowed a female player into their ranks over the past years.","open","narrow","angry","mid")
    call cho_main("And I've been the only female seeker at this school in over half a century.{w} Can you even believe that, [cho_genie_name]?","open","wide","base","mid")
    m "(A century? That's like a coffee brake for me girl...)"
    call cho_main("I don't want to brag, [cho_genie_name], but the role of a seeker is \"the\" most important position in a team by far!","smile","narrow","base","mid")
    call cho_main("If you don't have a good seeker, you have no chance of winning!","soft","closed","base","mid")
    m "Which is why you need my help so badly..."
    m "Because you are great at it..."
    call cho_main("That we're losing is neither my fault, nor my team's, [cho_genie_name]!","annoyed","base","angry","mid")
    m "So who's is it then?"
    call cho_main("The enemy team's, obviously!","soft","narrow","angry","mid")
    call cho_main("They are cheating! And they have done so for years!","open","narrow","angry","R")
    call cho_main("This is my last chance! And I'm growing more and more desperate with my situation...","angry","narrow","angry","mid")
    m "(...)"

    menu:
        "-Jerk off while she is talking-":
            hide screen cho_chang
            hide screen bld1
            with d5
            pause.5

            call gen_chibi("jerking_off_behind_desk")
            with d3
            pause.8

            $ cho_jerk_off_counter += 1
            $ masturbating = True

        "-Participate in the conversation-":
            $ masturbating = False

    call cho_main("Ever since I was a little girl Quidditch has been my dream...","quiver","narrow","sad","down")
    call cho_main("[cho_genie_name], can you imagine how \"hard\" it was for me?","soft","narrow","sad","mid")
    if masturbating:
        g4 "{size=-4}Yes, yes... It's so hard for you, you little slut!!!{/size}"
    call cho_main("How difficult it was for me at first?","open","narrow","sad","R")
    call cho_main("Getting accepted?","soft","closed","sad","mid")
    if masturbating:
        g4 "{size=-4}I'd accept your ass on my cock if you're in such a need for acceptance, you whore!{/size}"
    call cho_main("I'm the only female in my team. Constantly surrounded by other men...","soft","base","sad","down")
    if masturbating:
        g4 "{size=-4}Yes! Yes! And they all would like to have their way with you!{/size}"
    else:
        m "(Quite a sausage-party this Quidditch I have to admit.)"
        g4 "(Maybe telling Hermione off was a bad idea after all...{w} An \"all female\" team would be more fun to watch...)"
    call cho_main("I can constantly feel their gazes behind my back...","angry","base","sad","down")
    call cho_main("My own team, [cho_genie_name]!{w} They treat me like the plague!","upset","base","sad","mid")
    call cho_main("They ignore me during classes...","soft","closed","base","mid")
    call cho_main("When we're in our dormitories they are going out of their way to not cross paths with me...","annoyed","narrow","angry","R")
    call cho_main("And in the showers they're scared to even look at me!","angry","angry","angry","mid")
    if masturbating:
        g4 "{size=-4}Yes, yes!{w} Even in the showers you who-{/size}"
        with hpunch
        m "Wait a bloody minute!{w} You shower \"with\" your team?"
    else:
        m "The showers?{w} You shower \"with\" your team?"
    call cho_main("Of course, [cho_genie_name]. It was after my request, after all.","soft","base","raised","mid")
    g4 "No kidding?"
    call cho_main("They shouldn't exclude me from team activities just because I'm a girl.","open","base","base","R")
    call cho_main("It makes absolutely no difference!","base","base","base","mid")
    if masturbating:
        g4 "You are naked with them? In the shower?"
    else:
        m "Just to be clear. You are naked with them, in the shower."
    call cho_main("Of course we're all naked, [cho_genie_name]!","soft","base","angry","mid")
    call cho_main("Why would I take showers with my clothes still on?","soft","closed","base","mid")

    # Genie cums.
    if masturbating:
        g4 "{size=-4}You exhibitionistic slut!{/size}"
        g4 "*Argh* {size=-4}Here it comes!{/size}"

        call cum_block
        call gen_chibi("cumming_behind_desk")
        with d3
        pause.8

        call bld
        g4 "*heavy breathing* {size=-4}Take it!{/size}"

        call cum_block
        call cho_main("","base","narrow","raised","mid")
        g4 "*Argh!* {size=-4}Shower in this, you slut!{/size}"

        call cum_block
        call cho_main("[cho_genie_name], are you alright?","quiver","wide","base","mid")
        call cho_main("You're sweating and breathing quite heavily...","quiver","base","base","mid")

        call gen_chibi("came_on_desk")
        with d3
        pause.8

        call cho_main("Shall I get Madam Pomfrey to check on yo-","soft","narrow","base","mid")
        g4 "No, no! I'm..."
        m "I'm done.{w} Lets get back to the topic."
        call cho_main("Which was?","open","wink","raised","mid")
        m "You taking a shower with your \"teammates\"..."
        call cho_main("(...)","annoyed","narrow","angry","mid") # Annoyed

    m "Don't you think, the fact that they've seen you naked has no affect on their actions?"
    call cho_main("Why would it, [cho_genie_name]? We're all adults here...","soft","closed","base","mid")
    m "Maybe that's your response to it, girl."
    call cho_main("","annoyed","narrow","angry","mid")
    g9 "Maybe your \"teammates\" aren't as... \"mature\" as you."
    call cho_main("I've known my team for years.{w} We're all professionals!","soft","narrow","base","mid")
    m "Let me ask you a question..."
    m "In the showers,{w} do they all have their backs turned towards you?"
    call cho_main("I don't know. Maybe they uhm-...","open","base","base","mid")
    call cho_main("!!!","scream","wide","raised","mid") # Cho remembers something?!
    g9 "Yes?"
    g9 "What is it?"
    call cho_main("May I... May I leave, [cho_genie_name]?","quiver","closed","base","mid")
    g9 "Don't want to tell me?"
    call cho_main("No...","quiver","closed","sad","mid")
    m "Fine...{w} you may leave..."
    call cho_main("Thank you, [cho_genie_name].","soft","wink","sad","mid")

    # Cho very slowly walks out of your office...
    call cho_walk(action="leave", speed=3)

    call bld
    m "(...)"
    g9 "(That just gave me an idea!)"
    stop music fadeout 1.0

    $ cho_requests_unlocked = True
    call give_reward(">You can now buy \"Public Requests\" from Cho! (They are optional to her training.)","interface/icons/head/head_cho_1.png")


    return



# Third event
## Asking more questions abour her ex boyfriends and jerking off.

label cc_pf_talk_T1_E3: # Incomplete. Not posed.

    m "Care to tell me more about Quidditch?"
    cho "Of course, [cho_genie_name]. Anything specific you'd like to know?"
    m "Yes. Let's talk some more about Diggory..."
    g9 "Your ex-boyfriend."
    cho "{size=-4}I knew I shouldn't have told him...{/size}"
    cho "Why do you have to keep bringing that up, Sir? What's past is in the past..."
    m "I believe otherwise..."
    g4 "Did you already forget that he's our enemy?!"
    m "Your relationship with him is of the utmost importance right now!"
    m "I need to know every tiny bit of detail about the two of you."
    g4 "What you were doing when you were together. How often you made out with him. The exact locations where he touched you..."
    cho "What?!"
    m "As well as his sexual preferences. Secret fetishes he might have. Everything!"
    cho "I will not tell you any of those things!"
    g4 "Didn't you say you wanted to win?"
    cho "I did, Sir... But..."
    m "What did he like about you? Tell me! Maybe we can use it to our advantage!"
    cho "Okay, [cho_genie_name].{w} I'm willing to cooperate..."
    cho "Cedric was never too interested in me. His mind was always somewhere else. Drifting off..."
    cho "He always had this dead look in his eyes. Except for when-"
    cho "(...)"
    m "Yes? Go on..."
    cho "He had this weird, unhealthy obsession with my panties, Sir."

    if huffl_matches_won == 0:
        m "A panties obsession? So so…"
    else:
        g9 "Ha! I knew it!"

    cho "It was almost creepy how often he tried to look up my skirt."
    cho "And he’d always walk behind me when we went up the stairs, to get a better view I bet..."
    m "Did you ever show them to him?"
    cho "My panties?"
    m "No, your good manners... Yes, your panties!"
    cho "Why would I have wanted to? We weren’t that close!"
    m "So you were not close enough for a healthy relationship?"
    cho "What?"
    m "What kind of girl doesn't show her panties to her beloved?"
    cho "That’s just ridiculous..."

    if huffl_matches_won == 0:
        m "But, that made me think…"
        m "If he’s as obsessed with panties as you say, why don’t we use that information to our advantage?"
        cho "Like how?"
        m "We use them as a distraction!"
        m "Now we only have to find out how to show them off properly during the game."
        cho "I have to say I don’t like this notion one bit. But it might be worth a try..."
    else:
        m "Well, it worked."
        m "Beating him at Quayditch was almost too easy!"
        cho "Quidditch, Sir..."
        m "All we had to do was put some good-old panties in front of his face..."
        g4 "And he was like a wild goat chasing after them!"
        cho "A goat?"
        m "Yes. Don't you have those here?"
        cho "I'm still surprised how well that worked out, if I'm honest."
        m "You’re welcome."

    return


### Tier 2 ###

label cc_pf_talk_T2_E1: # Incomplete. Not posed.

    m "Could you tell me anything about who we are up against next?"
    cho "Our next game is against the Slytherin team."
    g9 "(Sweet! I will win Snape's bet sooner than I thought!)"
    m "Are they better than Hufflepuff?"
    cho "They are, by quite a bit."
    cho "However, Hufflepuff only had one really good player. Which was Cedric."
    cho "Slytherin on the other hand, they are almost unbeatable. They might even be better than Gryffindor!"
    m "You don't say. So why are they next and not Gryffindor?"
    cho "Because of their seeker, he's...{w} so,{w} so bad!"
    m "Who is?"
    cho "Draco Malfoy, Sir."
    m "Any chance you fooled around with him too?"
    cho "*Tzzzz* I'd never surround myself with Slytherin scum."
    m "I guess you and Granger have at least something in common..."
    cho "His daddy bought their whole team new brooms, which is the only reason they've let him in."
    m "His daddy?"
    cho "His father, Sir."
    m "Oh. I thought you might be talking about a different \"daddy\"."
    cho "Very funny, [cho_genie_name]..."
    cho "In any case, dealing with him won't be an issue at all! It's their team I'm more worried 'bout..."
    cho "You don't just win by catching the snitch first. You also have to be leading in points!"
    cho "If you catch the snitch too early, the game will be over."
    cho "That's how Slytherin won most of their games in the past. They win by letting the other seeker catch the Snitch..."
    m "Those rules are so idiotic..."

    # Plan how to deal with Slytherin's team.

    # Cho leaves.

    return


label cc_pf_T2_talking_2: # Incomplete. Not posed.

    # Cho is angry about Hermione.
    # Talks about all the things she'd do to her.
    # You get the option to jerk off.
    # Cho really gets into it.
    # If you are not masturbating, Genie says "fuck it" and starts jerking off regardless.
    # Cho notices you jerking off.
    # She finds it repulsive and disgusting.
    # She insults you which gets you off.
    # She angrily leaves...

    m "Miss Chang, with our Quidditch talk out of the way, I thought you maybe wanted to talk about your regular school life with me."
    cho "Very well, Sir. Anything in particular you'd like to hear about?"
    m "Not necessarily. Why don't you surprise me? Has anything interesting happened to you lately?"
    cho "I feel like people have shown me more affection even since our game against Hufflepuff."
    m "You don't say..."
    m "Do you have any idea why that might be?"
    cho "Because of our win, of course!"
    m "And it had nothing to do with the fact that half the school got to see your panties?"
    cho "No! Of course not!"
    cho "Please don't try to diminish my achievement, Sir!"
    cho "It's like I'm a celebrity now! I'm getting so much attention!"
    cho "It never happened that Ravenclaw won a game. And I made that possible!"
    m "Hey don't you forget about me."
    m "Where would you be without the great Dooblydore..."
    cho "Of course, Sir! Sorry, Sir!"

    menu:
        "Jerk off":
            $ masturbating = True
            m "Please, don't let me interrupt your thought..."
            g9 "I'd like to hear more!"
        "Don't":
            $ masturbating = False
            m "(No, I need to focus!)"
            m "Please, don't let me interrupt your thought..."
            m "Continue..."

    cho "Of course, Sir."
    cho "It's fun getting all of the boys attention! And seeing how jealous it makes all of the girls!"
    cho "Especially Granger!"
    if masturbating:
        g4 "Yes, the Gryffindor whore!"
    cho "You should see her face, [cho_genie_name]. She's so angry at me! I love it!"
    cho "She can't even bear to look at me anymore."
    cho "You should know, for whatever reason, almost all of Hufflepuff faults her for helping Ravenclaw secure the win!"
    cho "Several times she announced that Hufflepuff was leading in points, while they actually weren't!"
    cho "Which resulted in Hufflepuff playing far more defensively, when they should have been aggressive!"
    if masturbating:
        g4 "Oh you are one of those girls! I like going aggressive!"
    cho "I catched the Snitch at just the right time! If we wouldn't have been in the lead, we would have lost!"
    cho "I really need to thank Granger the next time I see her. I owe her a great deal..."
    if masturbating:
        g4 "I'd love to watch you thank her!"
        cho "Maybe I'll do something fun with her the next time I see her..."
        cho "Do something that would rile her up even more!"
    else:
        m "Yeah? How would you thank her?"
        cho "I don't know. Something that would rile her up even more!"
    cho "Like a kiss on her cheek, or an unconfortably long hug!"
    cho "Or I'll do something more naughty! Something she'd never expect!"
    g4 "*Argh!*"
    cho "Give her a proper kiss on the lips, perhaps?"
    cho "I bet a prude like her would be \"so\" shocked by that! I might even be her first!"
    if masturbating:
        g4 "Yes! You fucking sluts!"
    else:
        g4 "(Fuck it, this is too much!)"

        menu:
            "Jerk off":
                $ masturbating = True
                g4 "Please, continue!"

    cho "Oh, I'm sorry, Sir."
    cho "I forgot I was talking to you for a minute."
    cho "I sometimes can get a bit vitriolic when it comes to Granger..."
    cho "She's making my blood boil! That know it all, pretentious little bitch!"
    cho "Excuse my language, Sir."

    g4 "Yes, yes! How nasty!"


    call cho_main("I know exactly what you are doing!","angry","closed","angry","mid")
    call cho_main("Stop!","open","closed","angry","mid",trans="hpunch")
    call cho_main("Touching!","scream","angry","angry","mid",trans="hpunch")
    call cho_main("Yourself!!!","angry","angry","angry","mid",trans="hpunch")
    g4 "Jeeze..., no need to scream like that..."
    hide screen bld1
    with d3
    pause.2
    call gen_chibi("sit_behind_desk")
    pause.8
    call bld
    m "I will stop...{w} scratching...{w} my leg..."

    return


label cc_pf_T2_talking_3: # Incomplete. Not posed.

    menu:
        "Jerk off":
            $ masturbating = True
        "Don't":
            $ masturbating = False

    if masturbating:
        m "You don't mind if I..."
        cho "Mind doing what?!"
        cho "Oh..."
        m "I have urges, girl."
        cho "If you can't help yourself, Sir. I don't really care anyways..."
        g9 "Awesome!"
        cho "I have more important matters on my mind."
        m "Like what?"
    else:
        m "How's school? Anything to report?"
        cho "Rather boring, and uneventful as always, Sir."
        cho "That is, if constantly getting bullied is the new norm at this school..."
        m "You are getting bullied? By whom?"

    cho "The Slytherin Quidditch team. They've been total dicks lately..."
    m "You don't say.{w} What did they do?"
    cho "They've been harassing my team..."
    cho "Well mostly me, actually." # Embarrassed
    m "So,... would you like to report them?"
    cho "No, Sir."
    m "No?"
    cho "I do not endorse their behaviour, Sir. And I hope no other student has to share the same harassment that I receive."
    cho "Unless maybe Granger..." # Small text.
    cho "But{w}, watching them succumb to me has been rather fun..."
    m "Succumb to you?"
    cho "Yes. They're so desperately trying to embarrass me. To make me doubt myself before the big game..."
    if masturbating:
        g4 "Those asshole bullies... Show them who's boss!"
    else:
        g9 "And a strong, independent woman like yourself would never be intimidated by puny Slytherins!"
        cho "Of course not, Sir."
        g4 "I'm so proud!"
    cho "They think they can intimidate me. After all I'm only a small girl, and they are a group of ugly, brainless brutes!"

    # Add section here.
    # Cho describes what they have been doing to her.

    cho "But that's where they are mistaken!{w} They should be scared of me, [cho_genie_name]!"
    if masturbating:
        g4 "Yes! Show them what a slut you are!"
    cho "Of what I'm capable off!"
    if masturbating:
        g4 "*Argh!* I'm getting close!"
    cho  "Scared of what's about to come!"

    # Genie cums.
    if masturbating:
        g4 "Yes! Yes! It's coming!"
        call cum_block
        g4 "*Argh!* Take it!"

    else:
        g4 "I am scared already!"




    return



###  Stretching ###

label cho_stretching: # Not in use.

    #If you begin masturbating:
    #Tell me how you get ready for practice...

    #If you don’t masturbate:
    #How about you do some squats for me...

    # Choice to start jerking off
    menu:
        "\"(I will jerk off a little while she talks.)\"":
            $ cho_jerk_off_counter += 1
            $ masturbating = True
        "\"(I’ll ask her to show her flexibility instead.)\"":
            $ masturbating = False
            m "In that case..."

    #Tell me how you get ready for practice:
    if masturbating:
        m "How about you start by telling me a little bit about your Quidditch training. How do you get ready for practice for example?"
        cho "Okay..."
        cho "Well, we usually wake up pretty early in the morning..."
        "You take your cock out and begin stroking it underneath your desk"
        cho "Once I’m up I usually start by doing some stretches to get the blood flowing."
        g4 "\"Keep talking and you’ll get mine going pretty soon.\""
        cho "Sometimes I’ll have to do it in the dark not to wake anyone up..."
        m "\"Wakey wakey..."
        cho "As during later parts of the year the sun hasn’t even risen yet!"
        g9 "\"There we go, it’s risen... Good morning!\""
        cho "When I’m done with stretching I get dressed and make myself down to the great hall for breakfast..."
        g4 "\"Hhng... nude stretching...\""
        cho" As a player on a Quidditch team we get the whole hall to ourselves and a specially protein rich and energy filled filled breakfast."
        m "\"Yes, protein rich... that’s important. I’ll have to remember that one...\""
        cho "And then...{nw}"
        cho "Sir, are you still paying attention?"
        m "What?"
        # Genie stops masturbating
        cho "..."
        g9 "Protein rich breakfast... very important..."
        cho "Quite..."
        cho "Anyway..."



    #How about you do some squats for me:
    else:
        m "How about you start by doing some squats..."
        cho "Squats, sir?"
        m "Yes, squats... You know, bend your knees and stretch your arms forward..."
        cho "I know what squats are..."
        cho "I’m just a bit confused as to why you want me to start doing squats in your office."
        m "Well, I need to see if what you’re claiming is true. I’d like to see for myself if you’re really on par with the rest of your team."
        m "You’re asking a lot of me here if I were to break up any sort of student movement for you."
        cho "I don’t...{nw}"
        m "Unless what you’re saying is just a lie and you’re also just one of those amateur posers that you mentioned..."
        cho "..." # Annoyed, blushing
        cho "I’m not... look! Can a poser do this?"
        # cho squats down (could just be sprite for starter)
        # Later on if we add more chibi positions she’d show off even more here
        m "Impressive..."
        cho "Thank you..."
        m "How about a handstand?"
        cho "A handstand..."
        cho "That hasn’t been part of my training so far..."
        m "I see.."
        cho "But I could...{nw}"





label end_cho_favor:
    #if not first_cho_favor_done:
    #    $ first_cho_favor_done = True

    m "[current_payout] points to Gryffindor!"
    $ gryffindor += current_payout
    call cho_main("[cho_genie_name], I'm from Ravenclaw!","open","wide","raised","mid")
    m "Right, what did I say?"
    $ gryffindor -= current_payout

    m "[current_payout] points to Ravenclaw!"
    $ ravenclaw += current_payout
    $ cho_mood -= 10

    call cho_main("Thank you.","soft","base","base","mid")

    call nar(">Cho quickly puts her clothes on before leaving.")
    call load_cho_clothing_saves
    if daytime:
        call cho_main("Good day, [cho_genie_name].","smile","base","base","mid")
    else:
        call cho_main("Good night, [cho_genie_name].","smile","base","base","mid")
    call play_sound("door")

    jump end_cho_event
