from operator import itemgetter

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

def next_codon(sequence, offset=0):
    for i in range(0, len(sequence)-2-offset, 3):
        yield sequence[i+offset:i+3+offset]

def getStartCodons(sequence):
    last = -1
    while True:
        last = sequence.find("ATG", last+1)
        if last == -1:
            break
        yield last

def getORFs(dna_sequence, min_length=0):
    """
    :param dna_sequence:
    :return: list of tuples containing data about ORFs of the sequence. (<start_index>, <stop_index>, <length>).
    """
    stop_codons = set(["TAA", "TAG", "TGA"])
    orfs = []

    for start_position in getStartCodons(dna_sequence):
        for idx in range(start_position, len(dna_sequence)-2, 3):
            codon = dna_sequence[idx:idx+3]

            if codon in stop_codons:
                orfs.append((start_position, idx))

    return orfs

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

def DNA_to_RNA(sequence):
    return sequence.replace("T", "U")

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

def main(codon_dict):
    filename = "data/rosalind_orf.txt"
    fasta_data = read_FASTA(filename)

    for key in fasta_data:
        dna_sequence = fasta_data[key]
        reverse_dna = DNA_complement(dna_sequence)

        #print(dna_sequence)
        #print(reverse_dna)

        orfs = getORFs(dna_sequence)
        rorfs = getORFs(reverse_dna)

        distinct_protein_string = set()

        for orf in orfs:
            a = RNA__seq_to_Protein(codon_dict, DNA_to_RNA(dna_sequence[orf[0]:orf[1]]))
            distinct_protein_string.add(a)

        for orf in rorfs:
            a = RNA__seq_to_Protein(codon_dict, DNA_to_RNA(reverse_dna[orf[0]:orf[1]]))
            distinct_protein_string.add(a)

        result_file = open("results/ORF.txt", "a")


        for dp in distinct_protein_string:
            print(dp)
            result_file.write(dp+"\n")

        print("Distinct proteins length: ", len(distinct_protein_string))

if __name__ == '__main__':
    codon_dict = getRNA_codon_dict()
    main(codon_dict)
