
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


def LCS(data_list):
    """

    :param data_list: list of strings
    :return: longest common substring
    """

    #Get the shortest string and all others...
    data_set = set(data_list)
    string0 = data_list[0]

    substr = ""
    #Loop over first_string
    for i in range(0, len(string0)):
        #Create and check for substrings..
        for j in range(len(string0), i+len(substr), -1):
            candidate = string0[i:j]
            if len(candidate) > len(substr) and isSubstringOfAll(candidate, data_list):
                substr = candidate
    return substr




def isSubstringOfAll(substring, data_list):
    for i in range(len(data_list)):
        if substring not in data_list[i]:
            return False
    return True



def main():
    data = read_FASTA('data/rosalind_lcsm.txt')
    data_list = [data[key] for key in list(data)]
    #print(data_list)
    #print("---------------- RESULT ----------------")
    print(LCS(data_list))

if __name__ == '__main__':
    main()