
label __init_variables:
    python:
        mock_list_of_items = range(1,14)
        wardrobe_grid_tab = 0
        wardrobe_grid_char = 'hermione'

        hg_tops_tab = hg_clothing_items.all_type('top', 'characters/hermione/clothes/tops/')
        hg_bots_tab = hg_clothing_items.all_type('bottom', 'characters/hermione/clothes/bottoms/')
        hg_undr_tab = []
        hg_undr_tab.extend( hg_clothing_items.all_type('bra', 'characters/hermione/clothes/underwear/bra/') )
        hg_undr_tab.extend( hg_clothing_items.all_type('panties', 'characters/hermione/clothes/underwear/panties/') )

        wardrobe_grid_info = {
            'hermione': {
                'tabs_txt': [
                    '',
                    'Hair-Style & Head Accs.',
                    'Top Clothings',
                    'Bottom Clothings',
                    'Other Clothings',
                    'Miscellaneous',
                    'Underwear',
                    'Costumes & Outfits',
                    'Gifts & Quest Items',
                ],
                'tabs_lst': [
                    [],
                    [],
                    hg_tops_tab,
                    hg_bots_tab,
                    [],
                    hg_undr_tab,
                    [],
                    []
                ]
            },
            'astoria': {
                'tabs_txt': [
                    '',
                    'Hair-Style & Head Accs.',
                    'Top Clothings',
                    'Bottom Clothings',
                    'Other Clothings',
                    'Miscellaneous',
                    'Underwear',
                    'Costumes & Outfits',
                    'Gifts & Quest Items',
                ],
                'tabs_lst': [
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    []
                ]
            },
            'susan': {
                'tabs_txt': [
                    '',
                    'Hair-Style & Head Accs.',
                    'Top Clothings',
                    'Bottom Clothings',
                    'Other Clothings',
                    'Miscellaneous',
                    'Underwear',
                    'Costumes & Outfits',
                    'Gifts & Quest Items',
                ],
                'tabs_lst': [
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    []
                ]
            }

        }

return





# framework for an eaiser to manage grid of items
screen wardrobe_grid:

    $ war_grid_dic = wardrobe_grid_info[wardrobe_grid_char]
    $ war_grid_txt = war_grid_dic['tabs_txt']
    $ war_grid_lst = war_grid_dic['tabs_lst']

    $ mock_list_of_items = war_grid_lst[wardrobe_grid_tab]

    if daytime:
        $ root = "interface/wardrobe_grid/gold/"
    else:
        $ root = "interface/wardrobe_grid/gray/"

    # add root+"background/gray_full.png"

    # Grid of scrollable items
    hbox:
        xpos 75 ypos 235 xysize (453, 355)
        vpgrid:
            cols 5
            spacing 5
            draggable True
            mousewheel True

            scrollbars "vertical"

            side_xalign 0.5

            for item in mock_list_of_items:

                $ item_image = im.Scale(item, 83, 85)

                imagebutton:
                    xalign 0.5 yalign 0.5 xysize (83, 85)
                    idle LiveComposite(  (83,85), (0,0), root+"grid_background.png", (0,0), item_image )
                    hover LiveComposite( (83,85), (0,0), root+"grid_hover.png",      (0,0), item_image )
                    clicked [ SetVariable("wardrobe_test_grid", "item"), Jump("wardrobe_grid_return") ]


    add root+"/scroll_grid.png"

    # Exit and Tabs on Right
    imagemap:
        cache False

        ground LiveComposite( 
            (1080,600),
            (0,0), im.Scale(root+"tabs/"+str(wardrobe_grid_char)+"/"+str(wardrobe_grid_tab)+".png", 1080, 600),
            (0,0), root+"right_box.png" 
        )

        hover im.Scale(root+"tabs/hover.png", 1080, 600)

        hotspot (1025,10,45,45) clicked [SetVariable("wardrobe_test_grid",0),Jump("wardrobe_grid_return")]

        if wardrobe_grid_tab == 1:
            hotspot (561, 122, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")] #return to default
        else:
            hotspot (609, 122, 38, 93) clicked [SetVariable("wardrobe_grid_tab",1), Jump("wardrobe_grid_update")] #default

        if wardrobe_grid_tab == 2:
            hotspot (561, 232, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")]
        else:
            hotspot (609, 232, 38, 93) clicked [SetVariable("wardrobe_grid_tab",2), Jump("wardrobe_grid_update")]

        if wardrobe_grid_tab == 3:
            hotspot (561, 342, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")]
        else:
            hotspot (609, 342, 38, 93) clicked [SetVariable("wardrobe_grid_tab",3), Jump("wardrobe_grid_update")]

        if wardrobe_grid_tab == 4:
            hotspot (561, 452, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")]
        else:
            hotspot (609, 452, 38, 93) clicked [SetVariable("wardrobe_grid_tab",4), Jump("wardrobe_grid_update")]

        if wardrobe_grid_tab == 5:
            hotspot (987, 122, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")]
        else:
            hotspot (987, 122, 40, 93) clicked [SetVariable("wardrobe_grid_tab",5), Jump("wardrobe_grid_update")]

        if wardrobe_grid_tab == 6:
            hotspot (987, 232, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")]
        else:
            hotspot (987, 232, 40, 93) clicked [SetVariable("wardrobe_grid_tab",6), Jump("wardrobe_grid_update")]

        if wardrobe_grid_tab == 7:
            hotspot (987, 342, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")]
        else:
            hotspot (987, 342, 40, 93) clicked [SetVariable("wardrobe_grid_tab",7), Jump("wardrobe_grid_update")]

        if wardrobe_grid_tab == 8:
            hotspot (987, 452, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_grid_update")]
        else:
            hotspot (987, 452, 40, 93) clicked [SetVariable("wardrobe_grid_tab",8), Jump("wardrobe_grid_update")]

        text war_grid_txt[ wardrobe_grid_tab ] xalign 0.5 xpos 208 ypos 96 size 18

    zorder 5

label wardrobe_grid_update:

    call screen wardrobe_grid

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label wardrobe_grid_return:
    if wardrobe_test_grid == 0:
        hide screen wardrobe_grid
    else:
        $ renpy.say( None, str(wardrobe_test_grid) )

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu