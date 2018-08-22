init python:    
    class gift_item(generic_menu_item):
        id = 0
        whoringNeeded = 0
        cost = 0
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def costOf(self, number_of_item):
            return self.cost * number_of_item
        
        def get_description(self):
            out_des = ""
            if len(self.description) > 90:
                out_des = self.description[0:90] + "..."
            else:
                out_des = self.description
            return out_des
        
        def get_buttom_right(self):
            return "Cost: " + str(self.cost)
    
label __init_variables:
    
    if not hasattr(renpy.store,'Lollipop'): #important!
        $ Lollipop = gift_item()
    $ Lollipop.id = 0
    $ Lollipop.cost = 20
    $ Lollipop.title = "lollipop candy"
    $ Lollipop.unlocked = True
    $ Lollipop.imagepath = "images/store/gifts/1.png"
    $ Lollipop.description = "A lollipop candy. An adult candy for kids or kids candy for adults?"
    
    
    if not hasattr(renpy.store,'Chocolate'): #important!
        $ Chocolate = gift_item()
    $ Chocolate.id = 1
    $ Chocolate.cost = 40
    $ Chocolate.title = "Chocolate"
    $ Chocolate.unlocked = True
    $ Chocolate.imagepath = "images/store/gifts/2.png"
    $ Chocolate.description = "The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries)."
    
    if not hasattr(renpy.store,'PlushOwl'): #important!
        $ PlushOwl = gift_item()
    $ PlushOwl.id = 2
    $ PlushOwl.cost = 35
    $ PlushOwl.title = "Plush owl"
    $ PlushOwl.unlocked = True
    $ PlushOwl.imagepath = "images/store/gifts/3.png"
    $ PlushOwl.description = "a Toy owl stuffed with feathers of an actual owl. It's so cuddly!"
    
    if not hasattr(renpy.store,'Butterbeer'): #important!
        $ Butterbeer = gift_item()
    $ Butterbeer.id = 3
    $ Butterbeer.cost = 50
    $ Butterbeer.whoringNeeded = 3
    $ Butterbeer.title = "Butterbeer"
    $ Butterbeer.unlocked = True
    $ Butterbeer.imagepath = "images/store/gifts/4.png"
    $ Butterbeer.description = "Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}"
    
    if not hasattr(renpy.store,'EducationalMagazines'): #important!
        $ EducationalMagazines = gift_item()
    $ EducationalMagazines.id = 4
    $ EducationalMagazines.cost = 30
    $ EducationalMagazines.unlocked = True
    $ EducationalMagazines.title = "Educational magazines"
    $ EducationalMagazines.imagepath= "images/store/gifts/5.png"
    $ EducationalMagazines.description = "Educational magazines. \nthe Trusty companions of every social outcast."
    
    if not hasattr(renpy.store,'GirlyMagazines'): #important!
        $ GirlyMagazines = gift_item()
    $ GirlyMagazines.id = 5
    $ GirlyMagazines.cost = 45
    $ GirlyMagazines.title = "Girly magazines"
    $ GirlyMagazines.unlocked = True
    $ GirlyMagazines.imagepath= "images/store/gifts/6.png"
    $ GirlyMagazines.description = "Girly magazines. \nAll cool girls are reading these."
    
    if not hasattr(renpy.store,'AdultMagazines'): #important!
        $ AdultMagazines = gift_item()
    $ AdultMagazines.id = 6
    $ AdultMagazines.cost = 60
    $ AdultMagazines.title = "Adult magazines"
    $ AdultMagazines.unlocked = True
    $ AdultMagazines.imagepath= "images/store/gifts/7.png"
    $ AdultMagazines.description = "Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex."
    
    if not hasattr(renpy.store,'PornMagazines'): #important!
        $ PornMagazines = gift_item()
    $ PornMagazines.id = 7
    $ PornMagazines.cost = 80
    $ PornMagazines.whoringNeeded = 3
    $ PornMagazines.title = "Porn magazines"
    $ PornMagazines.unlocked = True
    $ PornMagazines.imagepath= "images/store/gifts/8.png"
    $ PornMagazines.description = "Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\"."
    
    if not hasattr(renpy.store,'ViktorKrumPoster'): #important!
        $ ViktorKrumPoster = gift_item()
    $ ViktorKrumPoster.id = 8
    $ ViktorKrumPoster.cost = 25 #placeholder number
    $ ViktorKrumPoster.title = "Viktor Krum Poster"
    $ ViktorKrumPoster.unlocked = True
    $ ViktorKrumPoster.imagepath= "images/store/gifts/9.png"
    $ ViktorKrumPoster.description = "A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world."
    
    if not hasattr(renpy.store,'SexyLingerie'): #important!
        $ SexyLingerie = gift_item()
    $ SexyLingerie.id = 9
    $ SexyLingerie.cost = 75 #placeholder number
    $ SexyLingerie.title = "Sexy lingerie"
    $ SexyLingerie.unlocked = True
    $ SexyLingerie.imagepath= "images/store/gifts/10.png"
    $ SexyLingerie.description = "Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath."
    
    if not hasattr(renpy.store,'PackOfCondoms'): #important!
        $ PackOfCondoms = gift_item()
    $ PackOfCondoms.id = 10
    $ PackOfCondoms.cost = 50
    $ PackOfCondoms.whoringNeeded = 3
    $ PackOfCondoms.title = "A pack of condoms"
    $ PackOfCondoms.unlocked = True
    $ PackOfCondoms.imagepath= "images/store/gifts/11.png"
    $ PackOfCondoms.description = "\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}"
    
    if not hasattr(renpy.store,'Vibrator'): #important!
        $ Vibrator = gift_item()
    $ Vibrator.id = 11
    $ Vibrator.cost = 55
    $ Vibrator.whoringNeeded = 3
    $ Vibrator.title = "Vibrator"
    $ Vibrator.unlocked = True
    $ Vibrator.imagepath= "images/store/gifts/12.png"
    $ Vibrator.description = "A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core."
    
    if not hasattr(renpy.store,'JarOfLube'): #important!
        $ JarOfLube = gift_item()
    $ JarOfLube.id = 12
    $ JarOfLube.cost = 60
    $ JarOfLube.title = "Jar of anal lubricant"
    $ JarOfLube.unlocked = True
    $ JarOfLube.imagepath= "images/store/gifts/13.png"
    $ JarOfLube.description = "A Jar of anal lube, Buy this for your loved one - show that you care."
    
    if not hasattr(renpy.store,'BallGagAndCuffs'): #important!
        $ BallGagAndCuffs = gift_item()
    $ BallGagAndCuffs.id = 13
    $ BallGagAndCuffs.cost = 70
    $ BallGagAndCuffs.title = "Ball gag and cuffs"
    $ BallGagAndCuffs.unlocked = True
    $ BallGagAndCuffs.imagepath= "images/store/gifts/14.png"
    $ BallGagAndCuffs.description = "Ball gag and cuffs, Turn your soulmate into your cellmate."
    
    if not hasattr(renpy.store,'AnalPlugs'): #important!
        $ AnalPlugs = gift_item()
    $ AnalPlugs.id = 14
    $ AnalPlugs.cost = 85
    $ AnalPlugs.whoringNeeded = 3
    $ AnalPlugs.title = "Anal plugs"
    $ AnalPlugs.unlocked = True
    $ AnalPlugs.imagepath= "images/store/gifts/15.png"
    $ AnalPlugs.description = "Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike."
    
    if not hasattr(renpy.store,'ThestralStrapon'): #important!
        $ ThestralStrapon = gift_item()
    $ ThestralStrapon.id = 15
    $ ThestralStrapon.cost = 200
    $ ThestralStrapon.whoringNeeded = 3
    $ ThestralStrapon.title = "Thestral Strap-on"
    $ ThestralStrapon.unlocked = True
    $ ThestralStrapon.imagepath= "images/store/gifts/16.png"
    $ ThestralStrapon.description = "Thestral strap-on.\nWhen you see it, you'll shit bricks."
    
    if not hasattr(renpy.store,'SpeedStick2000'): #important!
        $ SpeedStick2000 = gift_item()
    $ SpeedStick2000.id = 16
    $ SpeedStick2000.cost = 500
    $ SpeedStick2000.title = "Lady Speed Stick-2000"
    $ SpeedStick2000.unlocked = True
    $ SpeedStick2000.imagepath= "images/store/gifts/17.png"
    $ SpeedStick2000.description = "The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!"
    
    if not hasattr(renpy.store,'SexDollJoanne'): #important!
        $ SexDollJoanne = gift_item()
    $ SexDollJoanne.id = 17
    $ SexDollJoanne.cost = 350
    $ SexDollJoanne.title = "Sex doll \"Joanne\""
    $ SexDollJoanne.unlocked = True
    $ SexDollJoanne.imagepath= "images/store/gifts/18.png"
    $ SexDollJoanne.description = "Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort."
    
    if not hasattr(renpy.store,'AnalBeads'): #important!
        $ AnalBeads = gift_item()
    $ AnalBeads.id = 18
    $ AnalBeads.cost = 65 #placeholder number
    $ AnalBeads.title = "Anal beads"
    $ AnalBeads.unlocked = True
    $ AnalBeads.imagepath= "images/store/gift_anal_beads.png"
    $ AnalBeads.description = "Anal beads engraved with a strange inscription \"Property of L.C.\"."
    
    
    $ gift_list = []
    $ gift_list.append(Lollipop)
    $ gift_list.append(Chocolate)
    $ gift_list.append(PlushOwl)
    $ gift_list.append(Butterbeer)
    $ gift_list.append(EducationalMagazines)
    $ gift_list.append(GirlyMagazines)
    $ gift_list.append(AdultMagazines)
    $ gift_list.append(PornMagazines)
    $ gift_list.append(ViktorKrumPoster)
    $ gift_list.append(SexyLingerie)
    $ gift_list.append(PackOfCondoms)
    $ gift_list.append(Vibrator)
    $ gift_list.append(JarOfLube)
    $ gift_list.append(BallGagAndCuffs)
    $ gift_list.append(AnalPlugs)
    $ gift_list.append(ThestralStrapon)
    $ gift_list.append(SpeedStick2000)
    #$ gift_list.append(SexDollJoanne)
    #$ gift_list.append(AnalBeads)
    
    return

