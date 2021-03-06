#Regex find h\s+"([ -}]+)"
#Regex replace (call her_main\("\1","base","base" \))

#Title: Previously, at Hogwarts.
label prev_at_hogwarts:
    #Story Unlock requirements: Finish the first 3 Wizard Cards challenges.

    #Temporarily stored vars
    $ temp_date = day
    $ temp_gold = gold
    $ temp_day = daytime
    $ temp_color = interface_color
    $ temp_weather = weather_gen

    stop weather
    call play_music("stop")
    show screen blkfade
    with d9

    $ day = 1
    $ gold = 0
    $ daytime = True
    $ interface_color = "gold"
    $ weather_gen = 1
    $ show_weather()

    call room("main_room") # Hides all screens too.
    call gen_chibi("hide")
    show screen dumbledore

    pause 2

    centered "{size=+7}{color=#cbcbcb}Previously, at Hogwarts{w} school of Witchcraft and Wizardry...{/color}{/size}"

    pause 2

    call play_music("day_theme")
    hide screen blkfade
    with d9
    call ctc

    call play_sound("knocking")
    pause.8

    dum_[3] "Please, come in..."
    pause.2

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2.5)
    pause.5

    dum_[1] "Ah, Severus..."
    call sna_main("You called, sir?","snape_01",xpos="base",ypos="base")
    dum_[2] "Indeed, I wanted to talk to you about last night."
    call sna_main("Last night, sir?","snape_03")
    dum_[1] "Yes, last night... Don't think that I had forgotten already..."
    call sna_main("...","snape_04")
    call sna_main("I might have had a few. I hope I didn't say something inappropriate...","snape_05")
    dum_[2] "Quite... Do you remember why I hired you, Severus?"
    call sna_main("For my excellent potion making skills?","snape_25")
    dum_[1] "For your excellent potion making skills..."
    dum_[5] "{size=-6}And your piercing black eyes...{/size}"
    call sna_main("What?","snape_05")
    dum_[4] "What?"
    dum_[2] "I said, you're fierce and wise."
    call sna_main("...","snape_05")
    call sna_main("Why did you call me here again?","snape_03")
    dum_[1] "Ah yes, my apologies.... I got distracted."
    dum_[2] "How much do you remember from our previous discussion?"
    call sna_main("Not a lot... it's all a bit of a haze...","snape_04")
    dum_[1] "..."
    call sna_main("I think I mentioned a students spilling some flobberworm mucus down themselves which halted the whole lesson...","snape_01")
    call sna_main("And that Potter boy...","snape_08")
    dum_[3] "There it is..."
    call sna_main("The Potter boy?","snape_25")
    dum_[1] "Yes, I've noticed you've been quite stressed lately about this... Potter situation of yours for the lack of a better term."
    call sna_main("And your point?","snape_09")
    dum_[2] "Ah yes... my point."
    dum_[1] "Where was I again..."
    dum_[2] "Ah yes, your stress situation..."
    call sna_main("\"You're not really helping old man...\"","snape_08")
    dum_[1] "Have you tried a draught of peace?"
    call sna_main("What?","snape_03")
    dum_[2] "A draught of peace, it's a potion you know..."
    call sna_main("Are you joking with me right now?","snape_04")
    dum_[1] "I'm being quite serious... stress can be quite taxing on your body."
    call sna_main("I...","snape_01")
    call sna_main("I need a moment... I'll talk to you later Albus.","snape_06")
    dum_[1] "I thought we were getting somewhere..."
    call sna_main("...","snape_01")
    hide screen snape_main
    hide screen bld1
    with d3
    pause.2

    call sna_chibi("hide")
    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.2

    call sna_walk(action="leave", speed=2.5)

    call play_music("stop")

    dum_[2] "\"I don't think I'll ever understa-\""

    hide screen dumbledore
    show screen genie
    call teleport("desk")

    pause.8
    call bld
    m "..................?"
    m "Your majesty?"
    pause.2

    show screen blkfade
    with d9
    pause.8

    # Reset vars.
    $ day = temp_date
    $ gold = temp_gold
    $ daytime = temp_day
    $ interface_color = temp_color
    $ weather_gen = temp_weather
    $ show_weather()

    call room(hide_screens=True)
    jump enter_room_of_req



