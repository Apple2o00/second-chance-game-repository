# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("[player_name]")


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
    protagonist "I am so cool, and everyone likes me."
    protagonist "That's my story."

    jump openingscene

label openingscene:
    scene blank
    "[player_name] has been rejected from culinary school"
    "help [object_pronoun] get back on [possessive_pronoun] feet and become a master chef!"
    
    jump scene1

label scene1:
    scene home kitchen

    "[player_name] is in [possessive_pronoun] home kitchen"

    if player_variant == "pierre":
        show p happy
    else:
        show e happy

    protagonist "I need to find a way to prove myself and become a great chef!"
    "to do that, [player_name] must complete a series of mini-games to cook different dishes."

    jump minigame1

label minigame1:
    scene homekitchengame

    "Minigame 1: cididiid"
    #code the minigame here ok

    jump scene1close

label scene1close:
    scene home kitchen
    # add the cute ending scene here

    jump firstmiddle

label firstmiddle:
    scene blank
    "After completing the first mini-game, [player_name] feels more confident in [possessive_pronoun] cooking skills."
    "However, the journey to becoming a master chef is just beginning."

    jump scene2