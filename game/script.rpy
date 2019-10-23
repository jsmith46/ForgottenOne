﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("REMYA")

define k = Character("KEHIRA")

define e = Character("EZBRIL")

define n = Character("EDNA")

define l = Character("LADY")

define t = Character("THIEF")

define m = Character("MERCHANT")

define b = Character("BAKER")

define s = Character("SHEPHeRD")

define bk = Character("BRIDGE KEEPER")

define c1 = Character("CHILD 1")

define c2 = Character("CHILD 2")

define c3 = Character("CHILD 3")


# The game starts here.
label start:
    jump scene1:

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

    r "Sister? Kehira, you are interrupting an important tria- Actually, you
    came just in time."

    r "Ezbril, Irul of Destruction and Chaos. For the suffering you have caused,
     for the cruelty you have brought, for your part in the Mortal Realm crisis,
      I hereby pronounce you guilty."
    r "You shall be banished to the Darker Realm, where my sister will ensure
    that you are punished for eternity."

    e "Please! I am innoc-"

    r "The trial is over. Kehira, he is all yours."

    k "(grinning) This way."

    "Ezbril stands up and walks out with Kehira."

    jump scene2

label scene2:
    play music "Dark_throne.wav" fadeout 1.0 fadein 1.0

    "You are now in another great throne room, dimmer than the last one, but
    equally as magnificent and clean. Kehira sits upon her dark throne, a white
    cat on her lap."

    e "So this is the Darker Realm where I will be punished for a crime I did
     not commit. But why are we in a throne room?"

    k "You did not do it, did you?"

    "You stand there shocked."

    k "My cat got your tongue? You did not cause the Mortal Realm crisis, did
    you?"

    e "I did not!"

    e "You believe me?"

    k "The Mortal Realm crisis is a series of disasters causing chaos in the
    mortal world. Cruelty is high, famine is growing, and mortals are suffering."
    k "My sister and I are unsure about when exactly this all started, but we are
     determined to find and punish the Irul responsible for these unspeakable
     crimes."
    k "You are the Irul of Destruction and Chaos. Naturally, my sister believes
    that only an Irul of Chaos can cause so much suffering."
    k "However, as the Irul Queen of Darkness, I realize that this could not be
    the work of one Irul alone."

    e "Then why am I here? Will I be punished? I did no-"

    k "Relax, I will not punish you yet. I have much use for you."

    e "Me? What could the Irul Queen of Darkness want from a mere Irul of
    Chaos?"

    k "You are going to the Mortal Realm to see firsthand what this destruction
    looks like. We will be able to determine from there who may have started
    this crisis. By doing this, you may be able to prove your innocence."
    k "So what do you say? Are you up for this challenge?"

    e "(A look of thought on his face, and nods with approval) What about your
    sister, the Light Majesty? I am supposed to be banished and punished here.
    If I am seen in the Mortal Realm-"

    k "Then you must perform your task in stealth. (grins) Or would you rather
    stay here and find out what awaits you in the Darker Realm?"

    "A small childish looking boy appears behind you."

    n "Your Dark Majesty, have you spoken to Ezbril of our plan?"

    k "Yes, Edna. I was just beginning to tell Ezbril about our plan. He has
    agreed. But I didn’t get a chance to mention that you will also be joining
    us. (Kehira turns to look at Ezbril, who is looking confused by Edna’s
    entrance)"

    n "That is excellent! We need to get prepared quickly as possible! The
    mortals can not suffer much more. I have found a way to get us there safely,
     and undetected. Follow me."

    "A wave of confusion falls upon you but its clear that Kehira is expecting
    you to follow the small child. You flustardly run after him."

    jump chapter2scene1

