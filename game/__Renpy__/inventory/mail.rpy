

label read_letter:

    $ letter = letter_queue_list[0]

    $ menu_x = 0.5
    $ menu_y = 0.9

    show screen letter
    with d5
    label read_letter_again:
    call ctc

    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump read_letter_again

    $ letter.mailRead()

    $ menu_x = 0.5
    $ menu_y = 0.5

    hide screen letter
    hide screen bld1
    with d5

    if letter.label != "":
        pause.2
        show screen bld1
        with d3

        $ renpy.call(letter.label)

        hide screen bld1
        with d3

        if letter.label == "letter_from_hermione_A" and day == 1:
            jump event_00 # First event with Snape.

    call screen main_room_menu


screen letter:
    tag letter

    add "interface/points/letter.png" at Position(xpos=340, ypos=30)
    hbox:
        spacing 40 xpos 410 ypos 80 xmaximum 250
        text letter.getLetterText()

    zorder 4



### Letter Attachment Call Labels ###

# Hermione Granger Letters.
label letter_from_hermione_A:
    m "Ehm..............................."
    m "What?"
    m "................................."

    return

# Ministry of Magic letters.
label letter_paperwork_unlock:
    m "Payments? Hm..."

    call give_reward(">From now on you can do paperwork at your desk in order to earn additional gold...","interface/icons/gold.png")

    return

label letter_paperwork_report:
    call update_report_money
    call give_reward(">You received {size=+4}"+str(report_money)+"{/size} gold coins.","interface/icons/gold.png")
    $ gold += report_money

    $ report_money = 0
    $ finished_report = 0

    return

label update_report_money:

    if game_difficulty <= 1: #easy
        $ report_money += 80*finished_report

    elif game_difficulty == 2: #normal
        $ report_money += 60*finished_report

    else: #hardcore
        $ random_number = renpy.random.randint(1, 10)

        if random_number in [1]:
            $ report_money += 10*finished_report
        elif random_number in [2]:
            $ report_money += 100*finished_report
        elif random_number in [3,4]:
            $ report_money += 30*finished_report
        elif random_number in [5,6]:
            $ report_money += 80*finished_report
        else:
            $ report_money += 60*finished_report

    return

label letter_curse_complaint:
    m "That doesn't sound good..."
    m "Perhaps I should tell Snape about this."
    m "Or maybe miss granger?"

    return

### Mail about cardgame ###
label deck_mail_send:
    $ deck_unlocked = True

    m "That last bit just sounds like scam to me..."
    m "..."
    m "I guess I'll have a look at the starter pack at least..."    
    
    #Randomize starter pack (Hardcore difficulty gets randomized at the start of the game)
    if game_difficulty <= 2:
        python:
            card_rand_realm = random.choice([iris, jasmine, azalea])
            card_rand_girl = random.choice([her_schoolgirl, sus_schoolgirl, cho_schoolgirl, lun_schoolgirl])
            card_rand_item1 = random.choice([item_desk, item_bird])
            card_rand_item2 = random.choice([item_beads, item_dildo, item_doll, item_condoms, item_plugs])
            card_rand_item3 = random.choice([item_barbell, item_lingerie, item_stockings, item_badge, item_bdsm, item_lipstick])
            card_rand_item4 = random.choice([item_bookchairs, item_bookgala, item_bookgala2, item_bookwaifu, item_hat])
            card_rand_item5 = random.choice([item_eromag, item_pornmag, item_girlmag, item_scroll, item_wine, item_sweets])
        
            unlocked_cards = [genie, card_rand_realm, card_rand_girl, card_rand_item1, card_rand_item2, card_rand_item3, card_rand_item4, card_rand_item5]
            playerdeck = [genie, card_rand_realm, card_rand_girl, card_rand_item1, card_rand_item2]
            # Delete copies of playerdeck cards
            for i in range(0,5):
                playerdeck[i].copies -= 1
    
    show screen blktone
    show screen start_deck
    with Dissolve(.3)
    pause
    hide screen start_deck
    hide screen blktone
    with Dissolve(.3)
    
    g9 "Hell yes I'm playing this..."
    call give_reward(">You've unlocked Wizard cards.\nUse the deckbuilder available on your desk to learn the rules and edit your deck.","interface/icons/cards.png")

    return
    
