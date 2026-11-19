from pathlib import Path

DIR = Path("~/teste_sorter (Cópia)").expanduser()
DRY_RUN = False

items = sorted(DIR.iterdir())

reserved_destinations = set()
for item in items:
    if item.is_file() and item.suffix != ".crdownload" and item.suffix != ".part":
        # print(item)
        ext_original = "".join(item.suffixes)
        ext = "".join(item.suffixes).lower()
        DIR_EXT = Path(DIR / ext[1:])
        if item.name.startswith("."):
            print(f"IGNORE: {item}")
            continue
        elif ext == "":
            DIR_EXT = Path(DIR / "others")

        dst = DIR_EXT / item.name
        n = 0
        while dst.exists() or dst in reserved_destinations:
            n += 1
            new_name = f"{item.stem} ({n:03d}){ext_original}"
            # print("NEW NAME")
            # print(new_name)
            dst = DIR_EXT / new_name
        reserved_destinations.add(dst)

        print(f"{item} -> {dst}")
        # print("Reserved Destinations:")
        # print(f"{reserved_destinations}")
        # print()
        if not DRY_RUN:
            Path(DIR_EXT).mkdir(parents=True, exist_ok=True)
            if not dst.exists():
                item.rename(dst)
            else:
                print("NOTICE: Destination already exists")

    else:
        print("NOTICE: Unconfirmed files")
