# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define young = Character("A YOUNG VOICE", what_italic=True)

define young2 = Character("VOICE", what_italic=True)

define k = Character("KEHIRA", what_italic=True)

define e = Character("EZBRIL", what_italic=True)

define n = Character("ENDA", what_italic=True)

define z = Character("ZARTHARACKS", what_italic=True)

define l = Character("LADY", what_italic=True)

define t = Character("THIEF", what_italic=True)

define m = Character("MERCHANT", what_italic=True)

define b = Character("BAKER", what_italic=True)

define s = Character("SHEPHERD", what_italic=True)

define bk = Character("BRIDGE KEEPER", what_italic=True)

define v = Character("VILLAGER", what_italic=True)

define av = Character("ANOTHER VILLAGER", what_italic=True)

define c1 = Character("CHILD 1", what_italic=True)

define c2 = Character("CHILD 2", what_italic=True)

define c3 = Character("CHILD 3", what_italic=True)
#initializing sound channels
init python:
    renpy.music.register_channel("sfx2", "sfx", True)
    renpy.music.register_channel("sfx1", "sfx", True)
    renpy.music.register_channel("sfx3", "sfx", True)


# The game starts here.
label start:
    jump zarth
    jump prologue

label prologue:
    $ renpy.movie_cutscene("try.webm")

label scene1:
    $ renpy.pause(4)
    play music "Banished.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ renpy.pause(1)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    young "Ezbril? Irul of Destruction and Chaos, Her Majesty summons you. "

    # These display lines of dialogue.
    e "Kehira wishes to see me? It has been a while."

    menu:
        "Accept":
            jump scene2
        "Deny":
            young2 "I am afraid you cannot deny the request of Her Majesty."
            young2 "Don’t make her wait."
            jump scene2

label scene2:
    play sound "music/footsteps.ogg"
    $ renpy.pause(1.5)
    stop sound
    play music "Dark_throne.wav" fadeout 1.0 fadein 1.0
    scene throne_room
    with dissolve
    "It has been many years since you visited the Queen’s throne room, but it has not changed at all from what you remembered."
    "Great chandeliers of black crystal glare at you from above. Darkness, her favourite aura, engulfs every corner, and you never quite discovered how large this room really is."
    show kehira at right
    with dissolve
    "Kehira stands before her dark throne, her mighty power almost tangible from across the great room."
    "You are not sure what the Irul Queen wants from you.
    A smirk crosses blood red lips as a slender finger beckons you forward."
    show ezibrl2 at left
    with dissolve
    e "Your Majesty."

    "You bow deeply."

    k "So, you have answered my summon."

    e "Did I have a choice?"

    "The Queen’s eyes shine with a glimmer of amusement."

    k "I have a task for you. The Mortal Realm has fallen into chaos again."

    e "Kehira, you know that I have vowed to never return to the Mortal Realm. You must seek someone else."

    k "You were the only one who could control it before. Ezbril, Irul of Destruction and Chaos, you must control this chaos again."

    e "Why do you still care about the mortals?"

    "A low laugh, ancient and cold. "

    k "The Iruls get their powers from the amount of mortal followers they have. We are strong, yes, but we used to be mighty."
    k "Back in the days when the mortals still believed, the Iruls were the true rulers of both realms. "

    menu:
        "'{i}What makes us better than the greedy mortals?'":
            k "There this nothing wrong with wanting more, as long as no one gets hurt."
            k "When the mortals believed in Iruls and we were strong, the mortals themselves thrived from our blessings. Look at them now, falling into chaos."
        "'{i}Powers sounds appealing.'":
            pass

    e "However, I vowed to never associate with the mortals again."

    k "Ezbril, if you fail to act now, you would only bring more misery upon the mortals."

    k "I have someone who will escort you. Enda, come forward."
    hide kehira with dissolve
    show enda2 at right with dissolve
    "A small figure cautiously emerges from behind the throne. You have never seen such a young Irul before."

    n "Pleased to meet you!"

    "You recognize that voice."
    hide enda2 with dissolve
    show kehira at right with dissolve
    k "Ezbril, meet Enda, my personal messenger."
    k "Enda is a lesser-Irul, born after the mortals forgot us. Because the Iruls get their powers from the faith of the mortals, Enda’s powers are very limited."
    k "Unlike you and I, his life can be extinguished with a mortal wound. If we don’t regain mortal followers, every Irul born afterward would be a lesser-Irul."

    "Young eyes stare at you. You feel a tang of remorse for the lesser-Irul, his powers forever limited. "

    k "All I am asking from you is to identify the sources of disorder and rein in the chaos. This is an order from your Queen."

    "You are hesitant, but you must perform your duty."

    e "Yes, Your Majesty."

    jump chariot1

label chariot1:
    scene chariot with dissolve
    $ renpy.pause(1)
    play sfx1 "music/wing_beat.ogg"
    play sfx2 "music/horse_neigh.ogg"
    $ renpy.pause(2)
    stop sfx2
    show enda2 at right with dissolve
    n "Easy there!"
    n "Welcome aboard! This will be a long journey, so feel free to rest your eyes for a bit. "
    n "Now hold on tight…"
    hide enda2 with dissolve
    "Your eyes feel heavy, your mind swirling into weary nonsense. Darkness falls, slowly. "
    "And then all at once. "
    scene black with dissolve
    stop sfx1
    play music "music/flashback.mp3" fadeout 1.0 fadein 1.0
    $ renpy.pause(1)
    "{i}'Ezbril. {w}
    Ezbril. {w}
    You are the Irul of Destruction and Chaos. You are born from disorder, and only you can control it.'"
    $ renpy.pause(1)
    stop music
    play sfx1 "music/wing_beat.ogg"
    scene chariot with dissolve
    show enda2 at right with dissolve
    n "Wake up, Ezbril. We have arrived."
    $ renpy.pause(0.5)
    stop sfx1
    jump chapter2scene1

label chapter2scene1:
    play music "Maze.wav" fadeout 1.0 fadein 1.0
    scene rsz_forest with dissolve
    "The path before you leads to a lush forest. Along the forest’s edge, you can make out a small tribe of mortals."
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    n "Here we are, the Forest of Nourishment. For generations, the small tribe over there has relied on the forest’s generous blessings for food and wood. The ancient forest is also home to many animals."
    n "Her Majesty sensed a magic of destruction radiating from this forest."
    e "Magic of destruction? But I am the Irul of Destruction and Chaos, and I haven’t set foot in the Mortal Realm in ages."
    n "That is why we must find out who is responsible for this. Let’s start by exploring the forest, where Her Majesty sensed the foul magic."
    n "I have some glowing gemstones you can use to mark your path. You can drop them along the path to keep track of where we have been."
    hide enda2
    hide ezibrl2
    with dissolve
    $trees = False
    $peace = False
    $orbs = 5
    $orb_forest1 = False
    $orb_forestb1 = False
    $orb_forest2 = False
    $orb_forest3 = False
    $orb_forest4 = False
    $orb_forest5 = False
    $orb_forest6 = False
    $orb_forest7 = False
    $orb_forest8 = False
    $orb_lake1 = False
    $orb_lake2 = False
    $orb_bog = False
    $orb_deadend = False
    $orb_destroyed = False
    $orb_forest1c = 0
    $orb_forestb1c = 0
    $orb_forest2c = 0
    $orb_forest3c = 0
    $orb_forest4c = 0
    $orb_forest5c = 0
    $orb_forest6c = 0
    $orb_forest7c = 0
    $orb_forest8c = 0
    $orb_lake1c = 0
    $orb_lake2c = 0
    $orb_bogc = 0
    $orb_deadendc = 0
    $orb_destroyedc = 0
    $same = False
    $lake1seen = False
    $log = False
    $endaexplained = False
    jump forest0

label forest0:

    menu:
        "Head west into the forest":
            "You enter a landscape enriched with the luscious boreal forest, salt plains, and gypsum karst landforms. This large forest is covered by black spruce, jackpine, aspen, and poplar trees."
            "Not to mention the large bogs, muskeg and rich diversity which has sustained the mortals with their sustenance and way of life. The mortal tribe must also benefit from the river that flows out from here."
            jump forest1
        "Go south and investigate the village":
            show enda2 at right with dissolve
            n "The mortals from the tribe rely on the Forest of Nourishment for food and wood. I would like to explore the mortal ways, but we must find out what is causing chaos in the forest."
            hide enda2 with dissolve
            jump forest0
label forest1:
    play sfx1 "music/birds.ogg"
    $ renpy.pause(1)
    stop sfx1
    if  same == False:
        "You come across an intersection with 3 choices: north, west and east."
    if orb_forest1 == True and same == False:
        if orb_forest1c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest1c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest1c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest1c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest1c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go north":
            if trees == False:
                "Walking deeper, the trees begin to tower over you until you cannot see the topmost branches. The tallest trees must be over a few centuries old, at least."
                $trees = True
            jump forest3
        "Go west":
            if trees == False:
                "Walking deeper, the trees begin to tower over you until you cannot see the topmost branches. The tallest trees must be over a few centuries old, at least."
                $trees = True
            jump forestb1
        "Go east":
            "You leave the forest."
            jump forest0
        "Drop a gemstone":
            if orb_forest1 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest1 = True
                    $orb_forest1c = 5-orbs
                    if orb_forest1c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest1c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest1c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest1c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest1c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest1
label forestb1:
    if  same == False:
        "You come across an intersection with 2 choices: north and east ."
    if orb_forestb1 == True and same == False:
        if orb_forestb1c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forestb1c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forestb1c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forestb1c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forestb1c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go north":
            jump forest2
        "Go east":
            jump forest1
        "Drop a gemstone":
            if orb_forestb1 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forestb1 = True
                    $orb_forestb1c = 5-orbs
                    if orb_forestb1c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forestb1c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forestb1c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forestb1c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forestb1c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forestb1
label forest2:
    if  same == False:
        "You come across an intersection with 4 choices: north, west, east and south."
        "In the center of this crossroad is a tree that dwarfs all other visible trees."
    if endaexplained == False:
        show enda2 at right with dissolve
        n "Woah! That has to be the biggest tree I've ever seen."
        n "There are incredible sights in the Mortal Realm."
        e "Yes, the Mortal Realm is enchanting in its own way."
        hide enda2 with dissolve
        $endaexplained = True
    if orb_forest2 == True and same == False:
        if orb_forest2c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest2c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest2c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest2c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest2c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go north":
            jump forest6
        "Go west":
            jump forest4
        "Go east":
            jump forest3
        "Go south":
            jump forestb1
        "Drop a gemstone":
            if orb_forest2 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest2 = True
                    $orb_forest2c = 5-orbs
                    if orb_forest2c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest2c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest2c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest2c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest2c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest2

label forest3:
    if  same == False:
        "You come across an intersection with 3 choices: north, west and south."
    if orb_forest3 == True and same == False:
        if orb_forest3c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest3c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest3c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest3c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest3c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go north":
            jump lake1
        "Go west":
            jump forest2
        "Go south":
            jump forest1
        "Drop a gemstone":
            if orb_forest3 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest3 = True
                    $orb_forest3c = 5-orbs
                    if orb_forest3c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest3c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest3c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest3c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest3c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest3

label forest4:
    if  same == False:
        "You come across an intersection with 3 choices: north, west and east."
    if orb_forest4 == True and same == False:
        if orb_forest4c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest4c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest4c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest4c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest4c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go north":
            jump forest5
        "Go west":
            jump deadend
        "Go east":
            jump forest2
        "Drop a gemstone":
            if orb_forest4 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest4 = True
                    $orb_forest4c = 5-orbs
                    if orb_forest4c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest4c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest4c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest4c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest4c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest4

