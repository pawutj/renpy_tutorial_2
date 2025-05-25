#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8
from os import listdir
from os.path import isfile, join


def get_emotion_from_file(file_name):
    return c.split(".")[0].split("_")[-1]
########################
main_size = "(1433,3100)"

#########################################################################################

mypath = "./images/sprite/ayase"
directory_path ="ayase"
body_path = "ayase_body_00"
size = "(0,1525)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image ayase {get_emotion_from_file(emo_path)}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side ayase {get_emotion_from_file(emo_path)}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

################################################################################################################

mypath = "./images/sprite/eri"
directory_path ="eri"
body_path = "eri_body_00"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image eri {get_emotion_from_file(emo_path)}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side eri {get_emotion_from_file(emo_path)}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

######################################################################################################

mypath = "./images/sprite/mikan"
directory_path ="mikan"
body_path = "mikan_body"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image mikan {get_emotion_from_file(emo_path)}:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side mikan {get_emotion_from_file(emo_path)}:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

#################################################################################################################################

###############################################################################################################################

mypath = "./images/sprite/mikan2"
directory_path ="mikan2"
body_path = "mikan2_body_00"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image mikan {get_emotion_from_file(emo_path)}_2:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side mikan {get_emotion_from_file(emo_path)}_2:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

#################################################################################################################################


###############################################################################################################################

mypath = "./images/sprite/eri2"
directory_path ="eri2"
body_path = "eri2_body_0"
size = "(0,1625)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image eri {get_emotion_from_file(emo_path)}_2:""")
    print(f"""    zoom 0.75""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)
#Side#
for c in onlyfiles:
    emo_path = c.split('.')[0]
    print(f"""image side eri {get_emotion_from_file(emo_path)}_2:""")
    print(f"""    zoom 0.5""")
    print(f"""    yoffset 300""")
    print(f"""    xoffset -175""")
    print(f"""    im.Composite({main_size}, {size},"sprite/{directory_path}/{body_path}.png",{size},"sprite/{directory_path}/{emo_path}.png") """)

#################################################################################################################################



