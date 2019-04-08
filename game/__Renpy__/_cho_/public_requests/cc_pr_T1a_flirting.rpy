

### Flirt with the other Quidditch players ###

# Start
label cc_pr_flirt_start:

    # Intro
    if cc_pr_flirt_OBJ.points == 0:
        m "[cho_name], to continue your training I'll need you to get more involved with the other players."
        cho "With whom? The Gryffindor team?{w} Slytherin?"
        g9 "No, our focus will be on your own team!"
        cho "Ravenclaw?"
        m "For now, at least..."
        g9 "It's an idea I had after you've told me that you shower with them!"
        cho "(I knew I shouldn't have told him...)"
        cho "What idea did you have?"
        g9 "I need you to bond with them more! Acquire a deeper connection to your fellow team-mates!"
        cho "I can see why that would be benefitial to us. To strengthen our camaradery..."
        m "Yeah yeah... That's what I was going for."
        cho "And how would you suggest I do that, [cho_genie_name]?"
        g9 "Do what you girls do best! Flirt with them!"
        cho "Flirting? With my team?" # Shocked
        cho "[cho_genie_name] I don't think I can do that! I've known them for years!"
        cho "(They'd just think I'm acting weird...)"
        m "Just try it once, and we'll see what happens."
        cho "I'd rather not."
        m "If you question my methods, we might as well stop right here and you can say your Quiddtch-cup goodbye!"
        cho "(...)"
        cho "Very well, [cho_genie_name]."
        cho "But if they laugh or make fun of me we'll stop this at once!"
        m "Fine by me."
        m "Return to my office after classes and tell me how it went."
        cho "Ok, [cho_genie_name]."
        cho "See you after classes..."
        g9 "Off you go!"

    # Repeated
    else:
        m "I need you to have an eye on the other Quiddich players again."
        g9 "Flirt with them a little bit. See how they behave around you..."
        cho "Of course, Sir."
        m "Please return after classes to tell me about it."
        cho "Of course!"
        g9 "Now, off you go!"
        cho "See you later, [cho_genie_name]."

    $ cc_pr_flirt_OBJ.inProgress = True

    $ cc_pr_flirt_OBJ.points += 1

    jump end_cho_event



# Return
label cc_pr_flirt_return:

    $ cc_pr_flirt_OBJ.inProgress = False

    jump end_cho_event



# Ideas

# Tier 1:

# Intro:
# Cho was unsuccessful with flirting and gets angry at Genie. # cho "What did you think would happen?"
# Cho meets Cedric who asks her out on a date. She declines. Genie tells Cho to tease him more next time.
# She stumbles upon Hermione who interrogates Cho on the spot.

# Random/Repeatable:
# Cho flirts with a member of her team but it gets awkward.
# Cho gets called a bro by one of her team members and she got angry about it.
# Cho again meets Cedric. She teased him by showing him her panties, lifting her skirt.

# Tier 2:

# Intro:
# Hermione stalks her.
# Cho meets Harry. She flashes her panties at him but he was unimpressed. Genie wonders if he maybe isn't into panties.
# Che meets Ginny. Ginny is teasing Cho actually and she's embarrassed about it.

# Random/Repeatable:
# Cho gets a polite kiss on her cheek by her team captain.
# Cho again tries to flaunt Harry. Maybe he could compliment her ass?
# Ginny watches her while doing squads.They have a little Chat. Ginny reveals that she likes Cho.