label forest5:
    if  same == False:
        "You come across an intersection with 3 choices: west, east, and south."
    if orb_forest5 == True and same == False:
        if orb_forest5c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest5c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest5c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest5c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest5c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go west":
            jump bog
        "Go east":
            jump forest6
        "Go south":
            jump forest4
        "Drop a gemstone":
            if orb_forest5 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest5 = True
                    $orb_forest5c = 5-orbs
                    if orb_forest5c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest5c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest5c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest5c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest5c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest5

label forest6:
    if  same == False:
        "You come across an intersection with 2 choices: west and south."
    if orb_forest6 == True and same == False:
        if orb_forest6c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest6c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest6c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest6c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest6c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go west":
            jump forest5
        "Go south":
            jump forest2
        "Drop a gemstone":
            if orb_forest6 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest6 = True
                    $orb_forest6c = 5-orbs
                    if orb_forest6c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest6c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest6c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest6c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest6c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest6

label forest7:
    if peace == False:
        "As you travel further into the forest, you realize that your surroundings are unnaturally quiet. In fact, it has been a while since you saw any signs of wildlife."
        $peace = True
    if orb_forest7 == True and same == False:
        if orb_forest7c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest7c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest7c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest7c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest7c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    if orb_forest7 == True and same == False:
        "You see a gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go west":
            jump forest8
        "Go south":
            jump lake2
        "Drop a gemstone":
            if orb_forest7 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest7 = True
                    $orb_forest7c = 5-orbs
                    if orb_forest7c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest7c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest7c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest7c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest7c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest7

label forest8:
    if  same == False:
        "You come across an intersection with 3 choices: north, west and east."
    if orb_forest8 == True and same == False:
        if orb_forest8c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_forest8c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_forest8c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_forest8c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_forest8c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go north":
            jump destroyed
        "Go west":
            jump forestn
        "Go east":
            jump forest7
        "Drop a gemstone":
            if orb_forest8 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_forest8 = True
                    $orb_forest8c = 5-orbs
                    if orb_forest8c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_forest8c == 2:
                        "You place a red gemstone on the ground."
                    if orb_forest8c == 3:
                        "You place a green gemstone on the ground."
                    if orb_forest8c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_forest8c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump forest8
label lake1:
    play sfx1 "music/river.ogg"
    $ renpy.pause(0.5)
    if  same == False:
        "The path continues north until you reach a river. It seems skinnier here than any other part of the river."
        "If you had something long that could support your weight, you might be able to cross it."
    if orb_lake1 == True and same == False:
        if orb_lake1c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_lake1c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_lake1c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_lake1c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_lake1c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $lake1seen = True
    $same = False
    menu:
        "Place log across river" if log:
            "You place your log across the river and Enda nimbly makes his way across. You follow, slowly."
            "Just as you make it to the other side, the log slips and splashes into the river."
            show enda2 at right with dissolve
            n "That was close."
            hide enda2 with dissolve
            jump lake2
        "Go back south":
            stop sfx1
            jump forest3
        "Drop a gemstone":
            if orb_lake1 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_lake1 = True
                    $orb_lake1c = 5-orbs
                    if orb_lake1c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_lake1c == 2:
                        "You place a red gemstone on the ground."
                    if orb_lake1c == 3:
                        "You place a green gemstone on the ground."
                    if orb_lake1c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_lake1c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."

                else:
                    "You are out of gemstones."
            $same = True
            jump lake1
label lake2:
    if  same == False:
        "You are on the north side of the river. You can only go north from here."
    if orb_lake2 == True and same == False:
        if orb_lake2c == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_lake2c == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_lake2c == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_lake2c == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_lake2c == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go north":
            "You head back to your last intersection where you are facing south."
            stop sfx1
            jump forest7
        "Drop a gemstone":
            if orb_lake2 == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_lake2 = True
                    $orb_lake2c = 5-orbs
                    if orb_lake2c == 1:
                        "You place a blue gemstone on the ground."
                    if orb_lake2c == 2:
                        "You place a red gemstone on the ground."
                    if orb_lake2c == 3:
                        "You place a green gemstone on the ground."
                    if orb_lake2c == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_lake2c == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."
                else:
                    "You are out of gemstones."
            $same = True
            jump lake2
label bog:
    if  same == False:
        "The path continues west until you arrive at a bog. There sure are a lot of fallen trees around here."
        "Those logs look sturdy, as if someone could across them."
    if orb_bog == True and same == False:
        if orb_bogc == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_bogc == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_bogc == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_bogc == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_bogc == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Pick up a log" if lake1seen == True and log == False:
            "You pick up a log, feeling surprised to find it lighter than what you expected."
            show enda2 at right
            show ezibrl2 at left
            with dissolve
            n "You sure are strong."
            e "Irul's powers."
            hide enda2
            hide ezibrl2
            with dissolve
            $log = True
            $same = True
            jump bog
        "Go back":
            "You head back east to your last intersection."

            jump forest5
        "Drop a gemstone":
            if orb_bog == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_bog = True
                    $orb_bogc = 5-orbs
                    if orb_bogc == 1:
                        "You place a blue gemstone on the ground."
                    if orb_bogc == 2:
                        "You place a red gemstone on the ground."
                    if orb_bogc == 3:
                        "You place a green gemstone on the ground."
                    if orb_bogc == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_bogc == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."
                else:
                    "You are out of gemstones."
            $same = True
            jump bog
label deadend:
    if  same == False:
        "There is an overgrowth of vegetation along this path, until you cannot proceed any further."
    if orb_deadend == True and same == False:
        if orb_deadendc == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_deadendc == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_deadendc == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_deadendc == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_deadendc == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go back":
            "You head back west to your last intersection."
            jump forest4
        "Drop a gemstone":
            if orb_deadend == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_deadend = True
                    $orb_deadendc = 5-orbs
                    if orb_deadendc == 1:
                        "You place a blue gemstone on the ground."
                    if orb_deadendc == 2:
                        "You place a red gemstone on the ground."
                    if orb_deadendc == 3:
                        "You place a green gemstone on the ground."
                    if orb_deadendc == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_deadendc == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."
                else:
                    "You are out of gemstones."
            $same = True
            jump deadend
label destroyed:
    if  same == False:
        "The path curves west, but is blocked by a bevy of fallen trees, vines, and other vegetation."
        "There is nothing natural about this."
    if orb_destroyed == True and same == False:
        if orb_destroyedc == 1:
            "You see a blue gemstone lying on the ground, you must have been here before."
        if orb_destroyedc == 2:
            "You see a red gemstone lying on the ground, you must have been here before."
        if orb_destroyedc == 3:
            "You see a green gemstone lying on the ground, you must have been here before."
        if orb_destroyedc == 4:
            "You see a yellow gemstone lying on the ground, you must have been here before."
        if orb_destroyedc == 5:
            "You see a black gemstone lying on the ground, you must have been here before."
    $same = False
    menu:
        "Go back south":
            "You head back to your last intersection where you are facing south."
            jump forest8
        "Drop a gemstone":
            if orb_deadend == True:
                "You've already dropped a gemstone here."
            else:
                if orbs > 0:
                    $orbs -= 1
                    $orb_destroyed = True
                    $orb_destroyedc = 5-orbs
                    if orb_destroyedc == 1:
                        "You place a blue gemstone on the ground."
                    if orb_destroyedc == 2:
                        "You place a red gemstone on the ground."
                    if orb_destroyedc == 3:
                        "You place a green gemstone on the ground."
                    if orb_destroyedc == 4:
                        "You place a yellow gemstone on the ground."
                    if orb_destroyedc == 5:
                        "You place a black gemstone on the ground."
                    "You now have [orbs] gemstones left."
                else:
                    "You are out of gemstones."
            $same = True
            jump destroyed
label forestn:
    stop music
    jump forestcenter


label forestcenter:
    play music "Nazareth.wav"
    play sfx1 "music/river.ogg"
    play sfx2 "music/birds.ogg"
    $ renpy.pause(0.5)

    "A lonely, tranquil heart of a forest. A gushing spring could be heard,
    along with an occasional call of a songbird. An Irul sits gracefully on a
    water-smoothed stone, surrounded by an audience of white tailed deer and
    curious rabbits."
    "He seems preoccupied examining a twig, and has not noticed you yet."
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    n "Ezbril, I recognize him. Before you is Nazareth, the Irul of Spring, Harvest, and Life. For eons, he has travelled forest to forest, tribe to tribe, nourishing and looking after every being that breathes."
    n "However, his performance has been going downhill lately. Forests are disappearing, animals are fleeing their homes, and food is scarce."
    e "Enda, I can feel the magic of destruction that Kehira sensed. It seems strong within Nazareth. This might relate to his decremental performance."
    e "If he can create trees, he must be able to destroy them as well. That would explain the magic I sense."
    n "Would Nazareth destroy the very beings that he has nourished for many years?"
    stop sfx1
    stop sfx2
    "The carpet of moss starts to darken."
    n "Oh no! Does he know that we are here?"
    "Nazareth stands abruptly, and some of the rabbits begin to back away."
    "The grass under his feet begins to darken, then disappear. Like a ripple, the surrounding plants begin to vanish, leaving no evidence of the lush green that existed. The small company of critters begin to scurry, aiming for trees that disappear like a mirage."
    e "The Irul of Spring, Harvest and Life … destroying the ancient forest?"
    n "We must report this to Her Majesty."
    hide ezibrl2
    hide enda2
    with dissolve
    "Nazareth raises his arms, like a falcon about to take flight. He seems to
    hesitate a moment. Suddenly, he twirls and shoots toward the skies."
    "Time stops. You are not standing in a forest anymore."
    "The entire west half of the forest has vanished, leaving behind no blade of grass or whisper of what was once magical and green."
    "Now that the trees are gone, you can easily make out the small tribe from here; a tribe that once sat along the forest’s edge now stood bare in an open field. And in front of you…"
    play sfx1 "music/flames.ogg"
    $ renpy.pause(0.5)
    "A wall of flames. The west half of the forest is ablaze, the fire rushing
    toward you, the inferno leaping from tree to tree.  Enda instinctively darts behind you, his fear echoing in your own bones."
    "A dark aura begins to dance along the tips of your fingers. The chaos of the flames fuels your own. Your destructive energy resonates with the forest’s disorder."
    show enda2 at right
    show ezibrl2 at left
    with dissolve
    n "Ezbril!"
    "But you realize that you are safe. There are no trees, no vegetation left
    on this side to feed the hungry flames. The forest fire cannot spread."
    show ezibrl2 at left with dissolve
    n "That was a close one."
    e "Enda, no matter what happens, do not let me unleash my powers in the Mortal Realm. I have constrained my magic for too long. Were I to lose control, the destruction would be too great."
    n "Is that why you have not returned to the Mortal Realm in many years?"
    e "…"
    e "Let’s go, Enda. We must report our findings to Kehira."
    stop sfx1
    jump travellingback

label travellingback:
    scene chariot with dissolve
    play sfx1 "music/wing_beat.ogg"
    play sfx2 "music/horse_neigh.ogg"
    $ renpy.pause(2)
    stop sfx2
    show enda2 at right with dissolve
    n "Here comes our ride. Let’s go!"
    scene black with dissolve
    $ renpy.pause(1.5)
    "You feel exhausted. Sweet weariness greets you in a dark embrace."
    $ renpy.pause(3)
    "Two great armies clashing in a crimson field."
    "The land is drunk on a sea of blood."
    "Death looms over the ashen sky. "
    $ renpy.pause(3)
    scene chariot
    show enda2 at right
    with dissolve
    n "We have arrived."

    stop sfx1
    $ renpy.pause(0.5)
    jump chapter3scene1

