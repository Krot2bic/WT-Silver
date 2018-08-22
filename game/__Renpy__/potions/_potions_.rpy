label __init_variables:

    $ ingredients_list = {
        "bat_spleens" :
        potion_ingredient(
                id = "bat_spleens",
                title = "Bat spleens",
                unlocked = True,
                shop_item = True,
                effect = "",
                cost = 15,
                description = "Used in expansion potion",
            ),
        "bicorn_horn" :
        potion_ingredient(
                id = "bicorn_horn",
                title = "Bicorn Horn",
                unlocked = True,
                shop_item = True,
                effect = "",
                cost = 15,
                description = "Used in Polyjuice potion.",
            ),
        "cat_hair_fur" :
        potion_ingredient(
                id = "cat_hair_fur",
                title = "Cat hair/Fur",
                shop_item = False,
                effect = "",
                description = "Wormwood is sometimes found in the forbidden forest.",
            ),
        "chameleon_tail" :
        potion_ingredient(
                id = "chameleon_tail",
                title = "Chameleon Tail",
                unlocked = True,
                shop_item = True,
                effect = "",
                cost = 20,
                description = "Used in Transparency potion",
            ),
        "nettles" :
        potion_ingredient(
                id = "nettles",
                title = "Nettles",
                shop_item = False,
                effect = "",
                description = "Wormwood is sometimes found in the forbidden forest.",
            ),
        "fluxweed" :
        potion_ingredient(
                id = "fluxweed",
                title = "Fluxweed",
                unlocked = True,
                shop_item = True,
                effect = "",
                cost = 10,
                description = "Used in Polyjuice potion",
            ),
        "flobberworms_mucus" :
        potion_ingredient(
                id = "flobberworms_mucus",
                title = "Flobberworms/ mucus",
                unlocked = True,
                shop_item = True,
                effect = "",
                cost = 60,
                description = "Used in Cum addiction potion",
            ),
        "knotgrass" :
        potion_ingredient(
            id = "knotgrass",
            title = "Knotgrass",
            shop_item = False,
            effect = "",
            description = "Wormwood is sometimes found in the forbidden forest.",
            ),
        "leeches" :
        potion_ingredient(
                id = "leeches",
                title = "Leeches",
                unlocked = True,
                shop_item = True,
                effect = "",
                cost = 15,
                description = "Used in Polyjuice potion"
            ),
        "luna_hair" :
        potion_ingredient(
                id = "luna_hair",
                title = "Luna's Hair",
                shop_item = False,
                effect = "",
                description = "Wormwood is sometimes found in the forbidden forest.",
            ),
        "niffler_fancy" :
        potion_ingredient(
                id = "niffler_fancy",
                title = "Niffler's Fancy",
                shop_item = False,
                effect = "",
                description = "Wormwood is sometimes found in the forbidden forest.",
            ),
        "puffer_fish_eyes" :
        potion_ingredient(
                id = "puffer_fish_eyes",
                title = "Puffer-fish eyes",
                shop_item = True,
                unlocked = True,
                effect = "",
                cost = 15,
                description = "Used in Expansion potion",
            ),
        "wormwood" :
        potion_ingredient(
                id = "wormwood",
                title = "Wormwood",
                shop_item = False,
                effect = "",
                description = "Wormwood is sometimes found in the forbidden forest.",
            )
    }
    
    $ potion_list = {
        "polyjuice_luna" :
        silver_potion(
                id = "polyjuice_luna",
                cooking_steps = ["poly_base", "heat", "chopped_fluxweed", "crushed_knotgrass", "color:blue", "leeches", "crushed_bicorn_horn", "heat", "luna_hair", "color:green" ],
                title = "Polyjuice Luna"
            ),
        "polyjuice_cat" :
        silver_potion(
                id = "polyjuice_cat",
                cooking_steps = ["poly_base", "heat", "chopped_fluxweed", "crushed_knotgrass", "color:blue", "leeches", "crushed_bicorn_horn", "heat", "cat_hair_fur", "color:green" ],
                title = "Polyjuice Cat"
            ),
        "polyjuice_lamia" :
        silver_potion(
                id = "polyjuice_lamia",
                cooking_steps = ["poly_base", "heat", "chopped_fluxweed", "crushed_knotgrass", "color:blue", "leeches", "crushed_bicorn_horn", "heat", "lumia_scale" ],
                title = "Polyjuice Lamia"
            ),
        "expanding_breast" :
        silver_potion(
                id = "expanding_breast",
                cooking_steps = ["water", "crushed_bat_spleen", "heat", "nettles", "color:blue", "puffer_fish_eyes", "color:green", "breast_milk"],
                title = "Expanding Breast"
            ),
        "expanding_ass" :
        silver_potion(
                id = "expanding_ass",
                cooking_steps = ["water", "crushed_bat_spleen", "heat", "nettles", "color:blue", "puffer_fish_eyes", "color:green", "chemical_x"],
                title = "Expanding Ass"
            ),
        "cum_addiction" :
        silver_potion(
                id = "cum_addiction",
                cooking_steps = ["water", "heat", "crushed_flobberworms_mucus", "color:green", "wormwood", "heat", "moreish_mead", "color:light_green"],
                title = "Cum addiction"
            ),
        "transparent_tincture" :
        silver_potion(
                id = "transparent_tincture",
                cooking_steps = ["transparent_tincture", "heat", "crushed_niffler_fancy", "shift:purple", "chopped_chameleon_tail"],
                title = "Transparent tincture"
            ),
        "coloring_concoction" :
        silver_potion(
                id = "coloring_concoction",
                cooking_steps = [],
                title = "Coloring concoction"
            )
    }
    
    $ potion_ingredient_list = {
        "polyjuice_base" :
        silver_potion(
                id = "polyjuice_base",
                title = "Polyjuice Potion"
            ),
        "chemical_x" :
        silver_potion(
                id = "chemical_x",
                title = "Chemical X"
            ),
        "breast_milk" :
        silver_potion(
                id = "breast_milk",
                title = "Breast Milk"
            ),
        "moreish_mead" :
        silver_potion(
                id = "moreish_mead",
                title = "Moreish mead"
            ),
        "transparent_tincture" :
        silver_potion(
                id = "transparent_tincture",
                title = "Transparent Tincture"
            ),
        "water" :
        silver_potion(
                id = "water",
                title = "Water"
            )
    }
    
    
    
    
    
    
    return

init python:
    class silver_potion(generic_menu_item):
        id = ""
        cost = 0
        cooking_steps = []
        title = ""
        description = ""
        imagepath = ""
        whoring_rec = 0
        quantity = 0
        start_label = None
        unlocked = True

    class potion_ingredient(generic_menu_item):
        id = ""
        shop_item = False
        cost = 0
        quantity = 0
        effect = ""
        description = ""
        
        def get_buttom_right(self):
            return "Owned Amount: "+ str(self.quantity) + " Cost: " + str(self.cost)