label chapter2scene1:
    play music "Forest.wav" fadeout 1.0 fadein 1.0
    "The scenery has changed, you are now in front of a lush forest. A small
    tribe can be seen in the distance on your right and in front of you is a
    path that seems to lead deep into the forest."

    n "Here we are, the Forest of Nourishment. For decades, tribes of humans
    have relied on the forest’s generous blessings for wood and food. This place
     is also home to many animals."

    n "In the heart of the forest you will find Nazareth, the Irul of Spring,
    Harvest, and Life. For eons, he has travelled forest to forest, village to
    village, nourishing and looked after every being that breathes."

    n "However, his performance has been going downhill lately. Forests are
    disappearing, animals are fleeing their homes, and food is scarce."

    n "Among the mortals, rumor is that some have spotted Nazareth purposely
    destroying vegetation. He has not returned to the Greater Realm in almost a
    decade, which leads Kehira to suspect that he might be hiding something."

    e "Her majesty wants me to investigate Nazareth?"

    n "Not so fast. Remember, you are a fallen Irul and the Iruil believe that
    you are banished. If you are seen in the Mortal Realm, Nazareth can use that
     against you. You might not be lucky to be given a second chance."

    n "Your task is to find out what exactly Nazareth is doing, so Kehira
    and Remya can use that information to decide his fate. Be warned, the Forest
     of Nourishment is a sacred place and easy to get lost in."

    n "I have some glowing gemstones you can use to mark your path.  When you
    find Nazareth, stay hidden and collect any evidence you find that would
    support your claim against Nazareth."

    n "I have duties to perform, therefore this is where I depart. I will say
    this, keep your eyes sharp and be aware of your surroundings. Trust no one."
    n "When you have accomplished your goal, meet me here and I shall escort you
     back to the Darker Realm."

    "Edna hands you 5 glowing gemstones and teleports away."

    e "... Why am I always stuck in this mess?"


    jump forest1
label forest1:
    $ backwards = False
    menu:
        "Enter the forest":
            "You walk into the forest until you reach a fork in the path and can
            now see why Edna said this forest is like a maze."
            jump forest2
        "Investigate the village":
            "I can see the village in the distance and from here it looks very
            peaceful. The tribe probably relys on the forest for wood and food."
            "I should probably enter the forest now."
            jump forest1
label forest2:
    menu:
        "Take left branch":
            "After walking down the path for a while you come across a sprawling
             beautiful lake."
            "A dead end it seems."
            menu:
                "Turn around":
                    "You walk back to the branch in the path."
                    jump forest2
        "Take right branch":
            "Walking deeper the trees begin to tower over you even more, the
            tallest must be hundreds of years old."
            "You come across another branch in the path, your current path seems
             to continue straight but to the left there is an overgrown path."
            jump forest3
        "Leave the forest":
            jump forest1
label forest3:
    menu:
        "Take the overgrown path":
            "Path is harder to traverse than before, can see signs of decaying
            flowers."
            "The path keeps getting more overgrown the further you go on, making
             progress much slower."
            jump forest4
        "Stay on your current path":
            if backwards == False:
                "You continue down the path, passing by a large bog on your
                right."
                jump forest5
            else:
                "You come across a place you recognise as the first branch in
                the path when you entered the forest."
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
            "After bushwacking for what felt like ages you come across a large
            path similar to the one you strayed from earlier."
            "As soon as you step out from your makeshift path you lose track of
             where it was."
            menu:
                "Follow large path to the left":
                    jump forest5
                "Follow large path to the right":
                    "You follow the path past a bog on your left."
                    "You come across another branch in the path, your current
                    path seems to continue straight but to the right there is
                    an overgrown path."
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

    "A lonely, tranquil heart of a forest. A gushing spring could be heard,
    along with an occasional call of a songbird. An Irul sits gracefully on a
    water-smoothed stone, surrounded by an audience of white tailed deer and
    curious rabbits."
    e "That must be Nazareth. He seems peaceful."
    "The carpet of moss starts to darken. Nazareth stands, and some of the
    rabbits begin to back away. The grass under his feet begins to darken,
    then disappear. Like a ripple, the surrounding plants begin to vanish,
    leaving no evidence of the lush green that existed. The small company of
    critters starts to flee from their once home."
    e "The Irul of Spring, Harvest and Life … destroying the ancient forest?
    I must report this to Her Dark Majesty."
    "Nazareth raises his arms, like a falcon about to take flight. He seems to
    hesitate a moment. Suddenly, he twirls and shoots toward the skies. Time
    stops. You are not standing in a forest anymore."
    "The entire East half of the forest has vanished, leaving behind no blade
    of grass or whisper of what was once magical and green. You can easily make
     out the small tribe from here. And in front of you…"
    "A wall of flames. The West half of the forest is ablaze, the fire rushing
    toward you, the inferno leaping from tree to tree."
    "But you realize that you are safe. There are no trees, no vegetation left
    on this side to feed the hungry flames. The forest fire cannot spread."
    "A shift of air, a sudden flash of light to your right, and Edna stands
    beside you."
    n "Greetings! I’m ba-"
    n "(astonished) Wha- what happened here?"
    e "It seems to be a forest fire. I was confused when I witnessed Nazareth
    wiping out the ancient forest. I think he was just trying to protect the
    tribe of mortals yonder. The flames will not reach them."
    n "(sorrowful) It must be hard for Nazareth to obliterate the ancient Forest
     of Nourishment that he had nurtured for eons. Nazareth has proved that his
     heart is still kind toward the mortals. We have not found the real culprit
      of the Mortal Realm crisis, but we must report this to Her Majesty."
    jump chapter3scene1

