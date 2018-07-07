init -1 python:
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
            wear        = True,
            always_wear = True,
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
            wear        = True
        ),
        clothing_item(
            type        = "top",
            name        = "top_fishnets",
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

    )