### Twins card store unlocked ###
label cards_store_mail_send:
    $ twins_cards_stocked = True
    
    m "Great, let's see how they're doing."
    return
    
### Cardgame End of Content letter ###
label cardgame_eoc_mail_send:
    $ cardgame_eoc = True
    
    g9 "Sweet..."
    g9 "Fucking love prizes."
    
    #call unlock_clothing(text="You received a.. new outfit?",item=clothing_mail_item)
    
    g9 "Sweet..."
    g9 "Fucking love prizes."
    g4 "Wait, this is a womans outfit!"
    m "Wait... it's a womans outfit..."
    g9 "Might have to try and convice miss Granger put this one on..."
    return

label get_package:
    show screen blktone


    if clothing_mail_item != None:
        if clothing_mail_timer <= 1:
            call unlock_clothing(text="You received a new outfit.",item=clothing_mail_item)
            $ clothing_mail_item = None
            $ clothing_mail_timer = 0

    python:
        for item in deliveryQ.get_mail():
            if item.type == 'Event_item':
                pass

            if item.type == 'Gift':
                gift = item.object
                gift.number += item.quantity
                the_gift = gift.get_image()

                renpy.show_screen("gift")
                renpy.with_statement(Dissolve(0.3))
                if item.quantity > 1:
                    renpy.say(None,"You received "+str(item.quantity)+" "+str(gift.name)+"'s")
                else:
                    renpy.say(None,"You received "+str(item.quantity)+" "+str(gift.name))
                renpy.hide_screen("gift")
                renpy.with_statement(Dissolve(0.3))

    hide screen blktone
    with d3

    $ package_is_here = False

    call screen main_room_menu



