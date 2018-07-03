label __init_variables:
    
    # outfit purchases are the only dynamic value we care about so they have been separated into their own dict
    if not hasattr(renpy.store,'clothing_purchases'):
        $ clothing_purchases = {}
    if not hasattr(renpy.store,'hg_clothing_saves'):
        $ hg_clothing_saves  = {}
        # this stores the state of the custom_outfit_objs for whenever .save() is called 
        # b/c this is a basic dictionary it will also persist through reloads 


    if not hasattr(renpy.store,'hg_clothing'):
        $ hg_clothing = custom_outfit_obj('hg_clothing','hermione default clothing','hermione')
        # this is whats currently equipped to change to a diffrent outfit simply .load() it


    python:
        # this is an example of a devloper assigned static save
        hg_clothing_saves['example_static_save'] = {
            'name'          :'name_of_outfit/save',
            'top'           :'example_value_for_top',
            'top_color'     :'example_color',
            'panties'       :'example_value_for_panties',
            'wear_panties'  : False
        }

        # to load this save we would simply call hg_clothing.load('example_static_save')


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
        

    # Clothing Sets
    if not hasattr(renpy.store,'hg_gryffCheer_OBJ'):
        $ hg_gryffCheer_OBJ = hermione_outfit()
    $ hg_gryffCheer_OBJ.name = "Griffindor Cheerleader"
    $ hg_gryffCheer_OBJ.cost = 80
    $ hg_gryffCheer_OBJ.wait_time = 2
    $ hg_gryffCheer_OBJ.store_image = "cheer_gryff.png"
    if not hasattr(renpy.store,'hg_gryffCheerSkimpy_OBJ'):
        $ hg_gryffCheerSkimpy_OBJ = hermione_outfit()
    $ hg_gryffCheerSkimpy_OBJ.name = "Sexy Griffindor Cheerleader"
    $ hg_gryffCheerSkimpy_OBJ.cost = 140
    $ hg_gryffCheerSkimpy_OBJ.wait_time = 3
    $ hg_gryffCheerSkimpy_OBJ.store_image = "cheer_gryff_skimpy.png"

    if not hasattr(renpy.store,'hg_slythCheer_OBJ'):
        $ hg_slythCheer_OBJ = hermione_outfit()
    $ hg_slythCheer_OBJ.name = "Slythrin Cheerleader"
    $ hg_slythCheer_OBJ.cost = 80
    $ hg_slythCheer_OBJ.wait_time = 2
    $ hg_slythCheer_OBJ.store_image = "cheer_slyth.png"
    if not hasattr(renpy.store,'hg_slythCheerSkimpy_OBJ'):
        $ hg_slythCheerSkimpy_OBJ = hermione_outfit()
    $ hg_slythCheerSkimpy_OBJ.name = "Sexy Slythrin Cheerleader"
    $ hg_slythCheerSkimpy_OBJ.cost = 140
    $ hg_slythCheerSkimpy_OBJ.wait_time = 3
    $ hg_slythCheerSkimpy_OBJ.store_image = "cheer_slyth_skimpy.png"

    if not hasattr(renpy.store,'hg_ravenCheer_OBJ'):
        $ hg_ravenCheer_OBJ = hermione_outfit()
    $ hg_ravenCheer_OBJ.name = "Ravenclaw Cheerleader"
    $ hg_ravenCheer_OBJ.cost = 80
    $ hg_ravenCheer_OBJ.wait_time = 2
    $ hg_ravenCheer_OBJ.store_image = "cheer_raven.png"
    if not hasattr(renpy.store,'hg_ravenCheerSkimpy_OBJ'):
        $ hg_ravenCheerSkimpy_OBJ = hermione_outfit()
    $ hg_ravenCheerSkimpy_OBJ.name = "Sexy Ravenclaw Cheerleader"
    $ hg_ravenCheerSkimpy_OBJ.cost = 140
    $ hg_ravenCheerSkimpy_OBJ.wait_time = 3
    $ hg_ravenCheerSkimpy_OBJ.store_image = "cheer_raven_skimpy.png"

    if not hasattr(renpy.store,'hg_hufflCheer_OBJ'):
        $ hg_hufflCheer_OBJ = hermione_outfit()
    $ hg_hufflCheer_OBJ.name = "Hufflepuff Cheerleader"
    $ hg_hufflCheer_OBJ.cost = 80
    $ hg_hufflCheer_OBJ.wait_time = 2
    $ hg_hufflCheer_OBJ.store_image = "cheer_huffl.png"
    if not hasattr(renpy.store,'hg_hufflCheerSkimpy_OBJ'):
        $ hg_hufflCheerSkimpy_OBJ = hermione_outfit()
    $ hg_hufflCheerSkimpy_OBJ.name = "Sexy Hufflepuff Cheerleader"
    $ hg_hufflCheerSkimpy_OBJ.cost = 140
    $ hg_hufflCheerSkimpy_OBJ.wait_time = 3
    $ hg_hufflCheerSkimpy_OBJ.store_image = "cheer_huffl_skimpy.png"

    if not hasattr(renpy.store,'hg_MaidLingerie_OBJ'):
        $ hg_MaidLingerie_OBJ = hermione_outfit()
    $ hg_silkNightgown_OBJ.name = "Maid Lingerie"
    $ hg_silkNightgown_OBJ.cost = 160
    $ hg_silkNightgown_OBJ.wait_time = 2
    $ hg_silkNightgown_OBJ.store_image = "maid_lingerie.png"

    if not hasattr(renpy.store,'hg_silkNightgown_OBJ'):
        $ hg_silkNightgown_OBJ = hermione_outfit()
    $ hg_silkNightgown_OBJ.name = "Silk Nightgown"
    $ hg_silkNightgown_OBJ.cost = 140
    $ hg_silkNightgown_OBJ.wait_time = 2
    $ hg_silkNightgown_OBJ.store_image = "nightgown.png"

    if not hasattr(renpy.store,'hg_rocker_OBJ'):
        $ hg_rocker_OBJ = hermione_outfit()
    $ hg_rocker_OBJ.name = "Rocker"
    $ hg_rocker_OBJ.cost = 180
    $ hg_rocker_OBJ.wait_time = 2
    $ hg_rocker_OBJ.store_image = "rocker.png"


    $ hermione_clothing_set_list = []
    $ hermione_clothing_set_list.append(hg_gryffCheer_OBJ)
    $ hermione_clothing_set_list.append(hg_gryffCheerSkimpy_OBJ)
    $ hermione_clothing_set_list.append(hg_slythCheer_OBJ)
    $ hermione_clothing_set_list.append(hg_slythCheerSkimpy_OBJ)
    $ hermione_clothing_set_list.append(hg_ravenCheer_OBJ)
    $ hermione_clothing_set_list.append(hg_ravenCheerSkimpy_OBJ)
    $ hermione_clothing_set_list.append(hg_hufflCheer_OBJ)
    $ hermione_clothing_set_list.append(hg_hufflCheerSkimpy_OBJ)
    $ hermione_clothing_set_list.append(hg_MaidLingerie_OBJ)
    $ hermione_clothing_set_list.append(hg_silkNightgown_OBJ)
    $ hermione_clothing_set_list.append(hg_rocker_OBJ)



    # # Outfits
    # if not hasattr(renpy.store,'hg_maid_OBJ'): #important!
    #     $ hg_maid_OBJ = hermione_outfit()
    # $ hg_maid_OBJ.name = "Maid"
    # $ hg_maid_OBJ.cost = 250
    # $ hg_maid_OBJ.wait_time = 2
    # $ hg_maid_OBJ.store_image = "maid.png"
    # $ hg_maid_OBJ.outfit_layers = []
    # $ hg_maid_OBJ.outfit_layers.extend(("maid_stockings.png","maid_skirt.png","maid_top.png","maid_gloves.png"))
    # $ hg_maid_OBJ.breast_layer = "breasts_normal_pressed"
    # $ hg_maid_OBJ.top_layers = []
    # $ hg_maid_OBJ.top_layers.append("maid_hat.png")

    # if not hasattr(renpy.store,'hg_heartDancer_OBJ'):
    #     $ hg_heartDancer_OBJ = hermione_outfit()
    # $ hg_heartDancer_OBJ.name = "Heart Dancer"
    # $ hg_heartDancer_OBJ.cost = 300
    # $ hg_heartDancer_OBJ.wait_time = 4
    # $ hg_heartDancer_OBJ.store_image = "heart.png"
    # $ hg_heartDancer_OBJ.outfit_layers = []
    # $ hg_heartDancer_OBJ.outfit_layers.extend(("heart_legs.png","heart_top.png","heart_collar.png"))
    # $ hg_heartDancer_OBJ.breast_layer = "breasts_normal"

    # if not hasattr(renpy.store,'hg_pirate_OBJ'):
    #     $ hg_pirate_OBJ = hermione_outfit()
    # $ hg_pirate_OBJ.name = "Pirate"
    # $ hg_pirate_OBJ.cost = 75
    # $ hg_pirate_OBJ.wait_time = 2
    # $ hg_pirate_OBJ.store_image = "pirate.png"
    # $ hg_pirate_OBJ.outfit_layers = []
    # $ hg_pirate_OBJ.outfit_layers.extend(("pirate_legs.png","pirate_pants.png","pirate_top.png"))
    # $ hg_pirate_OBJ.breast_layer = "breasts_nipfix"

    # if not hasattr(renpy.store,'hg_powerGirl_OBJ'):
    #     $ hg_powerGirl_OBJ = hermione_outfit()
    # $ hg_powerGirl_OBJ.name = "Power Girl"
    # $ hg_powerGirl_OBJ.cost = 350
    # $ hg_powerGirl_OBJ.wait_time = 3
    # $ hg_powerGirl_OBJ.store_image = "power.png"
    # $ hg_powerGirl_OBJ.outfit_layers = []
    # $ hg_powerGirl_OBJ.outfit_layers.extend(("power_cape.png","power_top.png","power_gloves.png","power_belt.png"))
    # $ hg_powerGirl_OBJ.breast_layer = "breasts_normal"
    # $ hg_powerGirl_OBJ.hair_layer = "power_hair"

    # if not hasattr(renpy.store,'hg_msMarvel_OBJ'):
    #     $ hg_msMarvel_OBJ = hermione_outfit()
    # $ hg_msMarvel_OBJ.name = "Mrs Marvel"
    # $ hg_msMarvel_OBJ.cost = 250
    # $ hg_msMarvel_OBJ.wait_time = 5
    # $ hg_msMarvel_OBJ.store_image = "marvel.png"
    # $ hg_msMarvel_OBJ.outfit_layers = []
    # $ hg_msMarvel_OBJ.outfit_layers.extend(("marvel_pants.png","marvel_top.png","marvel_sash.png","marvel_gloves.png"))
    # $ hg_msMarvel_OBJ.breast_layer = "breasts_normal"

    # if not hasattr(renpy.store,'hg_harleyQuinn_OBJ'):
    #     $ hg_harleyQuinn_OBJ = hermione_outfit()
    # $ hg_harleyQuinn_OBJ.name = "Harley Quinn"
    # $ hg_harleyQuinn_OBJ.cost = 300
    # $ hg_harleyQuinn_OBJ.wait_time = 4
    # $ hg_harleyQuinn_OBJ.store_image = "harley.png"
    # $ hg_harleyQuinn_OBJ.outfit_layers = []
    # $ hg_harleyQuinn_OBJ.outfit_layers.extend(("harley_pants.png","harley_top.png","harley_gloves.png","harley_collar.png"))
    # $ hg_harleyQuinn_OBJ.breast_layer = "breasts_normal"
    # $ hg_harleyQuinn_OBJ.hair_layer = "harley_hair"

    # if not hasattr(renpy.store,'hg_ballDress_OBJ'):
    #     $ hg_ballDress_OBJ = hermione_outfit()
    # $ hg_ballDress_OBJ.name = "Ball Dress"
    # $ hg_ballDress_OBJ.cost = 1500
    # $ hg_ballDress_OBJ.wait_time = 7
    # $ hg_ballDress_OBJ.store_image = "ball_dress.png"
    # $ hg_ballDress_OBJ.outfit_layers = []
    # $ hg_ballDress_OBJ.outfit_layers.extend(("ball_dress_skirt.png","ball_dress_top.png"))
    # $ hg_ballDress_OBJ.breast_layer = "breasts_nipfix"

    # if not hasattr(renpy.store,'hg_christmas_OBJ'):
    #     $ hg_christmas_OBJ = hermione_outfit()
    # $ hg_christmas_OBJ.name = "Christmas Girl"
    # $ hg_christmas_OBJ.cost = 50
    # $ hg_christmas_OBJ.wait_time = 2
    # $ hg_christmas_OBJ.store_image = "christmas.png"
    # $ hg_christmas_OBJ.outfit_layers = []
    # $ hg_christmas_OBJ.outfit_layers.extend(("christmas_pants.png","christmas_top.png","christmas_gloves.png","christmas_collar.png"))
    # $ hg_christmas_OBJ.top_layers = []
    # $ hg_christmas_OBJ.top_layers.append("christmas_antlers.png")
    # $ hg_christmas_OBJ.breast_layer = "breasts_normal_pressed"

    # if not hasattr(renpy.store,'hg_laraCroft_OBJ'):
    #     $ hg_laraCroft_OBJ = hermione_outfit()
    # $ hg_laraCroft_OBJ.name = "Lara Croft"
    # $ hg_laraCroft_OBJ.cost = 270
    # $ hg_laraCroft_OBJ.wait_time = 2
    # $ hg_laraCroft_OBJ.store_image = "lara.png"
    # $ hg_laraCroft_OBJ.outfit_layers = []
    # $ hg_laraCroft_OBJ.outfit_layers.extend(("lara_pants.png","lara_top.png","lara_gloves.png"))
    # $ hg_laraCroft_OBJ.breast_layer = "breasts_normal"

    # if not hasattr(renpy.store,'hg_tifa_OBJ'):
    #     $ hg_tifa_OBJ = hermione_outfit()
    # $ hg_tifa_OBJ.name = "Tifa"
    # $ hg_tifa_OBJ.cost = 220
    # $ hg_tifa_OBJ.wait_time = 2
    # $ hg_tifa_OBJ.store_image = "tifa.png"
    # $ hg_tifa_OBJ.outfit_layers = []
    # $ hg_tifa_OBJ.outfit_layers.extend(("tifa_pants.png","tifa_top.png","tifa_gloves.png","tifa_ear.png"))
    # $ hg_tifa_OBJ.breast_layer = "breasts_normal"
    # $ hg_tifa_OBJ.hair_layer = "tifa_hair"

    # if not hasattr(renpy.store,'hg_present_OBJ'):
    #     $ hg_present_OBJ = hermione_outfit()
    # $ hg_present_OBJ.name = "Present"
    # $ hg_present_OBJ.cost = 35
    # $ hg_present_OBJ.wait_time = 1
    # $ hg_present_OBJ.store_image = "present.png"
    # $ hg_present_OBJ.outfit_layers = []
    # $ hg_present_OBJ.outfit_layers.extend(("present_pant.png","present_top.png"))
    # $ hg_present_OBJ.breast_layer = "breasts_nipfix"

    # if not hasattr(renpy.store,'hg_japan_OBJ'):
    #     $ hg_japan_OBJ = hermione_outfit()
    # $ hg_japan_OBJ.name = "Japanese Schoolgirl"
    # $ hg_japan_OBJ.cost = 125
    # $ hg_japan_OBJ.wait_time = 2
    # $ hg_japan_OBJ.store_image = "japan.png"
    # $ hg_japan_OBJ.outfit_layers = []
    # $ hg_japan_OBJ.outfit_layers.extend(("japan_pant.png","japan_top.png"))
    # $ hg_japan_OBJ.breast_layer = "breasts_normal_pressed"

    # if not hasattr(renpy.store,'hg_witch_OBJ'):
    #     $ hg_witch_OBJ = hermione_outfit()
    # $ hg_witch_OBJ.name = "Witch outfit"
    # $ hg_witch_OBJ.cost = 250
    # $ hg_witch_OBJ.wait_time = 3
    # $ hg_witch_OBJ.store_image = "witch.png"
    # $ hg_witch_OBJ.outfit_layers = []
    # $ hg_witch_OBJ.outfit_layers.extend(("witch_stockings.png","witch_top.png","witch_cloak.png","witch_hat.png"))
    # $ hg_witch_OBJ.breast_layer = "breasts_normal_pressed"

    # if not hasattr(renpy.store,'hg_bio_OBJ'):
    #     $ hg_bio_OBJ = hermione_outfit()
    # $ hg_bio_OBJ.name = "Bioshock outfit"
    # $ hg_bio_OBJ.cost = 400
    # $ hg_bio_OBJ.wait_time = 3
    # $ hg_bio_OBJ.store_image = "bio.png"
    # $ hg_bio_OBJ.outfit_layers = []
    # $ hg_bio_OBJ.outfit_layers.extend(("bio_skirt.png","bio_chocker.png","bio_corset.png","bio_jacket.png"))
    # $ hg_bio_OBJ.breast_layer = "breasts_normal_pressed"

    # if not hasattr(renpy.store,'hg_yenn_OBJ'):
    #     $ hg_yenn_OBJ = hermione_outfit()
    # $ hg_yenn_OBJ.name = "Yennefer's costume"
    # $ hg_yenn_OBJ.cost = 500
    # $ hg_yenn_OBJ.wait_time = 4
    # $ hg_yenn_OBJ.store_image = "yenn.png"
    # $ hg_yenn_OBJ.outfit_layers = []
    # $ hg_yenn_OBJ.outfit_layers.extend(("yenn_stockings.png","yenn_pant.png","yenn_skirt.png","yenn_top.png","yenn_gloves.png","yenn_chocker.png","yenn_scarf.png","yenn_belt.png"))
    # $ hg_yenn_OBJ.breast_layer = "breasts_normal"


    $ hermione_outfits_list = []
    # $ hermione_outfits_list.append(hg_maid_OBJ)
    # $ hermione_outfits_list.append(hg_heartDancer_OBJ)
    # $ hermione_outfits_list.append(hg_pirate_OBJ)
    # $ hermione_outfits_list.append(hg_powerGirl_OBJ)
    # $ hermione_outfits_list.append(hg_msMarvel_OBJ)
    # $ hermione_outfits_list.append(hg_harleyQuinn_OBJ)
    # $ hermione_outfits_list.append(hg_ballDress_OBJ)
    # $ hermione_outfits_list.append(hg_christmas_OBJ)
    # $ hermione_outfits_list.append(hg_laraCroft_OBJ)
    # $ hermione_outfits_list.append(hg_tifa_OBJ)
    # $ hermione_outfits_list.append(hg_present_OBJ)
    # $ hermione_outfits_list.append(hg_japan_OBJ)
    # $ hermione_outfits_list.append(hg_witch_OBJ)
    # $ hermione_outfits_list.append(hg_bio_OBJ)
    # $ hermione_outfits_list.append(hg_yenn_OBJ)

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
        id = 'default'
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


    class custom_outfit_obj(object):
        id = "default"  # unique string for internal use
        name = ""       # name to display to user
        root = ""       # the root folder for the character

        body_base = ""
        body_legs = ""
        body_breasts = ""
        body_right_arm = ""
        body_left_arm = ""
        body_pubic_hair = ""

        face_cheeks = ""
        face_eyes = ""
        face_eye_color = ""
        face_tears = ""
        face_mouth = ""

        hair = "A"
        hair_color = "base"

        top = "top_1" #the name of the item.
        top_version = "" #the varient of the top (_1, _skimpy, _sexy, _sleeves)
        top_color = "base" #which color folder the item is in.
        wear_top = True #if the item is currently worn.
        always_wear_top = True #if the item is worn on resetting the outfit.

        onepiece = "blank"
        onepiece_color = "base"
        wear_onepiece = False
        always_wear_onepiece = False

        bottom = "skirt_1"
        bottom_version = ""
        bottom_color = "_base"
        wear_bottom = True
        always_wear_bottom = True

        bra = "bra_base"
        bra_color = "base"
        wear_bra = True
        always_wear_bra = True

        panties = "panties_base"
        panties_color = "base"
        wear_panties = True
        always_wear_panties = True

        graterbelt = "blank"
        garterbelt_color = "base"
        wear_garterbelt = False
        always_wear_garterbelt = False

        neckwear = "blank"
        neckwear_color = "base"
        wear_neckwear = False
        always_wear_neckwear = False

        gloves = "blank"
        gloves_color = "base"
        wear_gloves  = False
        always_wear_gloves  = False

        stockings = "blank"
        stockings_color = "base"
        wear_stockings  = False
        always_wear_stockings  = False

        robe = "robe_1"
        robe_color = "base"
        wear_robe = False
        always_wear_robe = False

        hat = "blank"
        hat_color = "base"
        wear_hat = False
        always_wear_hat = False

        glasses = "blank"
        glasses_color = "base"
        wear_glasses = False
        always_wear_glasses = False

        ears = "blank"
        wear_ears = True
        always_wear_ears = True

        makeup_lipstick = "nude"
        makeup_list = []
        wear_makeup = False
        always_wear_makeup = False

        accs = []
        wear_accs = False
        always_wear_accs = False

        buttplug = "blank"
        buttplug_color = "base"
        wear_buttplug  = False
        always_wear_buttplug  = False

        tatoos = []
        piercings = []

        piercings_ears = "blank"
        piercings_ears_color = "base"
        piercings_nipples = "blank"
        piercings_nipples_color = "base"
        piercings_belly = "blank"
        piercings_belly_color = "base"
        piercings_genitals = "blank"
        piercings_genitals_color = "base"
        wear_piercings = False
        always_wear_piercings = False

        tattoos_forehead = "blank"
        tattoos_forehead_color = "base"
        tattoos_arm_left = "blank"
        tattoos_arm_left_color = "base"
        tattoos_arm_right = "blank"
        tattoos_arm_right_color = "base"
        tattoos_breasts = "blank"
        tattoos_breasts_color = "base"
        tattoos_waist = "blank"
        tattoos_waist_color = "base"
        tattoos_abdomen = "blank"
        tattoos_abdomen_color = "base"
        tattoos_leg_left = "blank"
        tattoos_leg_left_color = "base"
        tattoos_leg_right = "blank"
        tattoos_leg_right_color = "base"
        wear_tattoos = False
        always_wear_tattoos = False

        transparency = 1


        def get_layers(self):

            layers = []

            ### BEHIND BODY ###
            if self.buttplug.notNull():
                layers.append( self.root + "accessories/plugs/" + self.buttplug ".png" )
            if self.ears.notNull() and self.hair_color.notNull():
                layers.append( self.root + "accessories/ears/" + self.ears + "_tail_" + self.hair_color + ".png" )

            ### BODY LAYERS ###


            #Body & Legs
            if self.body_base.notNull():
                layers.add( self.root + "body/base/" + self.body_base + ".png" )
            if self.body_legs.notNull():
                layers.add( self.root + "body/legs/" + self.body_legs + ".png" )



                layers.add( self.root + "/" + self. + ".png" )

            #Hair
            if self.hair.notNull() and self.hair_color.notNull():
                layers.add( self.root + "body/head/" + self.hair + "_" + self.hair_color + ".png" )

            #Right Arm
            if self.body_right_arm.notNull():
                layers.add( self.root + "body/arms/right/" + self.body_right_arm + ".png" )

            #Breasts
            if self.body_breasts.notNull():
                layers.add( self.root + "body/breasts/" + self.body_breasts + ".png" )

            #Left Arm
            if self.body_left_arm.notNull():
                layers.add( self.root + "body/arms/left/" + self.body_left_arm + ".png" )

            #Pubic Hair
            if self.body_pubic_hair.notNull():
                layers.add( self.root + "body/pubic_hair/" + self.body_pubic_hair + ".png" )


            #Face
            if self.face_cheeks.notNull():
                layers.add( self.root + "face/pubic_hair/" + self.face_cheeks + ".png" )
            if self.face_eyes.notNull() and self.face_eye_color.notNull():
                layers.add( self.root + "face/eyes/" + self.face_eye_color + "/" + self.face_eyes + ".png" )
            if self.face_tears.notNull():
                layers.add( self.root + "face/tears/" + self.face_tears + ".png" )
            if self.face_mouth.notNull() and self.makeup_lipstick.notNull():
                layers.add( self.root + "face/mouth/" + self.makeup_lipstick + "/" + self.face_mouth + ".png" )


            #Tattoos
            if self.tatoos.notNull():
                layers.extend( [ self.root+"body/tatoos/"+tatoo+".png" for tatoo in self.tatoos ] )

            # #Body Fluids
            # if self.dribble:
            #     layers.add( self.root + "body/legs/dripping.png" )
            # if self.squirt:
            #     layers.add( self.root + "body/legs/squirting.png" )

            # #Penis
            # if self.futa and not self.wear_bottom and self.wear_panties:
            #     layers.add( self.root + "body/legs/dick.png" )

            #Piercings
            if self.piercings.notNull():
                layers.extend( [ self.root+"accessories/piercings/base/"+piercing+".png" for piercing in self.piercings ] )



            #########################################################
            #### REFRENCE FROM hermione_main for building layers ####
            #########################################################

            # ### CLOTHING LAYERS ###

            # #Uniform
            # if not hermione_costume:
            #     use hermione_uniform

            # #Costume
            # if hermione_costume:
            #     if hermione_wear_top:
            #         use hermione_costume
            #     else:
            #         use hermione_uniform

            # ### ACCESORIES LAYERS ###

            # #Glasses
            # if hermione_wear_glasses:
            #     add hermione_glasses xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

            # add hermione_hair_b xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

            # #Hat
            # if hermione_wear_hat:
            #     add hermione_hat xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

            # #Ears
            # if hermione_wear_ears:
            #     if h_ears == "elf_ears" and h_hair_style == "A": #Doesn't get added to normal hair
            #         pass
            #     else:
            #         add hermione_ears xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

            # #Makeup
            # if hermione_wear_makeup:
            #     use hermione_makeup


            # ### SPERM LAYERS ###

            # if uni_sperm:
            #     add u_sperm xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
            # if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
            #     add "characters/hermione/face/auto_02.png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
            # elif aftersperm: #Shows cum stains on Hermione's uniform.
            #     add "characters/hermione/face/auto_03.png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)


            # ### EMOTES ###
            # add hermione_emote xpos hermione_xpos ypos hermione_ypos


        def __init__(self, id, name, character_name):
            self.id = id
            self.name = name
            self.root = "characters/" + character_name + "/"


        # saves and loads the state of this object to the dictionary 'hg_clothing_saves'

        def save(self, id=None):
            global hg_clothing_saves
            if id == None:
                hg_clothing_saves[self.id] = self.__dict__
            else:
                hg_clothing_saves[id] = self.__dict__
        def load(self, id=None):
            global hg_clothing_saves
            if id == None:
                self.__dict__.update( hg_clothing_saves[self.id] )
            else:
                self.__dict__.update( hg_clothing_saves[id] )





