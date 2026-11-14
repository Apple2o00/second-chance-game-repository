# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("[player_name]")
define c = Character("Chicken")
define w = Character("Waffle")
define m = Character("macron")
define bc = Character("blue cheese")
define j = Character("jelly")
define wa = Character("Wasabi")
define pr = Character("Pop Rocks")
define hh = Character("Hordon Hamsey")
# The game starts here.

label start:

    # this is the opening scene,character choice,exposition
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene blank
    "Choose Your Character"

    menu:
        "Pierre (Male)":
            $ player_variant = "pierre"
            $ player_name = "Pierre"
            $ subject_pronoun = "he"
            $ object_pronoun = "him"
            $ possessive_pronoun = "his"
            jump player_selected

        "Emilie (Female)":
            $ player_variant = "emilie"
            $ player_name = "Emilie"
            $ subject_pronoun = "she"
            $ object_pronoun = "her"
            $ possessive_pronoun = "her"
            jump player_selected

label player_selected:
    scene bg room

    if player_variant == "pierre":
        show p happy
    else:
        show e happy

    protagonist "Bonjour, I am [player_name]."
    protagonist "I got rejected from my dream culinary school, but I will show everyone I won't give up!"
    protagonist "That's my story"

    jump openingscene

label openingscene:
    scene blank
    "Oh no! [player_name]'s dreams of being a professional chef are ruined. [object_pronoun] skills aren't good enough so no one wants to try [possessive_pronoun] weird food combos But wait! [player_name] is determined to bounce back, and [subject_pronoun]'ll bounce back in no time!"
    "help train [object_pronoun]!"
    
    jump scene1

label scene1:
    scene home kitchen

    "[player_name] is in [possessive_pronoun] kitchen, whipping up some new combos to get better cooking skills!"

    if player_variant == "pierre":
        show p happy
    else:
        show e happy

    protagonist "I am great at thinking up food combos, but I need your help to make them taste good! This combo is a but tricky..."

    jump minigame1

label minigame1:
    scene homekitchengame

    "Minigame 1: cididiid"
    #code the minigame here ok
    show c mad
    c "Don't even try to pair me up with that waffle, he's way too sweet for me!"
    hide c mad 
    show w happy
    w "I want to talk to chicken, but she doesn't like sweet guys like me... heh"
    hide w happy 
    "Task: Roll the chicken onto the waffle!"

    if player_variant == "pierre":
        show p happy
    else:
        show e happy
    protagonist "Use the spacebar to push the chicken onto the waffle, the faster you click the better!"
    
    if player_variant == "pierre":
        hide p happy
    else:
        hide e happy

    show c game
    #ts is where the mini game is 
    screen click_counter_game
    jump scene1close

label scene1close:
    scene chicken and waffle love
    w "Oh my! Are you ok?"
    c "I... I... yes."
    if player_variant == "pierre":
        show p happy
    else:
        show e happy
    "Couple Matched!"
    # add the cute ending scene here
image ceo/ yn 
pause 4 
image waffle and chicken 
    jump firstmiddle

label firstmiddle:
    scene chud confident cutscene
    "After completing the first mini-game, [player_name] feels more confident in [possessive_pronoun] cooking skills."
    "However, the journey to becoming a master chef is just beginning."

    jump scene2

label scene2:
    scene restaurant kitchen
menu:
    "Let's not get carried away now"
    "[player_name] is in [possessive_pronoun] restaurant kitchen"

    if player_variant == "pierre":
        show p happy
    else:
        show e happy

    protagonist "I'm so glad I got a job at a real restaurant kitchen!"
    "Now, the stakes are higher. Can you help [player_name] prove [object_pronoun]self to the head chef?"

    jump minigame2

