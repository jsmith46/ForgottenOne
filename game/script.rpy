# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("REMYA")

define k = Character("KEHIRA")

define e = Character("EZBRIL")

define n = Character("Edna")




# The game starts here.
label start:
    jump scene1

label scene1:
    play music "Banished.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    r "Guilty! Is there a punishment worthy of what you have done?"

    "Another god enters."

    r "Sister? Kehira, you are interrupting an important tria- Actually, you came just in time."

    r "Ezbril, Irul of Destruction and Chaos. For the suffering you have caused, for the cruelty you have brought, for your part in the Mortal Realm crisis, I hereby pronounce you guilty. You shall be banished to the Darker Realm, where my sister will ensure that you are punished for eternity."

    e "Please! I am innoc-"

    r "The trial is over. Kehira, he is all yours."

    k "(grinning) This way."

    "Ezbril stands up and walks out with Kehira."

    jump scene2

label scene2:
    play music "Dark_throne.wav" fadeout 1.0 fadein 1.0

    "You are now in another great throne room, dimmer than the last one, but equally as magnificent and clean. Kehira sits upon her dark throne, a white cat on her lap."

    e "So this is the Darker Realm where I will be punished for a crime I did not commit. But why are we in a throne room?"

    k "You did not do it, did you?"

    "You stand there shocked."

    k "My cat got your tongue? You did not cause the Mortal Realm crisis, did you?"

    e "I did not!"

    e "You believe me?"

    k "The Mortal Realm crisis is a series of disasters causing chaos in the mortal world. Cruelty is high, famine is growing, and mortals are suffering. My sister and I are unsure about when exactly this all started, but we are determined to find and punish the Irul responsible for these unspeakable crimes."

    k "You are the Irul of Destruction and Chaos. Naturally, my sister believes that only an Irul of Chaos can cause so much suffering. However, as the Irul Queen of Darkness, I realize that this could not be the work of one Irul alone."

    e "Then why am I here? Will I be punished? I did no-"

    k "Relax, I will not punish you yet. I have much use for you."

    e "Me? What could the Irul Queen of Darkness want from a mere Irul of Chaos?"

    k "You are going to the Mortal Realm to see firsthand what this destruction looks like. We will be able to determine from there who may have started this crisis. By doing this, you may be able to prove your innocence. So what do you say? Are you up for this challenge?"

    e "A look of thought on his face, and nods with approval. What about your sister, the Light Majesty? I am supposed to be banished and punished here. If I am seen in the Mortal Realm-"

    k "Then you must perform your task in stealth? (grins) Or would you rather stay here and find out what awaits you in the Darker Realm?"

    "A small childish looking boy appears behind you."

    n "Your Dark Majesty, have you spoken to Ezbril of our plan?"

    k "Yes, Edna. I was just beginning to tell Ezbril about our plan. He has agreed. But I didn’t get a chance to mention that you will also be joining us. Kehira turns to look at Ezbril, who is looking confused by Edna’s entrance."

    n "That is excellent! We need to get prepared quickly as possible! The mortals can not suffer much more. I have found a way to get us there safely, and undetected. Follow me."

    "A wave of confusion falls upon you but its clear that Kehira is expecting you to follow the small child, so you flustardly run after him."

    jump chapter2scene1

label chapter2scene1:
    play music "Forest.wav" fadeout 1.0 fadein 1.0
    "The scenery has changed, you are now in front of a lush forest. A small tribe can be seen in the distance on your right and in front of you is a path that seems to lead deep into the forest."

    n "Here we are, the Forest of Nourishment. For decades, tribes of humans have relied on the forest’s generous blessings for wood and food. This place is also home to many animals."

    n "In the heart of the forest you will find Nazareth, the Irul of Spring, Harvest, and Life. For eons, he has travelled forest to forest, village to village, nourishing and looked after every being that breathes."

    n "However, his performance has been going downhill lately. Forests are disappearing, animals are fleeing their homes, and food is scarce."

    n "Among the mortals, rumor is that some have spotted Nazareth purposely destroying vegetation. He has not returned to the Greater Realm in almost a decade, which leads Kehira to suspect that he might be hiding something."

    e "Her majesty wants me to investigate Nazareth?"

    n "Not so fast. Remember, you are a fallen Irul and the Iruil believe that you are banished. If you are seen in the Mortal Realm, Nazareth can use that against you. You might not be lucky to be given a second chance."

    n "EDNA: Your task is to find out what exactly Nazareth is doing, so Kehira and Remya can use that information to decide his fate. Be warned, the Forest of Nourishment is a sacred place and easy to get lost in."

    n "I have some glowing gemstones you can use to mark your path.  When you find Nazareth, stay hidden and collect any evidence you find that would support your claim against Nazareth."

    n "I have duties to perform, therefore this is where I depart. I will say this, keep your eyes sharp and be aware of your surroundings. Trust no one. When you have accomplished your goal, meet me here and I shall escort you back to the Darker Realm."

    "Edna hands you 5 glowing gemstones and teleports away."

    e "Why am I always stuck in this mess?"


    jump forest1
