init python:

    class wardrobe_grid_page(object):
        attr  = None # clothing_item attrabute of the item the tab relates to i.e. ( color, version, None )
        items = []   # The list of items to choose from

        def __init__(self, attr, items):
            self.attr  = attr
            self.items = items

        def get_items(self):
            grid_items = []
            for image, item in self.items:
                grid_items.append( wardrobe_grid_item(image, item.type, self.attr, item) )
            return grid_items


    class wardrobe_grid_item(object):
        image = None # image object to be displayed
        dest  = None # any of ( "face", "body", "clothing", "outfit" ) destinations
        attr  = None # custom_clothing attrabute to override
        value = None # the value which the destination will be set

        def __init__(self, file_path, item_dest, dest_attr, item_value, crop=None):

            image = file_path
            if crop != None:
                image = im.Crop( file_path, crop )

            self.image = im.Scale( image, 83, 85 )
            self.dest  = item_dest
            self.attr  = dest_attr
            self.value = item_value

    class wardrobe_grid_meta(object):

        selection = None
        page      = None
        tab       = 0

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
            'top': (288,64,642.642),
            'bottom': (340,735,465,465),
            'bra': (288,64,642.642),
            'panties': (365,465,520,520),
            'stockings': (340,735,465,465),
            'hair': (288,64,642.642)
            # 'high': (288,64,642.642),
            # 'mid': (365,465,520,520),
            # 'low': (340,735,465,465)
        }
        background_colors = ['yellow','blue','gray','green','red']
        background_color = 'yellow'

        clothing = None
        tab_text = []
        grid_list = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_tab_text(self):
            return self.tab_text[self.tab]

        def get_tab_items(self):
            li = []
            if self.tab in [1]:
                for b_opt in self.grid_list[self.tab]:
                    file = self.root + self.type_path[b_opt.type] + b_opt.option + "_" + str(b_opt.color) + ".png"
                    li.append((  file , b_opt ))
            elif self.tab in [2,3,4,6]:
                for item in self.grid_list[self.tab]:
                    li.append( wardrobe_grid_item(item.get_file(self.root), item.type, None, item) )
            elif self.tab in [7]:
                for outfit in self.outfits:
                    if outfit.purchased():
                        li.append( ( self.root + "clothes/custom/" + outfit.id + "/_menu_.png", outfit ) )
            return li

        # returns tuple of ( "display_text", page_object )
        def pages(self):
            pages = [] # The pages on top of the grid
            
            if self.selection != None:
                sel_val = self.selection.value
                pages.append( ("Home", None) )

                if hasattr(sel_val, 'versions') and len(sel_val.versions) > 0:
                    pages.append(( "Options", wardrobe_grid_page(
                        'version',
                        sel_val.get_versions(self.root)
                    )))
                if hasattr(sel_val, 'colors') and len(sel_val.colors) > 0:
                    pages.append(( "Colors", wardrobe_grid_page(
                        'color',
                        sel_val.get_colors(self.root)
                    )))

            return pages

        def page_items(self):
            li = []
            if self.selection != None:
                if hasattr(self.selection, 'versions') and len(self.selection.versions) > 0:
                    li.append((
                        'Options',
                        ('version', self.selection.get_versions( self.root + self.type_path[self.selection.type] )) 
                    ))
                if hasattr(self.selection, 'colors') and len(self.selection.colors) > 0:
                    li.append(( 
                        'Colors',
                        ('color', self.selection.get_colors( self.root + self.type_path[self.selection.type] ))
                    ))
                li.append((
                    'Equip/Unequip',
                    ('wear', [ ("interface/wardrobe_grid/pages/on.png", True), ("interface/wardrobe_grid/pages/off.png", False)])
                ))
            
            return li

        def apply_selected(self):
            if isinstance(self.selection, wardrobe_grid_item):
                # get value of selected grid item
                item = self.selection

                # get refrence to object of the values destination
                obj = getattr( silver_grid, item.dest )

                # override the whole object
                if item.attr == None:
                    obj = deepcopy( item.value )

                #override the objects attrabute
                else:
                    # set attrabute of the selected object to new value
                    setattr( obj, item.attr, deepcopy(item.value) )
            else:
                raise TypeError('selection must be type "wardrobe_grid_item" when "apply_selected()" is called')


        def selected_versions(self, selected_item):
            return None

        def selected_colors(self, selected_item):
            return None


label __init_variables:
    python:

        wardrobe_grid_char = 'hermione'

        war_grid_info = {
            'hermione': wardrobe_grid_meta(
                root = "characters/hermione/",
                face = hg_face,
                body = hg_body,
                clothing = hg_clothing,
                outfit = hg_outfit,
                outfits = hg_outfits.all(),
                tab_text = [
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
                    hg_options['hair'],
                    hg_options['clothing'].all_type('top'),
                    hg_options['clothing'].all_type('bottom'),
                    hg_options['clothing'].all_type('stockings'),
                    [],
                    hg_options['clothing'].all_type('bra', 'panties'),
                    [],
                    []
                ]
            )
        }
return


# Adds character to wardrobe grid screen
# 
# This needs to be set on a character by character basis
screen wd_grd_char_screen:

    if wardrobe_grid_char == 'hermione':
        $ hermione_xpos = 550
        use hg_main_sc