label chapter3scene1:
    play music "Dark_throne.wav" fadeout 1.0 fadein 1.0
    scene throne_room
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    n "We are back, your Majesty. "
    "You bow deeply."
    e "Your Majesty, we bring news."
    hide enda2 with dissolve
    show kehira at right with dissolve
    k "Oh? You have returned earlier than I expected, what have you discovered."
    menu:
        "{i}'The ancient forest is burning.'":
            e "A fire was ignited in the north part of the forest, and the flames were spreading fast. There was a tribe of mortals located at the eastern edge of the forest."
            e "If it weren’t for Nazareth, the flames would have devoured the entire forest and consumed the tribe as well."
        "{i}'Nazareth destroyed half of the ancient forest.'":
            k "Such nonsense you speak, Ezbril. Nazareth has nurtured the ancient Forest of Nourishment for eons, yet you claim that he would destroy his very own creation? How did it come to this?"
            e "A fire was ignited in the north part of the forest, and the flames were spreading fast. There was a tribe of mortals located at the eastern edge of the forest."
            e "If it weren’t for Nazareth, the flames would have devoured the entire forest and consumed the tribe as well."
    k "A bold move by Nazareth."
    k "Nevertheless, I am quite intrigued by this fire you mentioned. The ancient Forest of Nourishment has long stood proud, yet now half of it is gone, the rest ablaze."
    k "I cannot help but wonder what might have started the fire."
    "Kehira sharply glances your way."
    k "Did you lose your control again, Ezbril?"
    hide kehira with dissolve
    show enda2 at right with dissolve
    n "No, he did not!"
    n "-Your Majesty."
    n "I was with Ezbril the whole time, Your Majesty. We did not know about the fire until half the forest was already ablaze."
    n "If Nazareth hadn’t destroyed the eastern half, we would have been trapped amongst the flames ourselves."
    hide enda2 with dissolve
    show kehira at right with dissolve
    "The Queen ponders over Enda's words."
    k "We must get to the root of this fire, for it might be related to the disorder in the Mortal Realm."
    e "Who brings fire into the Mortal Realm?"
    k "That would be Cyvtis, Irul of the Skies. As the ruler of the skies, Cyvtis also rules over the sun and the moon. She harnessed the power of the sun and brought the first fire to the Mortal Realm."
    k "She could have harnessed this power again and set the forest on fire."
    k "Infact, I have been informed that Cyvtis was in that area recently."
    e "Why would Cyvtis do this?"
    k "When we discover the culprit behind this disorder, we can find out their intentions."
    k "Enda, escort Ezbril into the Mortal Realm again."
    hide kehira with dissolve
    show enda2 at right with dissolve
    n "I shall, Your Majesty."
    stop music
    jump travellingtomarket
label travellingtomarket:
    $ renpy.pause(1.5)
    scene chariot with dissolve
    play sfx1 "music/wing_beat.ogg"
    play sfx2 "music/horse_neigh.ogg"
    $ renpy.pause(2)
    stop sfx2
    show enda2 at right with dissolve
    n "Looks like I get to travel with you once more."
    n "Mortal Realm, here we come again!"
    hide enda2 with dissolve
    "You have never had a taste for flying. Maybe if you rest your eyes for a bit..."
    stop sfx1
    scene black with dissolve
    play music "music/flashback.mp3" fadeout 1.0 fadein 1.0
    $ renpy.pause(1)
    "{i}'Ezbril.{w} The mortals need you.{w} You must restore peace into the Mortal Realm again.'"
    $ renpy.pause(1)
    stop music
    scene chariot with dissolve
    play sfx1 "music/wing_beat.ogg"
    $ renpy.pause(0.5)
    show enda2 at right with dissolve
    n "You sure get tired a lot. In any case, here we are."
    stop sfx1
    $ renpy.pause(0.5)
    jump market_pre_intro
label market_pre_intro:
    scene rsz_marketplace with dissolve
    play music "Maze.wav"
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    n "Over there is the north of the ancient Forest of Nourishment we visited before. Looks like it is still burning. In front of you is a village where Cyvtis was reportedly spotted by a few Iruls."
    e "Is this the same village that we saw before?"
    n "Oh no, that one by the forest was a tribe, located at the eastern edge of the forest. The tribesmen love this land and the trees, and I have heard rumors that some of them still remember the Irul."
    n "On the other hand, the villagers are quite innovative with their techniques and love machinery over nature."
    n "Let’s go find what brings Cyvtis to this village."
    hide ezibrl2
    hide enda2
    with dissolve
    jump market_intro

label market_intro:
    $ market_intro_flag = True
    $ lady_flag = False
    $ lady_riddle = False
    $ apple_flag = False
    $ gone_girl = False
    $ pouch = False
    $ thief_flag = False
    $ no_thief = False
    $ t_riddle = False
    $ baker_flag = False
    $ no_baker = False
    $ baker_riddle = False
    $ bk_flag = False
    $ no_bk = False
    $ bk_riddle = False
    $ shepherd_flag = False
    $ no_shepherd = False
    $ shepherd_riddle = False
    $ merchant_flag = False
    $ no_merchant = False
    $ merchant_riddle = False
    $ kids_flag = False
    $ no_kids = False
    $ kids_riddle = False
    jump market_entrance

label market_entrance:

    "The cozy little village reminds you of the small tribe you saw before."
    "A glance eastward, and you can see what is left of the ancient Forest, still
    ablaze. To your west is the village marketplace, humming alive with busy
    mortals hurrying to make the most of their short time."
    "Cyvtis is somewhere in the village, perhaps disguised as a mortal."

    menu:
        "Go west":
            jump market_west
        "Go east":
            jump market_east

label market_west:
    if (market_intro_flag):
        "You have never been to a human marketplace, and you did not know what to
        expect. It seems that the entire village, no, all of the Mortal Realm has
        decided to gather here on consensus."
        "The marketplace needs no Irul of Chaos, for it has plenty of chaos of its own."
        "Merchants shouting their wares, buyers gathering up items as fast as they
        can, human younglings shoving and elbowing as they race through the crowd."
        "You tug close your hood, hoping to dissolve within its comforting shadow."
        "{i}'Stop! Thief!'"
        "You see a masked man running across the marketplace, a leather pouch in one hand and a broom stick in another. Thrusting villagers aside, he runs off into a shaded passageway."
    $market_intro_flag = False
    jump block_1


label market_east:
    "Even from this distance, you can see the ghastly orange grin taking what
    was once sacred and alive and casting it into the sky, first glowing red
    then cooling to black. Nazareth has bound the angry flames, but how long
    shall the inferno rage?"
    "But that is not your task. You must find Cytvis and figure out why she let the Sun ignite the ancient
    forest."

    jump market_entrance

label block_1:
    "You stand inside the marketplace. To your east is the entrance you just came from. Up north, you can see a path between two vendors’ tents. To your west is a narrow passage, shaded a quiet, contrary to the rest of the marketplace."
    menu:
        "Go west":
            jump thief
        "Go north":
            jump lady
        "Go east":
            jump market_entrance

label lady:

    "You squeeze through the bustling crowd and aim for the narrow path between
    two vendors’ tents. "

    if gone_girl == False:
        show ezibrl2 at left
        show lady2 at right
        with dissolve
        if lady_flag == False:

            "But the passage is blocked by a sobbing lady, pure agony on her
            elderly face."
            l "Sigh. Sig, sig, sob."
            e "..."
            l "Oh, good sirs, please help me! I just lost my pouch, it was full
            of coins."

            menu:
                "Approach her":
                    jump help_lady
                "Leave":
                    jump meanie_to_lady

        else:
            l "Oh, it’s you, good sirs! Did you find my pouch?"
            jump lady_menu
    else:
        jump block_4

label help_lady:
    hide ezibrl2 with dissolve
    show enda2 at left with dissolve
    n "Ma’am, what did the pouch look like?"
    l "It was a brown leather pouch. I had coins in it to purchase goods from
    the market. I put it down to examine some sweet apples, but when I looked
    again, it was gone. Oh, it must have been stolen!"
    l "Oh, sob, sob."
    hide lady2 with dissolve
    show enda2 at right
    show ezibrl2 at left with dissolve
    n "Ezbril, it must be the man we saw running through the market when we arrived."
    e "Indeed."

    $ lady_flag = True
    jump lady_menu

label lady_menu:
    menu:
        "Give her the pouch" if pouch:
            jump give_pouch
        "Ask if you can help her another way" if lady_riddle == False:
            jump lady_riddle
        "Ask for riddle" if lady_riddle == True:
            jump lady_riddle
        "Leave":
            jump leave_nicely


label meanie_to_lady:
    hide lady2 with dissolve
    show enda2 at right
    show ezibrl2 at left
    with dissolve
    n "Come on, Ezbril! Could we not help a crying lady?"
    e "We must focus on our task."
    hide ezibrl2
    hide enda2
    with disolve
    jump block_1

label give_pouch:
    hide enda2 with dissolve
    show lady2 at right with dissolve
    l "Oh good sirs, thank you! Thank you so much!"
    l "Wait here for just a moment."
    "The Lady rushes to a nearby merchant who trades her a dozen apples."
    l "Here, please take this as a token of my gratitude."
    "The Lady hands you a sweet apple."
    $ apple_flag = True
    l "Oh! The grandkids must be getting hungry. I shall be on my way."
    "The Lady walks away, humming a joyous tune. The path is clear now for you
    to proceed."
    hide lady2 with dissolve
    show enda2 at right with dissolve
    n "Such a sweet ma'am."
    e "I would warn you against growing too fond of the mortals."
    $ gone_girl = True
    hide ezibrl2
    hide lady2
    with dissolve
    jump block_4

label lady_riddle:
    if lady_riddle == False:
        $ lady_riddle = True
        hide ezibrl2 with dissolve
        show enda2 at left
        show lady2 at left
        with dissolve
        n "We have not seen your pouch, but is there another way we can help you?"
        l "Oh, would you help me, good sirs?"
        l "The villagers here love to trade in riddles. The good merchant over
        there said he would let me have a dozen of those sweet apples if I can
        answer his riddle. You look wise, good sirs. Can you help me solve the
         merchant’s riddle?"
        l "An apple has rolled its way down into a hole. This particular hole
        is extremely deep and has a sharp bend in the middle, making the apple
        impossible to retrieve by hand."
        l "To make matters worse, the ground around the hole is made of hard
        clay, so digging the apple out isn't an option. However, you have
        something incredibly commonplace on hand that you can use to get the
        apple out. He told me the answer has five letters."
        hide enda2 with dissolve
        show ezibrl2 at left with dissolve
        jump lady_riddle_answer
    else:
        hide enda2 with dissolve
        show lady2 at left with dissolve
        l "Good sirs, would you like to try the riddle again?"
        jump lady_riddle_answer

label lady_riddle_answer:
    l "What can you use to get the apple out?"
    $ answer = renpy.input("What do you use to get the apple out?")
    if (answer.lower() == "water"):
        jump riddle_solved
    else:
        l "Hmm... I tried that answer already. It didn't work."
        menu:
            "Hear riddle again":
                l "An apple has rolled its way down into a hole. This particular hole
                is extremely deep and has a sharp bend in the middle, making the apple
                impossible to retrieve by hand."
                l "To make matters worse, the ground around the hole is made of hard
                clay, so digging the apple out isn't an option. However, you have
                something incredibly commonplace on hand that you can use to get the
                apple out. Answer in five letters."
                jump lady_riddle_answer
            "Answer again":
                jump lady_riddle_answer
            "Leave":
                jump leave_nicely

