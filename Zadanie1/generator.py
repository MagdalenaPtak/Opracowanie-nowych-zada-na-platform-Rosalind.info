import random


def generate():
    """
    Function to generate random DNA sequence
    Example output: TCTTGGGGCTTGTCGATTTTCGCTGGAAAGAGTCTTTTTAAGGGCTATTCCTTAACATAGACCCCGTTGCCTAAGCGAAATGATACAATTGTAAACCAAC
    
    :return:    DNA sequence of 100 elements length
    :rtype:     string
    """
    return "".join(random.choice("TGAC") for _ in range(100))

