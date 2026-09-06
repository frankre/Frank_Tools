from pathlib import Path


# =============================
# CONFIG
# =============================

DIRECTORY = Path(r"C:\_PycharmProjects\RVC2-Frank-Stable1\results\batch_output")

OLD_TEXT = "AUPHONIC_VoiceEQ"
NEW_TEXT = "Yogini2"


# =============================
# FIND MATCHES
# =============================

renames = []

for file in DIRECTORY.iterdir():

    # Files only — ignore subdirectories
    if not file.is_file():
        continue

    if OLD_TEXT not in file.name:
        continue

    new_file = file.with_name(
        file.name.replace(OLD_TEXT, NEW_TEXT)
    )

    renames.append((file, new_file))


# =============================
# PREVIEW
# =============================

if not renames:
    print("No matching files found.")
    raise SystemExit

print(f"\n{len(renames)} file(s) will be renamed:\n")

for old_file, new_file in renames:
    print(f"{old_file.name}")
    print(f"  -> {new_file.name}\n")


# =============================
# CONFIRM
# =============================

if input("Type YES to rename: ") != "YES":
    print("Cancelled.")
    raise SystemExit


# =============================
# RENAME
# =============================

for old_file, new_file in renames:

    if new_file.exists():
        print(f"SKIPPED (already exists): {new_file.name}")
        continue

    old_file.rename(new_file)
    print(f"Renamed: {new_file.name}")


print("\nDone.")