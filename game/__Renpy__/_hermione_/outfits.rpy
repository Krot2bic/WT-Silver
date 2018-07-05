label __init_variables:
    
    # outfit purchases are the only dynamic value we care about so they have been separated into their own dict
    if not hasattr(renpy.store,'clothing_purchases'):
        $ clothing_purchases = {}
    if not hasattr(renpy.store,'hg_clothing_saves'):
        $ hg_clothing_saves  = {}
        # this stores the state of the custom outfit for whenever .save() is called 
        # b/c this is a basic dictionary it will also persist through reloads 


    if not hasattr(renpy.store,'hg_clothing'):
        $ hg_clothing = hg_custom_outfit('hg_clothing','hermione default clothing')
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
        

    # # Clothing Sets
    # if not hasattr(renpy.store,'hg_gryffCheer_OBJ'):
    #     $ hg_gryffCheer_OBJ = hermione_outfit()
    # $ hg_gryffCheer_OBJ.name = "Griffindor Cheerleader"
    # $ hg_gryffCheer_OBJ.cost = 80
    # $ hg_gryffCheer_OBJ.wait_time = 2
    # $ hg_gryffCheer_OBJ.store_image = "cheer_gryff.png"
    # if not hasattr(renpy.store,'hg_gryffCheerSkimpy_OBJ'):
    #     $ hg_gryffCheerSkimpy_OBJ = hermione_outfit()
    # $ hg_gryffCheerSkimpy_OBJ.name = "Sexy Griffindor Cheerleader"
    # $ hg_gryffCheerSkimpy_OBJ.cost = 140
    # $ hg_gryffCheerSkimpy_OBJ.wait_time = 3
    # $ hg_gryffCheerSkimpy_OBJ.store_image = "cheer_gryff_skimpy.png"

    # if not hasattr(renpy.store,'hg_slythCheer_OBJ'):
    #     $ hg_slythCheer_OBJ = hermione_outfit()
    # $ hg_slythCheer_OBJ.name = "Slythrin Cheerleader"
    # $ hg_slythCheer_OBJ.cost = 80
    # $ hg_slythCheer_OBJ.wait_time = 2
    # $ hg_slythCheer_OBJ.store_image = "cheer_slyth.png"
    # if not hasattr(renpy.store,'hg_slythCheerSkimpy_OBJ'):
    #     $ hg_slythCheerSkimpy_OBJ = hermione_outfit()
    # $ hg_slythCheerSkimpy_OBJ.name = "Sexy Slythrin Cheerleader"
    # $ hg_slythCheerSkimpy_OBJ.cost = 140
    # $ hg_slythCheerSkimpy_OBJ.wait_time = 3
    # $ hg_slythCheerSkimpy_OBJ.store_image = "cheer_slyth_skimpy.png"

    # if not hasattr(renpy.store,'hg_ravenCheer_OBJ'):
    #     $ hg_ravenCheer_OBJ = hermione_outfit()
    # $ hg_ravenCheer_OBJ.name = "Ravenclaw Cheerleader"
    # $ hg_ravenCheer_OBJ.cost = 80
    # $ hg_ravenCheer_OBJ.wait_time = 2
    # $ hg_ravenCheer_OBJ.store_image = "cheer_raven.png"
    # if not hasattr(renpy.store,'hg_ravenCheerSkimpy_OBJ'):
    #     $ hg_ravenCheerSkimpy_OBJ = hermione_outfit()
    # $ hg_ravenCheerSkimpy_OBJ.name = "Sexy Ravenclaw Cheerleader"
    # $ hg_ravenCheerSkimpy_OBJ.cost = 140
    # $ hg_ravenCheerSkimpy_OBJ.wait_time = 3
    # $ hg_ravenCheerSkimpy_OBJ.store_image = "cheer_raven_skimpy.png"

    # if not hasattr(renpy.store,'hg_hufflCheer_OBJ'):
    #     $ hg_hufflCheer_OBJ = hermione_outfit()
    # $ hg_hufflCheer_OBJ.name = "Hufflepuff Cheerleader"
    # $ hg_hufflCheer_OBJ.cost = 80
    # $ hg_hufflCheer_OBJ.wait_time = 2
    # $ hg_hufflCheer_OBJ.store_image = "cheer_huffl.png"
    # if not hasattr(renpy.store,'hg_hufflCheerSkimpy_OBJ'):
    #     $ hg_hufflCheerSkimpy_OBJ = hermione_outfit()
    # $ hg_hufflCheerSkimpy_OBJ.name = "Sexy Hufflepuff Cheerleader"
    # $ hg_hufflCheerSkimpy_OBJ.cost = 140
    # $ hg_hufflCheerSkimpy_OBJ.wait_time = 3
    # $ hg_hufflCheerSkimpy_OBJ.store_image = "cheer_huffl_skimpy.png"

    # if not hasattr(renpy.store,'hg_MaidLingerie_OBJ'):
    #     $ hg_MaidLingerie_OBJ = hermione_outfit()
    # $ hg_silkNightgown_OBJ.name = "Maid Lingerie"
    # $ hg_silkNightgown_OBJ.cost = 160
    # $ hg_silkNightgown_OBJ.wait_time = 2
    # $ hg_silkNightgown_OBJ.store_image = "maid_lingerie.png"

    # if not hasattr(renpy.store,'hg_silkNightgown_OBJ'):
    #     $ hg_silkNightgown_OBJ = hermione_outfit()
    # $ hg_silkNightgown_OBJ.name = "Silk Nightgown"
    # $ hg_silkNightgown_OBJ.cost = 140
    # $ hg_silkNightgown_OBJ.wait_time = 2
    # $ hg_silkNightgown_OBJ.store_image = "nightgown.png"

    # if not hasattr(renpy.store,'hg_rocker_OBJ'):
    #     $ hg_rocker_OBJ = hermione_outfit()
    # $ hg_rocker_OBJ.name = "Rocker"
    # $ hg_rocker_OBJ.cost = 180
    # $ hg_rocker_OBJ.wait_time = 2
    # $ hg_rocker_OBJ.store_image = "rocker.png"


    # $ hermione_clothing_set_list = []
    # $ hermione_clothing_set_list.append(hg_gryffCheer_OBJ)
    # $ hermione_clothing_set_list.append(hg_gryffCheerSkimpy_OBJ)
    # $ hermione_clothing_set_list.append(hg_slythCheer_OBJ)
    # $ hermione_clothing_set_list.append(hg_slythCheerSkimpy_OBJ)
    # $ hermione_clothing_set_list.append(hg_ravenCheer_OBJ)
    # $ hermione_clothing_set_list.append(hg_ravenCheerSkimpy_OBJ)
    # $ hermione_clothing_set_list.append(hg_hufflCheer_OBJ)
    # $ hermione_clothing_set_list.append(hg_hufflCheerSkimpy_OBJ)
    # $ hermione_clothing_set_list.append(hg_MaidLingerie_OBJ)
    # $ hermione_clothing_set_list.append(hg_silkNightgown_OBJ)
    # $ hermione_clothing_set_list.append(hg_rocker_OBJ)



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

        def save(self):
            dic = {}
            for att, value in self.__dict__.items():
                if value != getattr(outfit_item, att):
                    dic[att] = value
            return dic
        def load(self, dic):
            self.__dict__.update( dic )

    class hg_custom_outfit(object):
        id   = "default" # unique string for internal use
        name = ""        # name to display to user

        hair        = "A"
        hair_color  = "1"

        breasts = "breasts_normal_pressed"

        top = outfit_item(
            name        = "uni_top", # the name of the item.
            version     = "1",       # the varient of the top (_1, _skimpy, _sexy, _sleeves)
            color       = None,      # which color folder the item is in.
            wear        = True,      # if the item is currently worn.
            always_wear = True       # if the item is worn on resetting the outfit.
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
                

        def __init__(self, id, name):
            self.id = id
            self.name = name

        def get_layers(self):
            global hermione_action

            layers = []
            
            #Panties

            #Garterbelt
            if self.garterbelt.wear and notNull( self.garterbelt.color ):
                layers.append( "clothes/underwear/garterbelt_lace/" + str(self.garterbelt.color) + ".png" )


            #####################
            ## Fix files first ##
            #####################

            # if self.stockings.wear and notNull( self.stockings.name, self.stockings.color ):
            #     layers.append( "clothes/underwear/stockings/" + str(self.stockings.name) + "/" + str(self.stockings.color) + ".png" )


            #Bottom
            if self.bottom.wear:

                # not dealing with this now
                # if hermione_wear_onepiece and (h_onepiece in h_onepieces_list): #Skirt or Pants gets added later
                #     pass
                # else:

                if (hermione_action in ['none', 'hold_book']) or ( hermione_action != "lift_top" or  h_top not in h_lift_top_list ) and notNull( self.bottom.name, self.bottom.color ):
                    if notNull( self.bottom.version ):
                        layers.append( "clothes/bottoms/" + str(self.bottom.name) + "/" + str(self.bottom.color) + "_" + str(self.bottom.version) +".png" )
                    else:
                        layers.append( "clothes/bottoms/" + str(self.bottom.name) + "/" + str(self.bottom.color) + ".png" )
            elif self.panties.wear:
                layers.append( self.panties.get_file("clothes/underwear/panties/") )
                if self.panties.overlay:
                    layers.append( "clothes/underwear/pantystain.png" )


            # #Action/Pose Fix A (layer above skirt)
            # add hermione_action_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

            #Bra
            # if self.bra.wear and notNull( self.bra.name, self.bra.color ):
            #     layers.append( "clothes/underwear/bra/" + str(self.bra.name) + "/" + str(self.bra.color) + ".png" )

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

            # #Gloves
            # if hermione_wear_gloves:
            #     add hermione_gloves xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
            
            #Top
            if self.top.wear:
                layers.append( self.top.get_file( "clothes/tops/" ) )
            #Bra
            elif self.bra.wear:
                layers.append( self.bra.get_file( "clothes/underwear/bra/" ) )

            #Bottom #on top of top layer. #Most skirts get added here!
            # if hermione_wear_bottom:
            #     if hermione_action != "none" and hermione_action != "hold_book" and hermione_action != "lift_top":
            #         add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
            #     elif hermione_action == "lift_top":
            #         if h_top in h_lift_top_list:
            #             add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
            #     else:
            #         pass

            #Badges & Belts
            if notNull( self.accs ):
                layers.extend( [ "accessories/body_accs/"+str(acc)+".png" for acc in self.accs ] )

            # #Action/Pose Fix B (layer above top)
            # #add hermione_action_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
            # add hermione_action_b xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
            
            #Robe
            if self.robe.wear and notNull( self.robe.name ):
                layers.append( "clothes/robe/" + str(self.robe.name) + ".png" )


            #####################
            ## Fix files first ##
            #####################

            # #Neckwear
            # if self.neckwear.wear and notNull( self.neckwear.name ):
            #     layers.append( self.neckwear.get_file( "clothes/neckwear/" ) )

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
            if id == None:
                hg_clothing_saves[self.id] = dic
            else:
                hg_clothing_saves[id] = dic
        def load(self, id=None):
            global hg_clothing_saves
            if id == None:
                load_dic = hg_clothing_saves[self.id]
            else:
                load_dic = hg_clothing_saves[id]

            dic = {}
            for name, value in load_dic.items():
                if isinstance(value, dict):
                    for class_name in value:
                        constructor = globals()[class_name]
                        class_instance = constructor()
                        class_instance.__dict__.update(value[class_name])
                        setattr(self, name, class_instance )
                else:
                    dic[name] = value
            self.__dict__.update( dic )