label a_spaced_out_conversation:
    $ temp_time = daytime
    $ interface_color = "gray"
    $ daytime = False

    call room("main_room")
    call music_block

    hide screen genie
    hide screen chair_right
    $ fire_in_fireplace = True
    show screen fireplace_fire
    show screen desk
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    show screen blkfade
    with d3
    pause.3
    hide screen blkfade
    with d3

    nar "The flames flickered higher up the fireplace."
    nar "Licking in greedy hunger as if wanting taste the wine the two men sedately drank just out of the fire’s reach."
    nar "The men took no notice of the flames, except to silently acknowledge the warmth it provided."
    nar "They were an odd pair, these two, sitting as they frequently did, beside the old fireplace sipping wine."
    nar "One, dressed all in black, with matching flowing black hair, stared sullenly at his glass."
    nar "Perhaps it was the darkness surrounding him that made his skin look so pale."
    nar "And maybe it was only the voluminous robes wrapped loosely across his body that made him appear gaunt."
    nar "The other was even more mysterious..."
    nar "Draped in gray-white costume, he had a long, flowing beard and a curious aura of both age and vitality."
    nar "Sometimes, if the flames flickered just so, he almost appeared entirely different, as a burly, cowled man with a short curled beard."
    nar "They sat in front of the fire as they did on many nights and talked of worlds upon worlds. And of magic. The dark man was first to speak."

    call sna_main("So, let me try to understand this,","snape_05",ypos="head")

    nar "Snape said slowly."

    call sna_main("You live in a little bottle?","snape_05")

    nar "The gray figure nodded."

    call sna_main("How does that work?","snape_05")

    m "I believe it’s based on tessaracted space."

    nar "Genie said, his tone becoming akin to a professor lecturing a class."

    m "The whole process is very Loki."

    nar "Snape didn’t hear the last words as a flicker and shadow from the flames made Genie appear different."
    nar "Almost as if gleaming golden horns arose from his head."

    call sna_main("Come again?","snape_03")

    nar "Snape asked, gaping at the sight before it was gone so fast that he was left unsure he had seen anything."

    m "I said, they keep the whole thing low key."

    nar "Genie repeated."

    m "Keeps most people from knowing how they make it bigger on the inside."

    call sna_main("Most people?","snape_05")
    nar "Snape asked."

    m "Well, Who knows..."
    nar "Genie answered."

    call sna_main("Do you know?","snape_24")

    nar "Snape asked."

    m "Who knows."

    nar "Genie repeated."

    call sna_main("So, who knows?","snape_08")

    nar "Snape asked again, getting a little irritated."
    nar "Patience was not a trait Snape had ever cared to master."

    m "Yes, Who knows!"

    nar "Genie said."
    nar "Snape flicked his hands impatiently and just decided to move on"
    nar "Determining when Genie was serious or not was still beyond his ability."
    nar "Plus, there had been another one of those weird flickers and he could have sworn he had seen a multicolor scarf around Genie’s neck."

    call sna_main("And, you then grant the summoner three wishes?","snape_01")

    nar "Snape continued."

    call sna_main("Anything they want? You can make anything come true?","snape_05")

    m "Those are the rules of my existence, yes."

    nar "Genie replied, thinking, not for the first time, how limited his real life was."

    call sna_main("That seems stupid.","snape_09")

    nar "Snape said bluntly."
    nar "Genie smiled. Snape was never much for niceties."
    nar "Genie found it refreshing to talk with someone whose disdain for others so matched his own."

    nar "Snape frowned at that smile. He got along almost perfectly with Genie."
    nar "Their lusts and passions were quite similar..."
    nar "It’s just Genie’s sense of humor that made Snape doubt his seriousness sometimes."

    call sna_main("You’ve got the power of a god,","snape_06")

    nar "Snape pushed forward."

    call sna_main("Can’t you just magic yourself free?","snape_05")

    m "It doesn’t work that way,"

    nar "Genie said sadly."

    g "I can only grant magic to others."

    nar "Snape shook his head."

    call sna_main("It still seems stupid...","snape_06")
    call sna_main("What if I were to visit you in your world and make one of my wishes that you be free to use your magic however you should please?","snape_09")

    nar "Genie stared at Snape with something like wonder."
    nar "It takes quite a bit to make an ageless being like Genie gape in awe."

    g5 "That’s...That’s brilliant!"

    nar "Genie shouted."

    g6 "Great Gods, man, that could actually work!"

    nar "Snape was taken aback by Genie’s enthusiastic shout, but quickly recovered."
    nar "He was happy for his friend’s excitement, but puzzled."

    call sna_main("Haven’t you ever thought of that before?","snape_05")

    nar "Snape asked."

    m "Well, no..."

    nar "Said Genie, and if ageless beings could blush, one would assume that’s what Genie would be doing."

    m "It’s not something that ever came up."

    call sna_main("No one suggested it to you?","snape_01")

    nar "Snape asked, hoping to skip past Genie’s discomfort."

    m "Surprisingly, when given three opportunities at your fondest dreams, helping others doesn’t seem to come up very often."

    nar "Genie said with a sarcastic edge that relieved Snape."

    call sna_main("Well, then...","snape_01")

    nar "Snape said."

    call sna_main("After we find a way to get you back to your home, maybe I could come visit you and we could work something out.","snape_28")

    nar "Genie eyed him curiously and then, with a bit of his usual humor asked,"

    g9 "Are you sure you could resist the urge to use all three on yourself?"

    nar "Snape chuckled. He momentarily considered how rarely he chuckled."
    nar "Not with humor, at least. He hadn’t really done that since..."

    call sna_main("Yes","snape_28")

    nar "Snape said with sudden certainty."

    call sna_main("There is really only one wish I would really want.","snape_23")

    nar "Genie raised an eyebrow at that, but let it stand."

    m "What would be your wish, my friend?"

    nar "He asked Snape kindly."

    call sna_main("I wish I could go back and have wooed Lily for my own","snape_23")

    nar "Snape said dreamily. In his mind’s eye, he remembered the flaming red hair that lit a fire in his own heart."

    call sna_main("I sometimes wonder if that would have made all the difference.","snape_29")

    nar "Snape mused."

    call sna_main("If I would have been a better, a kinder man than I am today.","snape_06")

    g9 "But would you have been as popular?"

    nar "Genie asked."

    g10 "you were central in every book and movie. Everyone loves you."

    call sna_main("What?","snape_05")

    nar "Snape snapped from his reverie. He looked at Genie in confusion."

    m "I mean, would you have been as powerful."

    nar "Genie said hastily."

    m "Wasn’t that rejection what drove you to your studies and your mastery?"

    nar "Snape eyed Genie suspiciously, but let the matter pass."

    call sna_main("Yes, but I would sacrifice all that to be rid of this loneliness.","snape_06")

    nar "Snape returned to his imaginings."

    m "Well, even if you didn’t stay together,"

    nar "Genie said mischievously,"

    m "you could at least have had a little fun with her. Maybe even take her on her wedding night."

    nar "Snape’s head snapped up angrily. How dare Genie sully the memory of Lily."
    nar "But then, a wicked thought entered his head."

    call sna_main("Hmm, what if the boy wasn’t really James’ after all?","snape_02")

    nar "Snape said, and the smile that formed on his face could have frozen the dancing fire beside them."

    call sna_main("Then, one day, I could reach out to that insipid boy, with his foolish fantasies about Potter and say, ‘Harry, I am your father!’","snape_28")

    nar "Genie nodded."

    g9 "It could work. You’ve got the black robes already. You just need the helmet."

    nar "Snape cocked an eyebrow in confusion. The flames leapt and danced and Genie flickered once again."

    g9 "No mind pay you."

    nar "Genie said."

    g9 "Darkness that path, take you it will."

    call sna_main("Um?","snape_29")

    nar "Snape stammered."

    m "What?"

    nar "Genie asked."

    call sna_main("For a moment there, I thought you...","snape_01")

    nar "Snape trailed off, reluctant to go on."

    m "You thought I what?"

    nar "Genie prodded."

    m "Out with it man!"

    call sna_main("I thought you looked all shrunken, like a deformed house elf.","snape_06")

    nar "Snape finally managed to say."
    nar "Genie laughed."

    m "Muppet?"

    call sna_main("No thanks, I’ll just have the wine,","snape_05")

    nar "Snape replied."

    m "I’m afraid that’s the last of it."

    nar "Genie said, looking mournfully at the bottle."
    nar "He eyed Snape through the red droppings of wine still remaining in his glass. It looked like Snape was bleeding."
    nar "The image disturbed him and he put his glass down."

    m "So..."

    nar "Genie coughed once, cleared his throat and continued."

    m "Did you mean it?"

    call sna_main("About the wishes?","snape_05")

    nar "Snape asked."

    m "Yes."

    nar "Genie said, unable to keep the excitement from his voice."

    m "Would you really come to my world and set me free with a wish."

    call sna_main("Why not?","snape_06")

    nar "Snape said."

    call sna_main("Assuming we can find a way to send you back.","snape_09")

    m "Right."

    nar "Genie said, sobering up."

    m "There’s that."

    nar "Snape looked at his friend and sensed his growing gloom."

    call sna_main("Cheer up, Genie.","snape_23")

    nar "He said, clapping the image of his old wizard master on the shoulder."

    call sna_main("We just need to be careful. We don’t want to make a mistake and send you somewhere crazy.","snape_05")

    m "Like a space station?"

    nar "Genie asked, his humor returning with his hope."

    call sna_main("Exactly.","snape_28")

    nar "Snape replied."
    nar "Not sure what a ‘space station’ was."

    call sna_main("We don’t want you to end up far, far away.","snape_24")

    m "In the final frontier?"

    nar "Genie asked, with a wink that to Snape always meant some kind of inside joke Snape never understood."
    nar "He decided to ignore it as he had many other times."

    call sna_main("Let me continue to research why your powers of transdimensional travel are muted here and we’ll find a way to fix your problem.","snape_05")

    m "Both our problems."

    nar "Genie suggested and this time, both of them laughed together."

    call sna_main("You know, Genie, this could be the start of a beautiful friendship.","snape_23")

    nar "Snape said, standing to leave."
    hide screen snape_main
    with d3

    m "Well, you know what the game devs say."

    nar "Genie replied, causing the dark man to pause and look back quizzically."

    m "Play it again, Snape."

    "The End"

    $ daytime = temp_time
    if daytime:
        $ interface_color = "gold"
    else:
        $ interface_color = "gray"
    call room(hide_screens=True)
    $ fire_in_fireplace = False
    hide screen fireplace_fire
    hide screen with_snape_animated

    call update_snape
    jump enter_room_of_req