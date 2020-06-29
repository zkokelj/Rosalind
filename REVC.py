def main():
    file = open("data/rosalind_revc.txt", "r")
    sequence = file.readline()
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

    print(complement[::-1])


if __name__ == "__main__":
    main()