label leave_nicely:
    e "My apologies, but we must be on our way."
    hide ezibrl2 with dissolve
    show enda2 at left with dissolve
    n "We hope you find your pouch!"
    hide enda2
    hide lady2
    with dissolve
    jump block_1

label riddle_solved:
    l "Oh good sir, thank you! Thank you so much!"
    l "Wait here for just a moment."
    "The Lady rushes to a nearby merchant who trades her a dozen apples."
    l "Here, please take this as a token of my gratitude."
    "The Lady hands you a sweet apple."
    $ apple_flag = True
    l "Oh! The kids must be getting hungry. I shall be on my way."
    "The Lady walks away, humming a joyous tune. The path is clear now for you
    to proceed."
    $ gone_girl = True
    hide ezibrl2
    hide lady2
    with dissolve
    jump block_4

label thief:
    "You find yourself in a narrow passage, shaded and quiet, contrary to the
    rest of the marketplace."
    if no_thief == False:
        show ezibrl2 at left
        show thief2 at right
        with dissolve
        if thief_flag == False:
            "Before you stands a rough-looking, lanky man.
            You recognize him as the man running across the marketplace earlier."
            "He is examining a small leather pouch, the kind you have seen many
            mortal females carry in this market. The delicate, embroidered pouch
            looks peculiar in his large hands. You doubt it belongs to him."
            "The man senses your presence. For what seems like eternity, you
            stare at each other. Finally, he grins broadly."
            e "Enda, stand back."
            t "Nehehe. I don’t recall seeing you around. You must be
            new here."
            jump thief_menu
        else:
            t "Oh, its you again. What do you want?"
            jump thief_menu2
    else:
        jump block_2
label thief_menu:
    menu:
        "Ask for pouch":
            e "I think that pouch belongs to someone else. Give it to me."
            jump take_pouch
        "Leave":
            "You decide it is in your best interest to stay out of trouble."
            hide thief2 with dissolve
            show enda2 at right with dissolve
            n "That was a truly terrifying mortal."
            e "He is a craven."
            hide ezibrl2
            hide enda2
            with dissolve
            jump block_1

label take_pouch:
    t "Oh? Aahaha! We have quite a bold one here."
    t "I am this village’s most skilled thief. You dare walk into my lair and demand for what I have rightfully stolen? Nehehe, you amuse me!"
    t "I don’t think this pouch belongs to you either. Why, there is barely anything here! Such a waste of my skills."
    t "But there is something far more valuable I can get from you. You, outsider, did you know that in this village you
       can trade in riddles?"
    t "They value intellect here, because they think it sets them apart from the tribe men who live by that ancient forest.
       Or what used to be a forest- nehehehe."
    $ thief_flag = True

label thief_menu2:
    $ thief_again = False
    t "Answer this riddle, and you shall win the pouch in exchange."
    menu:
        "Answer riddle":
            if t_riddle == True:
                jump thief_riddle
            else:
                t "Let’s test you. Nehehehe."
                t "Give me food, and I will live; give me water, and I will die. What am I?"
            jump thief_riddle
        "Leave":
            t "Nehehehe. Intellect is rare and cannot be stolen, that’s why they value it around here"
            hide ezibrl2
            hide thief2
            with dissolve
            jump block_1

label thief_riddle:
    $ answer = renpy.input("What am I?")
    if (answer.lower() == "fire"):
        $ t_riddle = True

    if t_riddle == True:
        t "That answer should have been on the tip of my tongue with what is happening in the forest."
        t "You have my respect, nehehehe. Here, you can have this humble pouch. I can trade goods far more valuable with the answer you gave me, ahahaha."
        "You hear the jingle of coins as the thief tosses you the small pouch."
        t "I may be a renowned thief, but I am better than the village chief. At least I am not a murderer! Nehehehe."
        "The thief takes a step back, and melts into the shadows."
        hide thief2 with dissolve
        show enda2 at right with dissolve
        n "Village chief? Murderer? What was he talking about?"
        e "This village might harbor secrets we have yet to discover."
        $ pouch = True
        $ no_thief = True
        hide ezibrl2
        hide enda2
        with dissolve
        jump block_2
    else:
        t "Nehehehe. Intellect is rare and cannot be stolen, that’s why they value it around here."
        jump thief_menu2


label block_2:
    "To your north you can see a bridge not that far from where you are standing. To your west you can see the end of the narrow passage, blocked of by stalls.
    Far to the east along the narrow passage lies the exit to the market place."
    menu:
        "Go north":
            jump block_3
        "Go east":
            jump block_1

label block_3:
    "You have arrived at a crossroads. Far north is a bridge that crosses over the river running through the market. To your east is a narrow passage between two stalls. Down west is a trail by the river side which leads to another bridge."
    "To your south is a narrow passage which leads to the exit of the market."
    menu:
        "Go north":
            jump bridge_keeper
        "Go east":
            jump baker
        "Go south":
            jump block_2

label block_4:
    "You walk through the vendors’ tents and onto the narrow path. The path to your west leads to a bridge that crosses over the river running through the market. The path eastward leads to a dead end. Travelling southward would lead you back to the market entrance."
    menu:
        "Go west":
            jump baker
        "Go south":
            jump block_1

label baker:
    if no_baker == False:
        if baker_flag == False:
            "Sweet, welcoming aroma of cinnamon, honey, - and something you can only describe as “warm”-
            beckons you to a bright bake house with a hand painted sign."
            "Entranced by the golden loaves, fruit pies, jam filled buns, cakes, and the many delicacies,
            you wonder when the Iruls would learn some of the mortals’ tricks- the magic of turning wheat into soft bread."
            show ezibrl2 at left
            show baker2 at right
            with dissolve
            "A man in a white apron flashes you a warm grin as he presents a steel tray arranged with buttered buns."
            b "Good morrow, you two! Have not seen you around before. Might you be travellers?"
            e "Indeed."
            b "Welcome then! Try the best bread in the village, and you shall eat most well today. This one is on the house."
            "The golden glaze of melted butter on fresh bread is inviting, indeed."
            jump baker_menu
        else:
            t "Oh, its you again. If you can aid me with my problem, you may take a shortcut through the bakery."
            jump baker_menu2
    else:
        jump block_5
label baker_menu:
    menu:
        "Accept the bread":
            hide baker2 with dissolve
            show enda2 at right with dissolve
            n "Thank you, sir!"
            e "Thank you kindly."
            "The bun feels warm and fluffy in your hand, the butter glossing your fingers. You take a bite. It has only been a few hundred decades since you last tasted mortal food, yet the clever balance of various ingredients fascinates you."
            "The outer layer crisped to perfection, the inside delicately soft, but the taste- the taste you can only describe as joyous and alive and bestowed with sunshine itself."
            "The thought of sunshine reminds you of your purpose to find Cyvtis and discover why she let the sun ignite the Forest of Nourishment."
            $ baker_flag = True
            jump eat_bread
        "Leave":
            "The aroma of baken good might be mesmerizing, but you must stay focused on your task"
            hide baker2  with dissolve
            show enda2 at right with dissolve
            n "Those buns…"
            n "Looked delicious."
            hide enda2
            hide ezibrl2
            with dissolve
            jump block_4

label eat_bread:
    hide enda2  with dissolve
    show baker2 at right with dissolve
    b "You must be weary from your journey. The market can be labyrinth to navigate for visitors like yourself."
    b "If you can aid me with my problem, you may take a shortcut through the bakery."
    jump baker_menu2

label baker_menu2:
    menu:
        "Offer to help":
            if baker_riddle == True:
                jump help_baker
            else:
                e "A shortcut would be much appreciated."
                e "We can try to help you with your problem. What might it be, sir?"
                jump help_baker
        "Leave":
            e "I thank you for your offer, sir, but I would like to explore this area of the market first."
            b "See you around! Be wary lest you lose your bearing."
            hide ezibrl2 with dissolve
            show enda2 at left with dissolve
            n "Thank you for the bread."
            hide baker2
            hide enda2
            with dissolve
            jump block_2

label help_baker:
    b "Somebody ate nine loaves of my bread! Here's what my four kids have to say:"
    b "Aerith: {i}'Brock ate the loaves!{/i}'
    \nBrock: {i}'Daniel ate them all up!{/i}'
    \nCammy: {i}'I didn't eat them, no way!{/i}'
    \nDaniel: {i}'Brock's totally lying!{/i}'"
    b "I know that only one of these rascals are telling the truth and all the others are lying. Can you figure out who is telling the truth?"
    $ answer = renpy.input("Who ate the loaves? (Aerith, Brock, Cammy, Daniel)")
    if answer.lower() == "cammy":
        $ baker_riddle = True
    else:
        b "No, I don't think it's them."
    if baker_riddle == True:
        b "Bravo! I thank you for your help. You may take the shortcut through the bakery anytime you desire."
        hide baker2 with dissolve
        "You proceed through the golden bakery."
        show enda2 at right with dissolve
        n "If I was a mortal, I would like to be a baker."
        e "The Irul should learn some of the mortals’ ways."
        $ no_baker = True
        hide enda2
        hide ezibrl2
        with dissolve
        jump block_5
    else:
        menu:
            "Answer riddle again":
                jump help_baker
            "Leave":
                e "I thank you for your offer, sir, but I would like to explore this area of the market first."
                b "See you around! Be wary lest you lose your bearing."
                hide baker2
                hide ezibrl2
                with dissolve
                jump block_2

label block_5:
    "You have arrived at a crossroads. Far north is a bridge that crosses over the river running through the market. To your east is a narrow passage between two stalls. Down west is a trail by the river side which leads to another bridge."
    menu:
        "Go north":
            jump block_7
        "Go east":
            jump block_4
        "Go west":
            jump block_3

label bridge_keeper:
    if no_bk == False:
        if bk_flag == False:
            "You hear it before you see it, the bustling song of water eager to explore, and free.
            The river itself is a subtle sweep of a painter’s brush,
            glinting bright and managing to dominate its own path despite the labyrinth of the marketplace."
            "Cattails bow to the water’s might, and dragonflies drift lazily overhead. A weathered bridge connects the two shores."

            menu:
                "Walk across the bridge":
                    "The smell of damp wood greets you as you take your first step on the bridge. The suspension sways, but holds fast."
                    "Before you can manage another step, a short figure leaps in front of you. This man was probably hiding- under the bridge?"
                    $ bk_flag = True

                    jump take_bridge
                "Leave":
                    "You are unsure if the ropes would support you across. Perhaps there is another way to cross the river."
                    show ezibrl2 at left
                    show enda2 at right
                    with dissolve
                    n "I saw a sturdier looking bridge over there. Eastward, I think."
                    e "Let’s take a look."
                    hide ezibrl2
                    hide enda2
                    with dissolve
                    jump block_3
        else:
            jump take_bridge

    else:
        "You have crossed the bridge and went through a cornered passage"
        jump block_6

label take_bridge:
    show ezibrl2 at left
    show bridgekeep2 at right
    with dissolve
    bk "Hold it right there! None shall pass without answering the riddle."
    e "Most bizzare."
    hide ezibrl2 with dissolve
    show enda2 at left with dissolve
    n "This is the strangest mortal village I have visited."
    hide enda2 with dissolve
    show ezibrl2 at left with dissolve

    menu:
        "Answer riddle":
            if bk_riddle == True:
                jump solve_bk
            else:
                e "Tell me your riddle, and I shall answer it."
                jump solve_bk
        "Offer coins from the pouch" if pouch == True:
            jump bribe_bk
        "Leave":
            bk "You shall not pass!"
            hide ezibrl2
            hide bridgekeep2
            with dissolve
            jump block_3
