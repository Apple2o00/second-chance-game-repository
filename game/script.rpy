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

    "Minigame 2: dieieieidiei"
    #code the minigame here ok

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



