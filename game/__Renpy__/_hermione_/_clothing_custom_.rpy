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

        top     = hg_clothing_items.get('top','cheer_top'),
        bottom  = hg_clothing_items.get('bottom','cheer_skirt')
    ).save()
    $ hg_custom_clothing(
        id   = "hg_rocker",
        name = "Punk Rocker",
        static = True,

        breasts = "breasts_normal_pressed",

        top     = hg_clothing_items.get('top','wicked_leather_jacket'),
        bottom  = hg_clothing_items.get('bottom','pants_jeans'),

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

        top     = hg_clothing_items.get('top','wicked_rocker_top'),
        bottom  = hg_clothing_items.get('bottom','pants_rocker'),

        gloves = clothing_item(
            name        = "rocker_band",
            wear        = True
        )
    ).save()