label solve_bk:
    bk "Four people need to cross a bridge in the middle of the night."
    bk "The bridge can only hold two or less people at any time and they only have one flashlight so they must travel together (or alone). The flashlight can only travel with one person so every time it crosses the bridge it must be carried back."
    bk "Tom can cross in one minute, John can cross in two minutes, Sally can cross in five minutes, and Connor can cross in ten minutes. If two people cross together they go as fast as the slower person."
    bk "What is the shortest amount of time it would take the four of them to all cross?"
    $ answer = renpy.input("What is the shortest amount of time it would take the four of them to all cross? (Answer numerically, e.g. 1)")
    if answer == "17":
        $ bk_riddle = True
    else:
        bk "Sorry, that is wrong!"
        jump take_bridge

    if bk_riddle == True:
        bk "Hmph. You have answered correct."
        "Before you realize it, the man leaps into the river- yet you do not hear the splash of water. He was indeed hiding under the bridge."
        hide bridgekeep2 with dissolve
        show enda2 at right with dissolve
        n "Does he live there?"
        e "He might."
        "The bridge is now clear for you to pass."
        hide ezibrl2
        hide enda2
        with dissolve
        $ no_bk = True
        jump block_6
    else:
        jump solve_bk


label bribe_bk:
    "Maybe you can temp this greedy mortal with some coins.
    The clink of the few coins grab the man’s attention as you reach into the folds of your cloak. You fish out the leather pouch.
    Without looking away, the Bridge Keeper steps aside, leave a path wide open."
    bk "Humph. This shall do. You may pass."
    "You hold out the pouch, but the man is already snatching it away."
    hide ezibrl2 with dissolve
    show enda2 at left with dissolve
    n "Hey!"
    "A moment more, and he is gone, too fast for you to notice -perhaps back hiding under the bridge."
    hide bridgekeep2 with dissolve
    show enda2 at right
    show ezibrl2 at left
    with dissolve
    e "..."
    e "Despicable."
    "You continue your trek across the bridge."
    hide ezibrl
    hide enda2
    with dissolve
    jump block_6

label block_6:
    "You have arrived at a crossroads. Far north is a bridge that crosses over the river running through the market. To your east is a narrow passage between two stalls. Down west is a trail by the river side which leads to another bridge."
    menu:
        "Go north":
            jump shepherd
        "Go east":
            jump block_7
        "Go west":
            "You went through the cornered passage and crossed the bridge"
            jump block_3
label block_7:
    "You have come onto another crossroad. Just to your north is a very narrow road which leads to the north end of the market. To your east is a narrow cornered passage.
    To your west is another crossroad. To your south is a bridge."
    menu:
        "Go north":
            jump merchant
        "Go east":
            jump dead_end_1
        "Go west":
            jump block_6
        "Go south":
            jump block_5

label dead_end_1:
    "You have reached the end of this road. There is a large wall blocking you from progressing any further. You decide to head
    back to your previous crossroad as there is no point wasting your precious time here"
    jump block_7

label merchant:
    if no_merchant == False:
        "As you shove your way through the crowd, you find the path blocked by a merchant’s wagon."
        show ezibrl2 at left
        show merchant2 at right
        with dissolve
        if merchant_flag == False:
            "You have never seen a wagon up close before, and you cannot help but feel awed by the mortals’ inventive.
            The creative ensemble of refined wood and cloth allowed this merchant to carry heaps of furs,
            pulled through many roads by his patient horse."
            "The merchant stands leaning against his wagon,
            heedless of the path he has blocked. Your approach draws his attention."

            m "Hail, old friend! Would you be interested in some fine, silky furs? Perhaps a warm pelt for the young lad?"
            "You ignore him."
            m "I tell you, I did not trade these furs from yon tribesmen!"

            menu:
                "Talk to him":
                    jump talk_merchant

                "Leave":
                    "You have no interest in trading with the mortals."
                    hide ezibrl2
                    hide merchant2
                    with dissolve
                    jump block_7
        else:
            m "Aha, its you again. Are you here to solve my riddle?"
            jump merchant_menu
    else:
        jump block_8

label talk_merchant:
    "His words catch your interest."
    e "What tribesmen? What do the furs have to do with tribesmen?"
    m "Wh-no, no. I said the furs have nothing to do with the tribesm-"
    m "Oho! You must be an outsider here, just like your old friend."
    m "You see, old friend, the villagers here seem to have a dispute with the tribesmen east of the forest."
    m "The truth is, I stopped by the tribe for a few days and traded my wood for these fine furs. A merry folk they were, I tell you."
    m "They treated your old friend most kindly, and they took good care of the horse. I was sure their furs would fetch a generous price."
    m "Alas, the moment I mentioned the tribesmen here, the villagers have avoided my wagon. This is woodness, old friend!"
    hide ezibrl2 with dissolve
    show enda2 at left with dissolve
    n "I don’t understand, why would the mortals manifest such hate against their own kind?"
    hide merchant2 with dissolve
    show enda2 at right
    show ezibrl2 at left
    with dissolve
    e "You have a lot to witness, Enda."
    "The horse whips its tail to bat off a fly."
    hide enda2 with dissolve
    show merchant at right with dissolve
    m "Aha, but a gentleman thither offered to buy all of my furs, if I can prove myself more cultured than the tribesmen. Old friend, all is not in despair. He said something about only a refined man being able to solve this riddle."
    $ merchant_flag = True
    m "What say you, old friend? Would you mind helping a friend out here?"
    jump merchant_menu

label merchant_menu:
    menu:
        "Try the riddle":
            if merchant_riddle == True:
                jump merchant_help
            else:
                e "Uh, I can give it a try."
                jump merchant_help
        "Feed apple to the horse" if apple_flag == True:
            jump feed_horse
        "Leave":
            m "Woe, old friend! Mayhap we are not the cultured gentleman we try to be."
            hide ezibrl2
            hide merchant2
            with dissolve
            jump block_7

label merchant_help:
    m "The distance three racehorses can run around the racetrack a minute are as follows: \nHorse A: Two laps. \nHorse B: Three laps. \nHorse C: Half a lap."
    m "The horses line up at the starting line and start running in the same direction. How many minutes will pass before all three horses line up at the starting line again?"
    $ answer = renpy.input("How many minutes will pass before the horses line up? \n(Answer numerically, e.g. 1)")
    if answer == "2":
        $ merchant_riddle = True
    else:
        "Sorry, old friend. That's not the answer."
        jump merchant_menu
    if merchant_riddle == True:
        m "Most beauteous, old friend!"
        "He moves his wagon just enough for you to proceed."
        m "I will see you anon!"
        $ no_merchant = True
        hide ezibrl2
        hide merchant2
        with dissolve
        jump block_8
    else:
        jump merchant_menu

label feed_horse:
    "You ignore the jabbering merchant and reach into the folds of your cloak for the sweet apple the lady gave you."
    "The horse eyes your every movement. Slowly, the horse reaches forward toward your outstretched arm, the red apple smooth in your hand."
    "The greedy beast has moved the wagon just enough for you to proceed."
    hide merchant2 with dissolve
    show enda2 at right with dissolve
    n "Clever play, Ezbril!"
    hide ezibrl2
    hide enda2
    with dissolve
    jump block_8

label block_8:
        "You have reached the northend of the market. To your south is the cross from where you just came. To your west is a narrow path. You notice that the path o your east
        leads to an deadend."
        menu:
            "Go west":
                jump kids
            "Go south":
                jump block_7

label shepherd:
    "A glance skyward, and you see the clouds gathering up ahead."
    "Cyvtis, the Irul of the skies, must be close by."

    if no_shepherd == False:
        if shepherd_flag == False:
            "Still gazing upward,
            you slam into a cloud on the ground- no, a lamb?"
            show enda2 at left with dissolve
            n "How lovely! Come here, little lamb."
            "Up ahead, you see a vast herd of sheep, a mirror image to the cloudy sky above."
            "Amid the mass of rolling cotton walks a single mortal, already glancing your way.
            Her small stature allows the shepherd to skillfully navigate her way through the mob, a hound at her heels."
            show shepherd2 at right with dissolve
            s "Good day, misters! What brings you upon this humble herd?"

            menu:
                "You wish to proceed":
                    hide enda2 with dissolve
                    show ezibrl2 at left with dissolve
                    e "I would like to proceed to the other side of this herd."
                    s "Oh! Apologies, mister. We must be blocking your path."
                    $ shepherd_flag = True
                    s "I will move this herd to the pasture yonder, but I need to make sure I have everyone. Could you help me figure out how many sheep there are?"
                    jump help_shepherd

                "Leave":
                    "That herd does not look easy to navigate."
                    hide enda2
                    hide shepherd2
                    with dissolve
                    jump block_6

        else:
            jump help_shepherd
    else:
        jump block_9

label help_shepherd:
    menu:
        "Help her":
            if shepherd_riddle == True:
                jump solve_shepherd
            else:
                e "Sure, I can help you."
                jump solve_shepherd
        "Leave":
            e "Worry not about moving your herd. I shall find another path."
            hide ezibrl2
            hide shepherd2
            with dissolve
            jump block_6

label solve_shepherd:
    s "Sheep are famous for their ability to multiply at breakneck speeds. The type of sheep we have here give birth once a month, birthing 12 babies each time. Baby sheep mature and can give birth two months after they are born."
    s "My friend picked up one of these darling baby sheep from me and brought it home the day after it was born and it has been 10 months since then."
    s "Yesterday, she gave me all the sheep that she had now, but I forgot how many there were. Therefore, I do not know how many sheep I am supposed to have."
    s "I know how many sheep are mine, but can you figure out how many sheep my friend gave me?"
    $ answer = renpy.input("How many sheep did my friend give me? \n(Answer numerically, e.g. 120)")
    if answer == "1":
        $ shepherd_riddle = True
    else:
        s "I don't think that is the correct answer..."
        jump help_shepherd
    if shepherd_riddle == True:
        s "Oh! That makes sense, because a single sheep cannot give birth by itself. Looks like I have everyone."
        "The shepherd circles her staff twice in the air. On cue, her hound begins gathering the sheep."
        s "Safe travels to you and farewell!"
        hide shepherd2 with dissolve
        show enda2 at right with dissolve
        n "Would Kehira allow me to bring a sheep into the Greater Realm?"
        e "No."
        e "Well, for you, maybe if you ask nice enough."

        $ no_shepherd = True
        hide ezibrl2
        hide enda2
        with dissolve
        jump block_9
    else:
        jump solve_shepherd

label block_9:
    "You have come onto a crossroad. Just to your north is the Town Square, the heart of the market. To your east is a narrow cornered path between two stalls, leading towards the crossroad you came from before. To your west is a path going towards the river."
    menu:
        "Go north":
            jump town_square
        "Go east":
            jump block_6
        "Go west":
            jump dead_end_2

label dead_end_2:
    "You have reached the end of this road. There is a river blocking you from progressing any further. You decide to head back to your previous crossroad as there is no point wasting your prescious time here"
    jump block_9
label kids:
    "A peculiar shift of air reveals that the Irul of the Skies must be close by."
    if no_kids == False:

        "As you make your way through the suffocating mass of mortals, you find your path conveniently blocked by a group of insolent mortal younglings."
        if kids_flag == False:
            show kids2 at right with dissolve
            c1 "You can not play with us in our fort, you are a tribesman!"
            c2 "Boo, tribesman!"
            c3 "No, I am not!"
            c1 "I saw your folks travelling to the east side of the forest."
            c3 "That is a lie!"
            show enda2 at left with dissolve
            n "The villagers sure despise the tribesmen."
            hide enda2 with dissolve
            show ezibrl2 at left with dissolve

            menu:
                "Proceed past the younglings":
                    jump proceed_kids
                "Leave":
                    hide kids2 with dissolve
                    show enda at right with dissolve
                    "Strange creatures they are, the mortal younglings. Maybe you can find a way around."
                    n "I wanna make a fort like that when we return to the Greater Realm."
                    e "That looked nothing like a fort."
                    hide ezibrl2
                    hide enda2
                    with dissolve
                    jump block_8
        else:
            show ezibrl2 at left
            show kids2 at right
            with dissolve
            c1 "Oho, you're back"
            jump kids_code
    else:
        jump block_10