label forest1:
    $ backwards = False
    menu:
        "Enter the forest":
            "You walk into the forest until you reach a fork in the path and can now see why Edna said this forest is like a maze."
            jump forest2
        "Investigate the village":
            "I can see the village in the distance and from here it looks very peaceful. The tribe probably relys on the forest for wood and food."
            "I should probably enter the forest now."
            jump forest1
label forest2:
    menu:
        "Take left branch":
            "After walking down the path for a while you come across a sprawling beautiful lake."
            "A dead end it seems."
            menu:
                "Turn around":
                    "You walk back to the branch in the path."
                    jump forest2
        "Take right branch":
            "Walking deeper the trees begin to tower over you even more, the tallest must be hundreds of years old."
            "You come across another branch in the path, your current path seems to continue straight but to the left there is an overgrown path."
            jump forest3
        "Leave the forest":
            jump forest1
label forest3:
    menu:
        "Take the overgrown path":
            "Path is harder to traverse than before, can see signs of decaying flowers."
            "The path keeps getting more overgrown the further you go on, making progress much slower."
            jump forest4
        "Stay on your current path":
            if backwards == False:
                "You continue down the path, passing by a large bog on your right."
                jump forest5
            else:
                "You come across a place you recognise as the first branch in the path when you entered the forest."
                $ backwards = False
                "You turn and faced the crossroad."
                jump forest2
        "Turn around":
            if backwards == False:
                jump forest2
            else:
                $ backwards = False
                jump forest5
label forest4:
    menu:
        "Keep going forward":
            "After bushwacking for what felt like ages you come across a large path similar to the one you strayed from earlier."
            "As soon as you step out from your makeshift path you lose track of where it was."
            menu:
                "Follow large path to the left":
                    jump forest5
                "Follow large path to the right":
                    "You follow the path past a bog on your left."
                    "You come across another branch in the path, your current path seems to continue straight but to the right there is an overgrown path."
                    $ backwards = True
                    jump forest3
        "Turn around":
            jump forest3

label forest5:
    jump forestn

label forestn:
    stop music
    jump forestcenter

label forestcenter:
    play music "Nazareth.wav"

    "A lonely, tranquil heart of a forest. A gushing spring could be heard, along with an occasional call of a songbird. An Irul sits gracefully on a water-smoothed stone, surrounded by an audience of white tailed deer and curious rabbits."
    e "That must be Nazareth. He seems peaceful."
    "The carpet of moss starts to darken. Nazareth stands, and some of the rabbits begin to back away. The grass under his feet begins to darken, then disappear. Like a ripple, the surrounding plants begin to vanish, leaving no evidence of the lush green that existed. The small company of critters starts to flee from their once home."
    e "The Irul of Spring, Harvest and Life … destroying the ancient forest? I must report this to Her Dark Majesty."
    "Nazareth raises his arms, like a falcon about to take flight. He seems to hesitate a moment. Suddenly, he twirls and shoots toward the skies. Time stops. You are not standing in a forest anymore."
    "The entire East half of the forest has vanished, leaving behind no blade of grass or whisper of what was once magical and green. You can easily make out the small tribe from here. And in front of you…"
    "A wall of flames. The West half of the forest is ablaze, the fire rushing toward you, the inferno leaping from tree to tree."
    "But you realize that you are safe. There are no trees, no vegetation left on this side to feed the hungry flames. The forest fire cannot spread."
    "A shift of air, a sudden flash of light to your right, and Edna stands beside you."
    n "Greetings! I’m ba-"
    n "(astonished) What- what happened here?"
    e "It seems to be a forest fire. I was confused when I witnessed Nazareth wiping out the ancient forest. I think he was just trying to protect the tribe of mortals yonder. The flames will not reach them."
    n "(sorrowful) It must be hard for Nazareth to obliterate the ancient Forest of Nourishment that he had nurtured for eons. Nazareth has proved that his heart is still kind toward the mortals. We have not found the real culprit of the Mortal Realm crisis, but we must report this to Her Majesty."
    return
