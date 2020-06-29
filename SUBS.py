def getAllIndicesOfSubstring(s, t):
    start_position = 0
    while start_position < len(s):
        start_position = s.find(t, start_position)
        #Check if there is no more occurances
        if start_position == -1:
            return
        else:
            yield start_position+1
            start_position += 1



def findMotifInDNA():
    file = open("data/rosalind_subs.txt", "r")
    s = file.readline().rstrip()
    t = file.readline().rstrip()
    return list(getAllIndicesOfSubstring(s, t))


if __name__ == "__main__":
    r = " ".join(str(item) for item in findMotifInDNA())
    result_file = open("results/SUBS.txt", "w")
    result_file.write(r)
    print(r)