label proceed_kids:
    "Depicting no interest, you continue your trek."
    c1 "Hey you! If you want to pass through the fort, you must say the secret code."
    e "...Fort?"
    "You look around for the alleged fort."
    hide kids2 with dissolve
    show enda2 at right with dissolve
    n "This looks fun!"
    "You follow Enda’s gaze, but all you see is bags of flour and rice stacked in four piles, ragged blankets hanging between them."
    hide enda2 with dissolve
    show kids2 at right with dissolve
    c2 "Are they tribesman as well?"
    c1 "They might be, but if they can unravel the code then they are not."
    $ kids_flag = True
    jump kids_code

label kids_code:
    c2 "Our secret code is the hardest to break!"
    menu:
        "Try the code":
            if kids_riddle == True:
                jump solve_code
            else:
                e "Is it now? I bet you I can unravel your code."
                jump solve_code
        "Leave":
            c2 "Aha! Told you our secret code is the hardest to break!"
            c1 "Boo, tribesmen!"
            hide kids2 with dissolve
            show enda2 at right with dissolve
            n "..."
            e "Enda, ignore them."
            hide ezibrl2
            hide enda2
            with dissolve
            jump block_8

label solve_code:
    c1 "A boy and his big sister are sitting around the kitchen table chatting.\n {i}'You know, Sis, if I took away two years from my age and gave them to you, you'd be twice my age, huh!{/i}"
    c2 "'{i}Well, why don't you just give me one more on top of that? Then I'll be three times your age.'{/i}\nSo just how old is the youngest sibling?"
    $ answer = renpy.input("How old is the youngest sibling? (Answer numerically, e.g. 1)")
    if answer == "6":
        $ kids_riddle = True
    else:
        c2 "That's not how old he is!"
        c1 "You cannot pass!"
        jump kids_code
    if kids_riddle == True:
        c1 "Behold the sirs! You may travel through our fort in peace."
        e "You know, I am in fact a tribesman."
        "The kids look shocked."
        c2 "B-but you are a gentleman! How can a tribesman break our secret code?"
        c3 "Tribesmen must be real strong."
        c1 "Only tribesmen can break our secret code!"
        "You pass through the fort of flour and rice."
        hide kids2 with dissolve
        show enda2 at right with dissolve
        n "Tribesman? What was that about?"
        n "You are an Irul."
        e "Yes, I am."

        $ no_kids = True
        hide ezibrl2
        hide enda2
        with dissolve
        jump block_10
    else:
        jump solve_code


label block_10:
    "You are on a narrow path. Just to your west is the Town Square, the heart of the market."
    "To your east is a narrow path, leading towards towards the entrance to the northend of the market."
    menu:
        "Go west":
            jump town_square
        "Go east":
            jump block_8



label town_square:
    play music "Nazareth.wav" fadeout 1.0 fadein 1.0
    "The rough, cobbled alley twists and tapers, turn after turn straying from the market crowd. With every step, the passage gets quieter, and the walls seem to cast more shadows."
    "You almost missed it in the dark, the silhouette of a wooden cart against the weathered wall. But it is the faint sheen of metal that catches your eye. The cart is loaded with pitchforks, spears, hammers, axes, and daggers- weapons."
    "The village seems to be preparing for war. A sharp smell of damp wood catches your attention. On the ground, you see a pile of wooden torches, drenched in a small puddle of clear water."
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    n "I have a bad feeling about this, Ezbril."
    play sound "music/footsteps.ogg"
    "You hear footsteps behind you."
    hide enda2 with dissolve
    show villager at right with dissolve
    v "Strange choice of a place to explore, of all the locations you can be at in this fine village. Do you not think so, traveller?"
    "You can barely make out the figure from the shadows."
    v "Especially with that young lad with you. This is no place for children."
    "Enda moves closer to you as you take a step in front."
    e "I see the villagers here like to collect weapons."
    v "You seem to be a cultured man."
    e "Are you starting a war?"
    v "We are only ending the war. Long have the tribesmen disputed with our folks, but we shall tolerate the barbarians no longer. I cannot believe they survived the blazing forest."
    "The image of the burning forest suddenly aligns with the pile of torches on the ground. No, this cannot be..."
    e "Are you responsible for the burning of the ancient Forest of Nourishment?"
    v "Forest of Nourishment? Ha! It was just another old forest."
    v "Indeed, the villagers set the western trees on fire, hoping the flames would carry eastward and right into the tribe. Alas, our scheme ran unsuccessful."
    v "We were under the belief that the tribe is located along the woodland edge, but we seem to have been wrong. Apparently, the forest was much smaller than what we were led to believe."
    "This is madness. The chaos of this villagers’s heart fuels your own powers. Your blood flows hot as fire, then icy cold. An otherworldly darkness blurs your visions."
    v "Our people are not content, however. We will rage war. If we cannot use the forest, then we shall use our weapons."
    e "Why are you telling me this?"
    "Your voice sounds calm. Deadly."
    v "Ha! Because you may join us, if that is your wish. You seem interested in our fine weapons, and you look to be a cultured gentleman, similar to our own kind."
    v "If you made it this far through the market, you must have solved various intellectual problems. Truly, you belong with us in spirit. Were you to decide upon staying, you would be most welcomed here."
    "You cannot believe your ears. This man must be going crazy."
    "The shadows of the alley disguise the dark tendrils creeping from your fingers and across your arms, eagerly reaching toward the villager."
    "Enda nudges you in silent warning. You must not lose control."
    v "I have a council to attend soon. Farewell for now, traveller! I hope to see you join us."
    "The shadow of a man blends into more shadows. Silence greets you once again."
    hide villager with dissolve
    show enda2 at right with dissolve
    e "This has been an unexpected turn of events. We have not discovered Cyvtis’s purpose yet, but now we know the real culprit- or should I say, culprits, of the forest fire. We must report this to Kehira."
    n "I am ready to leave this village."
    hide ezibrl2
    hide enda2
    with dissolve
    "You realize that you do not remember your way back through the mayhem of the market. You decide to continue forward through the winding passage, toward the sliver of light promising fresh air."
    "The narrow, suffocating alleyway stretches at last into a vast town square. Where the market was crowded with vendors shouting their wares and buyers shoving through the mob, the town square is surprisingly peaceful."
    "Younglings running and playing, women engaging in pleasant conversations, and the elderly perched on comfortable stacks of hay and grains. A large basin of water occupies the centre, surrounded by young dancers."
    "Your attention fixates on the dancer in the far left. It is not her graceful movements, slightly peculiar and rather swift compared to the others, but the dance- you recognize her dance."
    "The Irul's dance of rain."
    "Long ago, the mortals would have remembered this dance as well, but they have forgotten the Iruls. What may seem like a brew of careless movements is in fact a display of meticulous maneuver by Cyvtis."
    "It begins as a whispering in the air. A tinkling sound comes to your ears as the sky’s first tear fall softly on your cheek."
    "Cyvtis cups her hands and brings them to her heart. With half a kick, her palms stretch eastward in a swirling motion. The winds whips and blows away the rain clouds toward the direction her palms are pointing- toward the still blazing forest."
    show enda2 at right with dissolve
    n "She is bringing rain to the Forest of Nourishment! Cyvtis is harnessing the power of the skies to quench the flames."
    hide enda2 with dissolve
    "You watch in awe as heaps of billowing clouds march toward the forest, the raging inferno fighting to its last ember."
    "The dance ends abruptly. With a nimble movement, Cyvtis is making her way toward the market, and possibly out of the village. This is a good chance for you to get out as well, and you follow her distantly."
    "A cold breeze licks at your face and creeps across your skin. The air is suddenly ice-cold and the once-bright sky now dimmer, as if the sun’s warmth has been directed elsewhere."
    v "Somebody set the weapons cart on fire!"
    av "The torches have also been drenched. They are useless now."
    "You quickly realize what has happened, and the increasing haste in Cyvtis’s light steps confirms your suspicions."
    "While you struggle to keep apace, the warmth returns to the air again. You lose Cyvtis in the market crowd, but fortunately, you can see the last few rows of vendors only a few yards away."
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    e "We must get out of here fast. The villagers would be looking for any foreigners soon."
    n "Here comes the chariot."
    jump chariot3

label chariot3:
    $ renpy.pause(1)
    scene chariot with dissolve
    play sfx1 "music/wing_beat.ogg"
    play sfx2 "music/horse_neigh.ogg"
    $ renpy.pause(2)
    stop sfx2
    show enda2 at right with dissolve
    n "Welcome aboard again."
    n "Let’s go!"
    scene black with dissolve
    "Your mind is befuddled with what you discovered in the village. A cacophony of haphazard thoughts drifts you to slumber."
    $ renpy.pause(3)
    "You stare into the depths of the puddle. Staring back at you, amidst darkness and destruction, is a grinning monster."
    $ renpy.pause(3)
    scene chariot with dissolve
    show enda2 at right with dissolve
    stop sfx1
    n "We are back in the Greater Realm."

    jump mission3
label mission3:
    play music "Dark_throne.wav" fadeout 1.0 fadein 1.0
    scene throne_room
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    n "We have returned, Your Majesty."
    "You bow deeply as Enda sprints out of the throne room."
    hide enda2 with dissolve
    show kehira at right with dissolve
    e "And we have discovered the true culprits of the disorder in the Mortal Realm."
    "The Queen arches a slender brow."
    e "The chaos of the Mortal Realm is the work of none but mortals themselves."
    k "Are you certain that this is not the work on an Irul, Ezbril? I sensed Irul magic entwined with the disorder."
    e "The magic you sensed is from various Irul attempting to restore harmony to the Mortal Realm."
    k "Ezbril, what did you witness in the village?"
    e "The villagers have a feud with the tribe by the forest east. They are planning war. The villagers set the west trees on fire, hoping the flames would spread right into the tribe. If it were not for Nazareth’s sacrifice, the tribe would have been destroyed."
    e "Nazareth faded the Ancient Forest of Nourishment to save a tribe of mortals. Cyvtis brough rain upon the blazing forest and harnessed the powers of the sun to alight the weapons meant to start war."
    e "From what I have witnessed, the Iruls are using magic to combat the evils of the Mortal Realm."
    "The Queen is silent. Contemplating."
    k "Ezbril, Irul of Chaos and Destruction, you bring bewildering news. Have the mortals fallen into darkness again?"
    e "I can not say that about all the mortals, for we do not know the tribe’s role in this feud. Moreover, despite the darkened hearts of a few, I met many kind folks in that vil-"
    play sound "music/footsteps.ogg"
    "Footsteps scurry into the throne room."
    hide ezibrl2 with dissolve
    show enda2 at left with dissolve
    n "Your Majesty! There has been a catastrophe. I have been sent to inform you of a great destruction in the Mortal Realm."
    k "What happened, Enda?"
    n "The v-village. The village Ezbril and I just visited. It has been wiped out by a mighty flood."
    hide enda2 with dissolve
    show ezibrl2 at left with dissolve
    "You are shocked. There may have been a few darkened souls in that village, but what about the many innocent ones? What happened to the laughing younglings who had so much to live for? The lively village that breathed a few heartbeats ago."
    "All of it, gone?"
    k "Ezbril, you say that the disorder of the Mortal Realm is work of the mortals, yet the mortals have no powers over the flow of a  river. The mortals can set forests on fire and forge weapons, but only the magic of an Irul could cause such a catastrophe."
    e "It must have been Cyvtis’s vengeance on the village. She brought excessive rains that flooded the river."
    k "Would Cyvtis save the tribe, only to go after the lives in the village? Were that her intention, it would require many days of rain."
    k "Cyvtis is the Irul of Skies, but let us not forget the Irul who controls the rivers."
    k "Ezbril, you have done well so far, yet your task has not concluded. Your next target is Zartharacks, the Irul of Sea and all Waters."
    k "Zartharacks is responsible for the flow of the rivers and streams, and maintaining balance in the waters. The rise in the river’s water level could have been a work of his."
    k "I must warn you, Zartharacks is- unique."
    e "Unique?"
    k "I am sure you will soon see for yourself. Enda, escort Ezbril to Zaratharacks’s lair."
    hide kehira with dissolve
    show enda2 at right with dissolve
    n "As you wish, Your Majesty."
    jump chariottowater
