import json


def score(input, correct_output, user_output):
    """
    Function to score codon task.
    
    :param input:           DNA string, example: 'TCTTGGGGCTTGTCGATTTTCGCTGGAAAGAGTCTTTTTAAGGGCTATTCCTTAACATAGACCCCGTTGCCTAAGCGAAATGATACAATTGTAAACCAAC'
    :type input:            basestring
    :param correct_output:  Correct JSON string, example: '{"UUA": 2, "UUG": 4, "CUU": 4, "CUC": 0, "CUA": 2, "CUG": 1}'
    :type correct_output:   basestring
    :param user_output:     User JSON string, example: '{"UUA": 2, "UUG": 1, "CUU": 4, "CUC": 0, "CUA": 2, "CUG": 1}'
    :type user_output:      basestring
    :return:                Pass/Fail mark
    :rtype:                 bool
    """
    correct_output = json.loads(correct_output)
    user_output = json.loads(user_output)
    for key in correct_output.keys():
        if correct_output[key] != user_output[key]:
            return False
    return True