label happy(sub_mad = 0):
    hide screen hermione_main
    with d3
    $ mad -= sub_mad
    if mad <= 0:
        $ mad = 0
    if mad == 0:
        ">Hermione's mood has improved...\n>Hermione is {size=+5}not upset{/size} with you..."
    else:
        ">Hermione's mood has improved...\n>Hermione is {size=+5}still upset{/size} with you..."
    return

label no_change:
    hide screen hermione_main
    with d3  
    ">Hermione's mood didn't change much..."
    return

label upset(add_mad):
    hide screen hermione_main
    with d3
    $ mad += add_mad
    ">Hermione's mood worsened...\n>Hermione is {size=+5}upset{/size} with you..."
    return
    
label her_gift_menu:
    python:
        choices = []
        for i in gift_list:
            if gift_item_inv[i.id] > 0:
                choices.append( ( ("-"+str(i.name)+"- ("+str(gift_item_inv[i.id])+")"), i) )
        
        choices.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(choices)
        
    if result == "nvm":
        jump day_time_requests
    else:
        call give_her_gift(result) 
    
label give_her_gift(gift_id):
    hide screen hermione_main
    with d5
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    if gift_id == 0:#candy
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A lollipop?","base","base") 
            call give_gift(">You give the candy to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","base") 
            call happy(5) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Candy?","normal","base") 
            call her_main("Candy is for kids, [genie_name].","open","base") 
            call give_gift(">You give the candy to Hermione...",gift_id) 
            call her_main("Thank you...","annoyed","worriedL") 
            call happy(5) 
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Candy?","normal","base") 
            call give_gift(">You give the candy to Hermione...",gift_id) 
            call her_main("Ehm... Sure, thanks...","open","suspicious") 
            call happy(5) 
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("A lollipop?","base","base") 
            call her_main("Clever girls use candy like this as a \"weapon\".","smile","baseL") 
            call give_gift(">You give the candy to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","happyCl") 
            call happy(5) 
            $ h_body = "body_128"
    if gift_id == 1:#chocolate
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A chocolate bar?","base","base") 
            call give_gift(">You give the chocolate to Hermione...", gift_id) 
            call her_main("Thank you, [genie_name].","base","base") 
            call happy(10) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A chocolate bar?","normal","base") 
            call her_main("Hm...","annoyed","frown") 
            call her_main("That thing about fairies...") 
            call her_main("That is a joke of some sort, right?","open","worried") 
            call give_gift(">You give the chocolate to Hermione...", gift_id) 
            call her_main("Thank you...","soft","base") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A chocolate bar?","normal","base") 
            call her_main("I just like the way it crunches, [genie_name]! N-not the taste...","grin","worriedCl",emote="05") 
            call give_gift(">You give the chocolate to Hermione...", gift_id) 
            call her_main("Ehm... Sure, thanks...","base","base") 
            call happy(10) 
        if whoring >= 18: # Lv 7+  
            call her_main("A chocolate bar?","base","base") 
            call her_main("You spoil me, [genie_name].","smile","angry") 
            call give_gift(">You give the chocolate to Hermione...", gift_id) 
            call her_main("Thank you.","base","suspicious") 
            call happy(10) 
    if gift_id == 2:#plush owl
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A stuffed owl?","base","base") 
            call her_main("It's cute...","base","base") 
            call give_gift(">You give the owl to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","base") 
            call happy(7) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A plush toy?","open","worried") 
            call her_main("I like it!","base","base") 
            call give_gift(">You give the owl to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","base") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A toy?","base","base") 
            call her_main("Toys are for kids, [genie_name].","open","base") 
            call her_main("But I'll take it...","annoyed","worriedL") 
            call give_gift(">You give the owl to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","base") 
            call happy(15) 
        if whoring >= 18: # Lv 7+  
            call her_main("This is one of those adult toys isn't it?","disgust","glance") 
            call her_main("There's got to be a switch or a button somewhere...","open","down") 
            call her_main("So... Does it vibrate or something?","base","down") 
            call her_main("Oh...?","open","squint",cheeks="blush") 
            call her_main("So it is really just a plush toy then?") 
            call her_main("Shame...","angry","down_raised") 
            call her_main("I mean, thank you, [genie_name].","angry","worriedCl",emote="05") 
            call give_gift(">You give the owl to Hermione...",gift_id) 
            $ h_body = "body_01"
            call happy(4) 
    if gift_id == 3:#butterbeer
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Butterbeer?","base","base") 
            call her_main("Are you sure about that, [genie_name]?","open","suspicious") 
            call her_main("It does contain alcohol, you know...","base","base") 
            call give_gift(">You give the bottle to Hermione...",gift_id) 
            call her_main("Thank you.","base","base") 
            call happy(3) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Butterbeer, [genie_name]?","open","worried") 
            call her_main("To let you in on a little secret, [genie_name]...","open","base") 
            call her_main("I'm a big fan of this completely harmless beverage.","base","base") 
            call give_gift(">You give the bottle to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","base") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Butterbeer?","base","base") 
            call her_main("Thank you, [genie_name].","grin","worriedCl",emote="05") 
            call give_gift(">You give the bottle to Hermione...",gift_id) 
            call her_main("I shall drink this with the girls later.","base","base") 
            call happy(15) 
        if whoring >= 18: # Lv 7+  
            call her_main("Butterbeer...?","base","base") 
            call her_main("Thank you, [genie_name].","base","base") 
            call give_gift(">You give the bottle to Hermione...",gift_id) 
            call her_main("I shall drink this later with the boys.","base","base") 
            call her_main("Err... I meant to say with the girls, of course.","open","baseL",cheeks="blush") 
            call happy(20) 
            $ h_body = "body_01"
    if gift_id == 4:#edu mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("\"Popular magic\" magazines?","base","base") 
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name]!","base","base") 
            call her_main("I will use them for my research!") 
            call happy(15) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Sometimes I find information in magazines that I could never find in a book...","base","base") 
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name]!","base","base") 
            call her_main("I will use them for my research!") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Oh...","open","base") 
            call her_main("Yes, I used to read magazines like that a lot...","base","base") 
            call her_main("Lately not so much though...","open","worriedL") 
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name]!","base","base") 
            call happy(3) 
        if whoring >= 18: # Lv 7+  
            call her_main("Ehm...","open","worriedL") 
            call her_main("To be honest, magazines like that lost their appeal to me completely lately...","open","suspicious") 
            call her_main("But I don't mind taking them off you hands anyway, [genie_name].","open","worried") 
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) 
            call her_main("Thank you.","soft","baseL") 
            call no_change 
    if gift_id == 5:#girl mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm?","soft","base") 
            call her_main("This is the sort of press some \"slytherin\" bimbo would appreciate.","annoyed","suspicious") 
            call her_main("I am way above silly magazines like that, [genie_name].","open","closed") 
            call no_change 
            $ h_body = "body_01"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("I don't read magazines of that nature, [genie_name]...","open","angryCl") 
            call her_main("................","soft","baseL") 
            call her_main("But I could give it a try just to humour you I suppose...","open","angryCl") 
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name]!","open","suspicious") 
            call happy(5) 
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("I ashamed to admit this, but...","open","worriedL") 
            call her_main("I really enjoy reading magazines like that lately...","grin","worriedCl",emote="05") 
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","open","suspicious") 
            call happy(15) 
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("The Latest edition of \"Girlz\"?!","angry","wide") 
            call her_main("I can't have enough of that brilliant magazine!","grin","worriedCl",emote="05") 
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","open","suspicious") 
            call happy(15) 
            $ h_body = "body_06"
    if gift_id == 6:#adult mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Are that...?","open","base") 
            call her_main("Adult magazines, [genie_name]?","open","base") 
            call her_main("Given to me by An esteemed wizard of your status?","annoyed","angryL") 
            call her_main("[genie_name], surely you could find a more productive way to spend your free time.","disgust","glance") 
            call her_main("And I most definitely would not have use for those...","angry","angry") 
            call upset(7) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Adult magazines?","angry","angry") 
            call her_main("[genie_name], I have no interest in things like that.","annoyed","angryL") 
            call her_main("And how is this an appropriate present for one of your students, [genie_name]?","angry","angry") 
            call upset(3) 
            $ h_body = "body_29"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Adult magazines?","open","base") 
            call her_main("[genie_name], this is such an inappropriate present for a girl my age...","angry","worriedCl",emote="05") 
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_id) 
            call her_main("I shall throw these away myself...","annoyed","annoyed") 
            call happy(8) 
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("The New edition of \"L.o.v.e.\"!!!","smile","happyCl") 
            call her_main("Err.. I mean, adult magazines?","angry","wink") 
            call her_main("This is a little inappropriate...") 
            call her_main("But I will take them...","base","happyCl") 
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_id) 
            call her_main("thank you, [genie_name].","base","happyCl") 
            call happy(15) 
    if gift_id == 7:#porn mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm... What is this?","base","base") 
            call her_main("[genie_name], those are porn magazines!","scream","wide") 
            call her_main("Shame on you, [genie_name]!","angry","angry",cheeks="blush") 
            call upset(15) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Porn magazines?","shock","wide") 
            call her_main("[genie_name], what do you expect me to do with those?","open","down") 
            call her_main("Research them?","annoyed","annoyed") 
            call her_main("Despicable!","scream","angry",emote="01") 
            call upset(8) 
            $ h_body = "body_120"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("That's hardcore porn, [genie_name].","open","base") 
            call her_main("Which is a completely inappropriate gift for a girl my age!","angry","worriedCl",emote="05") 
            call her_main("..............","angry","down_raised") 
            call her_main("But I will take them...","angry","base") 
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_id) 
            call her_main("And I shall throw them in the trash, where they and... girls who like these things belong...","annoyed","annoyed") 
            call no_change 
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("Pornography?","shock","wide") 
            call her_main("................","angry","down_raised") 
            call her_main("How can women even agree to do things like that, [genie_name]?","angry","base") 
            call her_main(".................","angry","down_raised") 
            call her_main("Alright, I shall accept them...","upset","closed") 
            call her_main("Solely for research purposes of course...","open","baseL",cheeks="blush") 
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_id) 
            call happy(15) 
            $ h_body = "body_45"
    if gift_id == 8:#krum poster
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A Quidditch poster?","annoyed","down") 
            call her_main("What am I supposed to do with it, [genie_name]?","annoyed","annoyed") 
            call her_main("No, thank you.","annoyed","closed") 
            call no_change 
            $ h_body = "body_71"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A Quidditch poster?","annoyed","down") 
            call her_main("Hm...","annoyed","annoyed") 
            call her_main("I think I saw this player once or twice...","annoyed","down") 
            call her_main("He is that Durmstrang student, right?","base","base") 
            call give_gift(">You give the poster to Hermione...",gift_id) 
            call happy(5) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A Viktor Krum poster, [genie_name]?","annoyed","down") 
            call her_main("Can't say that I care much for Quidditch, but...","open","suspicious") 
            call her_main("I can see why the girls find the brutish physique of some players appealing...","open","down") 
            call give_gift(">You give the poster to Hermione...",gift_id) 
            call happy(15) 
        if whoring >= 18: # Lv 7+  
            call her_main("A Viktor Krum poster?!","scream","wide_stare") 
            call her_main("Thank you, [genie_name]!","grin","worriedCl",emote="05") 
            call give_gift(">You give the poster to Hermione...",gift_id) 
            call her_main("Can't wait to hang it over my bed!","smile","baseL") 
            call her_main("The girls will go green with envy...","smile","glance") 
            call happy(25) 
    if gift_id == 9:#lingerie
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("lingerie?","angry","down_raised") 
            call her_main("[genie_name], I cannot accept a gift like this from you...","upset","closed") 
            call upset(10) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("sexy lingerie?","angry","down_raised") 
            call her_main("You know I cannot possibly accept a gift like that from you, [genie_name].","angry","base") 
            call her_main("(It's pretty though).........","angry","down_raised") 
            call no_change 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("sexy lingerie?","base","down") 
            call her_main("[genie_name] that is so inappropriate...","angry","wink") 
            call give_gift(">You give the lingerie to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush") 
            call happy(7) 
        if whoring >= 18: # Lv 7+  
            call her_main("sexy lingerie?","base","down") 
            call her_main("Do You think it will make me look like one of the witches in those adult magazines, [genie_name]?","grin","dead") 
            call her_main("Oh... I mean, thank you, [genie_name].","angry","wink") 
            call give_gift(">You give the lingerie to Hermione...",gift_id) 
            call happy(15) 
    if gift_id == 10:#condoms
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Condoms?!","angry","wide") 
            call her_main("[genie_name], I wouldn't even know what to do with them...","scream","angryCl") 
            call upset(6) 
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("...Condoms?","normal","frown") 
            call her_main("Ehm... Is this a part of some new Hogwarts sex ed program or something?","open","angryCl") 
            call her_main("No, [genie_name]... It feels wrong to accept a thing like this from you...","open","baseL",cheeks="blush") 
            call no_change 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A pack of condoms?","normal","base") 
            call her_main("[genie_name], what possible use could I have for those?") 
            call her_main("Well, I shall accept them simply because it is rude to refuse a gift...","open","angryCl") 
            call give_gift(">You give a pack of condoms to Hermione...", gift_id) 
            call happy(3) 
            $ h_body = "body_29"
        if whoring >= 18: # Lv 7+
            call her_main("A pack of condoms?","open","suspicious") 
            call her_main("I appreciate your concern, [genie_name]. Thank you.","base","glance") 
            call give_gift(">You give a pack of condoms to Hermione...", gift_id) 
            call happy(4) 
            $ h_body = "body_45"
    if gift_id == 11:#vibrator
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A magic wand?","base","base") 
            call her_main("No, it doesn't look like--","soft","base") 
            call her_main(".........?") 
            call her_main("!!!","angry","wide") 
            call her_main("[genie_name]!","angry","angry",cheeks="blush") 
            call her_main("This is just beyond inappropriate!","scream","angryCl") 
            call upset(10) 
            $ h_body = "body_120"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Is this what I think it is?","angry","down_raised") 
            call her_main("[genie_name], let me remind you that I belong to the noble house of \"Gryffindor\".","open","annoyed",cheeks="blush") 
            call her_main("A present like that would be appropriate for a girl from \"Slytherin\", [genie_name].","upset","closed") 
            call upset(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Is that a... vibrator?","angry","down_raised") 
            call her_main("The design...") 
            call her_main("it reminds me of my wand...") 
            call her_main("Did you have this custom made for me [genie_name]?","angry","down_raised") 
            call her_main("This is inappropriate...","scream","angryCl") 
            call her_main("But I shall take it nonetheless...","annoyed","worriedL") 
            call give_gift(">You give the vibrator to Hermione...",gift_id) 
            call no_change 
        if whoring >= 18: # Lv 7+  
            call her_main("This vibrator...","open","worried") 
            call her_main("It's... calling out for me...","open","worriedL") 
            call her_main("But not in a dirty way, [genie_name].","disgust","glance") 
            call give_gift(">You give the vibrator to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","down") 
            call happy(10) 
    if gift_id == 12:#anal lube
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("I don't know what this is...","open","base") 
            call her_main("But I have the feeling that the jar is full of something vile and inappropriate...","angry","angry") 
            call her_main("No, thank you, [genie_name].") 
            call upset(6) 
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Hm...","annoyed","down") 
            call her_main("I think I know what this is...","disgust","glance") 
            call her_main("But why would you give something like this to one of your pupils, [genie_name]?") 
            call her_main("No, thank you.","annoyed","angryL") 
            call upset(2) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Anal lubricant?","angry","down_raised") 
            call her_main("Ehm.. well... I know this girl...","open","baseL",cheeks="blush") 
            call her_main("I mean I don't know her, she is a friend of a friend...") 
            call her_main("Yes, I will take this for her...") 
            call give_gift(">You give the jar to Hermione...", gift_id, 0) 
            call her_main("Still, I think you should not give presents like this to your pupils, [genie_name].","open","annoyed",cheeks="blush") 
            call no_change 
            $ h_body = "body_79"
        if whoring >= 18: # Lv 7+  
            call her_main("Anal lubricant, [genie_name]?","base","down") 
            call her_main("I know a couple of girls who would do anything for a commodity like that.","open","annoyed",cheeks="blush") 
            call her_main("Thank for looking out for us, [genie_name].","base","glance") 
            call give_gift(">You give the jar to Hermione...", gift_id) 
            call happy(5) 
    if gift_id == 13:#gag and cuffs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("What is this?","angry","down_raised") 
            call her_main("Is this like one of those adult toys?","angry","suspicious",cheeks="blush") 
            call her_main("What woman in her right mind would subject herself to a humiliation like that?","scream","angryCl") 
            call her_main("And what possible use could I have for such objects?","open","annoyed",cheeks="blush") 
            call her_main("This is just insulting, [genie_name]...","angry","angry",cheeks="blush") 
            call upset(10) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], do you not realize how inappropriate it would be for me to accept a present like that?","open","annoyed",cheeks="blush") 
            call her_main("And I would not even know what to do with them anyway...","open","baseL",cheeks="blush") 
            call her_main("I mean these fluffy things are obviously handcuffs...","angry","down_raised") 
            call her_main("But this ball... ehm...") 
            call her_main("[genie_name], please...","upset","closed") 
            call her_main("Just put them away.") 
            call upset(5) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A month ago I would've felt insulted to receive a gift like this...","upset","closed") 
            call her_main("But by now I know that some girls really do find pleasure in toys like...","angry","down_raised") 
            call her_main("But I assure you that I am not one of them, [genie_name].","upset","closed") 
            call her_main("But I know a girl who knows a girl who is into things like...","open","baseL",cheeks="blush") 
            call her_main("Yes, I shall take these to her...","base","baseL",cheeks="blush") 
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_id) 
            call happy(9) 
        if whoring >= 18: # Lv 7+  
            call her_main("A ball gag and handcuffs?","open","squint",cheeks="blush") 
            call her_main("This is completely inappropriate, [genie_name].","angry","wink") # :)
            call her_main("But a gift is a gift, right?","base","suspicious") 
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_id) 
            call happy(15) 
    if gift_id == 14:#anal plugs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm...?","base","base") 
            call her_main("Are those like key-chain toys?","soft","base") 
            call give_gift(">You give the anal plugs to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","annoyed","annoyed") 
            call happy(8) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], are those adult toys of some sort?","open","annoyed",cheeks="blush") 
            call her_main("those are some of those anal things, aren't they?","angry","angry",cheeks="blush") 
            call her_main("[genie_name] this is nothing but a weapon meant to oppress women!") 
            call her_main("Despicable!","upset","closed") 
            call upset(15) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Yes, I know that some girls have uhm...","upset","closed") 
            call her_main("Have use for things such as these...","open","annoyed",cheeks="blush") 
            call her_main("But not me, [genie_name].") 
            call her_main("No, thank you.","upset","closed") 
            call no_change 
        if whoring >= 18: # Lv 7+  
            call her_main("Anal plugs?","angry","down_raised") 
            call her_main("I have no use for things like that, [genie_name]...","angry","base") 
            call her_main("They are so pretty though...","angry","wink") 
            call her_main(".....................","angry","down_raised") 
            call her_main("Well, alright. I shall take them off your hands if I must, [genie_name].","soft","ahegao") 
            call give_gift(">You give the anal plugs to Hermione...",gift_id) 
            call her_main("But I shall never use them of course...","open","closed") 
            call her_main("................","base","down") 
            call happy(10) 
    if gift_id == 15:#strap on
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("What is that?","angry","wide") 
            call her_main("An artifact of some sort or a trophy?","open","base") 
            call her_main("So well-crafted...","base","base") 
            call her_main("Are you sure that it's alright for me to have it, [genie_name]?","base","base") 
            call give_gift(">You give the strap-on to Hermione...",gift_id) 
            call her_main("Thank you very much, [genie_name]. I promise to take good care of it.","open","closed") 
            call happy(20) 
            $ h_body = "body_15"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("!!!","angry","wide") 
            call her_main("That is...","angry","down_raised") 
            call her_main("But it doesn't even look... human...") 
            call her_main("I mean...","annoyed","angryL") 
            call her_main("[genie_name], do you have no shame?!","scream","angry",emote="01") 
            call her_main("Presenting a thing like that to a pupil?!") 
            call her_main("..................","open","down") 
            call her_main("Please put it away, [genie_name].","angry","angry") 
            call upset(15) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("That thing...","angry","down_raised") 
            call her_main("Is that the actual size of the... of the real \"thing\"?","angry","base") 
            call her_main("I mean...","open","baseL",cheeks="blush") 
            call her_main(".......................","angry","down_raised") 
            call her_main("Is this like a party prank prop?","angry","base") 
            call her_main("It's so well-crafted though...","angry","down_raised") 
            call her_main("I will take it...","normal","worriedCl") 
            call give_gift(">You give the strap-on to Hermione...",gift_id) 
            call happy(10) 
        if whoring >= 18: # Lv 7+  
            call her_main("It's... It's magnificent, [genie_name]...","shock","wide") 
            call her_main("Is it really modeled after a thestral?","open","baseL",cheeks="blush") 
            call her_main("But the creatures are invisible...","open","squint",cheeks="blush") 
            call her_main("..................","angry","down_raised") 
            call her_main("Breathtaking...","grin","dead") 
            call her_main("Not in the way you think, [genie_name]...","upset","closed") 
            call her_main("I am merely admiring the craftsmanship...","open","closed") 
            call give_gift(">You give the strap-on to Hermione...",gift_id) 
            call her_main("Thank you for the gift, [genie_name].","base","suspicious") 
            call happy(30) 
    if gift_id == 16:#speed stick
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A broom...?","base","base") 
            call her_main("Hm...","normal","base") 
            call her_main("What is that silly-looking thing attached to it?","normal","frown") 
            call her_main("Is it like a saddle...?","open","suspicious") 
            call give_gift(">You give the broom to Hermione...",gift_id) 
            call her_main("Thank you for the gift, [genie_name].","open","worried") 
            $ h_body = "body_06"
            call happy(20) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A broom...?","base","base") 
            call her_main("Hm...","normal","frown") 
            call her_main("It's a sex-toy of some sort, isn't it?","angry","angry") 
            call her_main("But it is so well crafted...","open","down") 
            call give_gift(">You give the broom to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","upset","closed") 
            call happy(20) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A broom...?","angry","down_raised") 
            call her_main("Hm...") 
            call her_main("What kind of saddle is that...?","disgust","glance") 
            call her_main("Well, doesn't matter.","open","closed") 
            call her_main("Refusing an expensive gift like that would be rude...") 
            call give_gift(">You give the broom to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","upset","closed") 
            call happy(30) 
        if whoring >= 18: # Lv 7+  
            call her_main("A broom...","base","down") 
            call her_main("Hm...") 
            call her_main("That saddle, [genie_name]...","open","baseL",cheeks="blush") 
            call her_main("It was designed especially for witches, was it not?","open","squint",cheeks="blush") 
            call her_main("I am not sure whether this is inappropriate or clever...","annoyed","annoyed") 
            call her_main("But this is a brilliant piece of engineering eitherway...","base","suspicious") 
            call give_gift(">You give the broom to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","glance") 
            call happy(30) 
    if gift_id == 17:#sex doll
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Is this...","shock","wide") 
            call her_main("A sex doll?!","angry","worriedCl",emote="05") 
            call her_main("[genie_name]!!!","scream","worriedCl") 
            call upset(20) 
            $ h_body = "body_33"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A sex doll?","shock","wide") 
            call her_main("This is just so unbecoming for an esteemed wizard such as yourself, [genie_name]...","upset","closed") 
            call upset(20) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A sex doll...","angry","down_raised") 
            call her_main("This is a little inappropriate...","upset","closed") 
            call her_main("But maybe we could use it for a prank or something...","base","down") 
            call give_gift(">You give the blow-up doll to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","down") 
            call happy(10) 
        if whoring >= 18: # Lv 7+  
            call her_main("the Joanne sex doll?","annoyed","down") 
            call her_main("I Can't say that I approve of this...","open","baseL",cheeks="blush") 
            call her_main("But I know Harry would love to have a go at it...","base","down") 
            call give_gift(">You give the blow-up doll to Hermione...",gift_id) 
            call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush") 
            call happy(30) 
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    show screen hermione_main
    with d3
    return
    