label chapter3scene1:

    "placeholder description"
    e "(bows deeply) Your Majesty, we are back, and we bring news."
    k "What is it? Did you find what Nazareth was up to?"
    menu:
        "He destroyed the ancient forest":
            return
        "He saved a tribe of mortals":
            return
    return

label market_intro:
    $ lady_flag = False
    $ lady_riddle = False
    $ apple_flag = False
    $ gone_girl = False
    $ pouch = False
    $ theif_flag = False
    $ no_theif = False
    $ theif_riddle = False
    $ baker_flag = False
    $ no_baker = False
    $ baker_riddle = False
    $ bk_flag = False
    $ no_bk = False
    $ bk_riddle = False
    $ shepard_flag = False
    $ no_shepard = False
    $ shepard_riddle = False
    $ merchant_flag = False
    $ no_merchant = False
    $ merchant_riddle = False
    $ kids_flag = False
    $ no_kids = False
    $ kids_riddle = False
label market_entrance

    "The cozy little village reminds you of the small tribe you saw before. A
    glance eastward, and you can see what is left of the ancient Forest, still
    ablaze. To your west is the village marketplace, humming alive with busy
    mortals hurrying to make the most of their short time."
    "Cyvtis is somewhere in the village, perhaps disguised as a mortal."

    menu:
        "Go west":
            jump market_west
        "Go east":
            jump market_east

label market_west:
    "You have never been to a human marketplace, and you did not know what to
    expect. It seems that the entire village, no, all of the Mortal Realm has
    decided to gather here on consensus. The marketplace needs no Irul of Chaos,
    for it has plenty of chaos of its own."
    "Merchants shouting their wares, buyers gathering up items as fast as they
    can, human younglings shoving and elbowing as they race through the crowd."
    "You tug close your hood, hoping to dissolve within its comforting shadow."
    jump block_1


label market_east:
    "Even from this distance, you can see the ghastly orange grin taking what
    was once sacred and alive and casting it into the sky, first glowing red
    then cooling to black. Nazareth has bound the angry flames, but how long
    shall the inferno rage? But that is not your task."
    "You must find Cytvis and figure out why she let the Sun ignite the ancient
    forest."

    jump market_entrance

label block_1:
    "You are standing inside of the market place, infront of the exit which you can see to the east.
     On the north you can see a narrow path through 2 vendor tents. On the West you can see a narrow passage,
     shaded and quiet, contrary to the rest of the marketplace"

     menu:
         "Go west":
             jump theif
         "Go north":
             jump lady
         "Go east":
             jump market_entrance

label lady:

    "You squeeze through the bustling crowd and aim for the narrow path between
    two vendors’ tents. "

    if gone_girl == False:
        if lady_flag == False:
            "But the passage is blocked by a sobbing lady, pure agony on her young
            face. "

            l "(sobbing) Sigh. Sig, sig, sob."
            e "..."
            l "Oh, good sir, please help me! I just lost my pouch, it was full of
            coins."

            menu:
                "Approach her":
                    jump help_lady
                "Leave":
                    jump meanie_to_lady
        else:
            l "Oh, it’s you, good sir! Did you find my pouch?"
            jump lady_menu

label help_lady:
    e "What did it look like?"
    l "It was a brown leather pouch, I had coins in it to purchase goods from
    the market. I put it down to examine some sweet apples, but when I looked
    again, it was gone. Oh, it must have been stolen!"
    l "Oh, sob, sob."
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
    "You are unskilled in the art of being a gentleman"
    return

label give_pouch:
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

    jump block_4

