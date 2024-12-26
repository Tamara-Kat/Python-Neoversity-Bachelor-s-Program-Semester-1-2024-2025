from pathlib import Path

from colorama import Fore

def display_tree(path: Path, indent:str = "", prefix: str = ""):
  if path.is_dir():
    print(indent + prefix + Fore.BLUE + str(path.name) + Fore.RESET)
    indent += "    " if prefix else ""

    children = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name))
    for index, child in enumerate(children):
      is_last = index == len(children) - 1
      display_tree(child, indent, "└──" if is_last else "├──")
  else:
    print(indent + prefix + Fore.GREEN + str(path.name) + Fore.RESET)

if __name__ == "__main__":
  display_tree(Path("./picture"))