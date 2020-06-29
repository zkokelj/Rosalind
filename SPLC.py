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

def getRNA_codon_dict():
    """
    Reads file and returns RNA codon dictionary
    """
    codon_dict = {}
    with open("data/RNA_codon_table.txt", "r") as file:
        for line in file:
            line = line.rstrip().split()
            for idx, item in enumerate(line):
                if idx%2 == 0:
                    codon_dict[line[idx]] = line[idx+1]

    return  codon_dict

def RNA__seq_to_Protein(RNA_codon_dict, sequence):
    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        current = RNA_codon_dict[sequence[i:i+3]]
        if current == "Stop":
            return protein_sequence
        else:
            protein_sequence += current
    return protein_sequence

def cut_introns(string, intron):
    pos = string.find(intron)
    if pos == -1:
        return string

    return string[:pos]+string[pos+len(intron):]



def main():
    data = read_FASTA("data/rosalind_splc.txt")
    keys = list(data)
    dna_sequence = data[keys[0]]

    introns = []
    for i in range(1, len(keys)):
        introns.append(data[keys[i]])

    for intron in introns:
        dna_sequence = cut_introns(dna_sequence, intron)

    codon_dict = getRNA_codon_dict()

    proteins = RNA__seq_to_Protein(codon_dict, dna_sequence.replace("T", "U"))

    print(proteins)


if __name__ == '__main__':
    main()