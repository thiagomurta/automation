import os
import re
from pathlib import Path

# Code that corrects filenames containing the image resolution


def definition(name: str) -> bool:
    return bool(re.search(r"\d{4}[xX×]\d{4}", name))


def fix_name(name: str) -> str:
    return re.sub(r"[-_\s]*\d{4}[xX×]\d{4}", "", name)


IMAGES = Path("~/Imagens/Wallpaper (Cópia)/").expanduser()
img_list = os.listdir(IMAGES)

print(type(img_list))
print("========Before========")
print(*img_list, sep="\n")

print("========After========")
for name in img_list:
    if definition(name):
        old_name = IMAGES / name
        new_name = IMAGES / fix_name(name)
        old_name.rename(new_name)

    print(name)
