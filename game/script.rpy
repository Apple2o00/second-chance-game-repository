# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pierre")
define e = Character("Emilie")


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
            jump pierrescreen
        "Emilie (Female)"
            jump emiliescreen


 pierrescreen
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "chudhappy.png" to the images
    # directory.

    show p happy

    # These display lines of dialogue.

    p "bonjour, i am chud."

    p "i am so cool and quite maxing, chud maxing that is"

    jump openingscene

emiliescreen
    scene bg room

    show e happy

    e "bonjour, i am emilie"

    e "i am so cool and quite maxing, chud maxing that is"

    jump openingscene

openingscene
    "chud has been rejected from culinary school"