label chariottowater:
    $ renpy.pause(1)

    scene chariot with dissolve
    play sfx1 "music/wing_beat.ogg"
    play sfx2 "music/horse_neigh.ogg"
    $ renpy.pause(2)
    stop sfx2
    show enda2 at right with dissolve
    n "This has been quite an adventure!"
    n "Let’s go back, hopefully for the last time."
    hide enda2 with dissolve
    "Your thoughts are plagued with the faces of the mortal younglings you saw in the village. What about the other innocent souls in the Mortal Realm? How long until this darkness takes over?"
    stop sfx1
    scene black with dissolve
    play music "music/flashback.mp3" fadeout 1.0 fadein 1.0
    $ renpy.pause(1)
    "{i}'Ezbril.{w} Ezbril.{w} What have you done?'"
    $ renpy.pause(1)
    stop music
    play sfx1 "music/wing_beat.ogg"
    scene chariot with dissolve
    stop sfx1
    show enda2 at right with dissolve
    n "Ezbril, let’s go."
    jump beforemaze3
    $ renpy.pause(1)
label beforemaze3:
    play music "Banished.mp3"
    $ renpy.pause(1)
    scene ship_above with dissolve
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    n "Here we are. Zartharacks’s lair. Look, you can see the mortals tribe not far ahead."
    "Indeed, the mortals tribe is clearly visible from here, although it is not located at the edge of the forest anymore, thanks to Nazareth. You can make out some of the forest trees from here- or what remained of the forest, now drenched by Cyvtis’s rain."
    "You know that beyond the forest lies the village, now demolished by the river. The river flows through the remains of the village, swirling through the forest and the tribe, snaking from the tribe toward you and into-"
    e "The sea?"
    "Before you expands a murmuring domain of waters, the shimmering beast desolate, yet strangely alive."
    "The furious waves wrestle and crash into the menacing rocks, eager to spill the secrets of the unknown beyond. The destructive magic within you opens an eye."
    n "In the waters you will find a sunken ship, the one that remains apiece. Zartharacks had turned the mighty ship into his lair, his personal quarters located in the bottom most level of the ship."
    e "All we need to do is locate him within his lair, and unravel his plans?"
    e "Let's go."
    n "Ezbril."
    n "I am afraid I cannot join you this time."
    e "Oh?"
    n "As a lesser-Irul, I still need to breathe. Therefore, I cannot accompany you underwater."
    "You feel a pang of sorrow for the young Irul, but Enda looks cheerful."
    n "I have been wanting to explore the tribe up close. They say some of them still remember the Irul. I want to know if the rumors are correct."
    n "After you have found Zartharacks, you should come explore the tribe as well."
    e "I must focus on my task ahead, but I will join you afterward."
    n "I shall see you soon, then."
    "Enda sprints toward the colourful tribe, laughing joyously, as you turn toward your next quest."
    $ renpy.pause(0.5)
    jump maze3start

label maze3start:
    scene black with dissolve
    play music "Maze.wav" fadeout 1.0 fadein 1.0
    # starting position is 2,1
    $pos = [2,1]
    "Your footsteps are muted to a gentle thud as you prowl across the ashen sand and into the beckoning sea."
    "The sea is a malicious force, daring and cold. A taunting current sways you sideways, a loyal guardian to the hoard of wooden masts and planks that break the surface."
    "And then she catches your eye."
    "You know her when you see her, a sunken ship still apiece. The dark beast rests at the bottom most seabed, ancient and asleep. Zartharacks’s lair."
    scene underwater with dissolve
    "You stand on the main deck, but you must make your way to Zartharacks’s personal quarters on the lowest level."

    ##menu:
        ##"Go into the ship":
            ##pass
        ##"Return ashore":
            ##jump end

    "You go to the entrance and descend down the stairs. The deck you are on is empty, except for the vegetation and the few fish that have taken the ship as their home."
    "The deck is rectangular in shape. About twice as long as it is wide. You see the stairs leading to the lower decks directly north of you."
    "The water is calm where you are standing."
    $first = True
    jump maze3p1

label maze3p1:
    if pos == [2,6]:
        "You make it to the other end of the ship. You take the stairs and descend downwards into the lower deck of the ship."
        $pos = [2,1]
        "You are on one deck deeper inside of the ship. This deck is about the same size as the previous deck."
        "You see the stairs leading to the lower decks directly north of you."
        "Before you proceed, you notice the water change. While it was calm when you entered, it now moves with unrest."
        "As you take in your surroundings, you feel the water around you get calm."
        "You wait a few moments."
        $current = True
        jump maze3p2
    if pos in ([2,2],[1,3],[3,3],[1,5],[3,4],[2,4],[2,5]):
        "You make your movement."
        "The water surrounding you is uneasy but you are unsure which direction the current is coming from."
        if pos == [2,2]:
            "You see your destination directly in front of you."
        elif pos == [2,4]:
            "You see your destination directly in front of you. You are almost to the end."
        elif pos == [2,5]:
            "You see your destination directly in front of you. You are one step away from the end."
    elif pos in ([1,4],[2,3],[3,5]):
        "You make your movement."
        "As soon as you do, you feel the water immediate change from calm to something more vicious."
        "The current pushes against you, almost as if to push you away. You try to fight the current, but it is too strong for you."
        "The current throws you backwards. You fly further away from your destination."
        "As you are thrown back, you see the railing of the stairs that you just descended. It takes all of your strength to throw your arm out to grab the railing."
        "You hold on for dear life. After a few moments, the water calms and you are no longer pushed against your will."
        "You are back where you began."
        $pos = [2,1]
    else:
        if first:
            pass
        else:
            "You make your movement."
            "The water is calm where you are standing."
    menu:
        "Go north" if pos[1] != 7:
            $pos[1] += 1
        "Go west" if pos[0] != 1:
            $pos[0] -= 1
        "Go east" if pos[0] != 3:
            $pos[0] += 1
        "Go south" if pos[1] != 1:
            $pos[1] -= 1
    $first = False
    jump maze3p1

label maze3p2:
    if current:
        "The water suddenly flows with unease. Be careful where you go, lest you are moved against your wishes."
    else:
        "The water suddenly calms. No matter where you go, it is safe to proceed."
    if pos == [2,7]:
        $pos = [3,1]
        "You make it to the other end of the ship. You take the stairs and descend downwards into the lower deck of the ship."
        "You are on one deck deeper inside of the ship. This deck is not as long as the previous deck but it is wider."
        "You see the large oak doors directly north of you."
        "Similar to the previous deck, you notice the water shifts between being calm and restless as time pass."
        "However, unlike the previous floor, some of the currents are eternally restless."
        $current = False
        jump maze3p3
    if pos in ([1,1],[3,1],[2,2],[2,2],[3,3],[1,3],[1,6],[3,4],[3,6]):
        if current:
            "The water surrounding you is uneasy but you are unsure which direction the current is coming from."
        else:
            "The water surrounding you is calm but not as calm as you would like. The water around you will act up soon."
        if pos == [2,2]:
            "You see your destination directly in front of you."
        elif pos == [2,3]:
            "You see your destination directly in front of you. You are a bit closer to the end."
        elif pos == [2,4]:
            "You see your destination directly in front of you. You are about half way there."
        elif pos == [2,5]:
            "You see your destination directly in front of you. You are almost to the end."
        elif pos == [2,6]:
            "You see your destination directly in front of you. You are one step away from the end."
    elif pos in ([1,2],[3,5],[3,2],[1,5],[2,3]):
        if current:
            "You feel the water immediate change from calm to something more vicious."
            "The current pushes against you, almost as if to push you away. You try to fight the current, but it is too strong for you."
            "The current throws you backwards. You fly further away from your destination."
            "As you are thrown back, you see the railing of the stairs that you just descended. It takes all of your strength to throw your arm out to grab the railing."
            "You hold on for dear life. After a few moments, the water calms and you are no longer pushed against your will."
            "You are back where you began."
            $pos = [2,1]
        else:
            "The water surrounding you is especially riled. Do not linger in your position for long."
    else:
        "The water is calm around where you are standing."
    menu:
        "Go north" if pos[1] != 7:
            $pos[1] += 1
            "You make your movement."
        "Go west" if pos[0] != 1:
            $pos[0] -= 1
            "You make your movement."
        "Go east" if pos[0] != 3:
            $pos[0] += 1
            "You make your movement."
        "Go south" if pos[1] != 1:
            $pos[1] -= 1
            "You make your movement."
        "Stay":
            "You wait."
    if current:
        $current = False
    else:
        $current = True
    jump maze3p2

label maze3p3:
    if current:
        "The water suddenly flows with unease. Be careful where you go, lest you are moved against your wishes."
    else:
        "The uneasy water suddenly calms. Certain areas you go to are safe to proceed."
    if pos == [3,5]:
        "You make it to the other end of the ship. You push with all your strength to open the oak doors. Strangely, the doors open as easily as if you were on land."
        jump zarth

    if pos in ([2,1],[3,1],[4,2],[1,2],[3,3],[4,4]):
        #surrounded by changing water and just restless water
        if current:
            "The water surrounding you is uneasy but you are unsure which direction the current is coming from."
        else:
            "Some water surrounding you is uneasy but you are unsure which direction the current is coming from."
            "Some water surrounding you is calm but not as calm as you would like. The water around you will act up soon."
        if pos == [3,3]:
            "You see your destination directly in front of you. You are about half way there."
    elif pos in ([5,1],[5,3],[1,3],[1,5]):
        #surrounded by only changing water
        if current:
            "The water surrounding you is uneasy but you are unsure which direction the current is coming from."
        else:
            "The water surrounding you is calm but not as calm as you would like. The water around you will act up soon."
    elif pos in ([1,4],[5,5]):
        #surrounded by only just restless water
        "The water surrounding you is uneasy but you are unsure which direction the current is coming from."
    elif pos in ([2,2],[3,2],[2,4],[3,4],[4,5]):
        #enter bad water
        "As soon as you do, you feel the water immediate change from calm to something more vicious."
        "The current pushes against you, almost as if to push you away. You try to fight the current, but it is too strong for you."
        "The current throws you backwards. You fly further away from your destination."
        "As you are thrown back, you see the railing of the stairs that you just descended. It takes all of your strength to throw your arm out to grab the railing."
        "You hold on for dear life. After a few moments, the water calms and you are no longer pushed against your will."
        "You are back where you began."
        $pos = [3,1]
    elif pos in ([1,1],[4,1],[2,3],[4,3],[2,5]):
        #enter changing water bad
        if current:
            "You feel the water immediate change from calm to something more vicious."
            "The current pushes against you, almost as if to push you away. You try to fight the current, but it is too strong for you."
            "The current throws you backwards. You fly further away from your destination."
            "As you are thrown back, you see the railing of the stairs that you just descended. It takes all of your strength to throw your arm out to grab the railing."
            "You hold on for dear life. After a few moments, the water calms and you are no longer pushed against your will."
            "You are back where you began."
            $pos = [3,1]
        else:
            "The water surrounding you is especially riled. Do not linger in your position for long."
    else:
        "The water is calm around where you are standing."
    menu:
        "Go north" if pos[1] != 5:
            $pos[1] += 1
            "You make your movement."
        "Go west" if pos[0] != 1:
            $pos[0] -= 1
            "You make your movement."
        "Go east" if pos[0] != 5:
            $pos[0] += 1
            "You make your movement."
        "Go south" if pos[1] != 1:
            $pos[1] -= 1
            "You make your movement."
        "Stay":
            "You wait."
    if current:
        $current = False
    else:
        $current = True
    jump maze3p3

