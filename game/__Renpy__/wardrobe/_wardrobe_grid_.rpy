init python:
    class wardrobe_grid_tabs(object):


        root = ""
        type_path = {
            'top': "clothes/tops/",
            'bottom': "clothes/bottoms/",
            'bra': "clothes/underwear/bra/",
            'panties': "clothes/underwear/panties/",
            'stockings': "clothes/stockings/",
            'hair': "body/head/"
        }
        type_crop = {
            'high': (288,64,642.642),
            'mid': (365,465,520,520),
            'low': (340,735,465,465)
        }
        background_colors = ['yellow','blue','gray','green','red']
        background_color = 'yellow'

        selection = None
        clothing = None
        tabs_text = []
        page_text = []
        grid_list = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def tab_items(self, tab_number):
            li = []
            if tab_number in [1]:
                for b_opt in self.grid_list[tab_number]:
                    for color in b_opt.colors:
                        file = self.root + self.type_path[b_opt.type] + b_opt.option + "_" + str(color) + ".png"
                        obj = character_body_option(type='hair', option=b_opt.option, color=color)
                        li.append((  file , obj ))
            elif tab_number in [2,3,4,6]:
                for item in self.grid_list[tab_number]:
                    li.append( (item.get_file( self.root + self.type_path[item.type] ), item ) )
            return li

        def page_items(self):
            li = []
            if self.selection != None:
                if len(self.selection.versions) > 0:
                    li.append((
                        'Options',
                        ('version', self.selection.get_versions( self.root + self.type_path[self.selection.type] )) 
                    ))
                if len(self.selection.colors) > 0:
                    li.append(( 
                        'Colors',
                        ('color', self.selection.get_colors( self.root + self.type_path[self.selection.type] ))
                    ))
                li.append((
                    'Equip/Unequip',
                    ('wear', [ ("interface/wardrobe_grid/pages/on.png", True), ("interface/wardrobe_grid/pages/off.png", False)])
                ))
            return li


        def selected_versions(self, selected_item):
            return None

        def selected_colors(self, selected_item):
            return None

    