label __init_variables:

    if not hasattr(renpy.store,'letter_queue_list'):
        $ letter_queue_list = []
        $ report_money = 0

    # Hermione Granger Letters.
    if not hasattr(renpy.store,'letter_from_hermione_A_OBJ'):
        $ letter_from_hermione_A_OBJ = mail_letter_class()
    $ letter_from_hermione_A_OBJ.text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}"
    $ letter_from_hermione_A_OBJ.label = "letter_from_hermione_A"

    if not hasattr(renpy.store,'letter_from_hermione_B_OBJ'):
        $ letter_from_hermione_B_OBJ = mail_letter_class()
    $ letter_from_hermione_B_OBJ.text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided inme... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}"
    $ letter_from_hermione_B_OBJ.label = "" #No comment on letter.


    # Ministry of Magic Letters.
    if not hasattr(renpy.store,'letter_paperwork_unlock_OBJ'):
        $ letter_paperwork_unlock_OBJ = mail_letter_class()
    $ letter_paperwork_unlock_OBJ.text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore,\nWe remind you that only upon providing us with a completed report will we be able to make a payment in your name.\n\n{size=-3}With deepest respect,\nThe Ministry of Magic.{/size}"
    $ letter_paperwork_unlock_OBJ.label = "letter_paperwork_unlock"

    if not hasattr(renpy.store,'letter_paperwork_report_OBJ'):
        $ letter_paperwork_report_OBJ = mail_letter_class()
    $ letter_paperwork_report_OBJ.text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing a report this week.\n\nYou will find you payment in the attached purse.{/size}\n\n\n{size=-3}-With deepest respect-{/size}\n\n{size=-2}The Ministry of Magic.{/size}"
    $ letter_paperwork_report_OBJ.label = "letter_paperwork_report"

    if not hasattr(renpy.store,'letter_curse_complaint_OBJ'):
        $ letter_curse_complaint_OBJ = mail_letter_class()
    $ letter_curse_complaint_OBJ.text = "{size=-7}Dear Albus Dubmbledore, as we are sure you are aware, an unforgivable curse has been detected within the grounds of Hogwarts.\nWhile the punishment for such a curse is usually lifetime incarceration in the prison, Azkaban, we are allowing you to address this matter at your own discretion.\nThis is due to the possible nature of the spell being cast by a minor who has not fully grasped the serious nature of the curse.\nIf this is the case we expect no further communication from you regarding this unfortunate event.\nIf, however, you believe the curse has been cast by someone other than a student, or if any other complications arise we expect direct communication.\nLastly, the detection of any further curses will result in the immediate dispatchment of an auror to Hogwarts.\n\nCornelius Fudge,\nDepartment Head: Improper Use of Magic Office{/size}"
    $ letter_curse_complaint_OBJ.label = "letter_curse_complaint"
    
    if not hasattr(renpy.store,'letter_deck'):
        $ letter_deck = mail_letter_class()
    $ letter_deck.text = "{size=-3}Sir Albus Dumbledore{/size}\n\n{size=-7}We would like to present to you great opportunity to become a Wizard Cards champion. We've included a starter pack to our card game in the hopes that you will consider any of our resellers to stock our cards for your students to purchase and play.\n\nHere's a little bit of information about our cards:\nEvery Wizard card has an enchantment that will personalize its look just for you and show something of your own favorite interest.\n\nDo you like Quidditch? Every card will look like a famous Quidditch player or a sport related print.\nInterested in magical creatures? The cards will have magical creatures on them.\nFind out your unique illustrations today with a started pack, we don't even know what it is!{/size}\n\n{space=110}{size=-5}Wizard cards inc{/size}"
    $ letter_deck.label = "deck_mail_send"
    
    if not hasattr(renpy.store,'letter_cards_store'):
        $ letter_cards_store = mail_letter_class()
    $ letter_cards_store.text = "{size=-7}Weasley's Wizard Wheezes shop emporium is now officially partnering with Wizard cards.\nCheck out the notice board at our shop to find a list of challengers at your skill level.{/size}"
    $ letter_cards_store.label = "cards_store_mail_send"
    
    if not hasattr(renpy.store,'letter_cardgame_eoc'):
        $ letter_cardgame_eoc = mail_letter_class()
    $ letter_cardgame_eoc.text = "{size=-3}Congratulations!{/size}\n\n{size=-7}You've beaten your first 3 challenges of Wizard Cards.\nWe're currently working on expanding our business and are recruiting even more challengers so that in the future you'll be able to challenge even more people.\nIn the meanwhile, you'll be able to earn even more tokens by challenging someone again to complete your collection of items.\nThis time you'll only get one token per win but it should be a breeze for such a skilled player as you.\n\nYours truly,\nWeasley's Wizard Wheeze's and Team Silver{/size}"
    $ letter_cardgame_eoc.label = "cardgame_eoc_mail_send"

    return



init python:

    class deliveryItem(object):
        object = None
        transit_time = 0
        quantity=1
        type = ''

        def __init__(self,object,transit_time,quantity,type):
            self.object = object
            self.transit_time = transit_time
            self.quantity = quantity
            self.type = type

    class deliveryQueue(object):
        queue = []
        max_wait = 15

        def send(self, item, transit_time, quantity, type):
            if transit_time > self.max_wait:
                transit_time = self.max_wait
            self.queue.append(deliveryItem(item, transit_time, quantity, type))

        def got_mail(self):
            for i in self.queue:
                i.transit_time -= 1
            for i in self.queue:
                if i.transit_time <= 0:
                    return True
            return False

        def get_mail(self):
            delivery = []
            for i in self.queue:
                if i.transit_time <= 0:
                    delivery.append(i)
            for i in delivery:
                self.queue.remove(i)
            return delivery

    if not hasattr(renpy.store,'deliveryQ'):
        deliveryQ = deliveryQueue()

    class mail_letter_class(object):
        mailed = False
        read = False
        text = "Add Text"
        label = "" #If Genie doesn't comment on the letter, this should remain ""

        def getLetterText(self):
            return self.text

        def mailLetter(self):
            self.mailed = True
            self.read = False
            if self not in letter_queue_list:
                letter_queue_list.append(self)
            return

        def mailRead(self):
            self.read = True
            if self in letter_queue_list:
                letter_queue_list.remove(self)
            return