label lady_riddle:
    if lady_riddle == False:
        $ lady_riddle = True
        e "I have not seen your pouch, but is there another way I can help you?"
        l "Would you help me, good sir?"
        l "The villagers here love to trade in riddles. The good merchant over there
         said he would let me have a dozen of those sweet apples if I can answer his
          riddle. You look wise, good sir. Can you help me solve the merchant’s
          riddle?"
        l "riddle here"
    else:
        l "Good sir, would you like to try the riddle again?"

label leave_nicely:
    e "My apologies, but I must be on my way."
    jump block_1

jump riddle_solved:
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

    jump block_4

label theif
    "You find yourself in a narrow passage, shaded and quiet, contrary to the rest of the marketplace."
    if no_theif == False:
        if theif_flag == False:
            "Before you stand, you notice a rough looking bulky man.
            He is examining a small leather pouch, the kind you have seen many mortal females carry in this market.
            The delicate, embroidered pouch looks peculiar in his large hands. You doubt it belongs to him.
            The man senses your presence. For what seems like eternity, you stare at each other.
            Finally, he grins broadly."

            t "(smirking) Nehehe. I don’t recall seeing you around. You must be new here"
            jump theif_menu
        else:
            t "Oh, its you again. What do you want?"
            jump theif_menu2
    else:
        jump block_2
label theif_menu
    menu:
        "Ask for pouch":
            jump take_pouch
        "Leave":
            "You decide it is in your best interest to stay out of trouble."
            jump block_1

label take_pouch:
    e "I think that pouch belongs to someone else. Give it to me."
    t "Oh? Aahaha! We have quite a bold one here."
    t "I am this village’s most skilled thief. You dare walk into my lair and demand for what I have rightfully stolen? Nehehe, you amuse me!"
    t "I don’t think this pouch belongs to you either. Why, there is barely anything here! Such a waste of my skills."
    t "But there is something far more valuable I can get from you. You, outsider, did you know that in this village you
       can trade in riddles? They value intellect here, because they think it sets them apart from the tribe men who live by that ancient forest.
       Or what used to be a forest- nehehehe"
    $ theif_flag = True

label theif_menu2:
    t "Answer this riddle, and you shall win the pouch for exchange."
    menu:
        "Answer riddle":
            jump theif_riddle
        "Leave"
            t "Nehehehe. Intellect is rare and cannot be stolen, that’s why they value it around here"
            jump block_1

label theif_riddle:
    t "Let’s test you. Nehehehe"
    t "Riddle here"
    if theif_riddle == True:
        t "You have my respect, nehehehe. Here, you can have this humble pouch. I can trade goods far more valuable with the answer you gave me, ahahaha."
        "You hear the jingle of coins as the thief tosses you the small pouch."
        t "I may be a renowned thief, but I am better than the village chief. At least I am not a murderer! Nehehehe."
        "The thief takes a step back, and melts into the shadows."
        e "Village chief? Murderer? What was he talking about?"
        $ pouch == True
        $ no_theif == True
        jump block_2
    else:
        t "Nehehehe. Intellect is rare and cannot be stolen, that’s why they value it around here"
        jump theif_menu2
label block_2:
    "To your north you can see a bridge not that far from where you are standing. To your west you can see the end of the narrow passage, blocked of by stalls.
    Far to the East along the narrow passage lies the exit to the market place."
    menu:
        "Go north":
            jump block_3
        "Go east":
            jump block_1

label block_3:
    "You have come onto a crossroad. Just to your north is a bridge which goes over the river that seperates the market into 2. To your west is a deadend.
    To your east is a small passage by the riverside which leads to the entrace of another bridge. To your south is a Narrow passage which leads to the exit of the market "
    menu:
        "Go north":
            jump bridgekeeper
        "Go east":
            jump baker
        "Go south":
            jump block_2

label block_4:
    "You are on a narrow path between 2 stalls. Just to your west is the entrace to a bridge which goes over the river that seperates the market into 2.
    To your east is a deadend. To your south is a Narrow passage which leads to the exit of the market "
    menu:
        "Go west":
            jump baker
        "Go south":
            jump block_1
