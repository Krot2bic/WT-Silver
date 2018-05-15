

screen susan_bones:
    ### BASE IMAGE
    add sus_hair xpos sus_xpos ypos sus_ypos #Add hair
    add sus_arm_base xpos sus_xpos ypos sus_ypos #Add the arm base
    add sus_arms xpos sus_xpos ypos sus_ypos #Add the arms that need to be below the body
    add sus_base xpos sus_xpos ypos sus_ypos #Add the base body
    add sus_breast xpos sus_xpos ypos sus_ypos #Add the breast
    add sus_legs xpos sus_xpos ypos sus_ypos #Add the legs
    add sus_arm_2 xpos sus_xpos ypos sus_ypos #Add the arms that need to be above the body
    add sus_left_arm xpos sus_xpos ypos sus_ypos #Add the left arm
    ### EYES AND HAIR SHADOW
    add sus_eye xpos sus_xpos ypos sus_ypos #Add the eye outline
    add sus_pupil xpos sus_xpos ypos sus_ypos #Add the pupil
    add sus_eyebrow xpos sus_xpos ypos sus_ypos #Add the eyebrow
    add sus_hair_shadow xpos sus_xpos ypos sus_ypos #Add the hair shadow
    ### MOUTH
    add sus_mouth xpos sus_xpos ypos sus_ypos #Add the mouth
    ### CLOTHES 
    add sus_skirt xpos sus_xpos ypos sus_ypos # Add the skirt
    add sus_top xpos sus_xpos ypos sus_ypos # Add the top
    add sus_acc xpos sus_xpos ypos sus_ypos # Add the accessory
    add sus_vest xpos sus_xpos ypos sus_ypos # Add the vest
    add sus_stock xpos sus_xpos ypos sus_ypos # Add the stockings
    ### OTHER
    
    ### ZORDER
    zorder sus_zorder



init python: ###Method Definition for new characters
    def changeSusan(    susan_eye=None, 
                        susan_eyebrow=None, 
                        susan_pupil=None, 
                        susan_mouth=None, 
                        susan_arms=None, 
                        susan_left_arm=None,
                        x_pos=None, 
                        y_pos=None): # Susan
        ###DEFINE GLOBAL VARIABLES
        global sus_xpos
        global sus_ypos
        global sus_base
        global sus_breast
        global sus_cheeks
        global sus_eye
        global sus_pupil
        global sus_arms
        global sus_arm_2
        global sus_arm_base
        global sus_left_arm
        global sus_mouth
        global sus_eyebrow
        ###HIDE OLD SCREEN
        renpy.hide_screen("susan_bones")
        ###CHANGE INTS TO STRING
        susan_eye = str(susan_eye)
        susan_eyebrow = str(susan_eyebrow)
        susan_pupil = str(susan_pupil)
        susan_mouth = str(susan_mouth)

        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            sus_xpos = x_pos
        else:
            sus_xpos = sus_xpos
        if y_pos is not None:
            sus_ypos = sus_ypos
        else:
            sus_ypos = sus_ypos
        ###EMOTION CONTROL

        if susan_eye is not None:
            if susan_eye == "0":
                sus_eye = "characters/blank.png" 
            else:
                sus_eye = "characters/susan_bones/eye/eye_0"+susan_eye+".png" 


        if susan_eyebrow is not None:
            if susan_eyebrow == "0":
                sus_eyebrow = "characters/blank.png" 
            else:
                sus_eyebrow = "characters/susan_bones/eye/eyebrow_0"+susan_eyebrow+".png" 


        if susan_pupil is not None:
            if susan_pupil == "0":
                sus_pupil = "characters/blank.png" 
            else:
                sus_pupil = "characters/susan_bones/eye/pupil_0"+susan_pupil+".png" 


        if susan_mouth is not None:
            if susan_mouth == "0":
                sus_mouth = "characters/blank.png" 
            else:
                sus_mouth = "characters/susan_bones/mouth/mouth_0"+susan_mouth+".png" 

        if susan_arms is not None:
            sus_arms = "characters/susan_bones/base/blank.png"
            sus_arm_2 = "characters/susan_bones/base/blank.png" 
            sus_arm_base = "characters/susan_bones/base/blank.png" 
            if susan_arms == 1:
                sus_arms = "characters/susan_bones/base/arm_01.png"
                sus_arm_base = "characters/susan_bones/base/arm_base.png" 
            elif susan_arms == 2:
                sus_arm_2 = "characters/susan_bones/base/arm_02.png"
            elif susan_arms == 3:
                sus_arm_2 = "characters/susan_bones/base/arm_03.png"
                sus_arm_base = "characters/susan_bones/base/arm_base.png" 
            elif susan_arms == 4:
                sus_arm_2 = "characters/susan_bones/base/arm_04.png"
            elif susan_arms == 5:
                sus_arm_2 = "characters/susan_bones/base/arm_05.png" 
            else:
                sus_arms = sus_arms

        if susan_left_arm is not None:
            if susan_left_arm == 1:
                sus_left_arm = "characters/susan_bones/base/l_arm_01.png"
            elif susan_left_arm == 2:
                sus_left_arm = "characters/susan_bones/base/l_arm_02.png"
            elif susan_left_arm == 3:
                sus_left_arm = "characters/susan_bones/base/l_arm_03.png"
            elif susan_left_arm == 4:
                sus_left_arm = "characters/susan_bones/base/l_arm_04.png"
            elif susan_left_arm == 5:
                sus_left_arm = "characters/susan_bones/base/l_arm_05.png"
            else:
                sus_left_arm = sus_left_arm



        ###Update her arm pose

            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("susan_bones")
        renpy.with_statement(Dissolve(0.3))



    def sus_outfit(     outfit=None,   #WIP
                            outfit_var_1=None, 
                            outfit_var_2=None, 
                            outfit_var_3=None):

        global sus_skirt 
        global sus_top 
        global sus_acc
        global sus_vest 
        global sus_stock 
        global sus_breast

        ###HIDE OLD SCREEN
        renpy.hide_screen("susan_bones")

        if outfit == "naked":
            sus_vest = "characters/blank.png"
            sus_top = "characters/blank.png"
            sus_acc = "characters/blank.png"
            sus_skirt = "characters/blank.png"
            sus_stock = "characters/blank.png"
            sus_breast = "characters/susan_bones/base/breasts_01.png" 
        elif outfit == "uniform":
            sus_vest = "characters/susan_bones/clothes/uniform/vest.png" 
            sus_top = "characters/susan_bones/clothes/uniform/top.png" 
            sus_acc = "characters/susan_bones/clothes/uniform/tie.png" 
            sus_skirt = "characters/susan_bones/clothes/uniform/skirt.png" 
            sus_stock = "characters/susan_bones/clothes/uniform/stockings.png" 
            sus_breast = "characters/susan_bones/base/breasts_02.png" 
        elif outfit == "dress":
            sus_vest = "characters/blank.png"
            sus_top = "characters/susan_bones/clothes/heart_dress/Dress.png" 
            sus_skirt = "characters/blank.png"
            sus_acc = "characters/blank.png"
            sus_skirt = "characters/blank.png"
            sus_stock = "characters/blank.png"
            sus_breast = "characters/susan_bones/base/breasts_01.png" 


        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("susan_bones")
        renpy.with_statement(Dissolve(0.3))
