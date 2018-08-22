label __init_variables:
    
    $ hermione_clothing_set_list = []
    $ hermione_outfits_list = []

    return


init python:

    if not hasattr(renpy.store,'hg_clothing_saves'):
        hg_clothing_saves  = {}
        # this stores the state of the custom outfit for whenever .save() is called 
        # b/c this is a basic dictionary it will also persist through reloads 

    class hg_custom_outfit(character_outfit):
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

        top     = hg_clothing_items.get('top','uni_top')
        bottom  = hg_clothing_items.get('bottom','uni_skirt')

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
                layers.append( self.stockings.get_file( "clothes/stockings/" ) )

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