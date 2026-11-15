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
image e happy = "emiliehappy.png"
image e sad = "emiliesad.png"
image p happy = "pierrehappy.png"
image p sad = "pierresad.png"
image e normal = "emilienormal.png"
image p normal = "pierrenormal.png"
image p reject = "pierrereject.png"
image e reject = "emiliereject.png"
image home kitchen = "homekitchen.jpg"
image c mad = "chicken.png"
image w happy = "waffle.png"
default stop_slider = False


default click_times = 0
default countdown_time = 10.0
default count_clicks = True

init python:
    def click_counter():
        if store.count_clicks:
            store.click_times += 1

    def reset_click_game():
        store.click_times = 0
        store.countdown_time = 10.0
        store.count_clicks = True

    def tick_click_game():
        if store.count_clicks:
            store.countdown_time = max(0.0, store.countdown_time - 0.1)
            if store.countdown_time == 0:
                store.count_clicks = False

screen click_chicken_game():
    modal True
    on "show" action Function(reset_click_game)
    timer 0.1 repeat True action Function(tick_click_game)
    key "K_SPACE" action If(
        count_clicks,
        true=Function(click_counter),
        false=NullAction()
    )

    add Solid("#f39339")
    text "make the chicken spiritually conect with the waffle" align (0.5, 0.12) size 40
    text "Clicks: [click_times]" align (0.5, 0.25) size 32
    text "Time left: [countdown_time:.1f]" align (0.5, 0.32) size 28

    if count_clicks:
        imagebutton:
            idle "chicken.png"
            action Function(click_counter)
            align (0.5, 0.55)
    elif click_times >= 20:
        text "You did it!" align (0.5, 0.72) size 44
        textbutton "Continue" action Return(True):
            align (0.5, 0.85)
    else:
        text "Try again — you need 20 clicks." align (0.5, 0.72) size 36
        textbutton "Try Again" action Function(reset_click_game):
            align (0.5, 0.85)


# The game starts here.

label start:

    # this is the opening scene,character choice,exposition
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene home kitchen 
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

    "Minigame 1: Push the Chicken"

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
    protagonist "Click the chicken to push her onto the waffle, the faster you click the better!"
    
    if player_variant == "pierre":
        hide p happy
    else:
        hide e happy

    show c game
    call screen click_chicken_game

    if player_variant == "pierre":
        show p happy
    else:
        show e happy

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
    pause 1.0
    jump firstmiddle

label firstmiddle:
    scene chud confident cutscene
    "After completing the first mini-game, [player_name] feels more confident in [possessive_pronoun] cooking skills."
    "However, the journey to becoming a master chef is just beginning."

    jump scene2

label scene2:
    scene restaurant kitchen

    if player_variant == "pierre":
        show p happy
    else:
        show e happy

    protagonist "hey... do you think I have it in me to be a real chef? Like work at a real place? "
    menu:
        "Let's not get carried away now":
            if player_variant == "pierre":
                show p sad
            else:
                show e sad
        "It might be hard but you can try?":
            if player_variant == "pierre":
                show p happy
            else:
                show e happy
        "Of Course, you were born to do this twin!":
            if player_variant == "pierre":
                show p happy
            else:
                show e happy
        
    "after you shared some encouraging words, [player_name], applied for the restarunt across the way, and got in!"
    protagonist "I'm so happy! I've been to this place ever since my mother took me all those years ago... I could just get myself lost in that sauce, it's to die for. Hey! Maybe I can continue the legacy!"
    "[player_name] seems to be really excited, but now the stakes are much higher. Can you help [player_name] provve [possesive_pronoun]self to the head chef?"
    "[player_name] is in [possessive_pronoun] restaurant kitchen"
     
    if player_variant == "pierre":
        #block of code to run :
        hide p happy
    else:
        hide e happy


    protagonist "I'm so glad I got a job at a real restaurant kitchen!"
    jump reallydonenow

