label enter_snape_office:
    show screen snape_office_screen
    call screen snape_office_menu

    
screen snape_office_screen:
    add "images/rooms/snape_office/office.png"
    
screen snape_office_menu:
    imagebutton: # DOOR
        xpos 123
        ypos 167
        idle "images/main_room/door_r.png"
        hover "images/main_room/door_r_hover.png"
        action [Jump("leave_snape_office")]
        
label leave_snape_office:
    hide screen snape_office_menu
    hide screen snape_office_screen
    
    jump return_office