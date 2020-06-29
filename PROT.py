def RNA__seq_to_Protein(RNA_codon_dict):
    """
    Translates RNA sequence to protein sequence
    """
    file = open("data/rosalind_prot.txt", "r")
    lines = file.readlines()
    sequence = ""
    for line in lines:
        sequence += line.strip()

    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        current = RNA_codon_dict[sequence[i:i+3]]
        if current == "Stop":
            return protein_sequence
        else:
            protein_sequence += current
    return protein_sequence


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


if __name__ == "__main__":
    RNA_codon_dict = getRNA_codon_dict()
    ps = RNA__seq_to_Protein(RNA_codon_dict)
    #Write result to the file
    result_file = open("results/PROT.txt", "w")
    result_file.write(ps)