# framework for an eaiser to manage grid of items
screen wardrobe_grid:
    
    $ silver_grid = war_grid_info[wardrobe_grid_char]

    if silver_grid.page == None:
        $ grid_list = silver_grid.get_tab_items()
    else:
        $ grid_list = silver_grid.page.get_items()

    $ root = "interface/wardrobe_grid/"

    # add root+"background/"+str(silver_grid.background_color)+"_full.png"

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

                for item in grid_list:
                    imagebutton:
                        xalign 0.5 yalign 0.5 xysize (83, 85)
                        idle LiveComposite(
                            (83,85),
                            (0,0), root+"grid_background.png",
                            (0,0), item.image
                        )
                        hover LiveComposite(
                            (83,85),
                            (0,0), im.Scale(root+"grid_hover.png",83,85),
                            (0,0), item.image 
                        )
                        clicked [ SetField(silver_grid, "selection", item), Jump("wardrobe_grid_update") ]

    add root+"border.png"

    #Pages
    for i, (page_text, page) in enumerate(silver_grid.pages()):
        imagebutton:
            xpos (76+(90*i)) ypos 140 xysize (80, 80)
            idle LiveComposite(
                (80,80),
                (0,0), im.Scale(root+"grid_background.png",80,80)
            )
            hover LiveComposite(
                (80,80),
                (0,0), im.Scale(root+"grid_hover.png",80,80)
            )
            clicked [ SetField( silver_grid, "page", page ), Jump("wardrobe_grid_update") ]
        text page_text xpos 76+(90*i) ypos 215 size 10

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
            (0,0), im.Scale(root+"tabs/"+str(wardrobe_grid_char)+"/"+str(silver_grid.tab)+".png", 1080, 600),
            (994,11), root+"tabs/ground.png" 
        )

        hover root+"tabs/hover.png"

        # Selected Tab Text
        text silver_grid.get_tab_text() xalign 0.5 xpos 208 ypos 96 size 18

        # Exit
        hotspot (1025,10,45,45) clicked [Jump("wardrobe_grid_exit")]

        # Tabs
        if silver_grid.tab == 1:
            hotspot (561, 122, 86, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")] #return to default
        else:
            hotspot (609, 122, 38, 93) clicked [SetField(silver_grid,"tab",1), Jump("wardrobe_tab_return")] #default

        if silver_grid.tab == 2:
            hotspot (561, 232, 86, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (609, 232, 38, 93) clicked [SetField(silver_grid,"tab",2), Jump("wardrobe_tab_return")]

        if silver_grid.tab == 3:
            hotspot (561, 342, 86, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (609, 342, 38, 93) clicked [SetField(silver_grid,"tab",3), Jump("wardrobe_tab_return")]

        if silver_grid.tab == 4:
            hotspot (561, 452, 86, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (609, 452, 38, 93) clicked [SetField(silver_grid,"tab",4), Jump("wardrobe_tab_return")]

        if silver_grid.tab == 5:
            hotspot (987, 122, 84, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 122, 40, 93) clicked [SetField(silver_grid,"tab",5), Jump("wardrobe_tab_return")]

        if silver_grid.tab == 6:
            hotspot (987, 232, 84, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 232, 40, 93) clicked [SetField(silver_grid,"tab",6), Jump("wardrobe_tab_return")]

        if silver_grid.tab == 7:
            hotspot (987, 342, 84, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 342, 40, 93) clicked [SetField(silver_grid,"tab",7), Jump("wardrobe_tab_return")]

        if silver_grid.tab == 8:
            hotspot (987, 452, 84, 93) clicked [SetField(silver_grid,"tab",0), Jump("wardrobe_tab_return")]
        else:
            hotspot (987, 452, 40, 93) clicked [SetField(silver_grid,"tab",8), Jump("wardrobe_tab_return")]

    zorder 5

label wardrobe_grid_exit:
    hide screen wardrobe_grid

    $ silver_grid = war_grid_info[wardrobe_grid_char]

    $ silver_grid.tab  = 0
    $ silver_grid.page = None
    $ silver_grid.selection = None

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label wardrobe_grid_update:
    call screen wardrobe_grid

label wardrobe_tab_return:
    $ silver_grid = war_grid_info[wardrobe_grid_char]

    $ silver_grid.selection = None
    $ silver_grid.page = None

    call screen wardrobe_grid


# # This sets the value for the selected item in the grid
# label wardrobe_grid_set:
#     python:
#         if isinstance(wardrobe_grid_selection, wardrobe_grid_item):
#             # get value of selected grid item
#             item = wardrobe_grid_selection

#             # get refrence to object of the values destination
#             obj = getattr( silver_grid, item.dest )

#             # override the whole object
#             if item.attr == None:
#                 obj = deepcopy( item.value )

#             #override the objects attrabute
#             else:
#                 # set attrabute of the selected object to new value
#                 setattr( obj, item.attr, deepcopy(item.value) )
#         else:
#             raise TypeError('"wardrobe_grid_selection" must be type "wardrobe_grid_item" when "wardrobe_grid_set" is called')


label wd_grd_test:
    
    $ renpy.say(None, "Click")

    call screen wardrobe_grid


if daytime:
    jump day_main_menu
else:
    jump night_main_menu

