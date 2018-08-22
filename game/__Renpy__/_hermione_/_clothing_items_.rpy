init -1 python:
    # This file is essentally a refrence for any item/item-variant that a user may want to equip so that a menu/gui can be built off of this 
    # information and be able to correctly build a path to the corrassponding files

    hg_tattoos = [
        "head/cumslut",
        "head/cunt",
        "head/heart_cheek",
        "head/mudblood",
        "head/whore",
        "pubic/10g",
        "pubic/10g_raised",
        "pubic/cock_hole",
        "pubic/cum_here",
        "pubic/cumslut",
        "pubic/cunt",
        "pubic/deatheater",
        "pubic/deposit",
        "pubic/fuck_me",
        "pubic/impregnation",
        "pubic/inheat",
        "pubic/mudblood",
        "pubic/nocondoms",
        "pubic/paw",
        "pubic/punk_mudblood",
        "pubic/whore",
        "thigh/free",
        "thigh/signature",
        "thigh/tribal",
        "torso/cum_here",
        "torso/twist"
    ]

    hg_piercings = [
        "belly_pearls",
        "ears_hearts",
        "ears_hearts_large",
        "ears_pearls",
        "ears_straight",
        "nipples_pearls"
    ]


    hg_body_options = {
        'hair': [
            character_hair_option(
                type = "hair",
                option = "A",
                color = "1",
                colors = range(1,12)
            ),
            character_hair_option(
                type = "hair",
                option = "B",
                color = "1",
                colors = range(1,11)
            ),
            character_hair_option(
                type = "hair",
                option = "C",
                color = "1",
                colors = range(1,4)
            ),
            character_hair_option(
                type = "hair",
                option = "E",
                color = "1",
                colors = range(1,11)
            ),
            character_hair_option(
                type = "hair",
                option = "F",
                color = "1",
                colors = [1]
            ),
            character_hair_option(
                type = "hair",
                option = "G",
                color = "1",
                colors = [1]
            )
        ]
    }


    hg_clothing_items = clothing_item_container(
        
        #####################
        ### HERMIONE TOPS ###
        #####################

        clothing_item(
            type        = "top",                    # the type of item (top, bottom, gloves,...)
            name        = "uni_top",                # the name of the item.
            version     = "1",                      # the CURRENT varient of the top (1, skimpy, sexy, sleeves)
            color       = None,                     # which color folder the item is in.
            wear        = True,                     # if the item is currently worn.
            always_wear = True,                     # if the item is worn on resetting the outfit.
            actions     = ['lift_top'],             # the actions that this item has
            versions    = ['1','2','3','4','5','6'] # the POSSIBLE varients of the top (1,2,3,...) or ( '' , skimpy )
        ),
        clothing_item(
            type        = "top",
            name        = "cheer_top",
            color       = "g",
            wear        = True,
            always_wear = True,
            versions    = ['', 'skimpy'],
            colors      = ['g','h','r','s']
        ),
        clothing_item(
            type        = "top",
            name        = "pullover",
            color       = "base",
            wear        = True,
            always_wear = True,
            actions     = ['hold_book','lift_skirt','lift_top','pants_down'],
            versions    = ['', 'sexy'],
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "top",
            name        = "wicked_leather_jacket",
            version     = "sleeves",
            wear        = True,
            actions     = ['hold_book','lift_skirt','lift_top','pants_down'],
            versions    = ['sleeves', 'short_sleeves', 'sleeveless']
        ),
        clothing_item(
            type        = "top",
            name        = "normal_sweater",
            wear        = True
        ),
        clothing_item(
            type        = "top",
            name        = "normal_waitress_top",
            breasts     = "breasts_nonips",
            wear        = True
        ),
        clothing_item(
            type        = "top",
            name        = "top_fishnets",
            breasts     = "breasts_normal",
            wear        = True
        ),
        clothing_item(
            type        = "top",
            name        = "wicked_rocker_top",
            wear        = True
        ),


        ########################
        ### HERMIONE BOTTOMS ###
        ########################

        clothing_item(
            type        = "bottom",
            name        = "uni_skirt",
            version     = "1",
            color       = "base",
            wear        = True,
            always_wear = True,
            actions     = ['lift_skirt'],
            versions    = ['1','2','3','4','5'],
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bottom",
            name        = "uni_skirt_low",
            version     = "1",
            color       = "base",
            wear        = True,
            actions     = ['lift_skirt'],
            versions    = ['1','2','3','4'],
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bottom",
            name        = "skirt_belted",
            version     = "mini",
            color       = "base",
            wear        = True,
            actions     = ['lift_skirt'],
            versions    = ['mini','micro'],
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bottom",
            name        = "pants_rocker",
            color       = "base",
            wear        = True,
            actions     = ['lift_skirt'],
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bottom",
            name        = "pants_jeans",
            version     = "long",
            color       = "base",
            wear        = True,
            actions     = ['lift_skirt'],
            versions    = ['long','short'],
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bottom",
            name        = "cheer_skirt",
            color       = "g",
            wear        = True,
            actions     = ['lift_skirt'],
            versions    = ['', 'skimpy'],
            colors      = ['g','h','r','s']
        ),


        ##########################
        ### HERMIONE STOCKINGS ###
        ##########################
        
        clothing_item(
            type        = "stockings",
            name        = "cheer",
            color       = "g",
            wear        = True,
            versions    = ['', 'short', 'vibe'],
            colors      = ['g','h','r','s']
        ),
        clothing_item(
            type        = "stockings",
            name        = "cute",
            wear        = True
        ),
        clothing_item(
            type        = "stockings",
            name        = "fishnets",
            wear        = True
        ),
        clothing_item(
            type        = "stockings",
            name        = "high",
            wear        = True
        ),
        clothing_item(
            type        = "stockings",
            name        = "lace",
            wear        = True
        ),
        clothing_item(
            type        = "stockings",
            name        = "latex",
            wear        = True
        ),
        clothing_item(
            type        = "stockings",
            name        = "pantyhose",
            wear        = True
        ),
        clothing_item(
            type        = "stockings",
            name        = "striped",
            wear        = True
        ),
        clothing_item(
            type        = "stockings",
            name        = "striped_vibe",
            wear        = True
        ),



        ################################
        ###                          ###
        ###    HERMIONE UNDERWEAR    ###
        ###                          ###
        ################################


        #####################
        ### HERMIONE BRAS ###
        #####################

        clothing_item(
            type        = "bra",
            name        = "base",
            color       = "base",
            wear        = True,
            always_wear = True,
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bra",
            name        = "bikini_string",
            color       = "base",
            wear        = True,
            breasts     = "breasts_normal",
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bra",
            name        = "lace",
            color       = "base",
            wear        = True,
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "bra",
            name        = "bikini",
            breasts     = "breasts_normal",
            wear        = True,
        ),
        clothing_item(
            type        = "bra",
            name        = "fishnets",
            breasts     = "breasts_normal",
            wear        = True,
        ),
        clothing_item(
            type        = "bra",
            name        = "french_maid",
            breasts     = "breasts_normal",
            wear        = True,
        ),
        clothing_item(
            type        = "bra",
            name        = "latex",
            breasts     = "breasts_normal",
            wear        = True,
        ),
        clothing_item(
            type        = "bra",
            name        = "silk",
            breasts     = "breasts_normal",
            wear        = True,
        ),
        clothing_item(
            type        = "bra",
            name        = "tape",
            breasts     = "breasts_normal",
            wear        = True,
        ),


        ########################
        ### HERMIONE PANTIES ###
        ########################

        clothing_item(
            type        = "panties",
            name        = "base",
            color       = "base",
            wear        = True,
            always_wear = True,
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "panties",
            name        = "bikini_string",
            color       = "base",
            wear        = True,
            always_wear = True,
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "panties",
            name        = "lace",
            color       = "base",
            wear        = True,
            always_wear = True,
            colors      = ['base','black','blue','brown','crimson','dark_blue','dark_green','gray','green','orange','pink','purple','red','white','yellow']
        ),
        clothing_item(
            type        = "panties",
            name        = "bikini",
            wear        = True,
        ),
        clothing_item(
            type        = "panties",
            name        = "fishnet",
            wear        = True,
        ),
        clothing_item(
            type        = "panties",
            name        = "fishnet_string",
            wear        = True,
        ),
        clothing_item(
            type        = "panties",
            name        = "french_maid",
            wear        = True,
        ),
        clothing_item(
            type        = "panties",
            name        = "latex",
            wear        = True,
        ),
        clothing_item(
            type        = "panties",
            name        = "silk",
            wear        = True,
        ),
        clothing_item(
            type        = "panties",
            name        = "silk_low",
            wear        = True,
        )


    )