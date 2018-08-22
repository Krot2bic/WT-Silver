label __init_variables:
	
    $ hg_outfit = None

	# Clothing Sets
    # 99% of the data in theese objects is static so the dynamic data has been moved and these will serve as static refrences only
    $ hg_outfits = outfit_container(
        # hg_custom_outfit(
        #     id = 'hg_MaidLingerie',
        #     name = "Maid Lingerie",
        #     cost = 160,
        #     wait_time = 2,
        #     store_image = "maid_lingerie.png"
        # ),
        # hg_custom_outfit(
        #     id = 'hg_silkNightgown',
        #     name = "Silk Nightgown",
        #     cost = 140,
        #     wait_time = 2,
        #     store_image = "nightgown.png"
        # ),
        hg_custom_outfit(
            id = 'hg_maid',
            name = 'Maid',
            cost = 250,
            wait_time = 2,
            store_image = 'maid.png',
            outfit_layers = ['maid_stockings.png','maid_skirt.png','maid_top.png','maid_gloves.png'],
            breast_layer = 'breasts_normal_pressed',
            top_layers = ['maid_hat.png']
        ),
        hg_custom_outfit(
            id = 'hg_heartDancer',
            name = 'Heart Dancer',
            cost = 300,
            wait_time = 4,
            store_image = 'heart.png',
            outfit_layers = ['heart_legs.png','heart_top.png','heart_collar.png'],
            breast_layer = 'breasts_normal'
        ),
        hg_custom_outfit(
            id = 'hg_pirate',
            name = 'Pirate',
            cost = 75,
            wait_time = 2,
            store_image = 'pirate.png',
            outfit_layers = ['pirate_legs.png','pirate_pants.png','pirate_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hg_custom_outfit(
            id = 'hg_powerGirl',
            name = 'Power Girl',
            cost = 350,
            wait_time = 3,
            store_image = 'power.png',
            outfit_layers = ['power_cape.png','power_top.png','power_gloves.png','power_belt.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'power_hair',
            top_layers = ['power_cape_top.png']
        ),
        hg_custom_outfit(
            id = 'hg_msMarvel',
            name = 'Mrs Marvel',
            cost = 250,
            wait_time = 5,
            store_image = 'marvel.png',
            outfit_layers = ['marvel_pants.png','marvel_top.png','marvel_sash.png','marvel_gloves.png'],
            breast_layer = 'breasts_normal'
        ),
        hg_custom_outfit(
            id = 'hg_harleyQuinn',
            name = 'Harley Quinn',
            cost = 300,
            wait_time = 4,
            store_image = 'harley.png',
            outfit_layers = ['harley_pants.png','harley_top.png','harley_gloves.png','harley_collar.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'harley_hair'
        ),
        hg_custom_outfit(
            id = 'hg_ballDress',
            name = 'Ball Dress',
            cost = 1500,
            wait_time = 7,
            store_image = 'ball_dress.png',
            outfit_layers = ['ball_dress_skirt.png','ball_dress_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hg_custom_outfit(
            id = 'hg_christmas',
            name = 'Christmas Girl',
            cost = 50,
            wait_time = 2,
            store_image = 'christmas.png',
            outfit_layers = ['christmas_pants.png','christmas_top.png','christmas_gloves.png','christmas_collar.png'],
            breast_layer = 'breasts_normal_pressed',
            top_layers = ['christmas_antlers.png']
        ),
        hg_custom_outfit(
            id = 'hg_laraCroft',
            name = 'Lara Croft',
            cost = 270,
            wait_time = 2,
            store_image = 'lara.png',
            outfit_layers = ['lara_pants.png','lara_top.png','lara_gloves.png'],
            breast_layer = 'breasts_normal'
        ),
        hg_custom_outfit(
            id = 'hg_tifa',
            name = 'Tifa',
            cost = 220,
            wait_time = 2,
            store_image = 'tifa.png',
            outfit_layers = ['tifa_pants.png','tifa_top.png','tifa_gloves.png','tifa_ear.png'],
            breast_layer = 'breasts_normal',
            hair_layer = 'tifa_hair'
        ),
        hg_custom_outfit(
            id = 'hg_present',
            name = 'Present',
            cost = 35,
            wait_time = 1,
            store_image = 'present.png',
            outfit_layers = ['present_pant.png','present_top.png'],
            breast_layer = 'breasts_nipfix'
        ),
        hg_custom_outfit(
            id = 'hg_japan',
            name = 'Japanese Schoolgirl',
            cost = 125,
            wait_time = 2,
            store_image = 'japan.png',
            outfit_layers = ['japan_pant.png','japan_top.png'],
            breast_layer = 'breasts_normal_pressed'
        ),
        hg_custom_outfit(
            id = 'hg_witch',
            name = 'Witch outfit',
            cost = 250,
            wait_time = 3,
            store_image = 'witch.png',
            outfit_layers = ['witch_stockings.png','witch_top.png','witch_cloak.png'],
            breast_layer = 'breasts_normal_pressed',
            top_layers = ['witch_hat.png']
        ),
        hg_custom_outfit(
            id = 'hg_bio',
            name = 'Bioshock outfit',
            cost = 400,
            wait_time = 3,
            store_image = 'bio.png',
            outfit_layers = ['bio_skirt.png','bio_chocker.png','bio_corset.png','bio_jacket.png'],
            breast_layer = 'breasts_normal_pressed',
        ),
        hg_custom_outfit(
            id = 'hg_yenn',
            name = 'Yennefer\'s costume',
            cost = 500,
            wait_time = 4,
            store_image = 'yenn.png',
            outfit_layers = ['yenn_stockings.png','yenn_pant.png','yenn_skirt.png','yenn_top.png','yenn_gloves.png','yenn_chocker.png','yenn_scarf.png','yenn_belt.png'],
            breast_layer = 'breasts_normal'
        )
    )