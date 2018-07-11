init python:
    class wardrobe_grid_tabs(object):

        root = ""
        type_path = {
            'top': "clothes/tops/",
            'bottom': "clothes/bottoms/",
            'bra': "clothes/underwear/bra/",
            'panties': "clothes/underwear/panties/",
            'stockings': "clothes/stockings/"
        }

        clothing = None
        text = []
        grid_list = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def tab_items(self, tab_number):
            li = []
            for item in self.grid_list[tab_number]:
                li.append( (item.get_file( self.root + self.type_path[item.type] ), item ) )
            return li

        def selected_versions(self, selected_item):
            return None

        def selected_colors(self, selected_item):
            return None

    

label __init_variables:
    python:
        mock_list_of_items = range(1,14)
        wardrobe_grid_tab = 0
        wardrobe_grid_page = 0
        wardrobe_grid_color = 'yellow'
        wardrobe_grid_char = 'hermione'

        war_grid_info = {
            'hermione': wardrobe_grid_tabs(
                root = "characters/hermione/",
                clothing = hg_clothing,
                text = [
                    '',
                    'Hair-Style & Head Accs.',
                    'Top Clothings',
                    'Bottom Clothings',
                    'Other Clothings',
                    'Miscellaneous',
                    'Underwear',
                    'Costumes & Outfits',
                    'Gifts & Quest Items'
                ],
                grid_list = [
                    [],
                    [],
                    hg_clothing_items.all_type('top'),
                    hg_clothing_items.all_type('bottom'),
                    hg_clothing_items.all_type('stockings'),
                    [],
                    hg_clothing_items.all_type('bra', 'panties'),
                    [],
                    []
                ]
            )
        }
return





# framework for an eaiser to manage grid of items
screen wardrobe_grid:
    
    $ wardrobe_test_grid = 0

    $ grid_tabs = war_grid_info[wardrobe_grid_char]

    $ grid_list = grid_tabs.tab_items(wardrobe_grid_tab)

    $ root = "interface/wardrobe_grid/"

    # add root+"background/"+str(wardrobe_grid_color)+"_full.png"

    $ hermione_xpos = 550
    use hg_main_sc

    if daytime:
        $ root += "gold/"
    else:
        $ root += "gray/"

    # Grid of scrollable items
    if len(grid_list) > 0:
        hbox:
            xpos 75 ypos 235 xysize (453, 355)
            vpgrid:
                cols 5
                spacing 5
                draggable True
                mousewheel True

                scrollbars "vertical"

                side_xalign 0.5

                for file, item in grid_list:

                    $ item_image = im.Scale(file, 83, 85)

                    imagebutton:
                        xalign 0.5 yalign 0.5 xysize (83, 85)
                        idle LiveComposite(  (83,85), (0,0), root+"grid_background.png", (0,0), item_image )
                        hover LiveComposite( (83,85), (0,0), root+"grid_hover.png",      (0,0), item_image )
                        clicked [ SetVariable("wardrobe_grid_selection", item), Jump("wardrobe_grid_return") ]


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

        hotspot (1025,10,45,45) clicked [SetVariable("wardrobe_test_grid",None),Jump("wardrobe_grid_update")]

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

        text grid_tabs.text[ wardrobe_grid_tab ] xalign 0.5 xpos 208 ypos 96 size 18


        #Wardrobe background color
        $ wardrobe_grid_colors = ['yellow','blue','gray','green','red']
        for i in range(len(wardrobe_grid_colors)):
            $ col = i % 5

            hotspot (667+(20*col), 559, 20, 20) clicked [SetVariable("wardrobe_grid_color",wardrobe_grid_colors[i]), Jump("wardrobe_grid_update")]
            add "interface/wardrobe/icons/colors/"+wardrobe_grid_colors[i]+".png" xpos 668+(20*col) ypos 560


    zorder 5

label wardrobe_grid_update:
    
    if wardrobe_test_grid == None:
        hide screen wardrobe_grid
    else:
        call screen wardrobe_grid

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label wardrobe_grid_return:

    python:
        grid_tabs = war_grid_info[wardrobe_grid_char]
        if getattr(grid_tabs.clothing, wardrobe_grid_selection.type) != wardrobe_grid_selection:
            setattr(grid_tabs.clothing, wardrobe_grid_selection.type, wardrobe_grid_selection)
        else:
            item = getattr(grid_tabs.clothing, wardrobe_grid_selection.type)
            item.wear = not item.wear


    call screen wardrobe_grid


if daytime:
    jump day_main_menu
else:
    jump night_main_menu