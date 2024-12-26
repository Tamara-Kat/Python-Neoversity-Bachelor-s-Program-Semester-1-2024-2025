from pathlib import Path

def display_tree(path: Path, indent:str = ""):
  print(indent + str(path.name))

  if path.is_dir():
    for child in path.iterdir():
      display_tree(child, indent + "    ")


if __name__ == "__main__":
  display_tree(Path("./picture"))