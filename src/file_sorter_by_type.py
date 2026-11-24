from pathlib import Path

DIR = Path("~/teste_sorter (Cópia)").expanduser()
DRY_RUN = False

items = sorted(DIR.iterdir())
# items = sorted(DIR.iterdir(), reverse=True)

reserved_destinations = set()
for item in items:
    if item.is_file() and item.suffix != ".crdownload" and item.suffix != ".part":
        ext_original = "".join(item.suffixes)
        ext = "".join(item.suffixes).lower()

        DIR_EXT = DIR / ext[1:]

        if item.name.startswith("."):
            print(f"IGNORE: {item}")
            continue
        elif ext == "":
            DIR_EXT = DIR / "others"

        dst = DIR_EXT / item.name

        if not DIR_EXT.is_dir() and DIR_EXT.exists():
            print(f"IGNORED: {item}")
            continue

        n = 0

        while dst.exists() or dst in reserved_destinations:
            # while dst in reserved_destinations:
            n += 1
            new_name = f"{item.stem} ({n:03d}){ext_original}"
            dst = DIR_EXT / new_name
        reserved_destinations.add(dst)

        print(f"{item} -> {dst}")

        if not DRY_RUN:
            Path(DIR_EXT).mkdir(parents=True, exist_ok=True)

            if not dst.exists():
                item.rename(dst)
            else:
                print(f"NOTICE: Destination ({dst}) already exists")

    elif not item.is_file():
        print(f"NOTICE: Directories ({item})")
    else:
        print(f"NOTICE: Unconfirmed files ({item})")
