def main():
    sequences_dict = {}

    with open("data/rosalind_gc.txt", "r") as f:
        lines = f.readlines()

    current_label = ""

    for index, item in enumerate(lines):
        if item[0] == ">":
            current_label = item[1:].rstrip()
            sequences_dict[current_label] = ""
        else:
            sequences_dict[current_label] += item.rstrip()

    max_rate = 0
    max_label = ""

    for label in sequences_dict:
        rate = (sequences_dict[label].count("C") + sequences_dict[label].count("G")) / float(len(sequences_dict[label]))
        if rate > max_rate:
            max_rate = rate
            max_label = label

    print(max_label)
    print(max_rate*100)


if __name__ == "__main__":
    main()