import os
from pathlib import Path

current_dir = os.path.dirname(os.path.realpath(__file__))

# USERS
profiles_dir = os.path.join(Path(current_dir).parent.parent.parent,"data","users")

# IMAGES
images_dir = os.path.join(Path(current_dir).parent.parent.parent,"data","images")

long_button_dir = os.path.join(images_dir,"LongButton.png")
back_button_dir = os.path.join(images_dir,"buttonback.png")
x_button_dir = os.path.join(images_dir,"buttonx.png")
background_dir = os.path.join(images_dir,"Landscape5_2.png")
background_dir_2 = os.path.join(images_dir,"Landscape5_1.png")
avatar_button_dir = os.path.join(images_dir,"prueba_avatar_button.png")

avatar_dir = os.path.join(Path(current_dir).parent.parent.parent,"data","images","avatars")
avatars_dir = [
    os.path.join(avatar_dir,"avatar1.png"),
    os.path.join(avatar_dir,"avatar2.png"),
    os.path.join(avatar_dir,"avatar3.png"),
    os.path.join(avatar_dir,"avatar4.png"),
    os.path.join(avatar_dir,"avatar5.png"),
    os.path.join(avatar_dir,"avatar6.png"),
    os.path.join(avatar_dir,"avatar7.png"),
    os.path.join(avatar_dir,"avatar8.png"),
    os.path.join(avatar_dir,"avatar9.png")
]
