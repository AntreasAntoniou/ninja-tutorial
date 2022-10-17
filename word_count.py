def count_words_in_md_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
        words = []
        for line in lines:
            words += line.split(" ")
        return len(words)


if __name__ == "__main__":
    print(count_words_in_md_file("POST.md"))
