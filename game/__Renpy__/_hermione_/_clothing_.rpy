label __init_variables:
    
    if not hasattr(renpy.store,'hg_clothing') or True:
        $ hg_clothing = hg_custom_clothing(id='default', name='hermione default clothing', static=True)
        # this is whats currently equipped to change to a diffrent outfit simply .load() it

    $ hg_dev_clothing_saves = {}

    # this is an example of a devloper assigned static save
    # to load this save we would simply call hg_clothing.load('hg_g_cheer')
    $ hg_custom_clothing( id="default", name="hermione default clothing", static=True ).save()
    $ hg_custom_clothing(
        id   = "hg_cheer",
        name = "Generic Cheerleader",
        static = True,

        breasts = "breasts_normal_pressed",

        top     = hg_clothing_items.get('cheer_top'),
        bottom  = hg_clothing_items.get('cheer_skirt')
    ).save()
    $ hg_custom_clothing(
        id   = "hg_rocker",
        name = "Punk Rocker",
        static = True,

        breasts = "breasts_normal_pressed",

        top     = hg_clothing_items.get('wicked_leather_jacket'),
        bottom  = hg_clothing_items.get('pants_jeans'),

        gloves = clothing_item(
            name        = "leather_short",
            wear        = True
        )
    ).save()
    $ hg_custom_clothing(
        id   = "hg_wicked",
        name = "Wicked Rocker",
        static = True,

        breasts = "breasts_normal_pressed",

        top     = hg_clothing_items.get('wicked_rocker_top'),
        bottom  = hg_clothing_items.get('pants_rocker'),

        gloves = clothing_item(
            name        = "rocker_band",
            wear        = True
        )
    ).save()

    # Clothing Sets
    # 99% of the data in theese objects is static so the dynamic data has been moved and these will serve as static refrences only
    $ hg_outfits = outfit_container(
        # hg_outfit(
        #     id = 'hg_MaidLingerie',
        #     name = "Maid Lingerie",
        #     cost = 160,
        #     wait_time = 2,
        #     store_image = "maid_lingerie.png"
        # ),
        # hg_outfit(
        #     id = 'hg_silkNightgown',
        #     name = "Silk Nightgown",
        #     cost = 140,
        #     wait_time = 2,
        #     store_image = "nightgown.png"
        # ),
        hg_outfit(
            id = 'hg_maid',
            name = 'Maid',
            cost = 250,
            wait_time = 2,
            store_image = 'maid.png',
            outfit_layers = ['maid_stockings.png','maid_skirt.png','maid_top.png','maid_gloves.png'],
            breast_layer = 'breasts_normal_pressed',
            top_layers = ['maid_hat.png']
        ),
        hg_outfit(
            id = 'hg_heartDancer',
            name = 'Heart Dancer',
            cost = 300,
            wait_time = 4,
            store_image = 'heart.png',
            outfit_layers = ['heart_legs.png','heart_top.png','heart_collar.png'],
            breast_layer = 'breasts_normal'
        ),
        hg_outfit(
            id = 'hg_pirate',
            name = 'Pirate',
            cost = 75,
            wait_time = 2,
            store_image = 'pirate.png',
            outfit_layers = ['pirate_legs.png','pirate_pants.png','pirate_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hg_outfit(
            id = 'hg_powerGirl',
            name = 'Power Girl',
            cost = 350,
            wait_time = 3,
            store_image = 'power.png',
            outfit_layers = ['power_cape.png','power_top.png','power_gloves.png','power_belt.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'power_hair'
        ),
        hg_outfit(
            id = 'hg_msMarvel',
            name = 'Mrs Marvel',
            cost = 250,
            wait_time = 5,
            store_image = 'marvel.png',
            outfit_layers = ['marvel_pants.png','marvel_top.png','marvel_sash.png','marvel_gloves.png'],
            breast_layer = 'breasts_normal'
        ),
        hg_outfit(
            id = 'hg_harleyQuinn',
            name = 'Harley Quinn',
            cost = 300,
            wait_time = 4,
            store_image = 'harley.png',
            outfit_layers = ['harley_pants.png','harley_top.png','harley_gloves.png','harley_collar.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'harley_hair'
        ),
        hg_outfit(
            id = 'hg_ballDress',
            name = 'Ball Dress',
            cost = 1500,
            wait_time = 7,
            store_image = 'ball_dress.png',
            outfit_layers = ['ball_dress_skirt.png','ball_dress_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hg_outfit(
            id = 'hg_christmas',
            name = 'Christmas Girl',
            cost = 50,
            wait_time = 2,
            store_image = 'christmas.png',
            outfit_layers = ['christmas_pants.png','christmas_top.png','christmas_gloves.png','christmas_collar.png'],
            top_layers = ['christmas_antlers.png'],
            breast_layer = 'breasts_normal_pressed'
        ),
        hg_outfit(
            id = 'hg_laraCroft',
            name = 'Lara Croft',
            cost = 270,
            wait_time = 2,
            store_image = 'lara.png',
            outfit_layers = ['lara_pants.png','lara_top.png','lara_gloves.png'],
            breast_layer = 'breasts_normal'
        ),
        hg_outfit(
            id = 'hg_tifa',
            name = 'Tifa',
            cost = 220,
            wait_time = 2,
            store_image = 'tifa.png',
            outfit_layers = ['tifa_pants.png','tifa_top.png','tifa_gloves.png','tifa_ear.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'tifa_hair'
        ),
        hg_outfit(
            id = 'hg_present',
            name = 'Present',
            cost = 35,
            wait_time = 1,
            store_image = 'present.png',
            outfit_layers = ['present_pant.png','present_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hg_outfit(
            id = 'hg_japan',
            name = 'Japanese Schoolgirl',
            cost = 125,
            wait_time = 2,
            store_image = 'japan.png',
            outfit_layers = ['japan_pant.png','japan_top.png'],
            breast_layer = 'breasts_normal_pressed'
        ),
        hg_outfit(
            id = 'hg_witch',
            name = 'Witch outfit',
            cost = 250,
            wait_time = 3,
            store_image = 'witch.png',
            outfit_layers = ['witch_stockings.png','witch_top.png','witch_cloak.png','witch_hat.png'],
            breast_layer = 'breasts_normal_pressed'
        ),
        hg_outfit(
            id = 'hg_bio',
            name = 'Bioshock outfit',
            cost = 400,
            wait_time = 3,
            store_image = 'bio.png',
            outfit_layers = ['bio_skirt.png','bio_chocker.png','bio_corset.png','bio_jacket.png'],
            breast_layer = 'breasts_normal_pressed',
        ),
        hg_outfit(
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


init python:

    if not hasattr(renpy.store,'hg_clothing_saves'):
        hg_clothing_saves  = {}
        # this stores the state of the custom outfit for whenever .save() is called 
        # b/c this is a basic dictionary it will also persist through reloads 


    class hg_outfit(character_outfit):
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


    class hg_custom_clothing(custom_clothing):
        id   = "default" # unique string for internal use
        name = ""        # name to display to user
        static = False

        hair        = "A"
        hair_color  = "1"

        breasts = "breasts_nipfix"

        top     = hg_clothing_items.get('uni_top')
        bottom  = hg_clothing_items.get('uni_skirt')

        bra = clothing_item(
            name        = "base",
            color       = "base",
            wear        = True,
            always_wear = True
        )

        panties = clothing_item(
            name        = "base",
            color       = "base",
            overlay     = False,
            wear        = True,
            always_wear = True
        )

        onepiece    = clothing_item()
        garterbelt  = clothing_item()
        neckwear    = clothing_item()
        gloves      = clothing_item()
        stockings   = clothing_item()
        robe        = clothing_item( name="robe_1" )
        hat         = clothing_item()
        glasses     = clothing_item()
        ears        = clothing_item(
            wear        = True,
            always_wear = True
        )
        buttplug    = clothing_item()

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

        def get_layers(self, body):
            global hermione_action

            layers = []
            
            #Garterbelt
            if self.garterbelt.wear:
                layers.append( self.garterbelt.get_file( "clothes/underwear/garterbelts/" ) )

            #Stockings
            if self.stockings.wear:
                layers.append( self.stockings.get_file( "clothes/underwear/stockings/" ) )

            #Bottom
            bot_actions = ['lift_skirt']#, 'pants_down']
            if self.bottom.wear and body.action not in bot_actions:
                layers.append( self.bottom.get_file( "clothes/bottoms/" ) )
            #Panties
            elif self.panties.wear:
                layers.append( self.panties.get_file("clothes/underwear/panties/") )
                if hasattr(self.panties, 'overlay') and self.panties.overlay:
                    layers.append( "clothes/underwear/pantystain.png" )


            # #Action/Pose Fix A (layer above skirt)
            if 'a' in body.action_layers:
                layers.append( body.action_layers['a'] )

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
            top_actions = ['lift_top', 'lift_skirt', 'hold_book', 'pants_down']

            if body.large_breasts:
                top_path = "clothes/tops/__large_breasts__/"
            else:
                top_path = "clothes/tops/"

            if self.top.wear and body.action not in top_actions:
                layers.append( self.top.get_file( top_path ) )
            else:
                #Bra
                if self.bra.wear:
                    layers.append( self.bra.get_file( "clothes/underwear/bra/" ) )
                if body.action in self.top.actions  and body.action in top_actions:
                    layers.append( self.top.get_file( top_path + "_"+body.action+"_/" ) )

            # #Bottom above top layer
            # if self.bottom.wear and body.action not in bot_actions:
            #     if body.action not in [None, 'hold_book', 'lift_skirt'] or ( body.action == 'lift_top' ):
            #         layers.append( self.bottom.get_file( "clothes/bottoms/" ) )
            
            #lifted skirt
            if body.action in self.bottom.actions and body.action in bot_actions:
                layers.append( self.bottom.get_file( "clothes/bottoms/_"+body.action+"_/" ) )


            #Badges & Belts
            if notNull( self.accs ):
                layers.extend( [ "accessories/body_accs/"+str(acc)+".png" for acc in self.accs ] )

            #Action/Pose Fix B (layer above top)
            if 'b' in body.action_layers:
                layers.append( body.action_layers['b'] )
            
            #Robe
            if self.robe.wear:
                layers.append( self.robe.get_file( "clothes/robe/" ) )

            #Neckwear
            if self.neckwear.wear:
                layers.append( self.neckwear.get_file( "clothes/neckwear/" ) )

            return layers