import re

from pathlib import Path

lut_directory = Path.cwd() / "src" / "tuttifrutti" / "lut"
whitespace_or_number = re.compile(r"\s|\d")


def main() -> None:
    for file in lut_directory.iterdir():
        if not file.is_file():
            continue

        # only CUBE files
        # if file.suffix != ".CUBE":
        #     continue
        if file.suffix != ".cube":
            continue

        if not whitespace_or_number.search(file.name):
            continue

        better_name = whitespace_or_number.sub("", file.stem)
        better_path = file.with_name(f"{better_name}.cube")

        # copy contents over
        with file.open("r") as old_f:
            with better_path.open("w") as new_f:
                new_f.writelines(old_f)

        file.unlink()  # delete the file


def test() -> None:
    s: str = ""
    print(f"re.search({s}) == ", whitespace_or_number.search(s))
    s = "hello"
    print(f"re.search({s}) == ", whitespace_or_number.search(s))
    s = "he ll o"
    print(f"re.search({s}) == ", whitespace_or_number.search(s))
    s = "he 77 o"
    print(f"re.search({s}) == ", whitespace_or_number.search(s))


if __name__ == "__main__":
    # main()
    test()
