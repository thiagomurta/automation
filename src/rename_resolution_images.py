import re
from datetime import datetime
from pathlib import Path

# Code that corrects filenames containing the image resolution


# def definition(name: str) -> bool:
#     return bool(re.search(r"\d{3,4}[xX×]\d{3,4}", name))


def fix_name(name: str) -> str:
    return re.sub(r"[-_\s]*\d{3,4}[xX×]\d{3,4}", "", name)


IMAGES = Path("~/Imagens/Wallpaper/").expanduser()
DRY_RUN = True

img_list = sorted(p for p in IMAGES.iterdir() if p.is_file())

for n, img in enumerate(img_list, start=1):
    date = datetime.fromtimestamp(img.stat().st_mtime).strftime("%Y-%m-%d")
    name_img = fix_name(img.stem)
    new_name = img.with_name(f"{date}_{name_img}_{n:03d}{img.suffix.lower()}")

    if new_name.exists():
        continue

    print(f"{img.name} -> {new_name.name}")
    if not DRY_RUN:
        img.rename(new_name)
