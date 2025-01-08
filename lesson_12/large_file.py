def read_large_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def process_large_file(filename):
    for line in read_large_file(filename):
        print("Processing line:", line)


process_large_file("large_file.txt")