#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8
#python gen.py > chap1.rpy

import pandas as pd
FILE_NAME = "renpy_tutorial.csv"
VOICE_BASE_PATH="audio/voice"
VOICE_PATH = ""
SFX_BASE_PATH="audio/sfx"
data = pd.read_csv(FILE_NAME,encoding="utf-8")
data = data.fillna("")
shortcut_charector_1 = ""
def show_charector(charector1,charector2):


    if (character1 != "" and character2 != ""):
        print(f'hide eri')
        print(f'hide ayase')
        print(f'hide mikan')

    if ( charector1 == "" ):
        return
    
    #2 Charector Case
    if ( charector2 != ""):
        print(f'show {character1} normal at left')
        print(f'show {character2} normal at right with Dissolve(0.2) ')
        return
        
    #1 Character Case
    print(f'show {character1} normal at center with Dissolve(0.2) ')
    return

for i,c in data.iterrows():
    ### Assign ##############################

    bg = c['bg']
    bg_effect = c['bg_effect']
    bgm = c['bgm']
    character1 = c['character1']
    character2 = c['character2']
    face = c['face']
    who_talk = c['who_talk']
    talk = c['talk']
    voice = c['voice']
    sfx = c['sfx']
    ### Action ###############################

    if(bg):
        print(f'scene {bg} with Dissolve(1.0)')

    if(bgm and bgm != 'stop'):
        print(f"stop music")
        print(f'play music "audio/bgm/{bgm}.mp3" volume 0.5')
    
    if(bgm =='stop'):
        print(f"stop music")
    show_charector(character1, character2)
        
    if(sfx):
        print(f'play sound "{SFX_BASE_PATH}/{sfx}.mp3"')

    if(voice):
        print(f'play sound "{VOICE_BASE_PATH}/{who_talk}/{VOICE_PATH}/{voice}.mp3"')
    
    if(bg_effect):
        print(f'{bg_effect}')
    
    if(talk):
        if(who_talk):
            print(f'{who_talk} {(face)} "{talk}" with dissolve')
        else:
            print(f'th "{talk}" with dissolve')
    
print(f"return")