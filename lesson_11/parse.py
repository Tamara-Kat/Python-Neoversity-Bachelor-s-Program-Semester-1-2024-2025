from pathlib import Path

p = Path("./picture")

print(p.exists(), p.name, p.parent, p.is_dir(), p.is_file())

def parse_folder(path: Path):
  for file in path.iterdir():
    if file.is_file():
      print(f"This is a file: {file.name}")
    elif file.is_dir():
      print(f"This is a folder: {file.name}")
      parse_folder(file)

parse_folder(p)