label minigame2:
    scene restaurantkitchengame

    init python:
        def slider_update(st):
            global slider_speed

            if stop_slider:
                return None

            max_x = slider_bar_size[0] - slider_size[0]
            for sprite in slider_sprites:
                if sprite.type != "slider":
                    continue

                movement = slider_speed * chest_difficulty
                if sprite.direction == "right":
                    sprite.x = min(sprite.x + movement, max_x)
                    if sprite.x >= max_x:
                        sprite.direction = "left"
                        slider_speed = 2
                    else:
                        slider_speed += 0.04
                else:
                    sprite.x = max(sprite.x - movement, 0)
                    if sprite.x <= 0:
                        sprite.direction = "right"
                        slider_speed = 2
                    else:
                        slider_speed += 0.04

            return 0

        def check_slider_safe_zone():
            global chest_unlocked
            global chest_unlock_tries
            global stop_slider

            slider = next(sprite for sprite in slider_sprites if sprite.type == "slider")
            safe_zone = next(sprite for sprite in slider_sprites if sprite.type == "safe-zone")

            overlaps_safe_zone = (
                slider.x + slider_size[0] > safe_zone.x
                and slider.x < safe_zone.x + safe_zone_size[0]
            )
            if overlaps_safe_zone:
                chest_unlocked = True
                stop_slider = True
                renpy.play("winning.mp3", "sound")
            else:
                chest_unlock_tries -= 1
                renpy.play("losing.mp3", "sound")
                if chest_unlock_tries <= 0:
                    renpy.show_screen("game_over")
                    stop_slider = True

        def reset_chest_puzzle():
            global chest_unlocked
            global chest_unlock_tries
            global stop_slider
            global slider_speed

            chest_unlocked = False
            chest_unlock_tries = 3
            stop_slider = False
            slider_speed = 2

            #this includes randomising the location of safe zone each time
            for sprite in slider_sprites:
                if sprite.type == "slider":
                    sprite.x = 0
                    sprite.direction = "right"
                elif sprite.type == "safe-zone":
                    sprite.x = renpy.random.randint(
                        0, slider_bar_size[0] - safe_zone_size[0]
                    )

            slider_SM.redraw(0)
            renpy.restart_interaction()


    transform half_size:
        zoom 0.5

    transform chest_transform:
        zoom 0.5
        anchor (0.5, 0.5)
        align (0.5, 0.7)
        subpixel True
        on hover:
            easein 1.0 zoom 0.51
        on idle:
            easein 1.0 zoom 0.5

    transform chest_closed:
        zoom 0.5
        align (0.5, 0.7)

    transform chest_unlocked_anim:
        zoom 0.5
        alpha 0.0
        align (0.5, 0.7)
        parallel: 
            easein 3.0 zoom 0.7
        parallel:
            easein 2.0 alpha 1.0

    screen game_over():
        modal True
        key "K_SPACE" action [Hide("game_over"), Function(reset_chest_puzzle)]
        frame:
            background "#00000080"
            xfill True
            yfill True
            frame:
                background "#FFFFFFE6"
                xfill True
                padding (15, 0)
                align (0.5, 0.5)
                text "Out of tries — press Space to try again" color "#000000" size 30 xalign 0.5

    screen chest_puzzle():
        on "show" action Function(reset_chest_puzzle)
        key "K_SPACE" action If(
            chest_unlocked,
            true=Return(),
            false=Function(check_slider_safe_zone)
        )
        key "mousedown_1" action If(
            chest_unlocked,
            true=Return(),
            false=Function(check_slider_safe_zone)
        )
        add "restaurantkitchen.jpg" at half_size
        if not chest_unlocked:
            frame:
                background "#FFFFFF"
                padding (5, 5)
                align (0.5, 0.3)
                text "[chest_unlock_tries] tries" size 18 color "#000000" xalign 0.5
            frame:
                background None
                align (0.5, 0.4)
                xysize slider_bar_size
                add slider_SM
        add "slider-bar.png" at half_size
        if chest_unlocked:
            add "chest-opened.png" at chest_unlocked_anim
        else:
            add "chest-closed-idle.png" at chest_closed

    screen scene_1():
        add "restaurantkitchen.jpg" at half_size
        imagebutton:
            auto "chest-closed-%s.png"
            action Return()
            at chest_transform

    screen scene_2():
        add "restaurantkitchen.jpg" at half_size
        imagebutton:
            auto "chest-closed-%s.png"
            action Return()
            at chest_transform

    screen scene_3():
        add "restaurantkitchen.jpg" at half_size
        imagebutton:
            auto "chest-closed-%s.png"
            action Return()
            at chest_transform

    label start:
        $ slider_SM = SpriteManager(update=slider_update)
        $ slider_sprites = []

        $ safe_zone_image = Image("safe-zone.png")
        $ safe_zone_transform = Transform(child=safe_zone_image, zoom=0.5)
        $ safe_zone_size = (int(149 / 2), int(70 / 2))
        $ slider_sprites.append(slider_SM.create(safe_zone_transform))
        $ slider_sprites[-1].type = "safe-zone"

        $ slider_bar_size = (int(545 / 2), int(70 / 2))
        $ slider_image = Image("slider.png")
        $ slider_transform = Transform(child=slider_image, zoom=0.5)
        $ slider_sprites.append(slider_SM.create(slider_transform))
        $ slider_sprites[-1].type = "slider"
        $ slider_sprites[-1].direction = "right"
        $ slider_size = (int(48 / 2), int(66 / 2))
        $ slider_speed = 2
        $ stop_slider = False
        $ chest_unlocked = False
        $ chest_unlock_tries = 3

        $ chest_difficulty = 1
        call screen scene_1
        call screen chest_puzzle

        $ chest_difficulty = 2
        call screen scene_2
        call screen chest_puzzle

        $ chest_difficulty = 3
        call screen scene_3
        call screen chest_puzzle

        "You mixed all the batter!"
        call scene2close