label __init_variables:
    python:
        wardrobe_grid_tab = 0

        wardrobe_grid_page = None
        wardrobe_page_selection = None
        wardrobe_grid_selection = None

        wardrobe_grid_char = 'hermione'

        war_grid_info = {
            'hermione': wardrobe_grid_tabs(
                root = "characters/hermione/",
                body = hg_body,
                clothing = hg_clothing,
                tabs_text = [
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
                page_text = [
                    [],
                    ['Hair', 'Makeup', 'Glasses', 'Ears', 'Hats'],
                    [],#['Uniform', 'Muggle', 'Wicked'],
                    [],#['Uniform', 'Uniform Low', 'Skirts', 'Pants'],
                    [],#['Neckwear', 'Body Accs.', 'Gloves', 'Stockings', 'Robes'],
                    [],#['Potions', 'Toys', 'Piercings', 'Tattoos'],
                    [],#['Bras', 'Panties', 'Garterbelts', 'Stockings'],
                    [],#['Outfits', 'Costumes', 'Dresses', 'Custom'],
                    []#['Gifts', 'Quest Items']
                ],
                grid_list = [
                    [],
                    hg_body_options['hair'],
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


# adds character to wardrobe grid screen
screen wd_grd_char_screen:

    if wardrobe_grid_char == 'hermione':
        $ hermione_xpos = 550
        use hg_main_sc


# framework for an eaiser to manage grid of items
screen wardrobe_grid:
    
    $ silver_grid = war_grid_info[wardrobe_grid_char]


    if wardrobe_grid_page == None:
        $ grid_list = silver_grid.tab_items(wardrobe_grid_tab)
    else:
        $ grid_list = wardrobe_grid_page[1]

    $ page_list = silver_grid.page_items()

    $ root = "interface/wardrobe_grid/"

    # add root+"background/"+str(silver_grid.background_color)+"_full.png"

    # 
    use wd_grd_char_screen

    if daytime:
        $ root += "gold/"
    else:
        $ root += "gray/"

    # Grid of scrollable items
    # grid_list is expected to be a list of tuples where the first tuple is a path to an image to be dissplayed on the tile of the grid
    # the ssecond tuple iss extectedd to be the return value if the tile is clicked
    #
    # e.x.
    # ( 'path/to/an/image.png', 'image_tile_clicked' ) 
    # ( 'image/for/return/true.png', True ) 
    #
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

                    $ item_image = im.Scale( file, 83, 85 )

                    imagebutton:
                        xalign 0.5 yalign 0.5 xysize (83, 85)
                        idle LiveComposite(  (83,85), (0,0), root+"grid_background.png",            (0,0), item_image )
                        hover LiveComposite( (83,85), (0,0), im.Scale(root+"grid_hover.png",83,85), (0,0), item_image )
                        clicked [ SetVariable("wardrobe_grid_selection", item), Jump("wardrobe_grid_return") ]


    add root+"border.png"

    #Pages
    for i, page in enumerate(page_list):
        #$ page_image = "interface/wardrobe_grid/pages/"+str(wardrobe_grid_char)+"/"+str(wardrobe_grid_tab)+"_"+str(i)+".png"
        imagebutton:
            xpos (76+(90*i)) ypos 140 xysize (80, 80)
            idle LiveComposite( (80,80), (0,0), im.Scale(root+"grid_background.png",80,80) )#page_image )
            hover LiveComposite( (80,80), (0,0), im.Scale(root+"grid_hover.png",80,80) )# ,      (0,0), page_image )
            clicked [ SetVariable("wardrobe_page_selection", page[1] ), Jump("wardrobe_page_return") ]
        if wardrobe_grid_page != None and wardrobe_grid_page[0] == page[1][0]:
            text page[0] xpos 76+(90*i) ypos 200 size 15
        else:
            text page[0] xpos 76+(90*i) ypos 215 size 10

    #Background Colors:
    for i, color in enumerate(silver_grid.background_colors):
        imagebutton:
            xpos (661+(21*i)) ypos 566 xysize (20,20)
            idle "interface/wardrobe/icons/colors/"+color+".png"
            clicked [SetField(silver_grid, "background_color", color), Jump("wardrobe_grid_update")]


    #Exit and Tabs on Right
    imagemap:
        cache False

        ground LiveComposite( 
            (1080,600),
            (0,0), im.Scale(root+"tabs/"+str(wardrobe_grid_char)+"/"+str(wardrobe_grid_tab)+".png", 1080, 600),
            (994,11), root+"tabs/ground.png" 
        )

        hover root+"tabs/hover.png"

        #Selected Tab Text
        text silver_grid.tabs_text[ wardrobe_grid_tab ] xalign 0.5 xpos 208 ypos 96 size 18

        #Exit
        hotspot (1025,10,45,45) clicked [Jump("wardrobe_grid_exit")]

        if wardrobe_grid_tab == 1:
            hotspot (561, 122, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")] #return to default
        else:
            hotspot (609, 122, 38, 93) clicked [SetVariable("wardrobe_grid_tab",1), Jump("wardrobe_tab_return")] #default

        if wardrobe_grid_tab == 2:
            hotspot (561, 232, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (609, 232, 38, 93) clicked [SetVariable("wardrobe_grid_tab",2), Jump("wardrobe_tab_return")]

        if wardrobe_grid_tab == 3:
            hotspot (561, 342, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (609, 342, 38, 93) clicked [SetVariable("wardrobe_grid_tab",3), Jump("wardrobe_tab_return")]

        if wardrobe_grid_tab == 4:
            hotspot (561, 452, 86, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (609, 452, 38, 93) clicked [SetVariable("wardrobe_grid_tab",4), Jump("wardrobe_tab_return")]

        if wardrobe_grid_tab == 5:
            hotspot (987, 122, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 122, 40, 93) clicked [SetVariable("wardrobe_grid_tab",5), Jump("wardrobe_tab_return")]

        if wardrobe_grid_tab == 6:
            hotspot (987, 232, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 232, 40, 93) clicked [SetVariable("wardrobe_grid_tab",6), Jump("wardrobe_tab_return")]

        if wardrobe_grid_tab == 7:
            hotspot (987, 342, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 342, 40, 93) clicked [SetVariable("wardrobe_grid_tab",7), Jump("wardrobe_tab_return")]

        if wardrobe_grid_tab == 8:
            hotspot (987, 452, 84, 93) clicked [SetVariable("wardrobe_grid_tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 452, 40, 93) clicked [SetVariable("wardrobe_grid_tab",8), Jump("wardrobe_tab_return")]

    zorder 5

label wardrobe_grid_exit:
    hide screen wardrobe_grid

    $ silver_grid = war_grid_info[wardrobe_grid_char]

    $ wardrobe_grid_tab = 0

    $ silver_grid.selection = None
    $ wardrobe_grid_page = None
    $ wardrobe_page_selection = None
    $ wardrobe_grid_selection = None

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label wardrobe_grid_update:
    call screen wardrobe_grid

label wardrobe_tab_return:
    $ silver_grid = war_grid_info[wardrobe_grid_char]
    $ silver_grid.selection = None
    $ wardrobe_grid_page = None
    $ wardrobe_page_selection = None
    $ wardrobe_grid_selection = None

    call screen wardrobe_grid

label wardrobe_page_return:
    python:
        if wardrobe_page_selection != None:
            if wardrobe_grid_page != None and wardrobe_page_selection[0] == wardrobe_grid_page[0]:
                wardrobe_grid_page = None
            else:
                wardrobe_grid_page = wardrobe_page_selection
                wardrobe_page_selection = None

    call screen wardrobe_grid


label wardrobe_grid_return:

    python:
        silver_grid = war_grid_info[wardrobe_grid_char]

        if wardrobe_grid_selection != None:
            if wardrobe_grid_page == None:
                if isinstance(wardrobe_grid_selection, clothing_item):
                    silver_grid.selection = wardrobe_grid_selection
                    wardrobe_grid_selection = None
            else:
                attr = str(wardrobe_grid_page[0])
                value = wardrobe_grid_selection
                item = deepcopy(silver_grid.selection)
                setattr(item, attr, value)
                silver_grid.selection = item
                setattr(silver_grid.clothing, silver_grid.selection.type, item)
                wardrobe_grid_selection = None


                # attr = str(wardrobe_grid_page[0])
                # value = wardrobe_grid_selection
                # item = getattr(silver_grid.clothing, silver_grid.selection.type)
                # if hasattr(item, attr):
                #     setattr(item, attr, value)
                #     wardrobe_grid_selection = None


        # if isinstance( wardrobe_grid_selection, character_body_option ):
        #     if wardrobe_grid_selection.type == 'hair':
        #         silver_grid.body.hair = wardrobe_grid_selection.option
        #         silver_grid.body.hair_color = wardrobe_grid_selection.color
        # if isinstance( wardrobe_grid_selection, clothing_item ):
        #     if getattr(silver_grid.clothing, wardrobe_grid_selection.type).name != wardrobe_grid_selection.name:
        #         setattr(silver_grid.clothing, wardrobe_grid_selection.type, wardrobe_grid_selection)
        #     else:
        #         item = getattr(silver_grid.clothing, wardrobe_grid_selection.type)
        #         item.wear = not item.wear


    call screen wardrobe_grid

label wd_grd_test:
    
    $ renpy.say(None, "Click")

    call screen wardrobe_grid


if daytime:
    jump day_main_menu
else:
    jump night_main_menu

