import argparse
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description="Sort files")
parser.add_argument("--source", "-S", type=str, help="Source directory", required=True)
parser.add_argument(
    "--destination", "-D", type=str, help="Destination directory", default="dist"
)

args = vars(parser.parse_args())  # obj -> dict
source = Path(args.get("source"))
destination = Path(args.get("destination"))


def parse_folder(path: Path):
    for file in path.iterdir():
        if file.is_file():
            copy_file(file)
        elif file.is_dir():
            parse_folder(file)


def copy_file(file: Path):
    ext = file.suffix[1:].lower()
    new_path = destination / ext
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)


if __name__ == "__main__":
    parse_folder(source)