label baker:
    if no_baker == False:
        if baker_flag == False:
            "sweet, welcoming aroma of cinnamon, honey, - and something you can only describe as “warm”-
            beckons you to a bright bake house with a hand painted sign.
            Entranced by the golden loaves, fruit pies, jam filled buns, cakes, and the many delicacies,
            you wonder when the Iruil would learn some of the mortals’ tricks- the magic of turning wheat into soft bread."
            "A stout man in white napron flashes you a grin as he presents a steel tray arranged with buttered buns."

            b "Good morrow, Sir! Have not seen you around before. Might you be a traveller?"
            e "Indeed."
            b "Welcome then! Try the best bread in the village, and you shall eat most well today. This one is on the house."
            "The golden glaze of melted butter on fresh bread is inviting, indeed."
            jump baker_menu
        else:
            t "Oh, its you again. If you can aid me with my problem, you may take a shortcut through the bakery."
            jump baker_menu2
    else:
        jump block_5
label baker_menu
    menu:
    "Accept Bread":
        e "Thank you kindly."
        "The bun feels warm and fluffy in your hand, the butter glossing your fingers. You take a bite.
        It has only been a few hundred decades since you last tasted mortal food, yet the clever balance of various ingredients fascinates you.
        The outer layer crisped to perfection, the inside delicately soft, but the taste- the taste you can only describe as joyous and alive and bestowed with sunshine itself.
        The thought of sunshine reminds you of your purpose to find Cyvtis and discover why she let the sun ignite the Forest of Nourishment."
        $ baker_flag = True
        jump eat_bread
    "Leave":
        "The aroma of maken good might be mesmerizing, but you must stay focused on your task"
        jump block_4

label eat_bread:
    b "You must be weary from your journey. The market can be labrinth to navigate for visitors like yourself."
    b "If you can aid me with my problem, you may take a shortcut through the bakery."
    jump baker_menu2

label baker_menu2:
    menu:
        "Offer to help":
            e "I can try to help you with your problem. What might it be, Sir?"
            jump help_baker
        "Leave":
            e "I thank you for your offer, Sir, but I would like to explore this area of the market first."
            b "See you around! Be wary lest you lose your bearing."
            jump block_2

label help_baker:


    b "riddle here"
    if baker_riddle == True:
        b "Bravo! I thank you for your help. You may take the shortcut through the bakery anytime you desire."
        $ no_baker = True
        jump block_5
    else:
        jump help_baker

label block_5:
    "You have come onto a crossroad. Just to your north is a bridge which goes over the river that seperates the market into 2. To your east is a narrow passage between 2 stalls.
    To your west is a small passage by the riverside leading to another bridge."
    menu:
        "Go north":
            jump block_7
        "Go east":
            jump block_4
        "Go west":
            jump block_3

label bridge_keeper:
    if no_bk = False:
        if bk_flag == False:

        else:

    else:
        "You have crossed the bridge and went through a cornered passage"
        jump block_6

label block_6:
    "You have come onto another crossroad. Just to your north is a cornered passage going west. To your east is another cross road.
    To your west is the cornered passage leading to one of the bridges."
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
    To your west is another crossroad. To your south is a bridge"
    menu:
        "Go north":
            jump merchant
        "Go east":
            jump dead_end_1
        "Go west":
            jump block_6
        "Go south"
            jump block_5

label dead_end_1:
    "You have reached the end of this road. There is a large wall blocking you from progressing any further. You decide to head
    back to your previous crossroad as there is no point wasting your prescious time here"
    jump block_7

label merchant:
    if no_merchant == False:
        "As you shove your way through the crowd, you find the path blocked by a merchant’s wagon."
        if merchant_flag == False:
            "You have never seen a wagon up close before, and you cannot help but feel awed by the mortals’ inventive.
            The creative ensemble of refined wood and cloth allowed this merchant to carry heaps of furs,
            pulled through many roads by his patient horse. The merchant stands leaning against his wagon,
            heedless of the path he has blocked. Your approach draws his attention."

            m "Hail, old friend! Would you be interested in some fine, silky furs?"
            "You ignore him."
            m "I tell you, I did not trade these furs from your tribesmen!"

            menu:
                "Talk to him":
                    jump talk_merchant

                "Leave":
                    "You have no interest in trading with the mortals. "
                    jump block_7
        else:
            m "Aha, its you again. Are you here to solve my riddle?"
            jump merchant_menu
    else:
        jump block_8

