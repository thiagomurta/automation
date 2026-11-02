from pathlib import Path

DOWNLOADS_DIR = Path("~/Downloads/").expanduser()

# downloads_list = os.listdir(DOWNLOADS_DIR)

# print(*downloads_list, sep="\n")

directories = {}
for item in DOWNLOADS_DIR.iterdir():
    # print(item)
    if item.is_file():
        ext = item.suffix[1:]
        Path("~/Downloads/" + ext).expanduser().mkdir(parents=True, exist_ok=True)
        directories[ext] = item.name
        orig = Path(Path("~/Downloads/").expanduser() / item.name)
        dst = Path("~/Downloads/" + ext).expanduser() / item.name
        orig.rename(dst)
