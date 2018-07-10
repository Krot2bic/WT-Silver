label __init_variables:
    # TODO: set to False before release
    $ DEBUG = True
return

label debug_menu:
    
    menu:
        "-Test Wardrobe Grid-":
            call screen wardrobe_grid
        "-Set Herm Clothes-":
            label debug_herm_clothes:
            show screen hg_main_sc
            python:
                o_menu = []
                for outfit in hg_outfits:
                    o_menu.append(("-"+outfit+"-",outfit))
                o_menu.append(("-Never mind-", "nvm"))
                selection = renpy.display_menu(o_menu)
            if selection == "nvm":
                $ hg_outfit = None
                hide screen hg_main_sc
                jump debug_menu
            else:
                $ hg_outfit = hg_outfits[selection]
                jump debug_herm_clothes

        "-Load Clothes Saves-":
            $ hg_clothing.load('default')
            label debug_herm_clothes_saves:
            show screen hg_main_sc
            python:
                o_menu = []
                for key, value in hg_dev_clothing_saves.items():
                    o_menu.append(("-"+value['name']+"-",key))
                o_menu.append(("-Never mind-", "nvm"))
                selection = renpy.display_menu(o_menu)
            if selection == "nvm":
                hide screen hg_main_sc
                jump debug_menu
            else:
                $ hg_clothing.load(selection)
                jump debug_herm_clothes_saves

        "-Never mind-":
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu