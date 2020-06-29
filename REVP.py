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

def DNA_complement(sequence):
    complement = ""
    for i in sequence:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return complement[::-1]

def main():
    data = read_FASTA("data/rosalind_revp.txt")
    keys = list(data)
    dna_string = data[keys[0]]

    for start in range(0, len(dna_string)):
        for end in range(start, len(dna_string)):

            s = dna_string[start:end+1]
            l = len(s)

            if l >= 4 and l <= 12 and s == DNA_complement(s):
                print(str(start+1)+" "+str(end-start+1))

if __name__ == '__main__':
    main()