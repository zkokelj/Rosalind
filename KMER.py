from itertools import product


def readFile():
    sequences_dict = {}

    with open("data/rosalind_kmer.txt", "r") as f:
        lines = f.readlines()

    current_label = ""

    for index, item in enumerate(lines):
        if item[0] == ">":
            current_label = item[1:].rstrip()
            sequences_dict[current_label] = ""
        else:
            sequences_dict[current_label] += item.rstrip()

    return sequences_dict[current_label]


def countWithOverlapping(s, t):
    pos = count = 0
    while pos >= 0:
        pos = s.find(t, pos) + 1
        if pos > 0:
            count += 1
        else:
            return count


def countK_mers(sequence, k):
    l = []
    for xmer in (product('ACGT', repeat=k)):
        l.append(countWithOverlapping(sequence, "".join(xmer)))
    return l


if __name__ == "__main__":
    sequence = readFile()
    result = countK_mers(sequence, 4)
    result_file = open("results/KMER.txt", "w")
    result_file.write(" ".join(str(r) for r in result))
