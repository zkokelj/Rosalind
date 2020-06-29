def read_FASTA(file_path):
    sequences_dict = {}

    with open(file_path, "r") as f:
        lines = f.readlines()

    current_label = ""

    for index, item in enumerate(lines):
        if item[0] == ">":
            current_label = item[1:].rstrip()
            sequences_dict[current_label] = ""
        else:
            sequences_dict[current_label] += item.rstrip()

    return sequences_dict

def transition_transversion_ratio(s1, s2):
    if len(s1) != len(s2):
        return -1

    transition = 0
    transversion = 0

    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == "A" and s2[i] == "G" or s1[i] == "G" and s2[i] == "A" or \
               s1[i] == "C" and s2[i] == "T" or s1[i] == "T" and s2[i] == "C":
                transition += 1
            else:
                transversion += 1

    return round(transition/transversion, 11)


def main():
    data = read_FASTA("data/rosalind_tran.txt")
    keys = list(data)

    print(transition_transversion_ratio(data[keys[0]], data[keys[1]]))

if __name__ == '__main__':
    main()

