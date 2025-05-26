# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image artroom_afternoon = im.Scale("bg/school-park1.jpg",1920,1080)
image classroom_morning = im.Scale("bg/classroom_morning.jpg",1920,1080)
# The game starts here.



define cat = Character("แมว", image ="cat" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define ayase = Character("อายาเสะ",image = "ayase" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define eri = Character("เอริ",image = "eri" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define mikan = Character("มิคัง",image = "mikan" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

transform left3:
    xalign -0.25
    yalign 1.0

transform right3:
    xalign 1.25
    yalign 1.0

transform left:
    xalign -0.05
    yalign 1.0

transform right:
    xalign 1.05
    yalign 1.0

transform centerzoom:
    zoom 1.4
    xalign 0.5
    yalign 0.85

init -2:
    style nvl_dialogue:
        line_spacing 10
    style say_dialogue:
        line_spacing 10   


label start:
    jump chap1

    return
