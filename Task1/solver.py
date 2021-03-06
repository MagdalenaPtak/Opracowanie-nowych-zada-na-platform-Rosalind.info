import json


def solve(input):
    """
    Function to give number of UUA, UUG, CUU, CUC, CUA, CUG in given DNA string.
    Example input: 'TCTTGGGGCTTGTCGATTTTCGCTGGAAAGAGTCTTTTTAAGGGCTATTCCTTAACATAGACCCCGTTGCCTAAGCGAAATGATACAATTGTAAACCAAC'
    Example output: '{"UUA": 2, "UUG": 4, "CUU": 4, "CUC": 0, "CUA": 2, "CUG": 1}'
    
    :param input:   DNA sequence
    :type input:    basestring
    :return:        JSON string containing values of codons.
    :rtype:         basestring
    """

    if not isinstance(input, str) or not input:
        raise TypeError(input)

    for element in input:
        if element not in "TGAC":
            raise TypeError

    rna = input.replace("T", "U")
    solution = {
        "UUA": 0,
        "UUG": 0,
        "CUU": 0,
        "CUC": 0,
        "CUA": 0,
        "CUG": 0
    }
    for key in solution.keys():
        solution[key] = rna.count(key)

    return json.dumps(solution)
