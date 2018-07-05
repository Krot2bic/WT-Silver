label __init_variables:
    
    if not hasattr(renpy.store,'hg_clothing'):
        $ hg_clothing = hg_custom_outfit('hg_clothing','hermione default clothing')
        # this is whats currently equipped to change to a diffrent outfit simply .load() it

    $ hg_dev_clothing_saves = {}

    # this is an example of a devloper assigned static save
    # to load this save we would simply call hg_clothing.load('hg_g_cheer')
    $ hg_custom_outfit( id="default", name="default", static=True ).save()
    $ hg_custom_outfit(
        id   = "hg_g_cheer",
        name = "Gryffindor Cheerleader",
        static = True,

        breasts = "breasts_normal_pressed",

        top = outfit_item(
            name        = "cheer_top",
            color       = "g",
            wear        = True,
            always_wear = True
        ),

        bottom = outfit_item(
            name        = "cheer_skirt",
            color       = "g",
            wear        = True,
            always_wear = True
        )
    ).save()
    $ hg_custom_outfit(
        id   = "hg_g_cheer_skimp",
        name = "Sexy Gryffindor Cheerleader",
        static = True,

        breasts = "breasts_normal_pressed",

        top = outfit_item(
            name        = "cheer_top",
            color       = "g",
            version     = "skimpy",
            wear        = True,
            always_wear = True
        ),

        bottom = outfit_item(
            name        = "cheer_skirt",
            color       = "g",
            version     = "skimpy",
            wear        = True,
            always_wear = True
        )
    ).save()
    # $ hg_custom_outfit(
    #     id   = "hg_s_cheer",
    #     name = "Slythrin Cheerleader",
    #     static = True,

    #     breasts = "breasts_normal_pressed",

    #     top = outfit_item(
    #         name        = "cheer_top",
    #         color       = "s",
    #         wear        = True,
    #         always_wear = True
    #     ),

    #     bottom = outfit_item(
    #         name        = "cheer_skirt",
    #         color       = "s",
    #         wear        = True,
    #         always_wear = True
    #     )
    # ).save()
    # $ hg_custom_outfit(
    #     id   = "hg_s_cheer_skimp",
    #     name = "Sexy Slythrin Cheerleader",
    #     static = True,

    #     breasts = "breasts_normal_pressed",

    #     top = outfit_item(
    #         name        = "cheer_top",
    #         color       = "s",
    #         version     = "skimpy",
    #         wear        = True,
    #         always_wear = True
    #     ),

    #     bottom = outfit_item(
    #         name        = "cheer_skirt",
    #         color       = "s",
    #         version     = "skimpy",
    #         wear        = True,
    #         always_wear = True
    #     )
    # ).save()
    # $ hg_custom_outfit(
    #     id   = "hg_r_cheer",
    #     name = "Ravenclaw Cheerleader",
    #     static = True,

    #     breasts = "breasts_normal_pressed",

    #     top = outfit_item(
    #         name        = "cheer_top",
    #         color       = "r",
    #         wear        = True,
    #         always_wear = True
    #     ),

    #     bottom = outfit_item(
    #         name        = "cheer_skirt",
    #         color       = "r",
    #         wear        = True,
    #         always_wear = True
    #     )
    # ).save()
    # $ hg_custom_outfit(
    #     id   = "hg_r_cheer_skimp",
    #     name = "Sexy Ravenclaw Cheerleader",
    #     static = True,

    #     breasts = "breasts_normal_pressed",

    #     top = outfit_item(
    #         name        = "cheer_top",
    #         color       = "r",
    #         version     = "skimpy",
    #         wear        = True,
    #         always_wear = True
    #     ),

    #     bottom = outfit_item(
    #         name        = "cheer_skirt",
    #         color       = "r",
    #         version     = "skimpy",
    #         wear        = True,
    #         always_wear = True
    #     )
    # ).save()
    # $ hg_custom_outfit(
    #     id   = "hg_h_cheer",
    #     name = "Hufflepuff Cheerleader",
    #     static = True,

    #     breasts = "breasts_normal_pressed",

    #     top = outfit_item(
    #         name        = "cheer_top",
    #         color       = "h",
    #         wear        = True,
    #         always_wear = True
    #     ),

    #     bottom = outfit_item(
    #         name        = "cheer_skirt",
    #         color       = "h",
    #         wear        = True,
    #         always_wear = True
    #     )
    # ).save()
    # $ hg_custom_outfit(
    #     id   = "hg_h_cheer_skimp",
    #     name = "Sexy Hufflepuff Cheerleader",
    #     static = True,

    #     breasts = "breasts_normal_pressed",

    #     top = outfit_item(
    #         name        = "cheer_top",
    #         color       = "h",
    #         version     = "skimpy",
    #         wear        = True,
    #         always_wear = True
    #     ),

    #     bottom = outfit_item(
    #         name        = "cheer_skirt",
    #         color       = "h",
    #         version     = "skimpy",
    #         wear        = True,
    #         always_wear = True
    #     )
    # ).save()
    $ hg_custom_outfit(
        id   = "hg_rocker",
        name = "Punk Rocker",
        static = True,

        breasts = "breasts_normal_pressed",

        top = outfit_item(
            name        = "wicked_leather_jacket",
            version     = "sleeves",
            wear        = True
        ),

        bottom = outfit_item(
            name        = "pants_jeans",
            color       = "base",
            version     = "long",
            wear        = True
        ), 

        gloves = outfit_item(
            name        = "leather_short",
            wear        = True
        )
    ).save()
    $ hg_custom_outfit(
        id   = "hg_wicked",
        name = "Wicked Rocker",
        static = True,

        breasts = "breasts_normal_pressed",

        top = outfit_item(
            name        = "wicked_rocker_top",
            wear        = True
        ),

        bottom = outfit_item(
            name        = "pants_rocker",
            color       = "base",
            wear        = True
        ), 

        gloves = outfit_item(
            name        = "rocker_band",
            wear        = True
        )
    ).save()

    # Clothing Sets
    # 99% of the data in theese objects is static so the dynamic data has been moved and these will serve as static refrences only
    $ hg_outfits = outfit_container(
        # hermione_outfit(
        #     id = 'hg_gryffCheer',
        #     name = "Griffindor Cheerleader",
        #     cost = 80,
        #     wait_time = 2,
        #     store_image = "cheer_gryff.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_gryffCheerSkimpy',
        #     name = "Sexy Griffindor Cheerleader",
        #     cost = 140,
        #     wait_time = 3,
        #     store_image = "cheer_gryff_skimpy.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_slythCheer',
        #     name = "Slythrin Cheerleader",
        #     cost = 80,
        #     wait_time = 2,
        #     store_image = "cheer_slyth.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_slythCheerSkimpy',
        #     name = "Sexy Slythrin Cheerleader",
        #     cost = 140,
        #     wait_time = 3,
        #     store_image = "cheer_slyth_skimpy.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_ravenCheer',
        #     name = "Ravenclaw Cheerleader",
        #     cost = 80,
        #     wait_time = 2,
        #     store_image = "cheer_raven.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_ravenCheerSkimpy',
        #     name = "Sexy Ravenclaw Cheerleader",
        #     cost = 140,
        #     wait_time = 3,
        #     store_image = "cheer_raven_skimpy.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_hufflCheer',
        #     name = "Hufflepuff Cheerleader",
        #     cost = 80,
        #     wait_time = 2,
        #     store_image = "cheer_huffl.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_hufflCheerSkimpy',
        #     name = "Sexy Hufflepuff Cheerleader",
        #     cost = 140,
        #     wait_time = 3,
        #     store_image = "cheer_huffl_skimpy.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_MaidLingerie',
        #     name = "Maid Lingerie",
        #     cost = 160,
        #     wait_time = 2,
        #     store_image = "maid_lingerie.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_silkNightgown',
        #     name = "Silk Nightgown",
        #     cost = 140,
        #     wait_time = 2,
        #     store_image = "nightgown.png"
        # ),
        # hermione_outfit(
        #     id = 'hg_rocker',
        #     name = "Rocker",
        #     cost = 180,
        #     wait_time = 2,
        #     store_image = "rocker.png"
        # ),
        hermione_outfit(
            id = 'hg_maid',
            name = 'Maid',
            cost = 250,
            wait_time = 2,
            store_image = 'maid.png',
            outfit_layers = ['maid_stockings.png','maid_skirt.png','maid_top.png','maid_gloves.png'],
            breast_layer = 'breasts_normal_pressed',
            top_layers = ['maid_hat.png']
        ),
        hermione_outfit(
            id = 'hg_heartDancer',
            name = 'Heart Dancer',
            cost = 300,
            wait_time = 4,
            store_image = 'heart.png',
            outfit_layers = ['heart_legs.png','heart_top.png','heart_collar.png'],
            breast_layer = 'breasts_normal'
        ),
        hermione_outfit(
            id = 'hg_pirate',
            name = 'Pirate',
            cost = 75,
            wait_time = 2,
            store_image = 'pirate.png',
            outfit_layers = ['pirate_legs.png','pirate_pants.png','pirate_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hermione_outfit(
            id = 'hg_powerGirl',
            name = 'Power Girl',
            cost = 350,
            wait_time = 3,
            store_image = 'power.png',
            outfit_layers = ['power_cape.png','power_top.png','power_gloves.png','power_belt.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'power_hair'
        ),
        hermione_outfit(
            id = 'hg_msMarvel',
            name = 'Mrs Marvel',
            cost = 250,
            wait_time = 5,
            store_image = 'marvel.png',
            outfit_layers = ['marvel_pants.png','marvel_top.png','marvel_sash.png','marvel_gloves.png'],
            breast_layer = 'breasts_normal'
        ),
        hermione_outfit(
            id = 'hg_harleyQuinn',
            name = 'Harley Quinn',
            cost = 300,
            wait_time = 4,
            store_image = 'harley.png',
            outfit_layers = ['harley_pants.png','harley_top.png','harley_gloves.png','harley_collar.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'harley_hair'
        ),
        hermione_outfit(
            id = 'hg_ballDress',
            name = 'Ball Dress',
            cost = 1500,
            wait_time = 7,
            store_image = 'ball_dress.png',
            outfit_layers = ['ball_dress_skirt.png','ball_dress_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hermione_outfit(
            id = 'hg_christmas',
            name = 'Christmas Girl',
            cost = 50,
            wait_time = 2,
            store_image = 'christmas.png',
            outfit_layers = ['christmas_pants.png','christmas_top.png','christmas_gloves.png','christmas_collar.png'],
            top_layers = ['christmas_antlers.png'],
            breast_layer = 'breasts_normal_pressed'
        ),
        hermione_outfit(
            id = 'hg_laraCroft',
            name = 'Lara Croft',
            cost = 270,
            wait_time = 2,
            store_image = 'lara.png',
            outfit_layers = ['lara_pants.png','lara_top.png','lara_gloves.png'],
            breast_layer = 'breasts_normal'
        ),
        hermione_outfit(
            id = 'hg_tifa',
            name = 'Tifa',
            cost = 220,
            wait_time = 2,
            store_image = 'tifa.png',
            outfit_layers = ['tifa_pants.png','tifa_top.png','tifa_gloves.png','tifa_ear.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'tifa_hair'
        ),
        hermione_outfit(
            id = 'hg_present',
            name = 'Present',
            cost = 35,
            wait_time = 1,
            store_image = 'present.png',
            outfit_layers = ['present_pant.png','present_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hermione_outfit(
            id = 'hg_japan',
            name = 'Japanese Schoolgirl',
            cost = 125,
            wait_time = 2,
            store_image = 'japan.png',
            outfit_layers = ['japan_pant.png','japan_top.png'],
            breast_layer = 'breasts_normal_pressed'
        ),
        hermione_outfit(
            id = 'hg_witch',
            name = 'Witch outfit',
            cost = 250,
            wait_time = 3,
            store_image = 'witch.png',
            outfit_layers = ['witch_stockings.png','witch_top.png','witch_cloak.png','witch_hat.png'],
            breast_layer = 'breasts_normal_pressed'
        ),
        hermione_outfit(
            id = 'hg_bio',
            name = 'Bioshock outfit',
            cost = 400,
            wait_time = 3,
            store_image = 'bio.png',
            outfit_layers = ['bio_skirt.png','bio_chocker.png','bio_corset.png','bio_jacket.png'],
            breast_layer = 'breasts_normal_pressed',
        ),
        hermione_outfit(
            id = 'hg_yenn',
            name = 'Yennefer\'s costume',
            cost = 500,
            wait_time = 4,
            store_image = 'yenn.png',
            outfit_layers = ['yenn_stockings.png','yenn_pant.png','yenn_skirt.png','yenn_top.png','yenn_gloves.png','yenn_chocker.png','yenn_scarf.png','yenn_belt.png'],
            breast_layer = 'breasts_normal'
        )
    )
        
    
    $ hermione_clothing_set_list = []
    $ hermione_outfits_list = []

    return




## Outfit Blocks
label set_hermione_outfit(outfit):
    show screen blkfade
    hide screen hermione_main
    with d3
    call h_outfit_OBJ(outfit)
    pause .5
    hide screen blkfade
    with d5
    return

label h_outfit_OBJ(outfit):
    if outfit == None:
        $ hermione_costume = False
        call update_her_uniform
        call h_update_hair
    else:
        $ hermione_costume = True

        $ h_request_wear_top = True
        $ hermione_wear_top = True

        $ hermoine_outfit_GLBL = outfit

        if hermione_use_action and hermione_action in hermoine_outfit_GLBL.actions:
            pass
        else:
            call h_action("None")

        call update_her_uniform
        call h_update_hair

    return


label set_defined_menu_vars:
    python:
        tmp_list_a = []
        tmp_list_b = []
        for i in range(0,hermione_defined_outfit_list_size):
            if hermione_outfit_names[i] not in ["null",""]:
                tmp_list_a.append(hermione_outfit_names[i])
                tmp_list_b.append(i)

        h_menu_list = [[0 for i in xrange(2)] for i in xrange(len(tmp_list_a)+1)]
        for i in range(0,len(tmp_list_a)):
            h_menu_list[i][0] = tmp_list_a[i]
            h_menu_list[i][1] = tmp_list_b[i]
        h_menu_list[len(h_menu_list)-1][0] = "-nevermind-"
        h_menu_list[len(h_menu_list)-1][1] = -1
    return




init python:
    
    # outfit purchases are the only dynamic value we care about so they have been separated into their own dict
    if not hasattr(renpy.store,'clothing_purchases'):
        clothing_purchases = {}
    if not hasattr(renpy.store,'hg_clothing_saves'):
        hg_clothing_saves  = {}
        # this stores the state of the custom outfit for whenever .save() is called 
        # b/c this is a basic dictionary it will also persist through reloads 

    class outfit_container(dict):
            
        def __init__(self, *args):
            for arg in args:
                if hasattr(arg, 'id'):
                    self[arg.id] = arg

        def all(self):
            return self.values()
        
        def purchased(self, to_check):
            global clothing_purchases
            if isinstance(to_check,str):
                return clothing_purchases.get(self.to_check, False)
            if isinstance(to_check,list):
                return all( [ clothing_purchases.get(item, False) for item in to_check ] )
        
        def any_purchased(self, *to_check):
            global clothing_purchases
            if isinstance(to_check,list):
                return any( [ clothing_purchases.get(item, False) for item in to_check ] )
        
    class hermione_outfit(object):
        id = ''
        name = ''
        cost = 0
        wait_time = 0 #the ammount of time to wait until compleded from clothes store
        top_layers = []
        outfit_layers = []
        actions = []
        action_images = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"
        store_image = ""

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def purchase(self):
            global clothing_purchases
            clothing_purchases[self.id] = True
        def purchased(self):
            global clothing_purchases
            return clothing_purchases.get(self.id, False)
        def getMenuText(self):
            return "-"+self.name+"-"
        def getFullPath(self, files):
            return [ 'characters/hermione/clothes/custom/'+self.id+'/'+file for file in files ]
        def getOutfitLayers(self):
            return self.getFullPath(self.outfit_layers)
        def getTopLayers(self):
            return self.getFullPath(self.top_layers)
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]
        def getStoreImage(self):
           return "interface/store/icons/hermione/"+self.store_image

    class outfit_item(object):
        name        = None
        version     = None
        color       = None
        wear        = False
        always_wear = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def __bool__(self):
            return notNull(self.name)
        __nonzero__ = __bool__


        def __str__(self):
            if notNull(self.name, self.color, self.version):
                return '/'+str(self.name)+'/'+str(self.color)+'_'+str(self.version)
            if notNull(self.name, self.version):
                return '/'+str(self.name)+'_'+str(self.version)
            if notNull(self.name):
                return '/'+str(self.name)
            return ""

        def get_file(self, root):
            if notNull( self.name, self.color, self.version ):
                return ( root + str(self.name) + "/" + str(self.color) + "_" + str(self.version) + ".png" )
            elif notNull( self.name, self.version ):
                return ( root + str(self.name) + "/" + str(self.version) +".png" )
            elif notNull( self.name, self.color ):
                return ( root + str(self.name) + "/" + str(self.color) +".png" )
            elif notNull( self.name ):
                return ( root + str(self.name) + ".png" )
        
        def notNull(self, *atts):
            li = []
            for att in atts:
                if not hasattr(self, att) or getattr(self, att) == None or getattr(self, att) == "" or getattr(self, att) == []:
                    li.append(False)
                else:
                    li.append(True)
            return all(li)

        def save(self):
            dic = {}
            for att, value in self.__dict__.items():
                if value != getattr(outfit_item, att, "ATT_DNE"):
                    dic[att] = value
            return dic
        def load(self, dic):
            self.__dict__.update( dic )

    class hg_custom_outfit(object):
        id   = "default" # unique string for internal use
        name = ""        # name to display to user
        static = False

        hair        = "A"
        hair_color  = "1"

        action = None
        actions = {}
        breasts = "breasts_nipfix"

        top = outfit_item(
            name        = "uni_top", # the name of the item.
            version     = "1",       # the varient of the top (_1, _skimpy, _sexy, _sleeves)
            color       = None,      # which color folder the item is in.
            wear        = True,      # if the item is currently worn.
            always_wear = True,      # if the item is worn on resetting the outfit.
            can_lift    = False      # if the item has a action vairent
        )

        bottom = outfit_item(
            name        = "uni_skirt",
            version     = "1",
            color       = "base",
            wear        = True,
            always_wear = True
        )

        bra = outfit_item(
            name        = "base",
            color       = "base",
            wear        = True,
            always_wear = True
        )

        panties = outfit_item(
            name        = "base",
            color       = "base",
            overlay     = False,
            wear        = True,
            always_wear = True
        )

        onepiece    = outfit_item()
        garterbelt  = outfit_item()
        neckwear    = outfit_item()
        gloves      = outfit_item()
        stockings   = outfit_item()
        robe        = outfit_item( name="robe_1" )
        hat         = outfit_item()
        glasses     = outfit_item()
        ears        = outfit_item(
            wear        = True,
            always_wear = True
        )
        buttplug    = outfit_item()

        makeup_lipstick = "nude"
        makeup_list = []
        wear_makeup = False
        always_wear_makeup = False

        accs = []
        wear_accs = False
        always_wear_accs = False

        piercings = []
        wear_piercings = False
        always_wear_piercings = False

        tattoos = []
        wear_tattoos = False
        always_wear_tattoos = False

        transparency = 1
                

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_layers(self):
            global hermione_action

            layers = []
            
            #Garterbelt
            if self.garterbelt.wear:
                layers.append( self.garterbelt.get_file( "clothes/underwear/garterbelts/" ) )

            #Stockings
            if self.stockings.wear:
                layers.append( self.stockings.get_file( "clothes/underwear/stockings/" ) )

            #Bottom
            if self.bottom.wear:
                if self.action in [None, 'hold_book'] and not ( self.onepiece.wear or (hasattr(self.top,'can_lift') and self.top.can_lift) ):
                    layers.append( self.bottom.get_file( "clothes/bottoms/" ) )
            #Panties
            elif self.panties.wear:
                layers.append( self.panties.get_file("clothes/underwear/panties/") )
                if hasattr(self.panties, 'overlay') and self.panties.overlay:
                    layers.append( "clothes/underwear/pantystain.png" )


            # #Action/Pose Fix A (layer above skirt)
            if 'a' in self.actions:
                layers.append( self.actions['a'] )

            # not dealing with this now
            # #One-Piece
            # if hermione_wear_onepiece:
            #     if not h_onepiece in h_onepieces_nighties_list:
            #         add hermione_onepiece xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
            #     else: #Nighties
            #         if hermione_wear_top or hermione_wear_bottom:
            #             pass
            #         else:
            #             add hermione_onepiece xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
            #     if hermione_wear_bottom and h_onepiece in h_onepieces_list:
            #         add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

            #Gloves
            if self.gloves.wear:
                layers.append( self.gloves.get_file( "clothes/gloves/" ) )
            
            #Top
            if self.top.wear:
                layers.append( self.top.get_file( "clothes/tops/" ) )
            #Bra
            elif self.bra.wear:
                layers.append( self.bra.get_file( "clothes/underwear/bra/" ) )

            #Bottom above top layer
            if self.bottom.wear:
                if self.action not in [None, 'hold_book'] or ( self.top.can_lift and self.action == 'lift_top' ):
                    layers.append( self.bottom.get_file( "clothes/bottoms/" ) )

            #Badges & Belts
            if notNull( self.accs ):
                layers.extend( [ "accessories/body_accs/"+str(acc)+".png" for acc in self.accs ] )

            #Action/Pose Fix B (layer above top)
            if 'b' in self.actions:
                layers.append( self.actions['b'] )
            
            #Robe
            if self.robe.wear:
                layers.append( self.robe.get_file( "clothes/robe/" ) )

            #Neckwear
            if self.neckwear.wear:
                layers.append( self.neckwear.get_file( "clothes/neckwear/" ) )

            return layers




        # saves and loads the state of this object to the dictionary 'hg_clothing_saves'
        def save(self, id=None):
            global hg_clothing_saves
            dic = {}
            for att in dir(self):
                if not att.startswith('_'):
                    name = att
                    value = getattr(self, att)
                    if issubclass(value.__class__, object) and value.save():
                        dic[name] = { value.__class__.__name__ :  value.save() }
            dic.update(self.__dict__)
            if self.static:
                hg_dev_clothing_saves[self.id] = dic
            elif id == None:
                hg_clothing_saves[self.id] = dic
            else:
                hg_clothing_saves[id] = dic
        def load(self, id):

            # sets all atts back to default, prevents items from persisting across loads()
            for att in dir(hg_custom_outfit):
                if att not in ['get_layers', 'save', 'load'] and not att.startswith('_'):
                    setattr(self, att, getattr(hg_custom_outfit, att)) 

            global hg_clothing_saves
            if id in hg_dev_clothing_saves:
                load_dic = hg_dev_clothing_saves[id]
            else:
                load_dic = hg_clothing_saves[id]

            dic = {}
            for name, value in load_dic.items():
                if isinstance(value, dict):
                    for class_name in value:
                        class_ = globals()[class_name]
                        class_instance = class_()
                        class_instance.__dict__.update(value[class_name])
                        setattr(self, name, class_instance )
                else:
                    dic[name] = value
            self.__dict__.update( dic )