label give_gift(text = "", gift = 0):
    hide screen hermione_main
    with d3
    # note that gift is the index (starting with 0), while the image
    # files are starting with/off by 1!
    $ the_gift = "images/store/gifts/"+str(gift+1)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift_item_inv[gift] -= 1
    return
    
    
###GIVING CLOTHING RESPONSES
label giving_gryffindor_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A Cheerleading costume?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Gryffindor Cheerleading outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name], although I don't know when I'd wear it.","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    

label giving_slytherin_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A Cheerleading costume? For Slytherin?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Slytherin Cheerleading outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name], even though I'm not in Slytherin...","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    

label giving_maid_outfit:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    $ nets = 7 # Means already gifted.
    call her_main("A maid outfit?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A maid outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name].","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    

label giving_silk_nightgown:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A nightgown?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png"# blue box
    show screen gift
    with d3
    ">You give the nightgown to Hermione...\n>A silk nightgown has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name].","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    
    
    
label giving_skirt:
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
    $ days_without_an_event = 0
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5
    
    
    $ mad = 0
    m "Here... This is for you..."
    $ the_gift = "images/store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">You give the school miniskirt to Hermione..."
    hide screen gift
    with d3
    hide screen hermione_main
    with d3
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    call her_main("Hm...? What is this?","base","base") 
    call her_main("A skirt?","open","worried") 
    call her_main("Thank you [genie_name].","base","base") 
    #her "Thank you professor."
    m "Don't mention it."
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "body_01"
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    jump day_time_requests
    
### DRESS CODE ###
label mini_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("You cannot be serious, [genie_name]!","open","angryCl") 
        her "A skirt this short?!"
        call her_main("...It barely covers anything, [genie_name].","annoyed","annoyed") 
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","disgust","glance") 
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("well, alright...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset 
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","soft","base") 
        call her_main("But it's so short...","annoyed","suspicious") 
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","normal","frown") 
                call her_main("I refuse!","annoyed","frown") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") 
                call her_main("Well, in that case...","open","suspicious") 
                call her_main("As long as it benefits my house...","annoyed","worriedL") 
            "\"Fine. Forget it\"":
                call her_main("Alright...","base","base") 
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","soft","base") 
        call her_main("But it's so short...","annoyed","suspicious") 
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("Alright, alright...","annoyed","angryL") 
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") 
                call her_main("Alright. I don't mind then.","grin","baseL") 
            "\"Fine. Forget it\"":
                call her_main("Oh...","soft","baseL") 
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        call her_main("Of course, [genie_name]...","angry","down_raised") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_02 = True
    $ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label mini_off:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("I'm glad that you came to your senses, [genie_name].","open","angryCl") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Gladly, [genie_name].","base","base") 

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Alright...","soft","baseL") 
    
    if whoring >= 18: # Lv 7+
        call her_main("That boring thing again?","angry","worried") 
    
    
    $ legs_02 = False
    $ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
   
label tiny_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("You cannot be serious, [genie_name]!","open","angryCl") 
        her "A skirt THIS short?!"
        call her_main("...It doesn't cover anything, [genie_name].","annoyed","annoyed") 
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                her "........................"
                her "..............................."
                call her_main("well, alright...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset 
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","soft","base") 
        call her_main("But it's soooo short...","annoyed","suspicious") 
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","normal","frown") 
                call her_main("I refuse!","annoyed","frown") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                call her_main("Hm...","normal","frown") 
                call her_main("Well, in that case...","open","suspicious") 
                call her_main("As long as it benefits my house...","annoyed","worriedL") 
            "\"Fine. Forget it\"":
                call her_main("Alright...","base","base") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","soft","base") 
        call her_main("But it's soooo short...","annoyed","suspicious") 
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("Alright, alright...","annoyed","angryL") 
            "\"I will give you 10 points.\"":
                $ gryffindor +=10
                call her_main("Hm...","normal","frown") 
                call her_main("Alright. I don't mind then.","grin","baseL") 
            "\"Fine. Forget it\"":
                call her_main("Oh...","soft","baseL") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        call her_main("Of course, [genie_name]...","angry","down_raised") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_03 = True
    $ legs_02 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label give_glasses:
    call her_main("But I don't need glasses...","base","base") 
    
    $ glasses_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label take_glasses:
    call her_main("I was just getting used to them though.","base","base") 
    
    $ glasses_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label badge_put:
    call her_main("Of course, [genie_name]...","base","base") 
    
    $ hermione_badges = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_off:
    call her_main("That boring old thing? ok then","open","suspicious") 
    
    $ wear_shirts = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_on:
    call her_main("Finally, it was soooo boring dressing like this","base","base") 
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_on:
    call her_main("What, I can't do that, everyone would call me a slut","angry","angry") 
    m "just do it"
    $ h_body = "body_30"
    her "[genie_name], I have to draw a line somewhere, I'm not walking around with no shirt on!"
    m "i'll give you 100 points"
    her "200"
    m "sure, why not"
    her ".............fine"
    
    $ wear_shirts = False
    $ gryffindor +=200
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_off:
    call her_main("oh thank you, you have no idea what it was like...","base","base") 
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label g_stockings_on:
    call her_main("Ok then","base","base") 
    
    $ stockings = 2
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label g_stockings_off:
    call her_main("Ok.","base","base") 
    
    $ stockings = 0
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_on:
    call her_main("A bra?","base","base") 
    m "I thought that you could use a new one."
    her "Thank you [genie_name]."
    
    $ custom_bra = 1
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_off:
    call her_main("Ok","base","base") 
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_on:
    call her_main("You want me to wear this?","base","base") 
    m "No one will see it."
    her "...Fine"
    
    $ custom_bra = 2
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_off:
    call her_main("Finally. This thing isn't very comfortable.","base","base") 
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label silk_on:
    call her_main("You want me to change bra?","base","base") 
    her "Ok then"
    
    $ custom_bra = 3
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label silk_off:
    call her_main("Ok","base","base") 
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_on:
    call her_main("What is this?","base","base") 
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_06_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_off:
    call her_main("Ok","base","base") 
    
    $ custom_06_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_on:
    call her_main("What is this?","base","base") 
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_07_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_off:
    call her_main("Ok","base","base") 
    
    $ custom_07_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_08_on:
    call her_main("What is this?","base","base") 
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_08_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_08_off:
    call her_main("Ok","base","base") 
    
    $ custom_08_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_on:
    call her_main("What is this?","base","base") 
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_09_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_off:
    call her_main("Ok","base","base") 
    
    $ custom_09_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_10_on:
    call her_main("What is this?","base","base") 
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_10_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_10_off:
    call her_main("Ok","base","base") 
    
    $ custom_10_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label h_top_on:
    hide screen hermione_main
    with d5  
    $ hermione_wear_top = True
    call update_her_uniform 
    show screen hermione_main
    with d5 
    return
    
label h_top_off:
    hide screen hermione_main
    with d5    
    $ hermione_wear_top = False
    call update_her_uniform 
    show screen hermione_main
    with d5 
    return
    
label h_skirt_on:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = True
    call update_her_uniform 
    show screen hermione_main
    with d5 
    return
    
label h_skirt_off:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = False
    call update_her_uniform 
    show screen hermione_main
    with d5 
    return
    
###WEAR PANTIES
label h_panties_on:
    m "I want you to start wearing panties again"
    her "those boring old things"
    m "yep"
    her "do i get anything for this"
    menu:
        "hows 5 points sound":
            $ gryffindor += 5
            pass
        "nope just do it":
            pass
    her "fine I'll do it"
    $ h_request_wear_panties = True
    return
    
label h_panties_off:
    m "stop wearing those panties"
    her "freedom at last"
    $ h_request_wear_panties = False
    return
    
label h_badge_on(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = True
    $ h_badge = badge
    call update_her_uniform 
    show screen hermione_main
    with d5
    return
    
label h_badge_off(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = False
    $ h_badge = ""
    call update_her_uniform 
    show screen hermione_main
    with d5
    return
    

    


    
label set_h_costume(costume_id = 0):
    hide screen hermione_main
    with d5
    call h_outfit_OBJ(costume_id) 
    show screen hermione_main
    with d5
    return
    

#call play_sound("door") #Sound of a door opening.
    
label badge_take:
    call her_main("As you wish, [genie_name]...","base","base") 
    $ badges = True
    $ ba_01 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
### FISHNETS ###
label nets_put:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("fishnet stockings...?","open","worried") 
        call her_main("You cannot be serious, [genie_name]!","open","base") 
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","annoyed","angryL") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("well, alright...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 5
                call upset 
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","soft","base") 
        call her_main("I am not that kind of girl [genie_name]...","annoyed","suspicious") 
        her "You may have better luck with someone from \"Slytherin\"..."
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","normal","frown") 
                call her_main("I refuse!","annoyed","frown") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") 
                call her_main("Well, in that case...","open","suspicious") 
                call her_main("As long as it benefits my house...","annoyed","worriedL") 
            "\"Fine. Forget it\"":
                call her_main("Alright...","base","base") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
    
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","soft","base") 
        call her_main("Fishnet stockings?","annoyed","suspicious") 
        call her_main("I don't know about that [genie_name]...","annoyed","worriedL") 
        m "..."
        menu:
            "\"Just put them on!\"":
                call her_main("Alright, alright...","annoyed","angryL") 
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") 
                call her_main("Alright. I don't mind then.","grin","baseL") 
            "\"Fine. Forget it\"":
                call her_main("Oh...","soft","baseL") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3            
        jump day_time_requests
    
    if whoring >= 18: # Lv 7+
        call her_main("If you insist, [genie_name]...","angry","down_raised") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
    
    $ ne = True # Shows fishnets layer.
    $ ne_01 = True # Shows the fishnets.
    
    #$ legs_02 = True
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label nets_take:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("I'm glad that you came to your senses, [genie_name].","open","angryCl") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Gladly, [genie_name].","base","base") 

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("As you wish, [genie_name].","annoyed","angryL") 
    
    if whoring >= 18: # Lv 7+
        call her_main("Really? Aw...","angry","worried") 
    
    
    $ ne = False # Shows fishnets layer.
    $ ne_01 = False # Shows the fishnets.
    #$ legs_02 = False
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main
    with d3
    jump day_time_requests

#

    


    