"""
# init python:

     
    screen slider_puzzle():
        modal True
        on "show" action Function(reset_slider_puzzle)
        key "K_SPACE" action If(
            chest_unlocked or chest_unlock_tries <= 0,
            true=If(chest_unlocked, Return(True), NullAction()),
            false=Function(check_slider_safe_zone)
        )
        key "mousedown_1" action If(
            chest_unlocked or chest_unlock_tries <= 0,
            true=If(chest_unlocked, Return(True), NullAction()),
            false=Function(check_slider_safe_zone)
        )

        add "images/background/restaurantkitchen.jpg"
        add "images/sprites/happybowl.png" at slider_half_size
        add "images/sprites/redbar.png" at slider_half_size

        frame:
            background "#FFFFFF"
            padding (8, 5)
            align (0.5, 0.2)
            text "Tries left: [chest_unlock_tries]" color "#000000" size 24

        frame:
            background None
            xysize slider_bar_size
            align (0.5, 0.42)
            add slider_SM

        if chest_unlocked:
            text "Batter mixed!" align (0.5, 0.7) size 40
            textbutton "Continue" action Return(True):
                align (0.5, 0.85)
        elif chest_unlock_tries <= 0:
            text "Out of tries!" align (0.5, 0.7) size 40
            textbutton "Try again" action Function(reset_slider_puzzle):
                align (0.5, 0.85)
        else:
            text "Press Space or click when the spoon is in the safe zone.":
                align (0.5, 0.7)
                size 26
        
    init python:
            
                
        def slider_update(st):
            if store.stop_slider:
                return None

            max_x = store.slider_bar_size[0] - store.slider_size[0]
            for sprite in store.slider_sprites:
                if sprite.type != "slider":
                    continue

                movement = store.slider_speed * store.chest_difficulty
                if sprite.direction == "right":
                    sprite.x = min(sprite.x + movement, max_x)
                    if sprite.x >= max_x:
                        sprite.direction = "left"
                        store.slider_speed = 2
                    else:
                        store.slider_speed += 0.04
                else:
                    sprite.x = max(sprite.x - movement, 0)
                    if sprite.x <= 0:
                        sprite.direction = "right"
                        store.slider_speed = 2
                    else:
                        store.slider_speed += 0.04

            return 0

    def check_slider_safe_zone():
        slider = next(
            sprite for sprite in store.slider_sprites
            if sprite.type == "slider"
        )
        safe_zone = next(
            sprite for sprite in store.slider_sprites
            if sprite.type == "safe-zone"
        )

        overlaps_safe_zone = (
            slider.x + store.slider_size[0] > safe_zone.x
            and slider.x < safe_zone.x + store.safe_zone_size[0]
        )
        if overlaps_safe_zone:
            store.chest_unlocked = True
            store.stop_slider = True
            renpy.play("images/sound effects/winning.mp3", "sound")
        else:
            store.chest_unlock_tries -= 1
            renpy.play("images/sound effects/losing.mp3", "sound")
            if store.chest_unlock_tries <= 0:
                store.stop_slider = True

    def reset_slider_puzzle():
        store.chest_unlocked = False
        store.chest_unlock_tries = 3
        store.stop_slider = False
        store.slider_speed = 2

        for sprite in store.slider_sprites:
            if sprite.type == "slider":
                sprite.x = 0
                sprite.direction = "right"
            elif sprite.type == "safe-zone":
                sprite.x = renpy.random.randint(
                    0,
                    store.slider_bar_size[0] - store.safe_zone_size[0]
                )

        store.slider_SM.redraw(0)
        renpy.restart_interaction()

transform slider_half_size:
    zoom 0.5

label minigame2:
    scene restaurantkitchengame

    $ slider_SM = SpriteManager(update=slider_update)
    $ slider_sprites = []

    $ safe_zone_image = Image("images/sprites/safezone.png")
    $ safe_zone_transform = Transform(child=safe_zone_image, zoom=0.5)
    $ safe_zone_size = (int(149 / 2), int(70 / 2))
    $ slider_sprites.append(slider_SM.create(safe_zone_transform))
    $ slider_sprites[-1].type = "safe-zone"

    $ slider_bar_size = (int(545 / 2), int(70 / 2))
    $ slider_image = Image("images/sprites/spoonslider.png")
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
    call screen slider_puzzle
    $ chest_difficulty = 2
    call screen slider_puzzle
    $ chest_difficulty = 3
    call screen slider_puzzle

    "You mixed all the batter!"
    jump scene2close

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
   
    "Congratulations! [player_name] too, but let's be real you did all the work on this one. Maybe you should come too!"

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

"""

label reallydonenow:
    scene homekitchen
    "thank you for playing second chance!"
    #yap abt the game
