
# framework for an eaiser to manage grid of items
screen test_grid:

    $ mock_list_of_items = range(1,100)

    add "interface/wardrobe/gold/new_scroll_grid_back.png"

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

                frame:
                    xysize (83, 85)
                    imagebutton:
                        xalign 0.5 yalign 0.5
                        idle im.Scale("interface/store_icons/dyes/dye_2.png", 83, 85)
                        action Return(item)

    add "interface/wardrobe/gold/new_scroll_grid.png"
    
    zorder 99
