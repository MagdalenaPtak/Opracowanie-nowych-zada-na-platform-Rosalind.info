import random


def generate():
    """
    Function to generate random RNA sequence
    Example output: UGUCUGAGUAACUUGUCGGUCGUAUACAGUGGUAUUGUGCGGAAACAACCGUAGGGAGGUGUUACUGCUGGGAACAGCCUUUCGUUCGCCAGGCAAUAC

    :return:    RNA sequence of 99 elements length
    :rtype:     string
    """
    return "".join(random.choice("UGAC") for _ in range(99))