label zarth:
    young2 "Looking for me?"
    show ezibrl2 at left with dissolve
    e "Wha-"
    "Behind you stands the Irul of Waters- or you suppose he is an Irul, for he appears in form more similar to an ancient sea creature."
    show zartharacks at right with dissolve
    z "Ah, Ezbril. It has been some years. Have you returned to taint my waters crimson again?"
    z "Let me guess, you are here to inquire about the flood, and my role in it."
    e "Inquire not so much, I was supposed to spy on you."
    z "Ha! You think you could sneak up on me in my own territory? Fellow Irul, you amuse me so! Why, the waters whisper to me."
    e "Since you are so familiar with your waters, can you explain the flooding of the village beyond the forest."
    "Zartharacks looks weary. Solemn."
    z "The rubble from the broken dam pollutes my rivers. You didn't think I would flood the village and plague my own waters, did you?"
    e "The broken dam?"
    z "There once stood a dam in the river that flows through the village that has now been demolished. A powerful force collapsed the dam, for reasons beyond me."
    z "Why, whichever Irul destroyed the dam has been quite clever in their malicious intent."
    z "When the dam broke, the force of the monstrous wave was too strong, even for me, as I was not prepared for this."
    z "However, I was able to command the wave just enough to spare most of the villagers' lives."
    e "It was no Irul that destroyed the dam, Zartharacks. I have an inkling that this is the work of mortals."
    z "Mortals? Are you forgetting that this is a mortal village that has been destroyed?"
    z "Why would the mortals destroy a mortal village?"
    "A realization hits you."
    e "The tribe."
    z "What did you say?"
    e "Zartharacks, take me to the tribe by the river."
    z "Have you lost your bearing? There is clearly a war raging between the mortals. We would be wise to stay out of this, especially with your history."
    e "Enda is in the tribe."
    z "Oh, the small Messenger Irul?"
    "Zartharacks looks shocked. Angered."
    z "Are you telling me that you left the lesser-Irul by himself, after witnessing the evils of the mortals?"
    "Zartharacks gathers a furious wave that threatens a second flood."
    hide ezibrl2
    hide zartharacks
    with dissolve
    "The world swirls, and a few heartbeats later, you are standing on lush green grass."
    scene battle with dissolve
    "Lush green grass now painted red."
    "A foul smell smacks your conscience, the kind of smell that can only come from an animal slaughterhouse. In this case, the butchered animals are humans and their corpses are still warm."
    "Tribesmen and villagers lay scattered amongst the trees, like ghoulish mannequins."
    "Zartharacks curses under his breath. Row after row of waxy skin splattered crimson. Eyes of unsuspecting merchants and farmers staring forever into the skies. For once, the tribesmen and the villagers lay side by side. And that is when you see it-"
    "A small body in a dark puddle, an arrow protruding from a pale stomach. His chest rises and falls in hiccups of movement."
    "Enda."
    "He is alive, but mortally wounded. Standing above him is an archer from the village, bloodshot eyes staring at Enda’s small form on the ground."
    "The small sound that escapes from Enda sets your blood raging. Tendrils of darkness escape from between your fingers. Ebony flows from your eyes, your mouth and your ears, until you are engulfed in a black orb."
    "The archer has not noticed your presence."
    "You could do it. You could kill her. Half a thought from you, and the archer would be engulfed in black flames. She wouldn’t have time to scream."
    #flashback here
    "No. The past must not be repeated. You have made it this far, you must not lose control now. Enda would not want this."
    "The ice in your veins begins to melt, replaced by a deep, numbing sorrow. Dark tendril slowly reek back. The village archer is now on her knees by Enda’s side. You tense."
    "Gently, the archer scoops up the small form. Her bow drops to the ground, but she does not bend to retrieve it. Without hesitation, she begins to sprint across the field, through the rain of arrows and clash of blades, toward a small tent. A tribe healer’s tent."
    "The tribesmen stationed outside the tent draw their weapons at the sight of a village archer, but then they perceive the slight figure in her arms. Understanding shining in their eyes, they allow the archer to disappear into the tent with Enda."
    "A cool breeze gently caresses your face as you hear Zarthacks softly makes his way to your side. A tender wave gathers you back into the water and along the river, until you stand before the healer’s tent."
    "There is recognition in the tribesmen’s eyes as they let you through the flaps."
    "Resting across a murky blanket, Enda has fallen into a trance. His face is paler than the moon rising above, his cheek colder than the ice that glides on the winter sea. Blue stains his torn shirt, the telltale colour of an Irul’s sacred blood."
    "The lingering joy in his eyes sealed behind heavy lids, hidden from this undeserving world. His wound has been cleaned and covered with herbs, and two healers are draping a cotton cloth across his abdomen."
    "They show no surprise at the pool of cobalt blood, although the archer is gawking."
    show zartharacks at right with dissolve
    z "Alas that these evil days should be ours. The boy needs an Irul healer. Waste no time, my currents shall carry you through the waters and into the Greater Realm."
    "The healers finish covering the wound. Without a word, they stand aside as you pick up Enda’s light form and walk out of the tent, right into the river."
    "Zartharacks remains on land as a gentle, yet strong wave lifts you off the river bed and toward the sea, and beyond the sea into the dark stream that no mortal has ventured into."
    jump conclusion
label conclusion:
    scene black with dissolve
    $ renpy.pause(2)
    play music "Dark_throne.wav" fadeout 1.0 fadein 1.0
    #put a long pause here
    $ renpy.pause(2)
    scene throne_room
    show kehira at right
    with dissolve
    k "You may enter."
    show ezibrl2 at left with dissolve
    e "Kehira"
    e "I have answered your summon."
    "The Queen of Darkness has ruled over the Greater Realm for as long as any Irul could remember. The Queen has been ancient since the first time you saw her, but now she appears weathered- older."
    k "Enda is being taken care of. Without the cloth hindering the flow of his blood, he would have been beyond hope, even for the best of the Irul healers."
    k "I want to discuss the events you witnessed in the Mortal Realm. What you reported upon your return is bewildering news indeed."
    e "I have told you all that I know, Kehira. The flood was in fact no work of an Irul. The fire, the flood, and the massacre were all consequences of the war between the mortals."
    k "Yes, and this is not the first time that the mortals have brought such suffering upon themselves. I fear that eventually, the Iruls might become a victim of their anguish as well. We almost lost an Irul to the evils of the mortals."
    k "I had hoped to reunite the two realms, as they were in the olden days. I had wanted the Iruls to grow stronger, as we once were when the mortals remembered us. I sought power and it blinded me, until we almost lost one of our own."
    k "I cannot risk the well being of the Iruls any longer."
    k "Therefore, I have made the decision to withdraw from the Mortal Realm. The Iruls shall enjoy a blissful life in the Greater Realm, as we will seal the Gates between the two realms for eternity."
    e "Would you abandon the mortals, in order to save the Iruls?"
    k "As the Queen of Iruls, that is my priority. We may never get a chance to grow as strong as we once were, but the Iruls would be safe from the evils of the mortals."
    e "What about the mortals who still remember us? They are few in numbers, but they exist."
    e "What about the innocent younglings who had no perception on the chaos of their realm?"
    e "What about the villager who risked her life to carry Enda to safety, or the tribe healers who allowed him another chance at life?"
    e "While I have witnessed the worst of the mortals; I have also witnessed their kind and selfless spirit. I will not blame the entire realm for the wicked actions of a few."
    k "Your heart is noble, Ezbril. However, the decision has been made and this is what the Iruls want. The Gates shall be sealed."
    e "If that is your resolve, Kehira, then I will stay in the Mortal Realm."
    "The Queen is silent. Pondering."
    k "If you leave now, you will never be able to return to the Greater Realm again."
    e "I have made my decision. All these years I have been the outcast, the Irul who brings nothing but Chaos and Destruction. There is nothing here for me, but I have found the spark of hope in the Mortal Realm."
    e "The mortals need me, as much as I need them."
    "A faint smile dances across the Queen’s lips."
    k "You have been dismissed, Ezbril, Irul of Chaos and Destruction."
    #transition from throne room to gates
    scene black with dissolve
    "You stand before the mighty Gates between the two realms. You watch your last sunset in the Greater Realm, as it paints the sky a brilliant hue of orange."
    "You turn around to catch one last glance of your home."
    "A small form crashes into you, the firm force pushing you a step backward. Tears flood his eyes as Enda wraps his arms tightly around you."
    $ renpy.pause(1)
    play music "Nazareth.wav" fadeout 1.0 fadein 1.0
    #put a long pause here
    $ renpy.pause(2)
    show ezibrl2 at left
    show enda2 at right
    with dissolve
    "He begins to rasp between muffled sobs"
    n "Kehira told me that you are going to l-leave."
    e "Good to see you up and moving."
    n "She said that you will n-never be able to return to the Greater Realm."
    e "This is the beginning of the journey I must embark upon. I have discovered a purpose for myself."
    "Enda lets go of you, but a small hand still clenches your cloak."
    n "Then take me with you!"
    "You are stunned at the young Irul’s request, but challenge and determination shines in his eyes."
    n "I have travelled with you into the Mortal Realm and back. I have witnessed all that you have witnessed, and I also believe that there is hope for the mortals."
    n "I am begging you, take me on your journey!"
    "You consider Enda’s request. And then you smile."
    e "I suppose I would not mind a companion."
    "Enda’s delightful laugh brightens the skies as the two of you step out of the Greater Realm one last time."
    hide ezibrl2
    hide enda2
    with dissolve
    jump epilogue
label epilogue:
    $ renpy.pause(2)
    #pause for a while
    $ renpy.movie_cutscene("epilogue.webm")

    jump splashscreen

label splashscreen:
    scene black
    $ renpy.pause(3)

    show text "Eisha Ahmed" with dissolve
    $ renpy.pause(3)
    hide text with dissolve


    show text "Joshua Smith" with dissolve
    $ renpy.pause(3)
    hide text with dissolve


    show text "Mehrab Islam" with dissolve
    $ renpy.pause(3)
    hide text with dissolve


    show text "Melanie Dene" with dissolve
    $ renpy.pause(3)
    hide text with dissolve


    show text "Nelson Chen" with dissolve
    $ renpy.pause(3)
    hide text with dissolve


    show text "Thomas Pham" with dissolve
    $ renpy.pause(3)
    hide text with dissolve

    show text "Prologue and Epilogue Music: Horizon Zero Dawn Prologue" with dissolve
    $ renpy.pause(6)
    hide text with dissolve

    show text "Thanks for playing!{w}" with dissolve
    $ renpy.pause(3)
    hide text with dissolve

    return