label talk_merchant
    "His words catch your interest."
    e "What tribesmen? What do the furs have to do with tribesmen?"
    m "Wh-no, no. I said the furs have nothing to do with the tribesm-"
    m "Oho! You must be an outsider here, just like your old friend."
    m "You see, old friend, the villagers here seem to have a dispute with the tribesmen east of the forest."
    m "The truth is, I stopped by the tribe for a few days and traded my wood for these fine furs. A merry folk they were, I tell you.
      They treated your old friend most kindly, and they took good care of the horse. I was sure their furs would fetch a generous price."
    m "Alas, the moment I mentioned the tribesmen here, the villagers have avoided my wagon. This is woodness, old friend!"
        "The horse whips its tail to bat off a fly."
    m "Aha, but a gentleman thither offered to buy all of my furs, if I can prove myself more cultured than the tribesmen.
      Old friend, all is not in despair. He said something about only a refined man being able to solve this riddle."
    $ merchant_flag = True
    jump merchant_menu

label merchant_menu
    m "What say you, old friend? Would you mind helping a friend out here?"
    menu:
        "Try the riddel":
            jump merchant_help
        "Feed apple to the horse" if apple_flag == True:
            jump feed_horse
        "Leave":
            m "Woe, old friend! Mayhap we are not the cultured gentleman we try to be."
            jump block_7

label merchant_help:
    e "Uh, I can give it a try."
    m "riddle here"
    if merchant_riddle == True:
        m "Most beauteous, old friend!"
        "He moves his wagon just enough for you to proceed. "
        m "I will see you anon!"
        $ no_merchant = True
        jump block_8
    else:
        jump merchant_help

label feed_horse:
    "You ignore the jabbering merchant and reach into the folds of your cloak for the sweet apple the lady gave you.
    The horse eyes your every movement. Slowly, the horse reaches forward toward your outstretched arm, the red apple smooth in your hand."
    "The greedy beast has moved the wagon just enough for you to proceed."
    jump block_8

label block_8:
        "You have reached the northend of the market. To your south is the cross from where you just came. To your west is a narrow path. You notice that the path o your east
        leads to an deadend"
        menu:
            "Go west":
                jump kids
            "GO south":
                jump block_7
label shepherd:


label block_9:

label dead_end_2:
    "You have reached the end of this road. There is a river blocking you from progressing any further. You decide to head
    back to your previous crossroad as there is no point wasting your prescious time here"
    jump block_9
label kids:
    "A peculiar shift of air reveals that Cyvtis must be close by.
    As you make your way through the suffocating mass of mortals,
    you find your path conveniently blocked by a group of insolent mortal younglings. "
    if no_kids == False:
        if kids_flag == False:
            c1 "You can not play with us, you are a tribesman!"
            c2 "Boo, tribesman!"
            c3 "No, I am not!"
            c1 "I saw your folks travelling to the east side of the forest."
            c3 "(wailing) That is a lie!"
            e "Even their younglings despise the tribesmen."

            menu:
                "Proceed past the younglings":
                    jump proceed_kids
                "Leave":
                    "Strange creatures they are, the mortal younglings. Maybe you can find a way around."
                    jump block_8
        else:
            c1 "Oho, you're back"
            jump kids_code
    else:
        jump block_10

label proceed_kids:
    "Depicting no interest, you continue your trek."
    c1 "Hey you! If you want to pass through the fort, you must say the secret code."
    e "...fort?"
    "You look around for the alleged fort."
    c2 "Is he a tribesman as well?"
    c1 "He might be, but if he can unravel the code then he is not."
    $ kids_flag = True
    jump kids_code

label kids_code:
    c2 "Our secret code is the hardest to break!"
    menu:
        "Try Code":
            e " Is it now? I bet you I can unravel your code."
            jump solve_code

        "Leave":
            c2 "Aha! Told you our secret code is the hardest to break!"
            c1 "Boo, tribesman!"
            jump block_8

label solve_code:
    c1 "Insert riddle here"
    if kids_riddle == True:
        c1 "Behold the sir! You may travel through our fort in peace."
        e "You know, I am in fact a tribesman."
        c2 "(shocked) B-but you are a gentleman! How can a tribesman break our secret code?"
        c3 "(amazed) Tribesmen must be real strong."
        c1 "Only tribesmen can break our secret code!"
        $ no_kids = True
        jump block_10
    else:
        jump solve_code


label block_10:

label town_center