label scene2close:
    scene restaurant kitchen
    # add the cute ending scene here

    jump secondmiddle

label secondmiddle:
    scene blank
    "congratulations! [player_name] has been doing a stunning job at their new restaurant."
    "So stunning, you even got a strange letter on your desk..."

    jump desk

label desk:
    scene desklayout
    "You pick up the mysterious letter and open it..."
    # code the letter opening animation - maybe add the image
    #add the letter content here, add the real picture of gordon ramsay
    #make the image remove
    "Congratulations! [player_name] too, but let's be real you did all the work on this one. Maybe you should come too!]"

    jump scene3

label scene3:
    scene professional kitchen
    "After receiving the letter, [player_name] is invited to a prestigious cooking competition."
    "This is the ultimate test of [possessive_pronoun] skills. Can you help [player_name] win the competition and become a master chef?"
    #also introduce gordon ramsay

    if player_variant == "pierre":
        show p happy
    else:
        show e happy

    protagonist "I can't believe it! Gordon Ramsay himself is inviting me to compete in his cooking competition!"
    jump minigame3

label minigame3:
    scene professionalkitchengame

    "Minigame 3: iiiiiiii"
    #code the minigame here ok

    jump scene3close

label scene3close:
    scene professional kitchen
    # add the cute ending scene here

    jump thirdmiddle

label thirdmiddle:
    scene professional kitchen judge panel
    "After completing the final mini-game, [player_name] has proven [object_pronoun]self to be a master chef."
    "Gordon Ramsay himself is impressed with [possessive_pronoun] skills and offers [object_pronoun] a job at his restaurant, as well as a little bonus!"
    #code the image of ramsay handing the player a check and a toque

    jump ending

label ending:
    "Congratulations! [player_name] has achieved [possessive_pronoun] dream of becoming a great chef."
    "But where does that leave you?"
    #fade the images in and out of stock freedom
    "maybe it's time for you to head to the kitchen..."

    #fade the images in and out of the ingredients falling in love in polaroid flashbacks
    #try to get a dissolving effect in here
    jump reallydonenow

label reallydonenow:
    scene endingcolour
    "thank you for playing second chance!"
    #yap abt the game



